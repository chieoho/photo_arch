# -*- coding: utf-8 -*-
"""
@file: arch_transfer.py
@desc:
@author: Jaden Wu
@time: 2020/11/22 21:36
"""
from collections import defaultdict
import time
from typing import List
from distutils.dir_util import copy_tree
import os

from dataclasses import dataclass
from PySide2 import QtWidgets, QtCore, QtGui

from photo_arch.infrastructures.user_interface.qt.interaction.utils import (
    static, table_widget_to_xls)
from photo_arch.infrastructures.user_interface.qt.interaction.main_window import (
    MainWindow, Ui_MainWindow)
from photo_arch.infrastructures.user_interface.qt.interaction.setting import Setting

from photo_arch.infrastructures.databases.db_setting import session
from photo_arch.adapters.controller.arch_transfer import Controller, Repo


@dataclass
class Group:
    fonds_code: str = ''
    arch_category_code: str = ''
    group_code: str = ''
    group_title: str = ''
    taken_time: str = ''
    taken_locations: str = ''
    photographer: str = ''
    photo_num: str = ''


@dataclass
class Photo:
    format: str = ''


@dataclass
class Caption:
    title: str = ''
    cd_model: str = ''
    file_type: str = ''
    operation_date: str = ''
    operator: str = ''


@dataclass
class Label:
    fonds_name: str = ''
    fonds_code: str = ''
    group_codes: str = ''
    photo_num: str = ''
    cd_type: str = ''
    cd_num: str = ''


class View(object):
    def __init__(self, mw_: MainWindow):
        self.ui: Ui_MainWindow = mw_.ui

    def _fill_model_from_dict(self, parent, d):
        if isinstance(d, dict):
            for k, v in d.items():
                child = QtGui.QStandardItem(str(k))
                parent.appendRow(child)
                self._fill_model_from_dict(child, v)
        elif isinstance(d, list):
            for v in d:
                self._fill_model_from_dict(parent, v)
        else:
            parent.appendRow(QtGui.QStandardItem(str(d)))

    def display_transfer_arch(self, arch, priority_key='年度'):
        data = defaultdict(lambda: defaultdict(dict))
        for gi in arch:
            fc = gi.get('fonds_code')
            ye = gi.get('year')
            rp = gi.get('retention_period')
            if priority_key == '年度':
                data[fc][ye] = rp
            else:
                data[fc][rp] = ye
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderItem(0, QtGui.QStandardItem("照片档案"))
        self._fill_model_from_dict(model.invisibleRootItem(), data)
        self.ui.arch_tree_view_transfer.setModel(model)
        self.ui.arch_tree_view_transfer.expandAll()

    def get_caption(self):
        caption = Caption()
        for key in caption.__dict__:
            widget = getattr(self.ui, f'{key}_in_transfer')
            if isinstance(widget, QtWidgets.QComboBox):
                setattr(caption, key, widget.currentText())
            elif isinstance(widget, QtWidgets.QLineEdit):
                setattr(caption, key, widget.text())
        return caption

    def display_caption(self, caption: Caption):
        for key in caption.__dict__:
            widget = getattr(self.ui, f'{key}_in_transfer')
            if isinstance(widget, QtWidgets.QComboBox):
                widget.setCurrentText(getattr(caption, key))
            elif isinstance(widget, QtWidgets.QLineEdit):
                widget.setText(getattr(caption, key))

    def get_label(self):
        label = Label()
        for key in label.__dict__:
            widget = getattr(self.ui, f'{key}_in_transfer')
            if isinstance(widget, QtWidgets.QComboBox):
                setattr(label, key, widget.currentText())
            elif isinstance(widget, QtWidgets.QLineEdit):
                setattr(label, key, widget.text())
        return label

    def display_label(self, label: Label):
        for key in label.__dict__:
            widget = getattr(self.ui, f'{key}_in_transfer')
            if isinstance(widget, QtWidgets.QComboBox):
                widget.setCurrentText(getattr(label, key))
            elif isinstance(widget, QtWidgets.QLineEdit):
                widget.setText(getattr(label, key))


