# -*- coding: utf-8 -*-
"""
@file: group_description.py
@desc:
@author: Jaden Wu
@time: 2020/11/23 8:55
"""
import os
import typing
from datetime import datetime
import glob

from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from photo_arch.use_cases.interfaces.dataset import GroupInputData
from photo_arch.infrastructures.user_interface.qt.interaction.utils import (
    static, catch_exception, for_all_methods)
from photo_arch.infrastructures.user_interface.qt.interaction.main_window import (
    MainWindow, Ui_MainWindow, Overlay, RecognizeState)
from photo_arch.infrastructures.user_interface.qt.interaction.setting import Setting

from photo_arch.infrastructures.databases.db_setting import engine, make_session
from photo_arch.adapters.sql.repo import Repo
from photo_arch.adapters.controller.group_description import Controller
from photo_arch.adapters.presenter.group_description import Presenter
from photo_arch.adapters.view_model.group_description import ViewModel


@for_all_methods(catch_exception)
class View(object):
    def __init__(self, mw_: MainWindow, view_model: ViewModel):
        self.mw = mw_
        self.view_model = view_model

    def display_group(self, widget_suffix='_in_group'):
        for k, v in self.view_model.group.items():
            widget_name = k + widget_suffix
            if hasattr(self.mw.ui, widget_name):
                widget = getattr(self.mw.ui, widget_name)
                if isinstance(widget, QComboBox):
                    if v:
                        widget.setCurrentText(v)
                    else:
                        widget.setCurrentIndex(-1)
                else:
                    widget.setText(v)


