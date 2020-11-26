# -*- coding: utf-8 -*-
"""
@file: setting.py
@desc:
@author: Jaden Wu
@time: 2020/11/23 9:58
"""
import os

from photo_arch.infrastructures.user_interface.qt.interaction.main_window import (
    MainWindow, Ui_MainWindow)

from photo_arch.infrastructures.databases.db_setting import engine, make_session
from photo_arch.adapters.sql.repo import Repo
from photo_arch.adapters.controller.setting import Controller
from photo_arch.adapters.presenter.setting import Presenter
from photo_arch.adapters.view_model.setting import ViewModel


class View(object):
    def __init__(self, mw_: MainWindow, view_model: ViewModel):
        self.mw = mw_
        self.view_model = view_model

    def display_setting(self, description_path, package_path):
        self.mw.ui.description_path_line_edit.setText(description_path)
        self.mw.ui.package_path_line_edit.setText(package_path)


class Setting(object):
    def __init__(self, mw_: MainWindow):
        self.mw = mw_
        self.ui: Ui_MainWindow = mw_.ui
        self.view_model = ViewModel()
        self.presenter = Presenter(self.view_model)
        self.controller = Controller(Repo(make_session(engine)), self.presenter)
        self.view = View(mw_, self.view_model)

        self.description_path = ''
        self.package_path = ''
        self.fonds_code = ''

        self._get_setting()

    def _get_setting(self):
        self.description_path = os.path.abspath(r'.\已著录')
        self.package_path = os.path.abspath(r'.\已打包')
        self.fonds_code = 'A1'

        self.view.display_setting(
            self.description_path,
            self.package_path
        )