class ArchTransfer(object):
    def __init__(self, mw_: MainWindow, setting: Setting):
        self.mw = mw_
        self.ui: Ui_MainWindow = mw_.ui
        self.setting = setting
        self.controller = Controller(Repo(session))
        self.view = View(mw_)

        self.disk_icon_path = './icon/arch_cd.png'
        self.selected_condition_list = []
        self.partition_list: List[dict] = []
        self.cd_info_dict = defaultdict(dict)
        self.current_cd = ''

        self.ui.partition_list_widget.setViewMode(QtWidgets.QListWidget.IconMode)
        self.ui.partition_list_widget.setIconSize(QtCore.QSize(160, 160))
        self.ui.partition_list_widget.setFixedHeight(218)
        self.ui.partition_list_widget.setWrapping(False)  # 只一行显示

        self.ui.order_combobox_transfer.currentTextChanged.connect(static(self.display_arch))
        self.ui.arch_tree_view_transfer.doubleClicked.connect(static(self.select_arch))
        self.ui.selected_arch_list_widget.itemDoubleClicked.connect(static(self.unselect_arch))
        self.ui.cd_size_line_edit.returnPressed.connect(static(self.partition))
        self.ui.across_year_combo_box.currentTextChanged.connect(static(self.partition))
        self.ui.across_period_combo_box.currentTextChanged.connect(static(self.partition))
        self.ui.partition_list_widget.itemSelectionChanged.connect(static(self.display_cd_info))
        self.ui.packeage_btn.clicked.connect(static(self.package))

        catalog_tw = self.ui.cd_catalog_table_widget
        catalog_tw.verticalHeader().setVisible(True)
        catalog_tw.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        catalog_tw.horizontalHeader().setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

    def display_arch(self, priority_key):
        _, arch = self.controller.list_arch()
        self.view.display_transfer_arch(arch, priority_key)

    def select_arch(self, index):
        if index.child(0, 0).data():  # 点击的不是叶子则返回
            return
        parent_index = index.parent()
        fonds_code_index = parent_index.parent()
        selected_name1 = '-'.join([fonds_code_index.data(), parent_index.data(), index.data()])
        selected_name2 = '-'.join([fonds_code_index.data(), index.data(), parent_index.data()])
        if (selected_name1 in self.selected_condition_list) or \
                (selected_name2 in self.selected_condition_list):
            return
        item = QtWidgets.QListWidgetItem(selected_name1)
        self.ui.selected_arch_list_widget.addItem(item)
        self.selected_condition_list.append(selected_name1)
        self.partition()

    def unselect_arch(self, item):
        row = self.ui.selected_arch_list_widget.row(item)
        self.ui.selected_arch_list_widget.takeItem(row)
        item_text = item.text()
        if item_text in self.selected_condition_list:
            self.selected_condition_list.remove(item_text)
        self.partition()

    def partition(self):
        self.cd_info_dict.clear()
        self.ui.partition_list_widget.clear()
        cd_size = float(self.ui.cd_size_line_edit.text()) * 1024
        if (not cd_size) or (not self.selected_condition_list):
            return
        selected_group_list = self._get_selected_group()
        self.partition_list = []
        selected_cond, used_size, group_list = '', 0, []
        for sc_sgl in selected_group_list:
            selected_cond, sgl = sc_sgl
            for gi in sgl:
                folder_size = float(gi['folder_size'])
                # 组大小大于或等于光盘容量
                if folder_size >= cd_size:
                    for _ in range(int(folder_size//cd_size) + 1):
                        partition = {'group_list': [gi], 'selected_cond': selected_cond}
                        self.partition_list.append(partition)
                # 组大小小于光盘容量
                else:
                    used_size += folder_size
                    if used_size < cd_size:
                        group_list.append(gi)
                    else:
                        used_size -= folder_size
                        partition = {"used_size": used_size, 'group_list': group_list, 'selected_cond': selected_cond}
                        self.partition_list.append(partition)
                        used_size, group_list = 0, []
                        used_size += folder_size
                        group_list.append(gi)
            if used_size > 0:
                partition = {"used_size": used_size, 'group_list': group_list, 'selected_cond': selected_cond}
                self.partition_list.append(partition)

        self._display_partition_res()

    def _get_selected_group(self):
        selected_group_list = []
        for sc in self.selected_condition_list:
            fc, x1, x2 = sc.split('-')
            if x1.isdigit():
                ye, rp = x1, x2
            else:
                rp, ye = x1, x2
            _, archives = self.controller.get_selected_arch(fc, ye, rp)
            selected_group_list.append((sc, archives))
        return selected_group_list

    def _display_partition_res(self):
        for i, p in enumerate(self.partition_list, 1):
            item = QtWidgets.QListWidgetItem(QtGui.QIcon(self.disk_icon_path), f'{p["selected_cond"]} {i}号')
            self.ui.partition_list_widget.addItem(item)

    def display_cd_info(self):
        selected_items = self.ui.partition_list_widget.selectedItems()
        if selected_items:
            item = selected_items[0]
            row = self.ui.partition_list_widget.row(item)
            group_list = self.partition_list[row]['group_list']
            self._display_cd_catalog(group_list)

            cd_name = item.text()
            self._keep_tmp(self.current_cd)
            caption = self.cd_info_dict[cd_name].get('caption')
            label = self.cd_info_dict[cd_name].get('label')
            if caption:
                self.view.display_caption(caption)
                self.view.display_label(label)
            else:
                self._display_default_caption()
                self._display_default_label(row)
            self.current_cd = cd_name
        else:
            self._clear_data()
            self.current_cd = ''

    def _keep_tmp(self, current_cd):
        if not current_cd:
            return
        self.cd_info_dict[current_cd]['caption'] = self.view.get_caption()
        self.cd_info_dict[current_cd]['label'] = self.view.get_label()

    def _clear_data(self):
        for i in range(self.ui.cd_catalog_table_widget.rowCount(), -1, -1):
            self.ui.cd_catalog_table_widget.removeRow(i)

        self.ui.title_in_transfer.setText('')
        self.ui.group_codes_in_transfer.setText('')
        self.ui.photo_num_in_transfer.setText('')
        self.ui.cd_num_in_transfer.setText('')

    def _display_cd_catalog(self, group_list):
        for i in range(self.ui.cd_catalog_table_widget.rowCount(), -1, -1):
            self.ui.cd_catalog_table_widget.removeRow(i)
        for row, gi in enumerate(group_list):
            self.ui.cd_catalog_table_widget.insertRow(row)
            _, pi = self.controller.get_photo(gi['group_code'] + '-0001')
            group_dict = Group().__dict__
            photo_dict = Photo().__dict__
            columns = {**group_dict, **photo_dict}
            for col, key in enumerate(columns):
                if key in group_dict:
                    item_text = gi.get(key, '')
                else:
                    item_text = pi.get(key, '')
                item = QtWidgets.QTableWidgetItem(str(item_text))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.ui.cd_catalog_table_widget.setItem(row, col, item)

    def _display_default_caption(self):
        operation_date = time.strftime('%Y%m%d')
        self.ui.operation_date_in_transfer.setText(operation_date)
        self.ui.operator_in_transfer.setText(self.setting.fonds_name)

    def _display_default_label(self, row):
        self.ui.fonds_name_in_transfer.setText(self.setting.fonds_name)
        self.ui.fonds_code_in_transfer.setText(self.setting.fonds_code)
        group_list = self.partition_list[row]['group_list']
        if not group_list:
            return
        start_group_code = group_list[0]['group_code']
        end_group_code = group_list[-1]['group_code']
        self.ui.group_codes_in_transfer.setText(f'{start_group_code} 至 {end_group_code}')
        total_num = sum(map(lambda g: int(g['photo_num']), group_list))
        self.ui.photo_num_in_transfer.setText(str(total_num))
        self.ui.cd_num_in_transfer.setText(f'{row+1}号')

    def package(self):
        for r in range(self.ui.partition_list_widget.count()):
            item = self.ui.partition_list_widget.item(r)
            item.setSelected(True)
            cd_name = item.text()
            cd_path = os.path.join(self.setting.package_path, cd_name)
            group_list = self.partition_list[r]['group_list']
            for gi in group_list:
                group_name = gi['group_path']
                src_abspath = os.path.join(
                    self.setting.description_path,
                    '照片档案',
                    gi['year'],
                    gi['retention_period'],
                    group_name)
                dst_abspath = os.path.join(cd_path, group_name)
                copy_tree(src_abspath, dst_abspath)
            self._gen_catalog_file(cd_path)
            self._gen_caption_file(cd_name, cd_path)
            self._gen_label_file(cd_name, cd_path)
        self.mw.msg_box('打包成功', 'info')

    def _gen_catalog_file(self, cd_path):
        xls_name = '目录.xls'
        xls_path = os.path.join(cd_path, xls_name)
        table_widget_to_xls(self.ui.cd_catalog_table_widget, xls_path)

    def _gen_caption_file(self, cd_name, cd_path):
        caption = self.cd_info_dict[cd_name]['caption']
        caption_text = self._gen_caption_text(caption)
        with open(os.path.join(cd_path, 'SM.txt'), 'wb') as fw:
            fw.write(caption_text.encode())

    def _gen_label_file(self, cd_name, cd_path):
        label = self.cd_info_dict[cd_name]['label']
        label_text = self._gen_label_text(label)
        with open(os.path.join(cd_path, '标签.txt'), 'wb') as fw:
            fw.write(label_text.encode())

    def _gen_caption_text(self, cap: Caption):
        _ = self
        title = f'题名：{cap.title}；'
        cd_model = f'光盘型号：{cap.cd_model}；'
        file_type = f'文件类型：照片 {cap.file_type}；'
        operation_date = f'制作时间：{cap.operation_date}；'
        operator = f'制作人：{cap.operator}。'
        caption_text = '\n'.join([title, cd_model, file_type, operation_date, operator])
        return caption_text

    def _gen_label_text(self, label: Label):
        _ = self
        fonds_name = f'     全宗名称：{label.fonds_name}'
        fonds_code = f'     全宗号：{label.fonds_code}'
        group_codes = f'起止组号：{label.group_codes}'
        photo_num = f'张/件数：{label.photo_num}张'
        cd_type = f'光盘类型：{label.cd_type}'
        cd_num = f'盘号：{label.cd_num}'
        label_text = '\n'.join([fonds_name, fonds_code, '\n'*5, group_codes, photo_num, cd_type, cd_num])
        return label_text