@for_all_methods(catch_exception)
class GroupDescription(object):
    def __init__(self, mw_: MainWindow, setting: Setting):
        self.mw = mw_
        self.ui: Ui_MainWindow = mw_.ui
        self.setting = setting
        view_model = ViewModel()
        self.controller = Controller(Repo(make_session(engine)), Presenter(view_model))
        self.view = View(mw_, view_model)

        self.current_work_path = ''
        self.description_path_info = {}
        self.group_arch_code_info = {}

        height = int(self.mw.dt_height*30/1080)
        self.ui.treeWidget.setStyleSheet('#treeWidget::item{height:%spx;}' % (height + 5))
        self.ui.open_dir_btn.clicked.connect(static(self.open_dir))
        self.ui.treeWidget.itemClicked.connect(static(self.item_click))
        self.ui.add_folder_btn.clicked.connect(static(self.add_folder_item))
        self.ui.cancel_folder_btn.clicked.connect(static(self.cancel_folder_item))
        self.ui.save_group_btn.clicked.connect(static(self.save_group))

        self.ui.add_folder_btn.setStyleSheet(self.mw.button_style_sheet)
        self.ui.cancel_folder_btn.setStyleSheet(self.mw.button_style_sheet)
        self.ui.save_group_btn.setStyleSheet(self.mw.button_style_sheet)

        self.clear_group_info()

        self.ui.fonds_code_in_group.currentTextChanged.connect(static(self.display_arch_and_group_code))
        self.ui.arch_category_code_in_group.currentTextChanged.connect(static(self.display_arch_and_group_code))
        self.ui.retention_period_in_group.currentTextChanged.connect(static(self.display_arch_and_group_code))
        self.ui.year_in_group.textChanged.connect(static(self.display_arch_and_group_code))

    def clear_group_info(self):
        self.view.display_group()

    def open_dir(self):
        current_work_path = QFileDialog.getExistingDirectory(
            self.ui.treeWidget, "选择文件夹",
            options=QFileDialog.ShowDirsOnly
        )
        if not current_work_path:
            return
        self.ui.tabWidget.setCurrentIndex(0)
        self.current_work_path = os.path.abspath(current_work_path)
        self.ui.dir_lineEdit.setText(self.current_work_path)
        overlay = Overlay(self.ui.treeWidget, '初始化中', dynamic=True)
        overlay.show()
        while 1:
            if self.mw.interaction != typing.Any:
                break
            else:
                QApplication.processEvents()
        overlay.hide()
        arch_code_info = self.mw.interaction.get_arch_code(self.current_work_path)
        if arch_code_info and arch_code_info.get('root'):
            self._generate_tree_by_data(arch_code_info)
        else:
            self._generate_tree_by_path(self.current_work_path)
        self._reset_state()

    def display_group(self, path):
        group_folder = os.path.split(path)[1]
        if self.setting.description_path in path:  # 以路径来判断是否已著录（应以照片的md5来判断）
            group_code = group_folder.split(' ')[0]
            self.controller.get_group(group_code)
            self.view.display_group()
        else:
            self._display_default(group_folder)

    def display_arch_and_group_code(self):
        fonds_code = self.ui.fonds_code_in_group.currentText()
        arch_category = self.ui.arch_category_code_in_group.currentText()
        year = self.ui.year_in_group.text()
        retention_period = self.ui.retention_period_in_group.currentText()
        group_sn = self._get_group_sn(year)
        group_code = f'{arch_category}·{year}-{retention_period}-{group_sn}'
        group_arch_code = f'{fonds_code}-{group_code}'
        self.ui.group_code_in_group.setText(group_code)
        self.ui.arch_code_in_group.setText(group_arch_code)

    def save_group(self):
        group_in = GroupInputData()
        for k in group_in.__dict__.keys():
            widget = getattr(self.ui, k+'_in_group')
            if isinstance(widget, QComboBox):
                value = widget.currentText()
            elif isinstance(widget, QTextEdit):
                value = widget.toPlainText()
            else:
                value = widget.text()
            setattr(group_in, k, value)
        self.controller.save_group(group_in)

    def item_click(self, item):
        if item.text(0) == self.current_work_path:
            return
        if item.checkState(0) == Qt.Unchecked:
            item.setCheckState(0, Qt.Checked)
        else:
            item.setCheckState(0, Qt.Unchecked)

    def cancel_folder_item(self):
        item_value = QTreeWidgetItemIterator(self.ui.treeWidget).value()
        if item_value is None:
            return
        child_count = item_value.childCount()
        for i in range(child_count):
            if item_value.child(i).checkState(0) == Qt.Checked:
                item_value.child(i).setCheckState(0, Qt.Unchecked)

    def add_folder_item(self):
        arch_code_info = {
            "root": {},
            "children": {}
        }
        root_item = self.ui.treeWidget.invisibleRootItem().child(0)
        if root_item is None:
            return
        item_iterator = QTreeWidgetItemIterator(self.ui.treeWidget)
        items_value = item_iterator.value()
        for i in range(items_value.childCount()):
            item = items_value.child(i)
            if item.checkState(0) == Qt.Checked:
                path = item.text(0)
                arch_code = self.ui.arch_code_in_group.text()
                group_abspath = os.path.join(self.current_work_path, path)
                arch_code_info["children"].update({group_abspath: arch_code})
        self.mw.interaction.set_arch_code(arch_code_info)
        self._reset_state()

    def _reset_state(self):
        self.ui.radio_btn_group.setExclusive(False)
        for rb in [self.ui.all_photo_radioButton,
                   self.ui.part_recognition_radioButton,
                   self.ui.all_recognition_radioButton]:
            rb.setEnabled(True)
            rb.setChecked(False)
        self.ui.radio_btn_group.setExclusive(True)

        self.ui.recogni_btn.setEnabled(True)

        for label in self.mw.rcn_info_label_dict.values():
            label.clear()
        self.ui.progressBar.setValue(0)
        self.ui.arch_code_in_photo.clear()
        self.ui.photo_view.clear()
        for row in range(self.ui.tableWidget.rowCount(), -1, -1):
            self.ui.tableWidget.removeRow(row)
        self.ui.photo_index_label.clear()

        self.mw.run_state = RecognizeState.stop
        self.ui.pausecontinue_btn.setText('停止')
        self.ui.run_state_label.setText("停止")

        self.ui.verifycheckBox.setCheckState(False)

    def _generate_dir_tree(self, root_arch_info, file_arch_list):
        root_path, root_arch_code = root_arch_info
        _, volume_name = os.path.split(root_path)
        self.ui.treeWidget.setColumnWidth(0, int(520*self.mw.dt_width/1920))  # 设置列宽
        self.ui.treeWidget.clear()
        root = QTreeWidgetItem(self.ui.treeWidget)
        root.setText(0, root_path)
        for name, arch_code in file_arch_list:
            child = QTreeWidgetItem(root)
            child.setText(0, name)
            description_btn = self._gen_description_btn()
            self._connect(description_btn, root_path + '\\' + name)
            self.ui.treeWidget.setItemWidget(child, 1, description_btn)
            child.setFlags(Qt.ItemIsEnabled | Qt.ItemIsUserCheckable)
            child.setCheckState(0, Qt.Checked)
        self.ui.treeWidget.expandAll()

    def _gen_description_btn(self):
        description_btn = QtWidgets.QPushButton(
            ' ',
            self.ui.treeWidget
        )
        font = QFont()
        font.setFamily("新宋体")
        font.setPointSize(14)
        description_btn.setFont(font)
        description_btn.setStyleSheet("text-align: left; padding-left: 18px;")
        description_btn.setFlat(True)
        return description_btn

    def _connect(self, button, path):
        button.clicked.connect(lambda: self.display_group(path))

    def _generate_tree_by_path(self, root_path):
        file_list = filter(lambda p: os.path.isdir(os.path.join(root_path, p)), os.listdir(root_path))
        root_arch_info = (root_path, '')
        file_arch_list = [(fp, '') for fp in file_list]
        self._generate_dir_tree(root_arch_info, file_arch_list)

    def _generate_tree_by_data(self, arch_code_info):
        root_arch = arch_code_info['root']
        root_arch_info = list(root_arch.items())[0]
        root_path = root_arch_info[0]
        children_arch = {p: '' for p in filter(lambda p: os.path.isdir(os.path.join(root_path, p)),
                                               os.listdir(root_path))}
        children_arch.update({(fp[len(root_path)+1:], an) for fp, an in arch_code_info['children'].items()})
        arch_list = children_arch.items()
        self._generate_dir_tree(root_arch_info, arch_list)

    def _display_default(self, group_folder):
        self.ui.group_path_in_group.setText(group_folder)
        self.ui.fonds_code_in_group.setCurrentText(self.setting.fonds_code)
        self.ui.year_in_group.setText(str(datetime.now().year))
        self.ui.arch_category_code_in_group.setCurrentIndex(0)
        self.ui.retention_period_in_group.setCurrentIndex(0)
        self.ui.security_classification_in_group.setCurrentIndex(0)
        self.ui.opening_state_in_group.setCurrentIndex(0)
        self.ui.group_title_in_group.setText(group_folder)
        self.display_arch_and_group_code()

    def _get_group_sn(self, year):
        path = os.path.join(
            self.setting.description_path, '照片档案',
            year, '*', '*'
        )
        group_sn = str(len(glob.glob(path))+1).zfill(4)
        return group_sn
