# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1126, 905)
        MainWindow.setMinimumSize(QSize(1, 1))
        font = QFont()
        font.setFamily(u"\u65b0\u5b8b\u4f53")
        font.setPointSize(14)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u"icon/archives.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        MainWindow.setIconSize(QSize(24, 24))
        self.actionexit = QAction(MainWindow)
        self.actionexit.setObjectName(u"actionexit")
        self.action = QAction(MainWindow)
        self.action.setObjectName(u"action")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_24 = QGridLayout(self.centralwidget)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet(u"QTabBar::tab{\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"    background-color: rgb(83, 166, 249);\n"
"}")
        self.tabWidget.setIconSize(QSize(24, 24))
        self.group_tab = QWidget()
        self.group_tab.setObjectName(u"group_tab")
        self.group_tab.setFont(font)
        self.gridLayout_5 = QGridLayout(self.group_tab)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.splitter = QSplitter(self.group_tab)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Horizontal)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(500, 0))
        self.gridLayout_6 = QGridLayout(self.widget)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, -1, 12, -1)
        self.dir_lineEdit = QLineEdit(self.widget)
        self.dir_lineEdit.setObjectName(u"dir_lineEdit")
        self.dir_lineEdit.setMinimumSize(QSize(0, 23))
        self.dir_lineEdit.setFont(font)
        self.dir_lineEdit.setReadOnly(True)

        self.gridLayout_6.addWidget(self.dir_lineEdit, 0, 1, 1, 1)

        self.open_dir_btn = QPushButton(self.widget)
        self.open_dir_btn.setObjectName(u"open_dir_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.open_dir_btn.sizePolicy().hasHeightForWidth())
        self.open_dir_btn.setSizePolicy(sizePolicy2)
        self.open_dir_btn.setFont(font)
        self.open_dir_btn.setStyleSheet(u"padding:8px 18px;")
        icon1 = QIcon()
        icon1.addFile(u"icon/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.open_dir_btn.setIcon(icon1)
        self.open_dir_btn.setIconSize(QSize(24, 24))

        self.gridLayout_6.addWidget(self.open_dir_btn, 0, 2, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout_6.addWidget(self.label, 0, 0, 1, 1)

        self.tree_widget_group = QTreeWidget(self.widget)
        font1 = QFont()
        font1.setFamily(u"\u65b0\u5b8b\u4f53")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"\u6587\u4ef6\u5939");
        __qtreewidgetitem.setFont(0, font1);
        self.tree_widget_group.setHeaderItem(__qtreewidgetitem)
        self.tree_widget_group.setObjectName(u"tree_widget_group")
        self.tree_widget_group.setFont(font)
        self.tree_widget_group.setStyleSheet(u"")
        self.tree_widget_group.setFrameShape(QFrame.StyledPanel)
        self.tree_widget_group.setLineWidth(2)
        self.tree_widget_group.setMidLineWidth(2)
        self.tree_widget_group.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tree_widget_group.setSelectionMode(QAbstractItemView.SingleSelection)

        self.gridLayout_6.addWidget(self.tree_widget_group, 1, 0, 1, 3)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 50))
        self.frame_3.setFont(font)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_3)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(-1, 3, -1, 3)
        self.cancel_folder_btn = QPushButton(self.frame_3)
        self.cancel_folder_btn.setObjectName(u"cancel_folder_btn")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.cancel_folder_btn.sizePolicy().hasHeightForWidth())
        self.cancel_folder_btn.setSizePolicy(sizePolicy3)
        self.cancel_folder_btn.setMinimumSize(QSize(0, 0))
        self.cancel_folder_btn.setMaximumSize(QSize(280, 16777215))
        self.cancel_folder_btn.setFont(font)
        self.cancel_folder_btn.setFocusPolicy(Qt.NoFocus)
        self.cancel_folder_btn.setStyleSheet(u"padding-left: 30px; \n"
"padding-right: 30px;\n"
"padding-top: 8px; \n"
"padding-bottom: 8px;")
        icon2 = QIcon()
        icon2.addFile(u"icon/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cancel_folder_btn.setIcon(icon2)
        self.cancel_folder_btn.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.cancel_folder_btn, 0, 3, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_5, 0, 0, 1, 1)

        self.add_folder_btn = QPushButton(self.frame_3)
        self.add_folder_btn.setObjectName(u"add_folder_btn")
        sizePolicy3.setHeightForWidth(self.add_folder_btn.sizePolicy().hasHeightForWidth())
        self.add_folder_btn.setSizePolicy(sizePolicy3)
        self.add_folder_btn.setMinimumSize(QSize(0, 0))
        self.add_folder_btn.setMaximumSize(QSize(280, 16777215))
        self.add_folder_btn.setFont(font)
        self.add_folder_btn.setFocusPolicy(Qt.NoFocus)
        self.add_folder_btn.setStyleSheet(u"padding-left: 30px; \n"
"padding-right: 30px;\n"
"padding-top: 8px; \n"
"padding-bottom: 8px;")
        icon3 = QIcon()
        icon3.addFile(u"icon/add_file.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_folder_btn.setIcon(icon3)
        self.add_folder_btn.setIconSize(QSize(24, 24))

        self.gridLayout_7.addWidget(self.add_folder_btn, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_2, 0, 2, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_6, 0, 4, 1, 1)


        self.gridLayout_6.addWidget(self.frame_3, 3, 0, 1, 3)

        self.adding_processing = QLabel(self.widget)
        self.adding_processing.setObjectName(u"adding_processing")
        self.adding_processing.setMinimumSize(QSize(0, 45))

        self.gridLayout_6.addWidget(self.adding_processing, 2, 0, 1, 3)

        self.splitter.addWidget(self.widget)
        self.group_description_widget = QWidget(self.splitter)
        self.group_description_widget.setObjectName(u"group_description_widget")
        sizePolicy3.setHeightForWidth(self.group_description_widget.sizePolicy().hasHeightForWidth())
        self.group_description_widget.setSizePolicy(sizePolicy3)
        self.group_description_widget.setMinimumSize(QSize(300, 0))
        self.group_description_widget.setMaximumSize(QSize(1200, 16777215))
        self.group_description_widget.setFont(font)
        self.gridLayout_8 = QGridLayout(self.group_description_widget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(12, -1, -1, -1)
        self.year_in_group = QLineEdit(self.group_description_widget)
        self.year_in_group.setObjectName(u"year_in_group")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.year_in_group.sizePolicy().hasHeightForWidth())
        self.year_in_group.setSizePolicy(sizePolicy4)
        self.year_in_group.setFont(font)

        self.gridLayout_8.addWidget(self.year_in_group, 4, 4, 1, 1)

        self.reference_code_in_group = QLineEdit(self.group_description_widget)
        self.reference_code_in_group.setObjectName(u"reference_code_in_group")
        sizePolicy4.setHeightForWidth(self.reference_code_in_group.sizePolicy().hasHeightForWidth())
        self.reference_code_in_group.setSizePolicy(sizePolicy4)
        self.reference_code_in_group.setFont(font)

        self.gridLayout_8.addWidget(self.reference_code_in_group, 10, 4, 1, 1)

        self.taken_time_in_group = QLineEdit(self.group_description_widget)
        self.taken_time_in_group.setObjectName(u"taken_time_in_group")
        sizePolicy4.setHeightForWidth(self.taken_time_in_group.sizePolicy().hasHeightForWidth())
        self.taken_time_in_group.setSizePolicy(sizePolicy4)
        self.taken_time_in_group.setFont(font)

        self.gridLayout_8.addWidget(self.taken_time_in_group, 8, 4, 1, 1)

        self.horizontalSpacer_24 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_24, 3, 2, 1, 1)

        self.group_title_in_group = QLineEdit(self.group_description_widget)
        self.group_title_in_group.setObjectName(u"group_title_in_group")
        sizePolicy4.setHeightForWidth(self.group_title_in_group.sizePolicy().hasHeightForWidth())
        self.group_title_in_group.setSizePolicy(sizePolicy4)
        self.group_title_in_group.setFont(font)

        self.gridLayout_8.addWidget(self.group_title_in_group, 2, 1, 1, 4)

        self.label_21 = QLabel(self.group_description_widget)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(120, 16777215))
        self.label_21.setFont(font)
        self.label_21.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_21, 5, 0, 1, 1)

        self.group_code_in_group = QLineEdit(self.group_description_widget)
        self.group_code_in_group.setObjectName(u"group_code_in_group")
        sizePolicy4.setHeightForWidth(self.group_code_in_group.sizePolicy().hasHeightForWidth())
        self.group_code_in_group.setSizePolicy(sizePolicy4)
        self.group_code_in_group.setFont(font)

        self.gridLayout_8.addWidget(self.group_code_in_group, 5, 4, 1, 1)

        self.saving_processing = QLabel(self.group_description_widget)
        self.saving_processing.setObjectName(u"saving_processing")
        sizePolicy3.setHeightForWidth(self.saving_processing.sizePolicy().hasHeightForWidth())
        self.saving_processing.setSizePolicy(sizePolicy3)
        self.saving_processing.setMinimumSize(QSize(0, 45))

        self.gridLayout_8.addWidget(self.saving_processing, 14, 0, 1, 5)

        self.fonds_code_in_group = QLineEdit(self.group_description_widget)
        self.fonds_code_in_group.setObjectName(u"fonds_code_in_group")
        self.fonds_code_in_group.setFont(font)
        self.fonds_code_in_group.setReadOnly(True)

        self.gridLayout_8.addWidget(self.fonds_code_in_group, 3, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_6, 1, 1, 1, 1)

        self.taken_locations_in_group = QLineEdit(self.group_description_widget)
        self.taken_locations_in_group.setObjectName(u"taken_locations_in_group")
        sizePolicy4.setHeightForWidth(self.taken_locations_in_group.sizePolicy().hasHeightForWidth())
        self.taken_locations_in_group.setSizePolicy(sizePolicy4)
        self.taken_locations_in_group.setFont(font)

        self.gridLayout_8.addWidget(self.taken_locations_in_group, 9, 1, 1, 1)

        self.opening_state_in_group = QComboBox(self.group_description_widget)
        self.opening_state_in_group.addItem("")
        self.opening_state_in_group.addItem("")
        self.opening_state_in_group.addItem("")
        self.opening_state_in_group.setObjectName(u"opening_state_in_group")
        self.opening_state_in_group.setFont(font)

        self.gridLayout_8.addWidget(self.opening_state_in_group, 11, 1, 1, 1)

        self.label_42 = QLabel(self.group_description_widget)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMaximumSize(QSize(120, 16777215))
        self.label_42.setFont(font)
        self.label_42.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_42, 9, 0, 1, 1)

        self.label_23 = QLabel(self.group_description_widget)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(120, 16777215))
        self.label_23.setFont(font)
        self.label_23.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_23, 2, 0, 1, 1)

        self.frame_4 = QFrame(self.group_description_widget)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy3.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy3)
        self.frame_4.setMinimumSize(QSize(0, 50))
        self.frame_4.setFont(font)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_4)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(-1, 3, -1, 3)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_8, 0, 0, 1, 1)

        self.save_group_btn = QPushButton(self.frame_4)
        self.save_group_btn.setObjectName(u"save_group_btn")
        sizePolicy3.setHeightForWidth(self.save_group_btn.sizePolicy().hasHeightForWidth())
        self.save_group_btn.setSizePolicy(sizePolicy3)
        self.save_group_btn.setMinimumSize(QSize(0, 40))
        self.save_group_btn.setFont(font)
        self.save_group_btn.setStyleSheet(u"padding-left: 30px; \n"
"padding-right: 30px;\n"
"padding-top: 8px; \n"
"padding-bottom: 8px;")
        icon4 = QIcon()
        icon4.addFile(u"icon/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_group_btn.setIcon(icon4)
        self.save_group_btn.setIconSize(QSize(24, 24))

        self.gridLayout_13.addWidget(self.save_group_btn, 0, 1, 1, 1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_13.addItem(self.horizontalSpacer_11, 0, 2, 1, 1)


        self.gridLayout_8.addWidget(self.frame_4, 15, 0, 1, 5)

        self.photo_num_in_group = QLineEdit(self.group_description_widget)
        self.photo_num_in_group.setObjectName(u"photo_num_in_group")
        sizePolicy4.setHeightForWidth(self.photo_num_in_group.sizePolicy().hasHeightForWidth())
        self.photo_num_in_group.setSizePolicy(sizePolicy4)
        self.photo_num_in_group.setFont(font)

        self.gridLayout_8.addWidget(self.photo_num_in_group, 9, 4, 1, 1)

        self.label_24 = QLabel(self.group_description_widget)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font)
        self.label_24.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_24, 7, 3, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_8.addItem(self.verticalSpacer_7, 1, 4, 1, 1)

        self.label_26 = QLabel(self.group_description_widget)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)
        self.label_26.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_26, 8, 3, 1, 1)

        self.folder_size_in_group = QLineEdit(self.group_description_widget)
        self.folder_size_in_group.setObjectName(u"folder_size_in_group")
        sizePolicy4.setHeightForWidth(self.folder_size_in_group.sizePolicy().hasHeightForWidth())
        self.folder_size_in_group.setSizePolicy(sizePolicy4)
        self.folder_size_in_group.setFont(font)

        self.gridLayout_8.addWidget(self.folder_size_in_group, 7, 4, 1, 1)

        self.label_46 = QLabel(self.group_description_widget)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setMaximumSize(QSize(120, 16777215))
        self.label_46.setFont(font)
        self.label_46.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_46, 11, 0, 1, 1)

        self.retention_period_in_group = QComboBox(self.group_description_widget)
        self.retention_period_in_group.addItem("")
        self.retention_period_in_group.addItem("")
        self.retention_period_in_group.addItem("")
        self.retention_period_in_group.setObjectName(u"retention_period_in_group")
        self.retention_period_in_group.setFont(font)

        self.gridLayout_8.addWidget(self.retention_period_in_group, 4, 1, 1, 1)

        self.security_classification_in_group = QComboBox(self.group_description_widget)
        self.security_classification_in_group.addItem("")
        self.security_classification_in_group.addItem("")
        self.security_classification_in_group.addItem("")
        self.security_classification_in_group.addItem("")
        self.security_classification_in_group.addItem("")
        self.security_classification_in_group.setObjectName(u"security_classification_in_group")
        self.security_classification_in_group.setFont(font)

        self.gridLayout_8.addWidget(self.security_classification_in_group, 10, 1, 1, 1)

        self.arch_category_code_in_group = QComboBox(self.group_description_widget)
        self.arch_category_code_in_group.addItem("")
        self.arch_category_code_in_group.addItem("")
        self.arch_category_code_in_group.addItem("")
        self.arch_category_code_in_group.setObjectName(u"arch_category_code_in_group")
        self.arch_category_code_in_group.setFont(font)

        self.gridLayout_8.addWidget(self.arch_category_code_in_group, 3, 4, 1, 1)

        self.label_18 = QLabel(self.group_description_widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMaximumSize(QSize(120, 16777215))
        self.label_18.setFont(font)
        self.label_18.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_18, 4, 0, 1, 1)

        self.label_17 = QLabel(self.group_description_widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)
        self.label_17.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_17, 4, 3, 1, 1)

        self.label_43 = QLabel(self.group_description_widget)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font)
        self.label_43.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_43, 9, 3, 1, 1)

        self.author_in_group = QLineEdit(self.group_description_widget)
        self.author_in_group.setObjectName(u"author_in_group")
        sizePolicy4.setHeightForWidth(self.author_in_group.sizePolicy().hasHeightForWidth())
        self.author_in_group.setSizePolicy(sizePolicy4)

        self.gridLayout_8.addWidget(self.author_in_group, 7, 1, 1, 1)

        self.label_22 = QLabel(self.group_description_widget)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setFont(font)
        self.label_22.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_22, 12, 0, 1, 1)

        self.label_3 = QLabel(self.group_description_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(120, 16777215))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_27 = QLabel(self.group_description_widget)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setMaximumSize(QSize(120, 16777215))
        self.label_27.setFont(font)
        self.label_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_27, 8, 0, 1, 1)

        self.label_44 = QLabel(self.group_description_widget)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setMaximumSize(QSize(120, 16777215))
        self.label_44.setFont(font)
        self.label_44.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_44, 10, 0, 1, 1)

        self.group_caption_in_group = QTextEdit(self.group_description_widget)
        self.group_caption_in_group.setObjectName(u"group_caption_in_group")
        self.group_caption_in_group.setFont(font)

        self.gridLayout_8.addWidget(self.group_caption_in_group, 13, 0, 1, 5)

        self.label_25 = QLabel(self.group_description_widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMaximumSize(QSize(120, 16777215))
        self.label_25.setFont(font)
        self.label_25.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_25, 7, 0, 1, 1)

        self.photographer_in_group = QLineEdit(self.group_description_widget)
        self.photographer_in_group.setObjectName(u"photographer_in_group")
        sizePolicy4.setHeightForWidth(self.photographer_in_group.sizePolicy().hasHeightForWidth())
        self.photographer_in_group.setSizePolicy(sizePolicy4)

        self.gridLayout_8.addWidget(self.photographer_in_group, 8, 1, 1, 1)

        self.label_45 = QLabel(self.group_description_widget)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font)
        self.label_45.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_45, 10, 3, 1, 1)

        self.department_in_group = QLineEdit(self.group_description_widget)
        self.department_in_group.setObjectName(u"department_in_group")
        sizePolicy4.setHeightForWidth(self.department_in_group.sizePolicy().hasHeightForWidth())
        self.department_in_group.setSizePolicy(sizePolicy4)

        self.gridLayout_8.addWidget(self.department_in_group, 5, 1, 1, 1)

        self.label_20 = QLabel(self.group_description_widget)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font)
        self.label_20.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_20, 5, 3, 1, 1)

        self.label_16 = QLabel(self.group_description_widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)
        self.label_16.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_16, 3, 3, 1, 1)

        self.frame = QFrame(self.group_description_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 65))
        self.frame.setFont(font)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.frame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(-1, 3, -1, 3)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(120, 16777215))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_2, 0, 0, 1, 1)

        self.group_path_in_group = QLabel(self.frame)
        self.group_path_in_group.setObjectName(u"group_path_in_group")
        self.group_path_in_group.setFont(font)

        self.gridLayout_11.addWidget(self.group_path_in_group, 0, 1, 1, 2)

        self.label_47 = QLabel(self.frame)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setMaximumSize(QSize(120, 16777215))
        self.label_47.setFont(font)
        self.label_47.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_11.addWidget(self.label_47, 1, 0, 1, 1)

        self.horizontalSpacer_15 = QSpacerItem(20, 20, QSizePolicy.MinimumExpanding, QSizePolicy.Minimum)

        self.gridLayout_11.addItem(self.horizontalSpacer_15, 1, 2, 1, 1)

        self.arch_code_in_group = QLabel(self.frame)
        self.arch_code_in_group.setObjectName(u"arch_code_in_group")
        sizePolicy4.setHeightForWidth(self.arch_code_in_group.sizePolicy().hasHeightForWidth())
        self.arch_code_in_group.setSizePolicy(sizePolicy4)
        self.arch_code_in_group.setFont(font)

        self.gridLayout_11.addWidget(self.arch_code_in_group, 1, 1, 1, 1)


        self.gridLayout_8.addWidget(self.frame, 0, 0, 1, 5)

        self.splitter.addWidget(self.group_description_widget)

        self.gridLayout_5.addWidget(self.splitter, 0, 0, 1, 1)

        icon5 = QIcon()
        icon5.addFile(u"icon/dirtree.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.group_tab, icon5, "")
        self.recognition_tab = QWidget()
        self.recognition_tab.setObjectName(u"recognition_tab")
        self.recognition_tab.setFont(font)
        self.gridLayout = QGridLayout(self.recognition_tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame_2 = QFrame(self.recognition_tab)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFont(font)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 0, 2, 1, 1)

        self.pausecontinue_btn = QPushButton(self.frame_2)
        self.pausecontinue_btn.setObjectName(u"pausecontinue_btn")
        sizePolicy3.setHeightForWidth(self.pausecontinue_btn.sizePolicy().hasHeightForWidth())
        self.pausecontinue_btn.setSizePolicy(sizePolicy3)
        self.pausecontinue_btn.setMinimumSize(QSize(0, 0))
        self.pausecontinue_btn.setMaximumSize(QSize(280, 16777215))
        self.pausecontinue_btn.setFont(font)
        self.pausecontinue_btn.setFocusPolicy(Qt.NoFocus)
        self.pausecontinue_btn.setStyleSheet(u"padding-left: 30px; \n"
"padding-right: 30px;\n"
"padding-top: 8px; \n"
"padding-bottom: 8px;")
        icon6 = QIcon()
        icon6.addFile(u"icon/stop.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pausecontinue_btn.setIcon(icon6)
        self.pausecontinue_btn.setIconSize(QSize(24, 24))

        self.gridLayout_4.addWidget(self.pausecontinue_btn, 0, 3, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_3, 0, 0, 1, 1)

        self.recogni_btn = QPushButton(self.frame_2)
        self.recogni_btn.setObjectName(u"recogni_btn")
        sizePolicy3.setHeightForWidth(self.recogni_btn.sizePolicy().hasHeightForWidth())
        self.recogni_btn.setSizePolicy(sizePolicy3)
        self.recogni_btn.setMinimumSize(QSize(0, 0))
        self.recogni_btn.setMaximumSize(QSize(280, 16777215))
        self.recogni_btn.setFont(font)
        self.recogni_btn.setFocusPolicy(Qt.NoFocus)
        self.recogni_btn.setStyleSheet(u"padding-left: 30px; \n"
"padding-right: 30px;\n"
"padding-top: 8px; \n"
"padding-bottom: 8px;")
        icon7 = QIcon()
        icon7.addFile(u"icon/run.png", QSize(), QIcon.Normal, QIcon.Off)
        self.recogni_btn.setIcon(icon7)
        self.recogni_btn.setIconSize(QSize(24, 24))

        self.gridLayout_4.addWidget(self.recogni_btn, 0, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_4, 0, 4, 1, 1)


        self.gridLayout.addWidget(self.frame_2, 10, 0, 1, 4)

        self.label_9 = QLabel(self.recognition_tab)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(0, 35))
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_9, 5, 1, 1, 1)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_9, 2, 3, 1, 1)

        self.recognition_rate_label = QLabel(self.recognition_tab)
        self.recognition_rate_label.setObjectName(u"recognition_rate_label")
        self.recognition_rate_label.setFont(font)

        self.gridLayout.addWidget(self.recognition_rate_label, 3, 2, 1, 1)

        self.label_13 = QLabel(self.recognition_tab)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_13, 2, 1, 1, 1)

        self.label_7 = QLabel(self.recognition_tab)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 35))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_7, 7, 1, 1, 1)

        self.recognized_face_label = QLabel(self.recognition_tab)
        self.recognized_face_label.setObjectName(u"recognized_face_label")
        self.recognized_face_label.setFont(font)

        self.gridLayout.addWidget(self.recognized_face_label, 4, 2, 1, 1)

        self.progressBar = QProgressBar(self.recognition_tab)
        self.progressBar.setObjectName(u"progressBar")
        sizePolicy4.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy4)
        self.progressBar.setMaximumSize(QSize(16777215, 16777215))
        self.progressBar.setFont(font)
        self.progressBar.setValue(0)

        self.gridLayout.addWidget(self.progressBar, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 9, 1, 1, 1)

        self.label_10 = QLabel(self.recognition_tab)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 35))
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_10, 6, 1, 1, 1)

        self.run_state_label = QLabel(self.recognition_tab)
        self.run_state_label.setObjectName(u"run_state_label")
        self.run_state_label.setFont(font)

        self.gridLayout.addWidget(self.run_state_label, 1, 2, 1, 1)

        self.handled_photo_label = QLabel(self.recognition_tab)
        self.handled_photo_label.setObjectName(u"handled_photo_label")
        self.handled_photo_label.setFont(font)

        self.gridLayout.addWidget(self.handled_photo_label, 7, 2, 1, 1)

        self.all_recognized_photo_label = QLabel(self.recognition_tab)
        self.all_recognized_photo_label.setObjectName(u"all_recognized_photo_label")
        self.all_recognized_photo_label.setFont(font)

        self.gridLayout.addWidget(self.all_recognized_photo_label, 6, 2, 1, 1)

        self.label_6 = QLabel(self.recognition_tab)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 35))
        self.label_6.setFont(font)
        self.label_6.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1)

        self.part_recognized_photo_label = QLabel(self.recognition_tab)
        self.part_recognized_photo_label.setObjectName(u"part_recognized_photo_label")
        self.part_recognized_photo_label.setFont(font)

        self.gridLayout.addWidget(self.part_recognized_photo_label, 5, 2, 1, 1)

        self.unhandled_photo_label = QLabel(self.recognition_tab)
        self.unhandled_photo_label.setObjectName(u"unhandled_photo_label")
        self.unhandled_photo_label.setFont(font)

        self.gridLayout.addWidget(self.unhandled_photo_label, 8, 2, 1, 1)

        self.label_11 = QLabel(self.recognition_tab)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 35))
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_11, 8, 1, 1, 1)

        self.label_19 = QLabel(self.recognition_tab)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setMinimumSize(QSize(0, 35))
        self.label_19.setMaximumSize(QSize(16777215, 16777215))
        self.label_19.setFont(font)
        self.label_19.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_19, 1, 1, 1, 1)

        self.label_8 = QLabel(self.recognition_tab)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 35))
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_8, 4, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        icon8 = QIcon()
        icon8.addFile(u"icon/face.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.recognition_tab, icon8, "")
        self.photo_tab = QWidget()
        self.photo_tab.setObjectName(u"photo_tab")
        self.photo_tab.setFont(font)
        self.gridLayout_9 = QGridLayout(self.photo_tab)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.splitter_2 = QSplitter(self.photo_tab)
        self.splitter_2.setObjectName(u"splitter_2")
        sizePolicy.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy)
        self.splitter_2.setFont(font)
        self.splitter_2.setOrientation(Qt.Horizontal)
        self.widget_3 = QWidget(self.splitter_2)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy1.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy1)
        self.widget_3.setMinimumSize(QSize(650, 0))
        self.widget_3.setFont(font)
        self.gridLayout_14 = QGridLayout(self.widget_3)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(-1, -1, 12, -1)
        self.photo_view = QLabel(self.widget_3)
        self.photo_view.setObjectName(u"photo_view")
        self.photo_view.setFont(font)

        self.gridLayout_14.addWidget(self.photo_view, 0, 0, 1, 1)

        self.splitter_2.addWidget(self.widget_3)
        self.widget_4 = QWidget(self.splitter_2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy1.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy1)
        self.widget_4.setMinimumSize(QSize(300, 0))
        self.widget_4.setMaximumSize(QSize(900, 16777215))
        self.widget_4.setFont(font)
        self.gridLayout_15 = QGridLayout(self.widget_4)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(12, -1, -1, -1)
        self.group_code_in_photo = QLineEdit(self.widget_4)
        self.group_code_in_photo.setObjectName(u"group_code_in_photo")
        self.group_code_in_photo.setEnabled(False)
        self.group_code_in_photo.setFont(font)

        self.gridLayout_15.addWidget(self.group_code_in_photo, 6, 4, 1, 1)

        self.label_32 = QLabel(self.widget_4)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(120, 16777215))
        self.label_32.setFont(font)
        self.label_32.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_32, 6, 0, 1, 1)

        self.label_35 = QLabel(self.widget_4)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font)
        self.label_35.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_35, 11, 0, 1, 1)

        self.photo_code_in_photo = QLineEdit(self.widget_4)
        self.photo_code_in_photo.setObjectName(u"photo_code_in_photo")
        self.photo_code_in_photo.setFont(font)

        self.gridLayout_15.addWidget(self.photo_code_in_photo, 10, 1, 1, 1)

        self.label_40 = QLabel(self.widget_4)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMaximumSize(QSize(120, 16777215))
        self.label_40.setFont(font)
        self.label_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_40, 9, 0, 1, 1)

        self.peoples_in_photo = QTextEdit(self.widget_4)
        self.peoples_in_photo.setObjectName(u"peoples_in_photo")
        sizePolicy.setHeightForWidth(self.peoples_in_photo.sizePolicy().hasHeightForWidth())
        self.peoples_in_photo.setSizePolicy(sizePolicy)
        self.peoples_in_photo.setMaximumSize(QSize(16777215, 150))
        self.peoples_in_photo.setFont(font)
        self.peoples_in_photo.setReadOnly(True)

        self.gridLayout_15.addWidget(self.peoples_in_photo, 12, 0, 1, 5)

        self.label_38 = QLabel(self.widget_4)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMaximumSize(QSize(120, 16777215))
        self.label_38.setFont(font)
        self.label_38.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_38, 8, 0, 1, 1)

        self.label_41 = QLabel(self.widget_4)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font)
        self.label_41.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_41, 9, 3, 1, 1)

        self.all_photo_radioButton = QRadioButton(self.widget_4)
        self.radio_btn_group = QButtonGroup(MainWindow)
        self.radio_btn_group.setObjectName(u"radio_btn_group")
        self.radio_btn_group.addButton(self.all_photo_radioButton)
        self.all_photo_radioButton.setObjectName(u"all_photo_radioButton")
        self.all_photo_radioButton.setFont(font)

        self.gridLayout_15.addWidget(self.all_photo_radioButton, 1, 0, 1, 5)

        self.label_33 = QLabel(self.widget_4)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font)
        self.label_33.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_33, 6, 3, 1, 1)

        self.frame_7 = QFrame(self.widget_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMinimumSize(QSize(0, 45))
        self.frame_7.setFont(font)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.frame_7)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, -1, -1, -1)
        self.selected_dir_radioButton = QRadioButton(self.frame_7)
        self.selected_dir_radioButton.setObjectName(u"selected_dir_radioButton")
        self.selected_dir_radioButton.setFont(font)
        self.selected_dir_radioButton.setChecked(True)

        self.gridLayout_16.addWidget(self.selected_dir_radioButton, 0, 0, 1, 1)

        self.current_dir_radioButton = QRadioButton(self.frame_7)
        self.current_dir_radioButton.setObjectName(u"current_dir_radioButton")
        self.current_dir_radioButton.setFont(font)

        self.gridLayout_16.addWidget(self.current_dir_radioButton, 0, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(50, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_16.addItem(self.horizontalSpacer_14, 0, 2, 1, 1)


        self.gridLayout_15.addWidget(self.frame_7, 0, 0, 1, 5)

        self.photographer_in_photo = QLineEdit(self.widget_4)
        self.photographer_in_photo.setObjectName(u"photographer_in_photo")
        self.photographer_in_photo.setEnabled(False)
        self.photographer_in_photo.setFont(font)

        self.gridLayout_15.addWidget(self.photographer_in_photo, 7, 1, 1, 1)

        self.tableWidget = QTableWidget(self.widget_4)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tableWidget.setFont(font)
        self.tableWidget.setStyleSheet(u"   QHeaderView::section{\n"
"            border-top:0px solid #D8D8D8;\n"
"            border-left:0px solid #D8D8D8;\n"
"            border-right:1px solid #D8D8D8;\n"
"            border-bottom: 1px solid #D8D8D8;\n"
"            background-color:white;\n"
"            padding:4px;\n"
"        }\n"
"        QTableCornerButton::section{\n"
"            border-top:0px solid #D8D8D8;\n"
"            border-left:0px solid #D8D8D8;\n"
"            border-right:1px solid #D8D8D8;\n"
"            border-bottom: 1px solid #D8D8D8;\n"
"            background-color:white;\n"
"        }")
        self.tableWidget.setEditTriggers(QAbstractItemView.CurrentChanged)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(102)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.verticalHeader().setVisible(False)

        self.gridLayout_15.addWidget(self.tableWidget, 14, 0, 1, 5)

        self.label_31 = QLabel(self.widget_4)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font)
        self.label_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_31, 5, 3, 1, 1)

        self.format_in_photo = QLineEdit(self.widget_4)
        self.format_in_photo.setObjectName(u"format_in_photo")
        self.format_in_photo.setEnabled(True)
        self.format_in_photo.setFont(font)
        self.format_in_photo.setReadOnly(False)

        self.gridLayout_15.addWidget(self.format_in_photo, 8, 4, 1, 1)

        self.arch_category_code_in_photo = QLineEdit(self.widget_4)
        self.arch_category_code_in_photo.setObjectName(u"arch_category_code_in_photo")
        self.arch_category_code_in_photo.setEnabled(False)
        self.arch_category_code_in_photo.setFont(font)
        self.arch_category_code_in_photo.setReadOnly(False)

        self.gridLayout_15.addWidget(self.arch_category_code_in_photo, 5, 4, 1, 1)

        self.year_in_photo = QLineEdit(self.widget_4)
        self.year_in_photo.setObjectName(u"year_in_photo")
        self.year_in_photo.setEnabled(False)
        self.year_in_photo.setFont(font)

        self.gridLayout_15.addWidget(self.year_in_photo, 6, 1, 1, 1)

        self.label_37 = QLabel(self.widget_4)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)
        self.label_37.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_37, 7, 3, 1, 1)

        self.taken_time_in_photo = QLineEdit(self.widget_4)
        self.taken_time_in_photo.setObjectName(u"taken_time_in_photo")
        self.taken_time_in_photo.setEnabled(False)
        self.taken_time_in_photo.setFont(font)

        self.gridLayout_15.addWidget(self.taken_time_in_photo, 7, 4, 1, 1)

        self.part_recognition_radioButton = QRadioButton(self.widget_4)
        self.radio_btn_group.addButton(self.part_recognition_radioButton)
        self.part_recognition_radioButton.setObjectName(u"part_recognition_radioButton")
        self.part_recognition_radioButton.setFont(font)

        self.gridLayout_15.addWidget(self.part_recognition_radioButton, 2, 0, 1, 5)

        self.fonds_code_in_photo = QLineEdit(self.widget_4)
        self.fonds_code_in_photo.setObjectName(u"fonds_code_in_photo")
        self.fonds_code_in_photo.setEnabled(False)
        self.fonds_code_in_photo.setFont(font)
        self.fonds_code_in_photo.setReadOnly(False)

        self.gridLayout_15.addWidget(self.fonds_code_in_photo, 5, 1, 1, 1)

        self.frame_9 = QFrame(self.widget_4)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy5)
        self.frame_9.setMinimumSize(QSize(0, 45))
        self.frame_9.setFont(font)
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout_18 = QGridLayout(self.frame_9)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(-1, 5, -1, -1)
        self.pre_btn = QPushButton(self.frame_9)
        self.pre_btn.setObjectName(u"pre_btn")
        sizePolicy3.setHeightForWidth(self.pre_btn.sizePolicy().hasHeightForWidth())
        self.pre_btn.setSizePolicy(sizePolicy3)
        self.pre_btn.setMinimumSize(QSize(0, 40))
        self.pre_btn.setMaximumSize(QSize(290, 16777215))
        self.pre_btn.setFont(font)
        self.pre_btn.setFocusPolicy(Qt.NoFocus)
        self.pre_btn.setStyleSheet(u"padding-left: 12px; \n"
"padding-right: 12px;\n"
"padding-top: 8px; \n"
"padding-bottom: 8px;")
        icon9 = QIcon()
        icon9.addFile(u"icon/previous.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pre_btn.setIcon(icon9)
        self.pre_btn.setIconSize(QSize(24, 24))

        self.gridLayout_18.addWidget(self.pre_btn, 0, 0, 1, 1)

        self.photo_index_label = QLabel(self.frame_9)
        self.photo_index_label.setObjectName(u"photo_index_label")
        sizePolicy4.setHeightForWidth(self.photo_index_label.sizePolicy().hasHeightForWidth())
        self.photo_index_label.setSizePolicy(sizePolicy4)
        self.photo_index_label.setMaximumSize(QSize(16777215, 16777215))
        self.photo_index_label.setFont(font)
        self.photo_index_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_18.addWidget(self.photo_index_label, 0, 1, 1, 1)

        self.next_btn = QPushButton(self.frame_9)
        self.next_btn.setObjectName(u"next_btn")
        sizePolicy3.setHeightForWidth(self.next_btn.sizePolicy().hasHeightForWidth())
        self.next_btn.setSizePolicy(sizePolicy3)
        self.next_btn.setMinimumSize(QSize(0, 40))
        self.next_btn.setMaximumSize(QSize(290, 16777215))
        self.next_btn.setFont(font)
        self.next_btn.setFocusPolicy(Qt.NoFocus)
        self.next_btn.setLayoutDirection(Qt.RightToLeft)
        self.next_btn.setStyleSheet(u"padding-left: 12px; \n"
"padding-right: 12px;\n"
"padding-top: 8px; \n"
"padding-bottom: 8px;")
        icon10 = QIcon()
        icon10.addFile(u"icon/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next_btn.setIcon(icon10)
        self.next_btn.setIconSize(QSize(24, 24))

        self.gridLayout_18.addWidget(self.next_btn, 0, 2, 1, 1)


        self.gridLayout_15.addWidget(self.frame_9, 16, 0, 1, 5)

        self.label_39 = QLabel(self.widget_4)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font)
        self.label_39.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_39, 8, 3, 1, 1)

        self.security_classification_in_photo = QLineEdit(self.widget_4)
        self.security_classification_in_photo.setObjectName(u"security_classification_in_photo")
        self.security_classification_in_photo.setEnabled(False)
        self.security_classification_in_photo.setFont(font)
        self.security_classification_in_photo.setReadOnly(False)

        self.gridLayout_15.addWidget(self.security_classification_in_photo, 9, 1, 1, 1)

        self.taken_locations_in_photo = QLineEdit(self.widget_4)
        self.taken_locations_in_photo.setObjectName(u"taken_locations_in_photo")
        self.taken_locations_in_photo.setEnabled(False)
        self.taken_locations_in_photo.setFont(font)

        self.gridLayout_15.addWidget(self.taken_locations_in_photo, 8, 1, 1, 1)

        self.verifycheckBox = QCheckBox(self.widget_4)
        self.verifycheckBox.setObjectName(u"verifycheckBox")
        self.verifycheckBox.setFont(font)

        self.gridLayout_15.addWidget(self.verifycheckBox, 15, 0, 1, 2)

        self.frame_8 = QFrame(self.widget_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(True)
        self.frame_8.setMinimumSize(QSize(0, 43))
        self.frame_8.setFont(font)
        self.frame_8.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout_10 = QGridLayout(self.frame_8)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.label_29 = QLabel(self.frame_8)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setMaximumSize(QSize(120, 16777215))
        self.label_29.setFont(font)

        self.gridLayout_10.addWidget(self.label_29, 0, 0, 1, 1)

        self.arch_code_in_photo = QLineEdit(self.frame_8)
        self.arch_code_in_photo.setObjectName(u"arch_code_in_photo")
        self.arch_code_in_photo.setMinimumSize(QSize(0, 25))
        self.arch_code_in_photo.setFont(font)

        self.gridLayout_10.addWidget(self.arch_code_in_photo, 0, 1, 1, 1)

        self.horizontalSpacer_10 = QSpacerItem(62, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_10.addItem(self.horizontalSpacer_10, 0, 2, 1, 1)


        self.gridLayout_15.addWidget(self.frame_8, 4, 0, 1, 5)

        self.reference_code_in_photo = QLineEdit(self.widget_4)
        self.reference_code_in_photo.setObjectName(u"reference_code_in_photo")
        self.reference_code_in_photo.setEnabled(False)
        self.reference_code_in_photo.setFont(font)

        self.gridLayout_15.addWidget(self.reference_code_in_photo, 9, 4, 1, 1)

        self.label_36 = QLabel(self.widget_4)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(120, 16777215))
        self.label_36.setFont(font)
        self.label_36.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_36, 7, 0, 1, 1)

        self.label_30 = QLabel(self.widget_4)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setMaximumSize(QSize(120, 16777215))
        self.label_30.setFont(font)
        self.label_30.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_30, 5, 0, 1, 1)

        self.all_recognition_radioButton = QRadioButton(self.widget_4)
        self.radio_btn_group.addButton(self.all_recognition_radioButton)
        self.all_recognition_radioButton.setObjectName(u"all_recognition_radioButton")
        self.all_recognition_radioButton.setFont(font)

        self.gridLayout_15.addWidget(self.all_recognition_radioButton, 3, 0, 1, 5)

        self.label_34 = QLabel(self.widget_4)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setMaximumSize(QSize(120, 16777215))
        self.label_34.setFont(font)
        self.label_34.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_34, 10, 0, 1, 1)

        self.horizontalSpacer_25 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_25, 6, 2, 1, 1)

        self.splitter_2.addWidget(self.widget_4)

        self.gridLayout_9.addWidget(self.splitter_2, 0, 0, 1, 1)

        icon11 = QIcon()
        icon11.addFile(u"icon/photo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.photo_tab, icon11, "")
        self.training_tab = QWidget()
        self.training_tab.setObjectName(u"training_tab")
        font2 = QFont()
        font2.setFamily(u"\u65b0\u5b8b\u4f53")
        font2.setPointSize(9)
        self.training_tab.setFont(font2)
        self.gridLayout_3 = QGridLayout(self.training_tab)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.model_acc_label = QLabel(self.training_tab)
        self.model_acc_label.setObjectName(u"model_acc_label")
        sizePolicy4.setHeightForWidth(self.model_acc_label.sizePolicy().hasHeightForWidth())
        self.model_acc_label.setSizePolicy(sizePolicy4)
        self.model_acc_label.setMaximumSize(QSize(16777215, 16777215))
        self.model_acc_label.setFont(font)
        self.model_acc_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.model_acc_label, 4, 2, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_4, 6, 1, 1, 1)

        self.label_5 = QLabel(self.training_tab)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_5, 1, 1, 1, 1)

        self.label_14 = QLabel(self.training_tab)
        self.label_14.setObjectName(u"label_14")
        font3 = QFont()
        font3.setFamily(u"\u65b0\u5b8b\u4f53")
        self.label_14.setFont(font3)
        self.label_14.setContextMenuPolicy(Qt.CustomContextMenu)

        self.gridLayout_3.addWidget(self.label_14, 2, 2, 1, 1)

        self.untrained_num_label = QLabel(self.training_tab)
        self.untrained_num_label.setObjectName(u"untrained_num_label")
        sizePolicy4.setHeightForWidth(self.untrained_num_label.sizePolicy().hasHeightForWidth())
        self.untrained_num_label.setSizePolicy(sizePolicy4)
        self.untrained_num_label.setFont(font)

        self.gridLayout_3.addWidget(self.untrained_num_label, 3, 2, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_7, 3, 3, 1, 1)

        self.thresh_lineEdit = QLineEdit(self.training_tab)
        self.thresh_lineEdit.setObjectName(u"thresh_lineEdit")
        sizePolicy4.setHeightForWidth(self.thresh_lineEdit.sizePolicy().hasHeightForWidth())
        self.thresh_lineEdit.setSizePolicy(sizePolicy4)
        self.thresh_lineEdit.setMaximumSize(QSize(400, 16777215))
        self.thresh_lineEdit.setFont(font)

        self.gridLayout_3.addWidget(self.thresh_lineEdit, 1, 2, 1, 1)

        self.label_4 = QLabel(self.training_tab)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 35))
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_4, 3, 1, 1, 1)

        self.label_12 = QLabel(self.training_tab)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 35))
        self.label_12.setMaximumSize(QSize(16777215, 16777215))
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_3.addWidget(self.label_12, 4, 1, 1, 1)

        self.frame_5 = QFrame(self.training_tab)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setFont(font)
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_5)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.horizontalSpacer_12 = QSpacerItem(189, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_12, 0, 0, 1, 1)

        self.train_btn = QPushButton(self.frame_5)
        self.train_btn.setObjectName(u"train_btn")
        sizePolicy3.setHeightForWidth(self.train_btn.sizePolicy().hasHeightForWidth())
        self.train_btn.setSizePolicy(sizePolicy3)
        self.train_btn.setMaximumSize(QSize(300, 16777215))
        self.train_btn.setFont(font)
        self.train_btn.setFocusPolicy(Qt.NoFocus)
        self.train_btn.setStyleSheet(u"padding-left: 30px; \n"
"padding-right: 30px;\n"
"padding-top: 8px; \n"
"padding-bottom: 8px;")
        icon12 = QIcon()
        icon12.addFile(u"icon/start_training.png", QSize(), QIcon.Normal, QIcon.Off)
        self.train_btn.setIcon(icon12)
        self.train_btn.setIconSize(QSize(24, 24))

        self.gridLayout_12.addWidget(self.train_btn, 0, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(189, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_12.addItem(self.horizontalSpacer_13, 0, 2, 1, 1)


        self.gridLayout_3.addWidget(self.frame_5, 7, 0, 1, 4)

        self.label_15 = QLabel(self.training_tab)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font3)

        self.gridLayout_3.addWidget(self.label_15, 5, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 10, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_3.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        icon13 = QIcon()
        icon13.addFile(u"icon/training.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.training_tab, icon13, "")
        self.arch_browser_tab = QWidget()
        self.arch_browser_tab.setObjectName(u"arch_browser_tab")
        self.arch_browser_tab.setFont(font)
        self.gridLayout_17 = QGridLayout(self.arch_browser_tab)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.splitter_4 = QSplitter(self.arch_browser_tab)
        self.splitter_4.setObjectName(u"splitter_4")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.splitter_3 = QSplitter(self.splitter_4)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.widget_5 = QWidget(self.splitter_3)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(280, 1))
        self.widget_5.setMaximumSize(QSize(16777215, 16777215))
        self.widget_5.setFont(font)
        self.gridLayout_19 = QGridLayout(self.widget_5)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.order_combobox_browse = QComboBox(self.widget_5)
        self.order_combobox_browse.addItem("")
        self.order_combobox_browse.addItem("")
        self.order_combobox_browse.setObjectName(u"order_combobox_browse")
        self.order_combobox_browse.setFont(font)

        self.gridLayout_19.addWidget(self.order_combobox_browse, 0, 1, 1, 1)

        self.label_67 = QLabel(self.widget_5)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font)

        self.gridLayout_19.addWidget(self.label_67, 0, 0, 1, 1)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_19.addItem(self.horizontalSpacer_16, 0, 2, 1, 1)

        self.arch_tree_view_browse = QTreeView(self.widget_5)
        self.arch_tree_view_browse.setObjectName(u"arch_tree_view_browse")
        self.arch_tree_view_browse.setFont(font)
        self.arch_tree_view_browse.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.arch_tree_view_browse.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.gridLayout_19.addWidget(self.arch_tree_view_browse, 1, 0, 1, 3)

        self.splitter_3.addWidget(self.widget_5)
        self.widget_6 = QWidget(self.splitter_3)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(800, 16777215))
        self.widget_6.setFont(font)
        self.gridLayout_21 = QGridLayout(self.widget_6)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.gridLayout_21.setContentsMargins(18, 10, 18, 10)
        self.label_66 = QLabel(self.widget_6)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font)
        self.label_66.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_66, 10, 0, 1, 1)

        self.label_49 = QLabel(self.widget_6)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font)
        self.label_49.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_49, 3, 0, 1, 1)

        self.group_title_in_group_arch = QLineEdit(self.widget_6)
        self.group_title_in_group_arch.setObjectName(u"group_title_in_group_arch")
        sizePolicy4.setHeightForWidth(self.group_title_in_group_arch.sizePolicy().hasHeightForWidth())
        self.group_title_in_group_arch.setSizePolicy(sizePolicy4)
        self.group_title_in_group_arch.setFont(font)
        self.group_title_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.group_title_in_group_arch, 0, 1, 1, 4)

        self.label_59 = QLabel(self.widget_6)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font)
        self.label_59.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_59, 2, 0, 1, 1)

        self.label_62 = QLabel(self.widget_6)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setMaximumSize(QSize(120, 16777215))
        self.label_62.setFont(font)
        self.label_62.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_62, 0, 0, 1, 1)

        self.label_28 = QLabel(self.widget_6)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(120, 16777215))
        self.label_28.setFont(font)
        self.label_28.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_28, 6, 3, 1, 1)

        self.label_57 = QLabel(self.widget_6)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font)
        self.label_57.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_57, 9, 0, 1, 1)

        self.format_in_photo_arch = QLineEdit(self.widget_6)
        self.format_in_photo_arch.setObjectName(u"format_in_photo_arch")
        self.format_in_photo_arch.setFont(font)
        self.format_in_photo_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.format_in_photo_arch, 11, 1, 1, 1)

        self.label_64 = QLabel(self.widget_6)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setMaximumSize(QSize(120, 16777215))
        self.label_64.setFont(font)
        self.label_64.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_64, 10, 3, 1, 1)

        self.opening_state_in_group_arch = QLineEdit(self.widget_6)
        self.opening_state_in_group_arch.setObjectName(u"opening_state_in_group_arch")
        self.opening_state_in_group_arch.setFont(font)
        self.opening_state_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.opening_state_in_group_arch, 9, 4, 1, 1)

        self.security_classification_in_group_arch = QLineEdit(self.widget_6)
        self.security_classification_in_group_arch.setObjectName(u"security_classification_in_group_arch")
        self.security_classification_in_group_arch.setFont(font)
        self.security_classification_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.security_classification_in_group_arch, 8, 4, 1, 1)

        self.label_63 = QLabel(self.widget_6)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setMaximumSize(QSize(120, 16777215))
        self.label_63.setFont(font)
        self.label_63.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_63, 1, 3, 1, 1)

        self.photo_num_in_group_arch = QLineEdit(self.widget_6)
        self.photo_num_in_group_arch.setObjectName(u"photo_num_in_group_arch")
        sizePolicy4.setHeightForWidth(self.photo_num_in_group_arch.sizePolicy().hasHeightForWidth())
        self.photo_num_in_group_arch.setSizePolicy(sizePolicy4)
        self.photo_num_in_group_arch.setFont(font)
        self.photo_num_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.photo_num_in_group_arch, 8, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_21.addItem(self.verticalSpacer_8, 18, 0, 1, 1)

        self.reference_code_in_group_arch = QLineEdit(self.widget_6)
        self.reference_code_in_group_arch.setObjectName(u"reference_code_in_group_arch")
        sizePolicy4.setHeightForWidth(self.reference_code_in_group_arch.sizePolicy().hasHeightForWidth())
        self.reference_code_in_group_arch.setSizePolicy(sizePolicy4)
        self.reference_code_in_group_arch.setFont(font)
        self.reference_code_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.reference_code_in_group_arch, 9, 1, 1, 1)

        self.taken_time_in_group_arch = QLineEdit(self.widget_6)
        self.taken_time_in_group_arch.setObjectName(u"taken_time_in_group_arch")
        sizePolicy4.setHeightForWidth(self.taken_time_in_group_arch.sizePolicy().hasHeightForWidth())
        self.taken_time_in_group_arch.setSizePolicy(sizePolicy4)
        self.taken_time_in_group_arch.setFont(font)
        self.taken_time_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.taken_time_in_group_arch, 7, 1, 1, 1)

        self.department_in_group_arch = QLineEdit(self.widget_6)
        self.department_in_group_arch.setObjectName(u"department_in_group_arch")
        sizePolicy4.setHeightForWidth(self.department_in_group_arch.sizePolicy().hasHeightForWidth())
        self.department_in_group_arch.setSizePolicy(sizePolicy4)
        self.department_in_group_arch.setFont(font)
        self.department_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.department_in_group_arch, 3, 4, 1, 1)

        self.label_61 = QLabel(self.widget_6)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font)
        self.label_61.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_61, 7, 0, 1, 1)

        self.label_52 = QLabel(self.widget_6)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setMaximumSize(QSize(120, 16777215))
        self.label_52.setFont(font)
        self.label_52.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_52, 8, 3, 1, 1)

        self.label_50 = QLabel(self.widget_6)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setMaximumSize(QSize(120, 16777215))
        self.label_50.setFont(font)
        self.label_50.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_50, 7, 3, 1, 1)

        self.label_80 = QLabel(self.widget_6)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font)

        self.gridLayout_21.addWidget(self.label_80, 11, 0, 1, 1)

        self.label_60 = QLabel(self.widget_6)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setMaximumSize(QSize(120, 16777215))
        self.label_60.setFont(font)
        self.label_60.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_60, 3, 3, 1, 1)

        self.label_51 = QLabel(self.widget_6)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(120, 16777215))
        self.label_51.setFont(font)
        self.label_51.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_51, 4, 3, 1, 1)

        self.arch_code_in_photo_arch = QLineEdit(self.widget_6)
        self.arch_code_in_photo_arch.setObjectName(u"arch_code_in_photo_arch")
        self.arch_code_in_photo_arch.setFont(font)
        self.arch_code_in_photo_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.arch_code_in_photo_arch, 10, 1, 1, 1)

        self.group_caption_in_group_arch = QTextEdit(self.widget_6)
        self.group_caption_in_group_arch.setObjectName(u"group_caption_in_group_arch")
        self.group_caption_in_group_arch.setFont(font)
        self.group_caption_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.group_caption_in_group_arch, 13, 0, 1, 5)

        self.retention_period_in_group_arch = QLineEdit(self.widget_6)
        self.retention_period_in_group_arch.setObjectName(u"retention_period_in_group_arch")
        self.retention_period_in_group_arch.setFont(font)
        self.retention_period_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.retention_period_in_group_arch, 2, 4, 1, 1)

        self.photo_code_in_photo_arch = QLineEdit(self.widget_6)
        self.photo_code_in_photo_arch.setObjectName(u"photo_code_in_photo_arch")
        self.photo_code_in_photo_arch.setFont(font)
        self.photo_code_in_photo_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.photo_code_in_photo_arch, 10, 4, 1, 1)

        self.photographer_in_group_arch = QLineEdit(self.widget_6)
        self.photographer_in_group_arch.setObjectName(u"photographer_in_group_arch")
        sizePolicy4.setHeightForWidth(self.photographer_in_group_arch.sizePolicy().hasHeightForWidth())
        self.photographer_in_group_arch.setSizePolicy(sizePolicy4)
        self.photographer_in_group_arch.setFont(font)
        self.photographer_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.photographer_in_group_arch, 6, 4, 1, 1)

        self.label_55 = QLabel(self.widget_6)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font)
        self.label_55.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_55, 4, 0, 1, 1)

        self.fonds_code_in_group_arch = QLineEdit(self.widget_6)
        self.fonds_code_in_group_arch.setObjectName(u"fonds_code_in_group_arch")
        self.fonds_code_in_group_arch.setFont(font)
        self.fonds_code_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.fonds_code_in_group_arch, 1, 4, 1, 1)

        self.label_69 = QLabel(self.widget_6)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font)
        self.label_69.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_69, 14, 0, 1, 1)

        self.label_65 = QLabel(self.widget_6)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font)
        self.label_65.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_65, 1, 0, 1, 1)

        self.taken_locations_in_group_arch = QLineEdit(self.widget_6)
        self.taken_locations_in_group_arch.setObjectName(u"taken_locations_in_group_arch")
        sizePolicy4.setHeightForWidth(self.taken_locations_in_group_arch.sizePolicy().hasHeightForWidth())
        self.taken_locations_in_group_arch.setSizePolicy(sizePolicy4)
        self.taken_locations_in_group_arch.setFont(font)
        self.taken_locations_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.taken_locations_in_group_arch, 7, 4, 1, 1)

        self.label_48 = QLabel(self.widget_6)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font)
        self.label_48.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_48, 6, 0, 1, 1)

        self.group_code_in_group_arch = QLineEdit(self.widget_6)
        self.group_code_in_group_arch.setObjectName(u"group_code_in_group_arch")
        sizePolicy4.setHeightForWidth(self.group_code_in_group_arch.sizePolicy().hasHeightForWidth())
        self.group_code_in_group_arch.setSizePolicy(sizePolicy4)
        self.group_code_in_group_arch.setFont(font)
        self.group_code_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.group_code_in_group_arch, 4, 1, 1, 1)

        self.year_in_group_arch = QLineEdit(self.widget_6)
        self.year_in_group_arch.setObjectName(u"year_in_group_arch")
        sizePolicy4.setHeightForWidth(self.year_in_group_arch.sizePolicy().hasHeightForWidth())
        self.year_in_group_arch.setSizePolicy(sizePolicy4)
        self.year_in_group_arch.setFont(font)
        self.year_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.year_in_group_arch, 3, 1, 1, 1)

        self.peoples_in_photo_arch = QTextEdit(self.widget_6)
        self.peoples_in_photo_arch.setObjectName(u"peoples_in_photo_arch")
        sizePolicy.setHeightForWidth(self.peoples_in_photo_arch.sizePolicy().hasHeightForWidth())
        self.peoples_in_photo_arch.setSizePolicy(sizePolicy)
        self.peoples_in_photo_arch.setMaximumSize(QSize(16777215, 150))
        self.peoples_in_photo_arch.setFont(font)
        self.peoples_in_photo_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.peoples_in_photo_arch, 15, 0, 1, 5)

        self.arch_category_code_in_group_arch = QLineEdit(self.widget_6)
        self.arch_category_code_in_group_arch.setObjectName(u"arch_category_code_in_group_arch")
        self.arch_category_code_in_group_arch.setFont(font)
        self.arch_category_code_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.arch_category_code_in_group_arch, 2, 1, 1, 1)

        self.label_56 = QLabel(self.widget_6)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font)
        self.label_56.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_56, 8, 0, 1, 1)

        self.label_53 = QLabel(self.widget_6)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMaximumSize(QSize(120, 16777215))
        self.label_53.setFont(font)
        self.label_53.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_53, 9, 3, 1, 1)

        self.arch_code_in_group_arch = QLineEdit(self.widget_6)
        self.arch_code_in_group_arch.setObjectName(u"arch_code_in_group_arch")
        self.arch_code_in_group_arch.setFont(font)
        self.arch_code_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.arch_code_in_group_arch, 1, 1, 1, 1)

        self.label_54 = QLabel(self.widget_6)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setMaximumSize(QSize(120, 16777215))
        self.label_54.setFont(font)
        self.label_54.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_54, 2, 3, 1, 1)

        self.folder_size_in_group_arch = QLineEdit(self.widget_6)
        self.folder_size_in_group_arch.setObjectName(u"folder_size_in_group_arch")
        sizePolicy4.setHeightForWidth(self.folder_size_in_group_arch.sizePolicy().hasHeightForWidth())
        self.folder_size_in_group_arch.setSizePolicy(sizePolicy4)
        self.folder_size_in_group_arch.setFont(font)
        self.folder_size_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.folder_size_in_group_arch, 6, 1, 1, 1)

        self.label_58 = QLabel(self.widget_6)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font)
        self.label_58.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_21.addWidget(self.label_58, 12, 0, 1, 1)

        self.author_in_group_arch = QLineEdit(self.widget_6)
        self.author_in_group_arch.setObjectName(u"author_in_group_arch")
        sizePolicy4.setHeightForWidth(self.author_in_group_arch.sizePolicy().hasHeightForWidth())
        self.author_in_group_arch.setSizePolicy(sizePolicy4)
        self.author_in_group_arch.setFont(font)
        self.author_in_group_arch.setReadOnly(True)

        self.gridLayout_21.addWidget(self.author_in_group_arch, 4, 4, 1, 1)

        self.horizontalSpacer_26 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_21.addItem(self.horizontalSpacer_26, 1, 2, 1, 1)

        self.splitter_3.addWidget(self.widget_6)
        self.widget_7 = QWidget(self.splitter_3)
        self.widget_7.setObjectName(u"widget_7")
        self.widget_7.setMinimumSize(QSize(600, 0))
        self.widget_7.setFont(font)
        self.gridLayout_22 = QGridLayout(self.widget_7)
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.photo_view_in_arch = QLabel(self.widget_7)
        self.photo_view_in_arch.setObjectName(u"photo_view_in_arch")
        self.photo_view_in_arch.setFont(font)

        self.gridLayout_22.addWidget(self.photo_view_in_arch, 0, 0, 1, 1)

        self.splitter_3.addWidget(self.widget_7)
        self.splitter_4.addWidget(self.splitter_3)
        self.widget_8 = QWidget(self.splitter_4)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_20 = QGridLayout(self.widget_8)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.photo_list_widget = QListWidget(self.widget_8)
        self.photo_list_widget.setObjectName(u"photo_list_widget")
        self.photo_list_widget.setFont(font)
        self.photo_list_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.photo_list_widget.setItemAlignment(Qt.AlignBottom)

        self.gridLayout_20.addWidget(self.photo_list_widget, 0, 0, 1, 1)

        self.splitter_4.addWidget(self.widget_8)

        self.gridLayout_17.addWidget(self.splitter_4, 0, 0, 1, 1)

        icon14 = QIcon()
        icon14.addFile(u"icon/browse_arch.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.arch_browser_tab, icon14, "")
        self.search_archives_tab = QWidget()
        self.search_archives_tab.setObjectName(u"search_archives_tab")
        self.search_archives_tab.setFont(font)
        self.gridLayout_30 = QGridLayout(self.search_archives_tab)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.splitter_9 = QSplitter(self.search_archives_tab)
        self.splitter_9.setObjectName(u"splitter_9")
        self.splitter_9.setFont(font)
        self.splitter_9.setOrientation(Qt.Horizontal)
        self.widget_21 = QWidget(self.splitter_9)
        self.widget_21.setObjectName(u"widget_21")
        self.widget_21.setMinimumSize(QSize(240, 1))
        self.widget_21.setMaximumSize(QSize(320, 16777215))
        self.widget_21.setFont(font)
        self.gridLayout_54 = QGridLayout(self.widget_21)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.label_211 = QLabel(self.widget_21)
        self.label_211.setObjectName(u"label_211")
        self.label_211.setFont(font)

        self.gridLayout_54.addWidget(self.label_211, 2, 0, 1, 1)

        self.start_date_search = QDateEdit(self.widget_21)
        self.start_date_search.setObjectName(u"start_date_search")
        sizePolicy3.setHeightForWidth(self.start_date_search.sizePolicy().hasHeightForWidth())
        self.start_date_search.setSizePolicy(sizePolicy3)
        self.start_date_search.setMinimumSize(QSize(0, 26))
        self.start_date_search.setFont(font)
        self.start_date_search.setDateTime(QDateTime(QDate(2010, 1, 1), QTime(0, 0, 0)))

        self.gridLayout_54.addWidget(self.start_date_search, 2, 1, 1, 1)

        self.label_187 = QLabel(self.widget_21)
        self.label_187.setObjectName(u"label_187")
        self.label_187.setFont(font)

        self.gridLayout_54.addWidget(self.label_187, 0, 0, 1, 1)

        self.label_210 = QLabel(self.widget_21)
        self.label_210.setObjectName(u"label_210")
        self.label_210.setFont(font)

        self.gridLayout_54.addWidget(self.label_210, 1, 0, 1, 1)

        self.end_date_search = QDateEdit(self.widget_21)
        self.end_date_search.setObjectName(u"end_date_search")
        sizePolicy3.setHeightForWidth(self.end_date_search.sizePolicy().hasHeightForWidth())
        self.end_date_search.setSizePolicy(sizePolicy3)
        self.end_date_search.setMinimumSize(QSize(0, 26))
        self.end_date_search.setDateTime(QDateTime(QDate(2021, 1, 1), QTime(0, 0, 0)))

        self.gridLayout_54.addWidget(self.end_date_search, 2, 2, 1, 1)

        self.group_title_search = QLineEdit(self.widget_21)
        self.group_title_search.setObjectName(u"group_title_search")
        self.group_title_search.setFont(font)

        self.gridLayout_54.addWidget(self.group_title_search, 0, 1, 1, 2)

        self.peoples_search = QLineEdit(self.widget_21)
        self.peoples_search.setObjectName(u"peoples_search")
        self.peoples_search.setFont(font)

        self.gridLayout_54.addWidget(self.peoples_search, 1, 1, 1, 2)

        self.frame_19 = QFrame(self.widget_21)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setMinimumSize(QSize(0, 30))
        self.frame_19.setFont(font)
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.gridLayout_59 = QGridLayout(self.frame_19)
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.horizontalSpacer_47 = QSpacerItem(47, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_59.addItem(self.horizontalSpacer_47, 0, 0, 1, 1)

        self.search_btn = QPushButton(self.frame_19)
        self.search_btn.setObjectName(u"search_btn")
        sizePolicy4.setHeightForWidth(self.search_btn.sizePolicy().hasHeightForWidth())
        self.search_btn.setSizePolicy(sizePolicy4)
        self.search_btn.setFont(font)
        self.search_btn.setFocusPolicy(Qt.TabFocus)
        self.search_btn.setStyleSheet(u"padding-left: 30px; \n"
"padding-right: 30px;\n"
"padding-top: 8px; \n"
"padding-bottom: 8px;")
        icon15 = QIcon()
        icon15.addFile(u"icon/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon15)
        self.search_btn.setIconSize(QSize(24, 24))
        self.search_btn.setAutoDefault(True)

        self.gridLayout_59.addWidget(self.search_btn, 0, 1, 1, 1)

        self.horizontalSpacer_48 = QSpacerItem(47, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_59.addItem(self.horizontalSpacer_48, 0, 2, 1, 1)


        self.gridLayout_54.addWidget(self.frame_19, 4, 0, 1, 3)

        self.group_tree_widget_search = QTreeWidget(self.widget_21)
        self.group_tree_widget_search.setObjectName(u"group_tree_widget_search")
        self.group_tree_widget_search.setFont(font)
        self.group_tree_widget_search.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.group_tree_widget_search.setSelectionBehavior(QAbstractItemView.SelectItems)

        self.gridLayout_54.addWidget(self.group_tree_widget_search, 5, 0, 1, 3)

        self.frame_11 = QFrame(self.widget_21)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 30))
        self.frame_11.setFont(font)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_11)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_27, 0, 0, 1, 1)

        self.export_btn_search = QPushButton(self.frame_11)
        self.export_btn_search.setObjectName(u"export_btn_search")
        sizePolicy5.setHeightForWidth(self.export_btn_search.sizePolicy().hasHeightForWidth())
        self.export_btn_search.setSizePolicy(sizePolicy5)
        self.export_btn_search.setFont(font)
        self.export_btn_search.setFocusPolicy(Qt.TabFocus)
        self.export_btn_search.setStyleSheet(u"padding-left: 30px; \n"
"padding-right: 30px;\n"
"padding-top: 8px; \n"
"padding-bottom: 8px;")
        icon16 = QIcon()
        icon16.addFile(u"icon/export.png", QSize(), QIcon.Normal, QIcon.Off)
        self.export_btn_search.setIcon(icon16)
        self.export_btn_search.setIconSize(QSize(24, 24))
        self.export_btn_search.setAutoDefault(True)

        self.gridLayout_31.addWidget(self.export_btn_search, 0, 1, 1, 1)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_31.addItem(self.horizontalSpacer_28, 0, 2, 1, 1)


        self.gridLayout_54.addWidget(self.frame_11, 6, 0, 1, 3)

        self.splitter_9.addWidget(self.widget_21)
        self.splitter_8 = QSplitter(self.splitter_9)
        self.splitter_8.setObjectName(u"splitter_8")
        self.splitter_8.setFont(font)
        self.splitter_8.setOrientation(Qt.Vertical)
        self.splitter_7 = QSplitter(self.splitter_8)
        self.splitter_7.setObjectName(u"splitter_7")
        self.splitter_7.setFont(font)
        self.splitter_7.setOrientation(Qt.Horizontal)
        self.widget_22 = QWidget(self.splitter_7)
        self.widget_22.setObjectName(u"widget_22")
        self.widget_22.setMaximumSize(QSize(800, 16777215))
        self.widget_22.setFont(font)
        self.gridLayout_55 = QGridLayout(self.widget_22)
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.gridLayout_55.setContentsMargins(18, 10, 18, 10)
        self.group_caption_in_group_search = QTextEdit(self.widget_22)
        self.group_caption_in_group_search.setObjectName(u"group_caption_in_group_search")
        self.group_caption_in_group_search.setFont(font)
        self.group_caption_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.group_caption_in_group_search, 13, 0, 1, 5)

        self.label_206 = QLabel(self.widget_22)
        self.label_206.setObjectName(u"label_206")
        self.label_206.setMaximumSize(QSize(120, 16777215))
        self.label_206.setFont(font)
        self.label_206.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_206, 8, 3, 1, 1)

        self.label_191 = QLabel(self.widget_22)
        self.label_191.setObjectName(u"label_191")
        self.label_191.setMaximumSize(QSize(120, 16777215))
        self.label_191.setFont(font)
        self.label_191.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_191, 7, 3, 1, 1)

        self.verticalSpacer_25 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_55.addItem(self.verticalSpacer_25, 18, 0, 1, 1)

        self.arch_category_code_in_group_search = QLineEdit(self.widget_22)
        self.arch_category_code_in_group_search.setObjectName(u"arch_category_code_in_group_search")
        self.arch_category_code_in_group_search.setFont(font)
        self.arch_category_code_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.arch_category_code_in_group_search, 2, 1, 1, 1)

        self.label_197 = QLabel(self.widget_22)
        self.label_197.setObjectName(u"label_197")
        self.label_197.setFont(font)

        self.gridLayout_55.addWidget(self.label_197, 11, 0, 1, 1)

        self.label_190 = QLabel(self.widget_22)
        self.label_190.setObjectName(u"label_190")
        self.label_190.setMaximumSize(QSize(120, 16777215))
        self.label_190.setFont(font)
        self.label_190.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_190, 2, 3, 1, 1)

        self.label_195 = QLabel(self.widget_22)
        self.label_195.setObjectName(u"label_195")
        self.label_195.setFont(font)
        self.label_195.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_195, 3, 0, 1, 1)

        self.label_189 = QLabel(self.widget_22)
        self.label_189.setObjectName(u"label_189")
        self.label_189.setFont(font)
        self.label_189.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_189, 6, 0, 1, 1)

        self.label_196 = QLabel(self.widget_22)
        self.label_196.setObjectName(u"label_196")
        self.label_196.setFont(font)
        self.label_196.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_196, 12, 0, 1, 1)

        self.retention_period_in_group_search = QLineEdit(self.widget_22)
        self.retention_period_in_group_search.setObjectName(u"retention_period_in_group_search")
        self.retention_period_in_group_search.setFont(font)
        self.retention_period_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.retention_period_in_group_search, 2, 4, 1, 1)

        self.label_200 = QLabel(self.widget_22)
        self.label_200.setObjectName(u"label_200")
        self.label_200.setMaximumSize(QSize(120, 16777215))
        self.label_200.setFont(font)
        self.label_200.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_200, 4, 3, 1, 1)

        self.folder_size_in_group_search = QLineEdit(self.widget_22)
        self.folder_size_in_group_search.setObjectName(u"folder_size_in_group_search")
        sizePolicy4.setHeightForWidth(self.folder_size_in_group_search.sizePolicy().hasHeightForWidth())
        self.folder_size_in_group_search.setSizePolicy(sizePolicy4)
        self.folder_size_in_group_search.setFont(font)
        self.folder_size_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.folder_size_in_group_search, 6, 1, 1, 1)

        self.label_208 = QLabel(self.widget_22)
        self.label_208.setObjectName(u"label_208")
        self.label_208.setMaximumSize(QSize(120, 16777215))
        self.label_208.setFont(font)
        self.label_208.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_208, 9, 3, 1, 1)

        self.photo_code_in_photo_search = QLineEdit(self.widget_22)
        self.photo_code_in_photo_search.setObjectName(u"photo_code_in_photo_search")
        self.photo_code_in_photo_search.setFont(font)
        self.photo_code_in_photo_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.photo_code_in_photo_search, 10, 4, 1, 1)

        self.arch_code_in_photo_search = QLineEdit(self.widget_22)
        self.arch_code_in_photo_search.setObjectName(u"arch_code_in_photo_search")
        self.arch_code_in_photo_search.setFont(font)
        self.arch_code_in_photo_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.arch_code_in_photo_search, 10, 1, 1, 1)

        self.label_198 = QLabel(self.widget_22)
        self.label_198.setObjectName(u"label_198")
        self.label_198.setMaximumSize(QSize(120, 16777215))
        self.label_198.setFont(font)
        self.label_198.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_198, 0, 0, 1, 1)

        self.photographer_in_group_search = QLineEdit(self.widget_22)
        self.photographer_in_group_search.setObjectName(u"photographer_in_group_search")
        sizePolicy4.setHeightForWidth(self.photographer_in_group_search.sizePolicy().hasHeightForWidth())
        self.photographer_in_group_search.setSizePolicy(sizePolicy4)
        self.photographer_in_group_search.setFont(font)
        self.photographer_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.photographer_in_group_search, 6, 4, 1, 1)

        self.photo_num_in_group_search = QLineEdit(self.widget_22)
        self.photo_num_in_group_search.setObjectName(u"photo_num_in_group_search")
        sizePolicy4.setHeightForWidth(self.photo_num_in_group_search.sizePolicy().hasHeightForWidth())
        self.photo_num_in_group_search.setSizePolicy(sizePolicy4)
        self.photo_num_in_group_search.setFont(font)
        self.photo_num_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.photo_num_in_group_search, 8, 1, 1, 1)

        self.taken_time_in_group_search = QLineEdit(self.widget_22)
        self.taken_time_in_group_search.setObjectName(u"taken_time_in_group_search")
        sizePolicy4.setHeightForWidth(self.taken_time_in_group_search.sizePolicy().hasHeightForWidth())
        self.taken_time_in_group_search.setSizePolicy(sizePolicy4)
        self.taken_time_in_group_search.setFont(font)
        self.taken_time_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.taken_time_in_group_search, 7, 1, 1, 1)

        self.label_194 = QLabel(self.widget_22)
        self.label_194.setObjectName(u"label_194")
        self.label_194.setFont(font)
        self.label_194.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_194, 8, 0, 1, 1)

        self.label_205 = QLabel(self.widget_22)
        self.label_205.setObjectName(u"label_205")
        self.label_205.setMaximumSize(QSize(120, 16777215))
        self.label_205.setFont(font)
        self.label_205.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_205, 10, 3, 1, 1)

        self.label_199 = QLabel(self.widget_22)
        self.label_199.setObjectName(u"label_199")
        self.label_199.setMaximumSize(QSize(120, 16777215))
        self.label_199.setFont(font)
        self.label_199.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_199, 3, 3, 1, 1)

        self.label_192 = QLabel(self.widget_22)
        self.label_192.setObjectName(u"label_192")
        self.label_192.setFont(font)
        self.label_192.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_192, 10, 0, 1, 1)

        self.peoples_in_photo_search = QTextEdit(self.widget_22)
        self.peoples_in_photo_search.setObjectName(u"peoples_in_photo_search")
        sizePolicy.setHeightForWidth(self.peoples_in_photo_search.sizePolicy().hasHeightForWidth())
        self.peoples_in_photo_search.setSizePolicy(sizePolicy)
        self.peoples_in_photo_search.setMaximumSize(QSize(16777215, 150))
        self.peoples_in_photo_search.setFont(font)
        self.peoples_in_photo_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.peoples_in_photo_search, 15, 0, 1, 5)

        self.arch_code_in_group_search = QLineEdit(self.widget_22)
        self.arch_code_in_group_search.setObjectName(u"arch_code_in_group_search")
        self.arch_code_in_group_search.setFont(font)
        self.arch_code_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.arch_code_in_group_search, 1, 1, 1, 1)

        self.label_207 = QLabel(self.widget_22)
        self.label_207.setObjectName(u"label_207")
        self.label_207.setMaximumSize(QSize(120, 16777215))
        self.label_207.setFont(font)
        self.label_207.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_207, 6, 3, 1, 1)

        self.group_title_in_group_search = QLineEdit(self.widget_22)
        self.group_title_in_group_search.setObjectName(u"group_title_in_group_search")
        sizePolicy4.setHeightForWidth(self.group_title_in_group_search.sizePolicy().hasHeightForWidth())
        self.group_title_in_group_search.setSizePolicy(sizePolicy4)
        self.group_title_in_group_search.setFont(font)
        self.group_title_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.group_title_in_group_search, 0, 1, 1, 4)

        self.label_202 = QLabel(self.widget_22)
        self.label_202.setObjectName(u"label_202")
        self.label_202.setFont(font)
        self.label_202.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_202, 7, 0, 1, 1)

        self.label_203 = QLabel(self.widget_22)
        self.label_203.setObjectName(u"label_203")
        self.label_203.setMaximumSize(QSize(120, 16777215))
        self.label_203.setFont(font)
        self.label_203.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_203, 1, 3, 1, 1)

        self.label_188 = QLabel(self.widget_22)
        self.label_188.setObjectName(u"label_188")
        self.label_188.setFont(font)
        self.label_188.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_188, 14, 0, 1, 1)

        self.label_193 = QLabel(self.widget_22)
        self.label_193.setObjectName(u"label_193")
        self.label_193.setFont(font)
        self.label_193.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_193, 1, 0, 1, 1)

        self.taken_locations_in_group_search = QLineEdit(self.widget_22)
        self.taken_locations_in_group_search.setObjectName(u"taken_locations_in_group_search")
        sizePolicy4.setHeightForWidth(self.taken_locations_in_group_search.sizePolicy().hasHeightForWidth())
        self.taken_locations_in_group_search.setSizePolicy(sizePolicy4)
        self.taken_locations_in_group_search.setFont(font)
        self.taken_locations_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.taken_locations_in_group_search, 7, 4, 1, 1)

        self.label_201 = QLabel(self.widget_22)
        self.label_201.setObjectName(u"label_201")
        self.label_201.setFont(font)
        self.label_201.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_201, 2, 0, 1, 1)

        self.format_in_photo_search = QLineEdit(self.widget_22)
        self.format_in_photo_search.setObjectName(u"format_in_photo_search")
        self.format_in_photo_search.setFont(font)
        self.format_in_photo_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.format_in_photo_search, 11, 1, 1, 1)

        self.group_code_in_group_search = QLineEdit(self.widget_22)
        self.group_code_in_group_search.setObjectName(u"group_code_in_group_search")
        sizePolicy4.setHeightForWidth(self.group_code_in_group_search.sizePolicy().hasHeightForWidth())
        self.group_code_in_group_search.setSizePolicy(sizePolicy4)
        self.group_code_in_group_search.setFont(font)
        self.group_code_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.group_code_in_group_search, 4, 1, 1, 1)

        self.security_classification_in_group_search = QLineEdit(self.widget_22)
        self.security_classification_in_group_search.setObjectName(u"security_classification_in_group_search")
        self.security_classification_in_group_search.setFont(font)
        self.security_classification_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.security_classification_in_group_search, 8, 4, 1, 1)

        self.author_in_group_search = QLineEdit(self.widget_22)
        self.author_in_group_search.setObjectName(u"author_in_group_search")
        sizePolicy4.setHeightForWidth(self.author_in_group_search.sizePolicy().hasHeightForWidth())
        self.author_in_group_search.setSizePolicy(sizePolicy4)
        self.author_in_group_search.setFont(font)
        self.author_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.author_in_group_search, 4, 4, 1, 1)

        self.year_in_group_search = QLineEdit(self.widget_22)
        self.year_in_group_search.setObjectName(u"year_in_group_search")
        sizePolicy4.setHeightForWidth(self.year_in_group_search.sizePolicy().hasHeightForWidth())
        self.year_in_group_search.setSizePolicy(sizePolicy4)
        self.year_in_group_search.setFont(font)
        self.year_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.year_in_group_search, 3, 1, 1, 1)

        self.label_204 = QLabel(self.widget_22)
        self.label_204.setObjectName(u"label_204")
        self.label_204.setFont(font)
        self.label_204.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_204, 4, 0, 1, 1)

        self.department_in_group_search = QLineEdit(self.widget_22)
        self.department_in_group_search.setObjectName(u"department_in_group_search")
        sizePolicy4.setHeightForWidth(self.department_in_group_search.sizePolicy().hasHeightForWidth())
        self.department_in_group_search.setSizePolicy(sizePolicy4)
        self.department_in_group_search.setFont(font)
        self.department_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.department_in_group_search, 3, 4, 1, 1)

        self.reference_code_in_group_search = QLineEdit(self.widget_22)
        self.reference_code_in_group_search.setObjectName(u"reference_code_in_group_search")
        sizePolicy4.setHeightForWidth(self.reference_code_in_group_search.sizePolicy().hasHeightForWidth())
        self.reference_code_in_group_search.setSizePolicy(sizePolicy4)
        self.reference_code_in_group_search.setFont(font)
        self.reference_code_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.reference_code_in_group_search, 9, 1, 1, 1)

        self.label_209 = QLabel(self.widget_22)
        self.label_209.setObjectName(u"label_209")
        self.label_209.setFont(font)
        self.label_209.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_55.addWidget(self.label_209, 9, 0, 1, 1)

        self.fonds_code_in_group_search = QLineEdit(self.widget_22)
        self.fonds_code_in_group_search.setObjectName(u"fonds_code_in_group_search")
        self.fonds_code_in_group_search.setFont(font)
        self.fonds_code_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.fonds_code_in_group_search, 1, 4, 1, 1)

        self.opening_state_in_group_search = QLineEdit(self.widget_22)
        self.opening_state_in_group_search.setObjectName(u"opening_state_in_group_search")
        self.opening_state_in_group_search.setFont(font)
        self.opening_state_in_group_search.setReadOnly(True)

        self.gridLayout_55.addWidget(self.opening_state_in_group_search, 9, 4, 1, 1)

        self.horizontalSpacer_29 = QSpacerItem(25, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_55.addItem(self.horizontalSpacer_29, 1, 2, 1, 1)

        self.splitter_7.addWidget(self.widget_22)
        self.widget_23 = QWidget(self.splitter_7)
        self.widget_23.setObjectName(u"widget_23")
        self.widget_23.setMinimumSize(QSize(600, 0))
        self.widget_23.setFont(font)
        self.gridLayout_56 = QGridLayout(self.widget_23)
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.photo_view_search = QLabel(self.widget_23)
        self.photo_view_search.setObjectName(u"photo_view_search")
        self.photo_view_search.setFont(font)

        self.gridLayout_56.addWidget(self.photo_view_search, 0, 0, 1, 1)

        self.splitter_7.addWidget(self.widget_23)
        self.splitter_8.addWidget(self.splitter_7)
        self.widget_24 = QWidget(self.splitter_8)
        self.widget_24.setObjectName(u"widget_24")
        self.widget_24.setMaximumSize(QSize(16777215, 16777215))
        self.widget_24.setFont(font)
        self.gridLayout_57 = QGridLayout(self.widget_24)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.photo_list_widget_search = QListWidget(self.widget_24)
        self.photo_list_widget_search.setObjectName(u"photo_list_widget_search")
        self.photo_list_widget_search.setFont(font)
        self.photo_list_widget_search.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.photo_list_widget_search.setItemAlignment(Qt.AlignBottom)

        self.gridLayout_57.addWidget(self.photo_list_widget_search, 0, 0, 1, 1)

        self.splitter_8.addWidget(self.widget_24)
        self.splitter_9.addWidget(self.splitter_8)

        self.gridLayout_30.addWidget(self.splitter_9, 0, 0, 1, 1)

        icon17 = QIcon()
        icon17.addFile(u"icon/search_arch.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.search_archives_tab, icon17, "")
        self.arch_transfer_tab = QWidget()
        self.arch_transfer_tab.setObjectName(u"arch_transfer_tab")
        self.arch_transfer_tab.setFont(font)
        self.gridLayout_23 = QGridLayout(self.arch_transfer_tab)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.splitter_5 = QSplitter(self.arch_transfer_tab)
        self.splitter_5.setObjectName(u"splitter_5")
        self.splitter_5.setOrientation(Qt.Horizontal)
        self.widget_9 = QWidget(self.splitter_5)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMaximumSize(QSize(500, 16777215))
        self.widget_9.setFont(font)
        self.gridLayout_2 = QGridLayout(self.widget_9)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, -1, 12, -1)
        self.label_68 = QLabel(self.widget_9)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font)
        self.label_68.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_2.addWidget(self.label_68, 0, 0, 1, 1)

        self.order_combobox_transfer = QComboBox(self.widget_9)
        self.order_combobox_transfer.addItem("")
        self.order_combobox_transfer.addItem("")
        self.order_combobox_transfer.setObjectName(u"order_combobox_transfer")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.order_combobox_transfer.sizePolicy().hasHeightForWidth())
        self.order_combobox_transfer.setSizePolicy(sizePolicy6)
        self.order_combobox_transfer.setFont(font)

        self.gridLayout_2.addWidget(self.order_combobox_transfer, 0, 1, 1, 1)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_17, 0, 2, 1, 1)

        self.arch_tree_view_transfer = QTreeView(self.widget_9)
        self.arch_tree_view_transfer.setObjectName(u"arch_tree_view_transfer")
        self.arch_tree_view_transfer.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_2.addWidget(self.arch_tree_view_transfer, 1, 0, 1, 3)

        self.label_70 = QLabel(self.widget_9)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font)

        self.gridLayout_2.addWidget(self.label_70, 2, 0, 1, 2)

        self.selected_arch_list_widget = QListWidget(self.widget_9)
        self.selected_arch_list_widget.setObjectName(u"selected_arch_list_widget")
        sizePolicy.setHeightForWidth(self.selected_arch_list_widget.sizePolicy().hasHeightForWidth())
        self.selected_arch_list_widget.setSizePolicy(sizePolicy)
        self.selected_arch_list_widget.setFont(font)
        self.selected_arch_list_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.selected_arch_list_widget.setDragEnabled(False)

        self.gridLayout_2.addWidget(self.selected_arch_list_widget, 3, 0, 1, 3)

        self.splitter_5.addWidget(self.widget_9)
        self.widget_10 = QWidget(self.splitter_5)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setMinimumSize(QSize(0, 0))
        self.widget_10.setFont(font)
        self.gridLayout_25 = QGridLayout(self.widget_10)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_25.setContentsMargins(12, -1, -1, -1)
        self.label_86 = QLabel(self.widget_10)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setFont(font)
        self.label_86.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_86, 6, 0, 1, 1)

        self.label_77 = QLabel(self.widget_10)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font)
        self.label_77.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_77, 1, 0, 1, 1)

        self.label_82 = QLabel(self.widget_10)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font)
        self.label_82.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_82, 7, 0, 1, 1)

        self.label_87 = QLabel(self.widget_10)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font)
        self.label_87.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_87, 11, 0, 1, 1)

        self.label_73 = QLabel(self.widget_10)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font)
        self.label_73.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_73, 0, 2, 1, 1)

        self.across_year_combo_box = QComboBox(self.widget_10)
        self.across_year_combo_box.addItem("")
        self.across_year_combo_box.addItem("")
        self.across_year_combo_box.setObjectName(u"across_year_combo_box")
        self.across_year_combo_box.setFont(font)

        self.gridLayout_25.addWidget(self.across_year_combo_box, 0, 3, 1, 1)

        self.label_89 = QLabel(self.widget_10)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setFont(font)
        self.label_89.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_89, 12, 0, 1, 1)

        self.label_90 = QLabel(self.widget_10)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setFont(font)
        self.label_90.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_90, 13, 4, 1, 1)

        self.across_period_combo_box = QComboBox(self.widget_10)
        self.across_period_combo_box.addItem("")
        self.across_period_combo_box.addItem("")
        self.across_period_combo_box.setObjectName(u"across_period_combo_box")
        self.across_period_combo_box.setFont(font)

        self.gridLayout_25.addWidget(self.across_period_combo_box, 0, 5, 1, 2)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_25.addItem(self.horizontalSpacer_18, 0, 7, 1, 1)

        self.label_88 = QLabel(self.widget_10)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setFont(font)
        self.label_88.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_88, 11, 2, 1, 1)

        self.frame_10 = QFrame(self.widget_10)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy3.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy3)
        self.frame_10.setMinimumSize(QSize(0, 50))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_10)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.gridLayout_27.setContentsMargins(-1, 3, -1, 3)
        self.horizontalSpacer_19 = QSpacerItem(307, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_19, 0, 0, 1, 1)

        self.packeage_btn = QPushButton(self.frame_10)
        self.packeage_btn.setObjectName(u"packeage_btn")
        sizePolicy3.setHeightForWidth(self.packeage_btn.sizePolicy().hasHeightForWidth())
        self.packeage_btn.setSizePolicy(sizePolicy3)
        self.packeage_btn.setMinimumSize(QSize(0, 42))
        self.packeage_btn.setFont(font)
        self.packeage_btn.setStyleSheet(u"padding-left: 30px; \n"
"padding-right: 30px;\n"
"padding-top: 8px; \n"
"padding-bottom: 8px;")
        icon18 = QIcon()
        icon18.addFile(u"icon/package.png", QSize(), QIcon.Normal, QIcon.Off)
        self.packeage_btn.setIcon(icon18)
        self.packeage_btn.setIconSize(QSize(24, 24))

        self.gridLayout_27.addWidget(self.packeage_btn, 0, 1, 1, 1)

        self.horizontalSpacer_20 = QSpacerItem(307, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_27.addItem(self.horizontalSpacer_20, 0, 2, 1, 1)


        self.gridLayout_25.addWidget(self.frame_10, 19, 0, 1, 8)

        self.cd_size_line_edit = QLineEdit(self.widget_10)
        self.cd_size_line_edit.setObjectName(u"cd_size_line_edit")
        sizePolicy6.setHeightForWidth(self.cd_size_line_edit.sizePolicy().hasHeightForWidth())
        self.cd_size_line_edit.setSizePolicy(sizePolicy6)
        self.cd_size_line_edit.setFont(font)

        self.gridLayout_25.addWidget(self.cd_size_line_edit, 0, 1, 1, 1)

        self.operation_date_in_transfer = QLineEdit(self.widget_10)
        self.operation_date_in_transfer.setObjectName(u"operation_date_in_transfer")
        self.operation_date_in_transfer.setFont(font)

        self.gridLayout_25.addWidget(self.operation_date_in_transfer, 7, 6, 1, 1)

        self.group_codes_in_transfer = QLineEdit(self.widget_10)
        self.group_codes_in_transfer.setObjectName(u"group_codes_in_transfer")
        self.group_codes_in_transfer.setFont(font)

        self.gridLayout_25.addWidget(self.group_codes_in_transfer, 12, 1, 1, 3)

        self.cd_catalog_table_widget = QTableWidget(self.widget_10)
        if (self.cd_catalog_table_widget.columnCount() < 9):
            self.cd_catalog_table_widget.setColumnCount(9)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.cd_catalog_table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.cd_catalog_table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.cd_catalog_table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.cd_catalog_table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.cd_catalog_table_widget.setHorizontalHeaderItem(4, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        self.cd_catalog_table_widget.setHorizontalHeaderItem(5, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font1);
        self.cd_catalog_table_widget.setHorizontalHeaderItem(6, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font1);
        self.cd_catalog_table_widget.setHorizontalHeaderItem(7, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font1);
        self.cd_catalog_table_widget.setHorizontalHeaderItem(8, __qtablewidgetitem11)
        self.cd_catalog_table_widget.setObjectName(u"cd_catalog_table_widget")
        sizePolicy.setHeightForWidth(self.cd_catalog_table_widget.sizePolicy().hasHeightForWidth())
        self.cd_catalog_table_widget.setSizePolicy(sizePolicy)
        self.cd_catalog_table_widget.setFont(font)
        self.cd_catalog_table_widget.setStyleSheet(u"   QHeaderView::section{\n"
"            border-top:0px solid #D8D8D8;\n"
"            border-left:0px solid #D8D8D8;\n"
"            border-right:1px solid #D8D8D8;\n"
"            border-bottom: 1px solid #D8D8D8;\n"
"            background-color:white;\n"
"            padding:4px;\n"
"        }\n"
"        QTableCornerButton::section{\n"
"            border-top:0px solid #D8D8D8;\n"
"            border-left:0px solid #D8D8D8;\n"
"            border-right:1px solid #D8D8D8;\n"
"            border-bottom: 1px solid #D8D8D8;\n"
"            background-color:white;\n"
"        }")
        self.cd_catalog_table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.cd_catalog_table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.cd_catalog_table_widget.horizontalHeader().setCascadingSectionResizes(False)
        self.cd_catalog_table_widget.horizontalHeader().setStretchLastSection(False)
        self.cd_catalog_table_widget.verticalHeader().setVisible(False)
        self.cd_catalog_table_widget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_25.addWidget(self.cd_catalog_table_widget, 4, 0, 1, 8)

        self.cd_num_in_transfer = QLineEdit(self.widget_10)
        self.cd_num_in_transfer.setObjectName(u"cd_num_in_transfer")
        self.cd_num_in_transfer.setFont(font)

        self.gridLayout_25.addWidget(self.cd_num_in_transfer, 13, 6, 1, 1)

        self.label_83 = QLabel(self.widget_10)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font)
        self.label_83.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_83, 7, 4, 1, 1)

        self.label_74 = QLabel(self.widget_10)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font)
        self.label_74.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_74, 0, 4, 1, 1)

        self.label_84 = QLabel(self.widget_10)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font)
        self.label_84.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_84, 7, 2, 1, 1)

        self.fonds_code_in_transfer = QLineEdit(self.widget_10)
        self.fonds_code_in_transfer.setObjectName(u"fonds_code_in_transfer")
        self.fonds_code_in_transfer.setFont(font)
        self.fonds_code_in_transfer.setReadOnly(True)

        self.gridLayout_25.addWidget(self.fonds_code_in_transfer, 11, 3, 1, 1)

        self.label_72 = QLabel(self.widget_10)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font)
        self.label_72.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_72, 0, 0, 1, 1)

        self.label_85 = QLabel(self.widget_10)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setFont(font)
        self.label_85.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_85, 8, 0, 1, 1)

        self.fonds_name_in_transfer = QLineEdit(self.widget_10)
        self.fonds_name_in_transfer.setObjectName(u"fonds_name_in_transfer")
        self.fonds_name_in_transfer.setFont(font)
        self.fonds_name_in_transfer.setReadOnly(True)

        self.gridLayout_25.addWidget(self.fonds_name_in_transfer, 11, 1, 1, 1)

        self.partition_list_widget = QListWidget(self.widget_10)
        self.partition_list_widget.setObjectName(u"partition_list_widget")
        sizePolicy.setHeightForWidth(self.partition_list_widget.sizePolicy().hasHeightForWidth())
        self.partition_list_widget.setSizePolicy(sizePolicy)
        self.partition_list_widget.setMinimumSize(QSize(1, 1))
        self.partition_list_widget.setFont(font)
        self.partition_list_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.gridLayout_25.addWidget(self.partition_list_widget, 2, 0, 1, 8)

        self.label_79 = QLabel(self.widget_10)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font)

        self.gridLayout_25.addWidget(self.label_79, 5, 0, 1, 1)

        self.title_in_transfer = QLineEdit(self.widget_10)
        self.title_in_transfer.setObjectName(u"title_in_transfer")
        self.title_in_transfer.setFont(font)

        self.gridLayout_25.addWidget(self.title_in_transfer, 6, 1, 1, 6)

        self.label_78 = QLabel(self.widget_10)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font)

        self.gridLayout_25.addWidget(self.label_78, 10, 0, 1, 1)

        self.label_71 = QLabel(self.widget_10)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font)

        self.gridLayout_25.addWidget(self.label_71, 3, 0, 1, 1)

        self.label_91 = QLabel(self.widget_10)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setFont(font)
        self.label_91.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_91, 13, 0, 1, 1)

        self.photo_num_in_transfer = QLineEdit(self.widget_10)
        self.photo_num_in_transfer.setObjectName(u"photo_num_in_transfer")
        self.photo_num_in_transfer.setFont(font)

        self.gridLayout_25.addWidget(self.photo_num_in_transfer, 13, 1, 1, 1)

        self.label_81 = QLabel(self.widget_10)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font)
        self.label_81.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_25.addWidget(self.label_81, 13, 2, 1, 1)

        self.cd_model_in_transfer = QComboBox(self.widget_10)
        self.cd_model_in_transfer.addItem("")
        self.cd_model_in_transfer.addItem("")
        self.cd_model_in_transfer.setObjectName(u"cd_model_in_transfer")
        self.cd_model_in_transfer.setFont(font)

        self.gridLayout_25.addWidget(self.cd_model_in_transfer, 7, 1, 1, 1)

        self.file_type_in_transfer = QComboBox(self.widget_10)
        self.file_type_in_transfer.addItem("")
        self.file_type_in_transfer.addItem("")
        self.file_type_in_transfer.addItem("")
        self.file_type_in_transfer.addItem("")
        self.file_type_in_transfer.setObjectName(u"file_type_in_transfer")
        self.file_type_in_transfer.setFont(font)

        self.gridLayout_25.addWidget(self.file_type_in_transfer, 7, 3, 1, 1)

        self.cd_type_in_transfer = QComboBox(self.widget_10)
        self.cd_type_in_transfer.addItem("")
        self.cd_type_in_transfer.setObjectName(u"cd_type_in_transfer")
        self.cd_type_in_transfer.setFont(font)

        self.gridLayout_25.addWidget(self.cd_type_in_transfer, 13, 3, 1, 1)

        self.operator_in_transfer = QLineEdit(self.widget_10)
        self.operator_in_transfer.setObjectName(u"operator_in_transfer")
        self.operator_in_transfer.setFont(font)

        self.gridLayout_25.addWidget(self.operator_in_transfer, 8, 1, 1, 3)

        self.splitter_5.addWidget(self.widget_10)

        self.gridLayout_23.addWidget(self.splitter_5, 0, 0, 1, 1)

        icon19 = QIcon()
        icon19.addFile(u"icon/arch_transfer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.arch_transfer_tab, icon19, "")
        self.setting_tab = QWidget()
        self.setting_tab.setObjectName(u"setting_tab")
        self.setting_tab.setFont(font)
        self.gridLayout_32 = QGridLayout(self.setting_tab)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.verticalSpacer_12 = QSpacerItem(20, 15, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_32.addItem(self.verticalSpacer_12, 0, 1, 1, 1)

        self.horizontalSpacer_33 = QSpacerItem(245, 49, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_33, 1, 0, 1, 1)

        self.groupBox_2 = QGroupBox(self.setting_tab)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy3.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy3)
        self.groupBox_2.setFont(font)
        self.gridLayout_28 = QGridLayout(self.groupBox_2)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(-1, 12, -1, 20)
        self.label_93 = QLabel(self.groupBox_2)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setFont(font)

        self.gridLayout_28.addWidget(self.label_93, 1, 0, 1, 1)

        self.fonds_name_in_setting = QLineEdit(self.groupBox_2)
        self.fonds_name_in_setting.setObjectName(u"fonds_name_in_setting")
        self.fonds_name_in_setting.setFont(font)

        self.gridLayout_28.addWidget(self.fonds_name_in_setting, 0, 1, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_28.addItem(self.horizontalSpacer_21, 0, 2, 1, 1)

        self.fonds_code_in_setting = QLineEdit(self.groupBox_2)
        self.fonds_code_in_setting.setObjectName(u"fonds_code_in_setting")
        self.fonds_code_in_setting.setFont(font)

        self.gridLayout_28.addWidget(self.fonds_code_in_setting, 1, 1, 1, 1)

        self.label_92 = QLabel(self.groupBox_2)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font)

        self.gridLayout_28.addWidget(self.label_92, 0, 0, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox_2, 1, 1, 1, 1)

        self.horizontalSpacer_30 = QSpacerItem(342, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_30, 1, 2, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_32.addItem(self.verticalSpacer_9, 2, 2, 1, 1)

        self.horizontalSpacer_34 = QSpacerItem(245, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_34, 3, 0, 1, 1)

        self.groupBox = QGroupBox(self.setting_tab)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.groupBox.setFont(font)
        self.gridLayout_26 = QGridLayout(self.groupBox)
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.gridLayout_26.setContentsMargins(-1, 12, -1, 20)
        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_26.addItem(self.horizontalSpacer_22, 0, 3, 1, 1)

        self.description_path_in_setting = QLineEdit(self.groupBox)
        self.description_path_in_setting.setObjectName(u"description_path_in_setting")
        sizePolicy5.setHeightForWidth(self.description_path_in_setting.sizePolicy().hasHeightForWidth())
        self.description_path_in_setting.setSizePolicy(sizePolicy5)
        self.description_path_in_setting.setFont(font)

        self.gridLayout_26.addWidget(self.description_path_in_setting, 0, 1, 1, 1)

        self.select_description_dir_btn = QPushButton(self.groupBox)
        self.select_description_dir_btn.setObjectName(u"select_description_dir_btn")
        sizePolicy6.setHeightForWidth(self.select_description_dir_btn.sizePolicy().hasHeightForWidth())
        self.select_description_dir_btn.setSizePolicy(sizePolicy6)
        self.select_description_dir_btn.setFont(font)
        self.select_description_dir_btn.setStyleSheet(u"padding-left: 30px; \n"
"padding-right: 30px;\n"
"padding-top: 8px; \n"
"padding-bottom: 8px;")
        self.select_description_dir_btn.setIcon(icon1)
        self.select_description_dir_btn.setIconSize(QSize(24, 24))

        self.gridLayout_26.addWidget(self.select_description_dir_btn, 0, 2, 1, 1)

        self.package_path_in_setting = QLineEdit(self.groupBox)
        self.package_path_in_setting.setObjectName(u"package_path_in_setting")
        sizePolicy5.setHeightForWidth(self.package_path_in_setting.sizePolicy().hasHeightForWidth())
        self.package_path_in_setting.setSizePolicy(sizePolicy5)
        self.package_path_in_setting.setFont(font)

        self.gridLayout_26.addWidget(self.package_path_in_setting, 1, 1, 1, 1)

        self.label_75 = QLabel(self.groupBox)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font)

        self.gridLayout_26.addWidget(self.label_75, 0, 0, 1, 1)

        self.select_package_dir_btn = QPushButton(self.groupBox)
        self.select_package_dir_btn.setObjectName(u"select_package_dir_btn")
        sizePolicy6.setHeightForWidth(self.select_package_dir_btn.sizePolicy().hasHeightForWidth())
        self.select_package_dir_btn.setSizePolicy(sizePolicy6)
        self.select_package_dir_btn.setFont(font)
        self.select_package_dir_btn.setStyleSheet(u"padding-left: 30px; \n"
"padding-right: 30px;\n"
"padding-top: 8px; \n"
"padding-bottom: 8px;")
        self.select_package_dir_btn.setIcon(icon1)
        self.select_package_dir_btn.setIconSize(QSize(24, 24))

        self.gridLayout_26.addWidget(self.select_package_dir_btn, 1, 2, 1, 1)

        self.label_76 = QLabel(self.groupBox)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font)

        self.gridLayout_26.addWidget(self.label_76, 1, 0, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox, 3, 1, 1, 1)

        self.horizontalSpacer_31 = QSpacerItem(345, 140, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_31, 3, 2, 1, 1)

        self.verticalSpacer_10 = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout_32.addItem(self.verticalSpacer_10, 4, 2, 1, 1)

        self.horizontalSpacer_35 = QSpacerItem(245, 20, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_35, 5, 0, 1, 1)

        self.groupBox_3 = QGroupBox(self.setting_tab)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy3.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy3)
        self.groupBox_3.setFont(font)
        self.gridLayout_29 = QGridLayout(self.groupBox_3)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(-1, 12, -1, 20)
        self.label_96 = QLabel(self.groupBox_3)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setFont(font)

        self.gridLayout_29.addWidget(self.label_96, 1, 0, 1, 1)

        self.license_path_in_setting = QLineEdit(self.groupBox_3)
        self.license_path_in_setting.setObjectName(u"license_path_in_setting")
        self.license_path_in_setting.setFont(font)

        self.gridLayout_29.addWidget(self.license_path_in_setting, 0, 1, 1, 1)

        self.license_remaining_photo_num = QLineEdit(self.groupBox_3)
        self.license_remaining_photo_num.setObjectName(u"license_remaining_photo_num")
        self.license_remaining_photo_num.setEnabled(True)
        self.license_remaining_photo_num.setFont(font)
        self.license_remaining_photo_num.setReadOnly(True)

        self.gridLayout_29.addWidget(self.license_remaining_photo_num, 2, 1, 1, 1)

        self.license_enable_export = QLineEdit(self.groupBox_3)
        self.license_enable_export.setObjectName(u"license_enable_export")
        self.license_enable_export.setEnabled(True)
        self.license_enable_export.setFont(font)
        self.license_enable_export.setReadOnly(True)

        self.gridLayout_29.addWidget(self.license_enable_export, 4, 1, 1, 1)

        self.label_95 = QLabel(self.groupBox_3)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setFont(font)

        self.gridLayout_29.addWidget(self.label_95, 2, 0, 1, 1)

        self.label_97 = QLabel(self.groupBox_3)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setFont(font)

        self.gridLayout_29.addWidget(self.label_97, 3, 0, 1, 1)

        self.license_enable_gpu = QLineEdit(self.groupBox_3)
        self.license_enable_gpu.setObjectName(u"license_enable_gpu")
        self.license_enable_gpu.setEnabled(True)
        self.license_enable_gpu.setFont(font)
        self.license_enable_gpu.setReadOnly(True)

        self.gridLayout_29.addWidget(self.license_enable_gpu, 3, 1, 1, 1)

        self.import_license_btn = QPushButton(self.groupBox_3)
        self.import_license_btn.setObjectName(u"import_license_btn")
        sizePolicy6.setHeightForWidth(self.import_license_btn.sizePolicy().hasHeightForWidth())
        self.import_license_btn.setSizePolicy(sizePolicy6)
        self.import_license_btn.setFont(font)
        self.import_license_btn.setStyleSheet(u"padding: 8px 15px; \n"
"")
        icon20 = QIcon()
        icon20.addFile(u"icon/import.png", QSize(), QIcon.Normal, QIcon.Off)
        self.import_license_btn.setIcon(icon20)
        self.import_license_btn.setIconSize(QSize(24, 24))

        self.gridLayout_29.addWidget(self.import_license_btn, 0, 2, 1, 1)

        self.label_94 = QLabel(self.groupBox_3)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setFont(font)

        self.gridLayout_29.addWidget(self.label_94, 0, 0, 1, 1)

        self.license_remaining_days = QLineEdit(self.groupBox_3)
        self.license_remaining_days.setObjectName(u"license_remaining_days")
        self.license_remaining_days.setEnabled(True)
        self.license_remaining_days.setFont(font)
        self.license_remaining_days.setReadOnly(True)

        self.gridLayout_29.addWidget(self.license_remaining_days, 1, 1, 1, 1)

        self.label_98 = QLabel(self.groupBox_3)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setFont(font)

        self.gridLayout_29.addWidget(self.label_98, 4, 0, 1, 1)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_29.addItem(self.horizontalSpacer_23, 0, 3, 1, 1)


        self.gridLayout_32.addWidget(self.groupBox_3, 5, 1, 1, 1)

        self.horizontalSpacer_32 = QSpacerItem(345, 220, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.gridLayout_32.addItem(self.horizontalSpacer_32, 5, 2, 1, 1)

        self.verticalSpacer_11 = QSpacerItem(20, 184, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_32.addItem(self.verticalSpacer_11, 6, 2, 1, 1)

        icon21 = QIcon()
        icon21.addFile(u"icon/setting.png", QSize(), QIcon.Normal, QIcon.Off)
        self.tabWidget.addTab(self.setting_tab, icon21, "")

        self.gridLayout_24.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.tabWidget, self.dir_lineEdit)
        QWidget.setTabOrder(self.dir_lineEdit, self.open_dir_btn)
        QWidget.setTabOrder(self.open_dir_btn, self.tree_widget_group)
        QWidget.setTabOrder(self.tree_widget_group, self.fonds_code_in_group)
        QWidget.setTabOrder(self.fonds_code_in_group, self.arch_category_code_in_group)
        QWidget.setTabOrder(self.arch_category_code_in_group, self.retention_period_in_group)
        QWidget.setTabOrder(self.retention_period_in_group, self.year_in_group)
        QWidget.setTabOrder(self.year_in_group, self.department_in_group)
        QWidget.setTabOrder(self.department_in_group, self.group_code_in_group)
        QWidget.setTabOrder(self.group_code_in_group, self.author_in_group)
        QWidget.setTabOrder(self.author_in_group, self.folder_size_in_group)
        QWidget.setTabOrder(self.folder_size_in_group, self.photographer_in_group)
        QWidget.setTabOrder(self.photographer_in_group, self.taken_time_in_group)
        QWidget.setTabOrder(self.taken_time_in_group, self.taken_locations_in_group)
        QWidget.setTabOrder(self.taken_locations_in_group, self.photo_num_in_group)
        QWidget.setTabOrder(self.photo_num_in_group, self.security_classification_in_group)
        QWidget.setTabOrder(self.security_classification_in_group, self.reference_code_in_group)
        QWidget.setTabOrder(self.reference_code_in_group, self.opening_state_in_group)
        QWidget.setTabOrder(self.opening_state_in_group, self.group_caption_in_group)
        QWidget.setTabOrder(self.group_caption_in_group, self.save_group_btn)
        QWidget.setTabOrder(self.save_group_btn, self.selected_dir_radioButton)
        QWidget.setTabOrder(self.selected_dir_radioButton, self.current_dir_radioButton)
        QWidget.setTabOrder(self.current_dir_radioButton, self.all_photo_radioButton)
        QWidget.setTabOrder(self.all_photo_radioButton, self.part_recognition_radioButton)
        QWidget.setTabOrder(self.part_recognition_radioButton, self.all_recognition_radioButton)
        QWidget.setTabOrder(self.all_recognition_radioButton, self.arch_code_in_photo)
        QWidget.setTabOrder(self.arch_code_in_photo, self.fonds_code_in_photo)
        QWidget.setTabOrder(self.fonds_code_in_photo, self.arch_category_code_in_photo)
        QWidget.setTabOrder(self.arch_category_code_in_photo, self.year_in_photo)
        QWidget.setTabOrder(self.year_in_photo, self.group_code_in_photo)
        QWidget.setTabOrder(self.group_code_in_photo, self.photographer_in_photo)
        QWidget.setTabOrder(self.photographer_in_photo, self.taken_time_in_photo)
        QWidget.setTabOrder(self.taken_time_in_photo, self.taken_locations_in_photo)
        QWidget.setTabOrder(self.taken_locations_in_photo, self.format_in_photo)
        QWidget.setTabOrder(self.format_in_photo, self.security_classification_in_photo)
        QWidget.setTabOrder(self.security_classification_in_photo, self.reference_code_in_photo)
        QWidget.setTabOrder(self.reference_code_in_photo, self.photo_code_in_photo)
        QWidget.setTabOrder(self.photo_code_in_photo, self.peoples_in_photo)
        QWidget.setTabOrder(self.peoples_in_photo, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.verifycheckBox)
        QWidget.setTabOrder(self.verifycheckBox, self.thresh_lineEdit)
        QWidget.setTabOrder(self.thresh_lineEdit, self.order_combobox_browse)
        QWidget.setTabOrder(self.order_combobox_browse, self.arch_tree_view_browse)
        QWidget.setTabOrder(self.arch_tree_view_browse, self.photo_list_widget)
        QWidget.setTabOrder(self.photo_list_widget, self.arch_code_in_group_arch)
        QWidget.setTabOrder(self.arch_code_in_group_arch, self.fonds_code_in_group_arch)
        QWidget.setTabOrder(self.fonds_code_in_group_arch, self.arch_category_code_in_group_arch)
        QWidget.setTabOrder(self.arch_category_code_in_group_arch, self.retention_period_in_group_arch)
        QWidget.setTabOrder(self.retention_period_in_group_arch, self.year_in_group_arch)
        QWidget.setTabOrder(self.year_in_group_arch, self.department_in_group_arch)
        QWidget.setTabOrder(self.department_in_group_arch, self.group_code_in_group_arch)
        QWidget.setTabOrder(self.group_code_in_group_arch, self.author_in_group_arch)
        QWidget.setTabOrder(self.author_in_group_arch, self.folder_size_in_group_arch)
        QWidget.setTabOrder(self.folder_size_in_group_arch, self.photographer_in_group_arch)
        QWidget.setTabOrder(self.photographer_in_group_arch, self.taken_time_in_group_arch)
        QWidget.setTabOrder(self.taken_time_in_group_arch, self.taken_locations_in_group_arch)
        QWidget.setTabOrder(self.taken_locations_in_group_arch, self.photo_num_in_group_arch)
        QWidget.setTabOrder(self.photo_num_in_group_arch, self.security_classification_in_group_arch)
        QWidget.setTabOrder(self.security_classification_in_group_arch, self.reference_code_in_group_arch)
        QWidget.setTabOrder(self.reference_code_in_group_arch, self.opening_state_in_group_arch)
        QWidget.setTabOrder(self.opening_state_in_group_arch, self.arch_code_in_photo_arch)
        QWidget.setTabOrder(self.arch_code_in_photo_arch, self.photo_code_in_photo_arch)
        QWidget.setTabOrder(self.photo_code_in_photo_arch, self.format_in_photo_arch)
        QWidget.setTabOrder(self.format_in_photo_arch, self.group_caption_in_group_arch)
        QWidget.setTabOrder(self.group_caption_in_group_arch, self.peoples_in_photo_arch)
        QWidget.setTabOrder(self.peoples_in_photo_arch, self.group_title_search)
        QWidget.setTabOrder(self.group_title_search, self.peoples_search)
        QWidget.setTabOrder(self.peoples_search, self.search_btn)
        QWidget.setTabOrder(self.search_btn, self.group_tree_widget_search)
        QWidget.setTabOrder(self.group_tree_widget_search, self.photo_list_widget_search)
        QWidget.setTabOrder(self.photo_list_widget_search, self.arch_code_in_group_search)
        QWidget.setTabOrder(self.arch_code_in_group_search, self.fonds_code_in_group_search)
        QWidget.setTabOrder(self.fonds_code_in_group_search, self.arch_category_code_in_group_search)
        QWidget.setTabOrder(self.arch_category_code_in_group_search, self.retention_period_in_group_search)
        QWidget.setTabOrder(self.retention_period_in_group_search, self.year_in_group_search)
        QWidget.setTabOrder(self.year_in_group_search, self.department_in_group_search)
        QWidget.setTabOrder(self.department_in_group_search, self.group_code_in_group_search)
        QWidget.setTabOrder(self.group_code_in_group_search, self.author_in_group_search)
        QWidget.setTabOrder(self.author_in_group_search, self.folder_size_in_group_search)
        QWidget.setTabOrder(self.folder_size_in_group_search, self.photographer_in_group_search)
        QWidget.setTabOrder(self.photographer_in_group_search, self.taken_time_in_group_search)
        QWidget.setTabOrder(self.taken_time_in_group_search, self.taken_locations_in_group_search)
        QWidget.setTabOrder(self.taken_locations_in_group_search, self.photo_num_in_group_search)
        QWidget.setTabOrder(self.photo_num_in_group_search, self.security_classification_in_group_search)
        QWidget.setTabOrder(self.security_classification_in_group_search, self.reference_code_in_group_search)
        QWidget.setTabOrder(self.reference_code_in_group_search, self.opening_state_in_group_search)
        QWidget.setTabOrder(self.opening_state_in_group_search, self.arch_code_in_photo_search)
        QWidget.setTabOrder(self.arch_code_in_photo_search, self.photo_code_in_photo_search)
        QWidget.setTabOrder(self.photo_code_in_photo_search, self.format_in_photo_search)
        QWidget.setTabOrder(self.format_in_photo_search, self.group_caption_in_group_search)
        QWidget.setTabOrder(self.group_caption_in_group_search, self.peoples_in_photo_search)
        QWidget.setTabOrder(self.peoples_in_photo_search, self.order_combobox_transfer)
        QWidget.setTabOrder(self.order_combobox_transfer, self.arch_tree_view_transfer)
        QWidget.setTabOrder(self.arch_tree_view_transfer, self.selected_arch_list_widget)
        QWidget.setTabOrder(self.selected_arch_list_widget, self.cd_size_line_edit)
        QWidget.setTabOrder(self.cd_size_line_edit, self.across_year_combo_box)
        QWidget.setTabOrder(self.across_year_combo_box, self.across_period_combo_box)
        QWidget.setTabOrder(self.across_period_combo_box, self.partition_list_widget)
        QWidget.setTabOrder(self.partition_list_widget, self.cd_catalog_table_widget)
        QWidget.setTabOrder(self.cd_catalog_table_widget, self.title_in_transfer)
        QWidget.setTabOrder(self.title_in_transfer, self.cd_model_in_transfer)
        QWidget.setTabOrder(self.cd_model_in_transfer, self.file_type_in_transfer)
        QWidget.setTabOrder(self.file_type_in_transfer, self.operation_date_in_transfer)
        QWidget.setTabOrder(self.operation_date_in_transfer, self.operator_in_transfer)
        QWidget.setTabOrder(self.operator_in_transfer, self.fonds_name_in_transfer)
        QWidget.setTabOrder(self.fonds_name_in_transfer, self.fonds_code_in_transfer)
        QWidget.setTabOrder(self.fonds_code_in_transfer, self.group_codes_in_transfer)
        QWidget.setTabOrder(self.group_codes_in_transfer, self.photo_num_in_transfer)
        QWidget.setTabOrder(self.photo_num_in_transfer, self.cd_type_in_transfer)
        QWidget.setTabOrder(self.cd_type_in_transfer, self.cd_num_in_transfer)
        QWidget.setTabOrder(self.cd_num_in_transfer, self.packeage_btn)
        QWidget.setTabOrder(self.packeage_btn, self.fonds_name_in_setting)
        QWidget.setTabOrder(self.fonds_name_in_setting, self.fonds_code_in_setting)
        QWidget.setTabOrder(self.fonds_code_in_setting, self.description_path_in_setting)
        QWidget.setTabOrder(self.description_path_in_setting, self.select_description_dir_btn)
        QWidget.setTabOrder(self.select_description_dir_btn, self.package_path_in_setting)
        QWidget.setTabOrder(self.package_path_in_setting, self.select_package_dir_btn)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)
        self.search_btn.setDefault(False)
        self.export_btn_search.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u7167\u7247\u6863\u6848AI\u8f85\u52a9\u8457\u5f55\u7ba1\u7406\u7cfb\u7edfV1.0", None))
        self.actionexit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa(X)", None))
        self.action.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e...", None))
#if QT_CONFIG(tooltip)
        self.open_dir_btn.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u5feb\u6377\u952e\uff1aCtrl+O</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.open_dir_btn.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
#if QT_CONFIG(shortcut)
        self.open_dir_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u5de5\u4f5c\u76ee\u5f55\uff1a", None))
#if QT_CONFIG(tooltip)
        self.tree_widget_group.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u53cc\u51fb\u52fe\u9009</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cancel_folder_btn.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88", None))
        self.add_folder_btn.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0", None))
        self.adding_processing.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u90e8\u95e8", None))
        self.saving_processing.setText("")
        self.opening_state_in_group.setItemText(0, QCoreApplication.translate("MainWindow", u"\u4e3b\u52a8\u516c\u5f00", None))
        self.opening_state_in_group.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4f9d\u7533\u8bf7\u516c\u5f00", None))
        self.opening_state_in_group.setItemText(2, QCoreApplication.translate("MainWindow", u"\u4e0d\u516c\u5f00", None))

        self.label_42.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u5730\u70b9", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u9898\u540d", None))
        self.save_group_btn.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u5927\u5c0f/MB", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u65f6\u95f4", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u653e\u72b6\u6001", None))
        self.retention_period_in_group.setItemText(0, QCoreApplication.translate("MainWindow", u"D10", None))
        self.retention_period_in_group.setItemText(1, QCoreApplication.translate("MainWindow", u"D30", None))
        self.retention_period_in_group.setItemText(2, QCoreApplication.translate("MainWindow", u"Y", None))

        self.security_classification_in_group.setItemText(0, QCoreApplication.translate("MainWindow", u"\u516c\u5f00\u8d44\u6599", None))
        self.security_classification_in_group.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5185\u90e8\u8d44\u6599", None))
        self.security_classification_in_group.setItemText(2, QCoreApplication.translate("MainWindow", u"\u79d8\u5bc6", None))
        self.security_classification_in_group.setItemText(3, QCoreApplication.translate("MainWindow", u"\u673a\u5bc6", None))
        self.security_classification_in_group.setItemText(4, QCoreApplication.translate("MainWindow", u"\u7edd\u5bc6", None))

        self.arch_category_code_in_group.setItemText(0, QCoreApplication.translate("MainWindow", u"ZP", None))
        self.arch_category_code_in_group.setItemText(1, QCoreApplication.translate("MainWindow", u"LY", None))
        self.arch_category_code_in_group.setItemText(2, QCoreApplication.translate("MainWindow", u"LX", None))

        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u7ba1\u671f\u9650", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u5ea6", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"\u5f20\u6570", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u8bf4\u660e\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5b97\u53f7", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u8005", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7ea7", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u8d23\u4efb\u8005", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u89c1\u53f7", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u53f7", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u95e8\u7c7b\u4ee3\u7801", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u6587\u4ef6\u5939\uff1a", None))
        self.group_path_in_group.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"\u6863\u53f7\uff1a", None))
        self.arch_code_in_group.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.group_tab), QCoreApplication.translate("MainWindow", u"\u7ec4\u8457\u5f55", None))
        self.pausecontinue_btn.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.recogni_btn.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"\u90e8\u5206\u8bc6\u522b\u56fe\u7247\uff1a", None))
        self.recognition_rate_label.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u8fdb\u5ea6\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u5904\u7406\u56fe\u7247\uff1a", None))
        self.recognized_face_label.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u8bc6\u522b\u56fe\u7247\uff1a", None))
        self.run_state_label.setText(QCoreApplication.translate("MainWindow", u"\u505c\u6b62", None))
        self.handled_photo_label.setText("")
        self.all_recognized_photo_label.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u6574\u4f53\u8bc6\u522b\u7387\uff1a", None))
        self.part_recognized_photo_label.setText("")
        self.unhandled_photo_label.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u672a\u5904\u7406\u56fe\u7247\uff1a", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u72b6\u6001\uff1a", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u8bc6\u522b\u4eba\u7269\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.recognition_tab), QCoreApplication.translate("MainWindow", u"\u4eba\u8138\u8bc6\u522b", None))
        self.photo_view.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u5ea6", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u7269\uff1a", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7ea7", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u5730\u70b9", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u89c1\u53f7", None))
        self.all_photo_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u672c\u6b21\u8bc6\u522b\u6240\u6709\u7167\u7247(Alt+Q)", None))
#if QT_CONFIG(shortcut)
        self.all_photo_radioButton.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+Q", None))
#endif // QT_CONFIG(shortcut)
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u53f7", None))
#if QT_CONFIG(tooltip)
        self.selected_dir_radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u663e\u793a\u672c\u6b21\u8bc6\u522b\u6240\u9009\u76ee\u5f55\u4e0b\u7684\u7167\u7247</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.selected_dir_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u672c\u6b21\u8bc6\u522b", None))
#if QT_CONFIG(tooltip)
        self.current_dir_radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u663e\u793a\u5f53\u524d\u5de5\u4f5c\u76ee\u5f55\u4e0b\u7684\u7167\u7247</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.current_dir_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u76ee\u5f55", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u53f7", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u59d3\u540d", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91", None));
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"\u95e8\u7c7b\u4ee3\u7801", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u65f6\u95f4", None))
        self.part_recognition_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u672c\u6b21\u8bc6\u522b\u90e8\u5206\u8bc6\u522b\u7167\u7247(Alt+W)", None))
#if QT_CONFIG(shortcut)
        self.part_recognition_radioButton.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+W", None))
#endif // QT_CONFIG(shortcut)
        self.pre_btn.setText(QCoreApplication.translate("MainWindow", u"\u4e0a\u4e00\u5f20", None))
#if QT_CONFIG(shortcut)
        self.pre_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Left", None))
#endif // QT_CONFIG(shortcut)
        self.photo_index_label.setText("")
        self.next_btn.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u4e00\u5f20", None))
#if QT_CONFIG(shortcut)
        self.next_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Right", None))
#endif // QT_CONFIG(shortcut)
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u683c\u5f0f", None))
        self.verifycheckBox.setText(QCoreApplication.translate("MainWindow", u"\u5df2\u6838\u9a8c(Ctrl+S)", None))
#if QT_CONFIG(shortcut)
        self.verifycheckBox.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"\u6863\u53f7\uff1a", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u8005", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5b97\u53f7", None))
        self.all_recognition_radioButton.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u672c\u6b21\u8bc6\u522b\u5168\u90e8\u8bc6\u522b\u7167\u7247(Alt+E)", None))
#if QT_CONFIG(shortcut)
        self.all_recognition_radioButton.setShortcut(QCoreApplication.translate("MainWindow", u"Alt+E", None))
#endif // QT_CONFIG(shortcut)
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"\u5f20\u53f7", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.photo_tab), QCoreApplication.translate("MainWindow", u"\u5f20\u8457\u5f55", None))
        self.model_acc_label.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8bc6\u522b\u51c6\u786e\u5ea6\uff1a", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#868686;\">\u786e\u8ba4\u662f\u67d0\u67d0\u4eba\u7684\u6982\u7387\u6709\u591a\u5927\uff0c\u6982\u7387\u8d8a\u5927\u8868\u793a\u662f\u67d0\u4eba\u7684\u51e0\u7387\u5c31\u8d8a\u5927\uff0c\u9ed8\u8ba4\u503c\u4e0d\u5c0f\u4e8e90%\u3002</span></p></body></html>", None))
        self.untrained_num_label.setText("")
        self.thresh_lineEdit.setText(QCoreApplication.translate("MainWindow", u"0.9", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u672a\u8bad\u7ec3\u4eba\u8138\u7167\u7247\uff1a", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u7cbe\u5ea6\uff1a", None))
        self.train_btn.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u8bad\u7ec3", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" color:#868686;\">\u5982\u679c\u6a21\u578b\u7cbe\u5ea6\u5c0f\u4e8e0.9\uff0c\u5efa\u8bae\u8fdb\u4e00\u6b65\u5f3a\u5316\u8bad\u7ec3\u3002</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.training_tab), QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u8bad\u7ec3", None))
        self.order_combobox_browse.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5e74\u5ea6", None))
        self.order_combobox_browse.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4fdd\u7ba1\u671f\u9650", None))

        self.label_67.setText(QCoreApplication.translate("MainWindow", u"\u4f18\u5148\u6392\u5e8f\uff1a", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"\u5f20\u6863\u53f7", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u5ea6", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"\u95e8\u7c7b\u4ee3\u7801", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u9898\u540d", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u8005", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u89c1\u53f7", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"\u5f20\u53f7", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5b97\u53f7", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u65f6\u95f4", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7ea7", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u5730\u70b9", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u683c\u5f0f", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"\u90e8\u95e8", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"\u8d23\u4efb\u8005", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u53f7", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u7269\uff1a", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u6863\u53f7", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"\u5927\u5c0f/MB", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"\u5f20\u6570", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u653e\u72b6\u6001", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u7ba1\u671f\u9650", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u8bf4\u660e\uff1a", None))
        self.photo_view_in_arch.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.arch_browser_tab), QCoreApplication.translate("MainWindow", u"\u6863\u6848\u6d4f\u89c8", None))
        self.label_211.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4", None))
        self.start_date_search.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.label_187.setText(QCoreApplication.translate("MainWindow", u"\u9898\u540d", None))
        self.label_210.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u7269", None))
        self.end_date_search.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/dd", None))
        self.search_btn.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        ___qtreewidgetitem = self.group_tree_widget_search.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"\u641c\u7d22\u7ed3\u679c", None));
#if QT_CONFIG(tooltip)
        self.group_tree_widget_search.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u53ef\u52fe\u9009\u5bfc\u51fa</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.group_tree_widget_search.setWhatsThis(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.export_btn_search.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u51fa", None))
        self.label_206.setText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7ea7", None))
        self.label_191.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u5730\u70b9", None))
        self.label_197.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u683c\u5f0f", None))
        self.label_190.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u7ba1\u671f\u9650", None))
        self.label_195.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u5ea6", None))
        self.label_189.setText(QCoreApplication.translate("MainWindow", u"\u5927\u5c0f/MB", None))
        self.label_196.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u8bf4\u660e\uff1a", None))
        self.label_200.setText(QCoreApplication.translate("MainWindow", u"\u8d23\u4efb\u8005", None))
        self.label_208.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u653e\u72b6\u6001", None))
        self.label_198.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u9898\u540d", None))
        self.label_194.setText(QCoreApplication.translate("MainWindow", u"\u5f20\u6570", None))
        self.label_205.setText(QCoreApplication.translate("MainWindow", u"\u5f20\u53f7", None))
        self.label_199.setText(QCoreApplication.translate("MainWindow", u"\u90e8\u95e8", None))
        self.label_192.setText(QCoreApplication.translate("MainWindow", u"\u5f20\u6863\u53f7", None))
        self.label_207.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u8005", None))
        self.label_202.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u65f6\u95f4", None))
        self.label_203.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5b97\u53f7", None))
        self.label_188.setText(QCoreApplication.translate("MainWindow", u"\u4eba\u7269\uff1a", None))
        self.label_193.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u6863\u53f7", None))
        self.label_201.setText(QCoreApplication.translate("MainWindow", u"\u95e8\u7c7b\u4ee3\u7801", None))
        self.label_204.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u53f7", None))
        self.label_209.setText(QCoreApplication.translate("MainWindow", u"\u53c2\u89c1\u53f7", None))
        self.photo_view_search.setText("")
#if QT_CONFIG(tooltip)
        self.photo_list_widget_search.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u53cc\u51fb\u52fe\u9009\u6216\u53d6\u6d88</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.search_archives_tab), QCoreApplication.translate("MainWindow", u"\u6863\u6848\u641c\u7d22", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"\u4f18\u5148\u6392\u5e8f\uff1a", None))
        self.order_combobox_transfer.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5e74\u5ea6", None))
        self.order_combobox_transfer.setItemText(1, QCoreApplication.translate("MainWindow", u"\u4fdd\u7ba1\u671f\u9650", None))

#if QT_CONFIG(tooltip)
        self.arch_tree_view_transfer.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u53cc\u51fb\u9009\u62e9\u6863\u6848</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"\u79fb\u4ea4\u5217\u8868\uff1a", None))
#if QT_CONFIG(tooltip)
        self.selected_arch_list_widget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u53cc\u51fb\u79fb\u9664\u6863\u6848</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"\u9898\u540d", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"\u5206\u76d8\u7ed3\u679c\uff1a", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"\u5149\u76d8\u578b\u53f7", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5b97\u540d\u79f0", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"\u5e74\u5ea6\u8de8\u76d8", None))
        self.across_year_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.across_year_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5426", None))

        self.label_89.setText(QCoreApplication.translate("MainWindow", u"\u8d77\u6b62\u7ec4\u53f7", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"\u76d8\u53f7", None))
        self.across_period_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.across_period_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"\u5426", None))

        self.label_88.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5b97\u53f7", None))
        self.packeage_btn.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5305", None))
        self.cd_size_line_edit.setText(QCoreApplication.translate("MainWindow", u"4.7", None))
        ___qtablewidgetitem3 = self.cd_catalog_table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5b97\u53f7", None));
        ___qtablewidgetitem4 = self.cd_catalog_table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u95e8\u7c7b", None));
        ___qtablewidgetitem5 = self.cd_catalog_table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u53f7", None));
        ___qtablewidgetitem6 = self.cd_catalog_table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u7ec4\u9898\u540d", None));
        ___qtablewidgetitem7 = self.cd_catalog_table_widget.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u65f6\u95f4", None));
        ___qtablewidgetitem8 = self.cd_catalog_table_widget.horizontalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u5730\u70b9", None));
        ___qtablewidgetitem9 = self.cd_catalog_table_widget.horizontalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u62cd\u6444\u8005", None));
        ___qtablewidgetitem10 = self.cd_catalog_table_widget.horizontalHeaderItem(7)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u5f20\u6570", None));
        ___qtablewidgetitem11 = self.cd_catalog_table_widget.horizontalHeaderItem(8)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u683c\u5f0f", None));
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"\u5236\u4f5c\u65f6\u95f4", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"\u671f\u9650\u8de8\u76d8", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u7c7b\u578b", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"\u5355\u76d8\u5927\u5c0f/GB", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"\u5236\u4f5c\u4eba", None))
#if QT_CONFIG(tooltip)
        self.partition_list_widget.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u70b9\u51fb\u67e5\u770b\u5bf9\u5e94\u76d8\u4fe1\u606f</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"\u5149\u76d8\u8bf4\u660e\uff1a", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"\u5149\u76d8\u6807\u7b7e\uff1a", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"\u76d8\u5185\u76ee\u5f55\uff1a", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"\u5f20\u6570", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"\u5149\u76d8\u7c7b\u578b", None))
        self.cd_model_in_transfer.setItemText(0, QCoreApplication.translate("MainWindow", u"CD-R", None))
        self.cd_model_in_transfer.setItemText(1, QCoreApplication.translate("MainWindow", u"DVD", None))

        self.file_type_in_transfer.setItemText(0, QCoreApplication.translate("MainWindow", u"JPEG", None))
        self.file_type_in_transfer.setItemText(1, QCoreApplication.translate("MainWindow", u"TIFF", None))
        self.file_type_in_transfer.setItemText(2, QCoreApplication.translate("MainWindow", u"RAW", None))
        self.file_type_in_transfer.setItemText(3, QCoreApplication.translate("MainWindow", u"DNG", None))

        self.cd_type_in_transfer.setItemText(0, QCoreApplication.translate("MainWindow", u"\u5907\u4efd\u76d8", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.arch_transfer_tab), QCoreApplication.translate("MainWindow", u"\u6863\u6848\u79fb\u4ea4", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5168\u5b97\u4fe1\u606f", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5b97\u53f7", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"\u5168\u5b97\u540d\u79f0", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u8def\u5f84\u8bbe\u7f6e", None))
        self.select_description_dir_btn.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"\u8457\u5f55\u8def\u5f84", None))
        self.select_package_dir_btn.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5305\u8def\u5f84", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"License\u4fe1\u606f", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"\u5269\u4f59\u5929\u6570", None))
#if QT_CONFIG(tooltip)
        self.license_remaining_photo_num.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u8fd8\u53ef\u4ee5\u8bc6\u522b\u7684\u7167\u7247\u5f20\u6570</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.license_enable_export.setText("")
#if QT_CONFIG(tooltip)
        self.label_95.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">\u8fd8\u53ef\u4ee5\u8bc6\u522b\u7684\u7167\u7247\u5f20\u6570</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"\u5269\u4f59\u5f20\u6570", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u542fGPU", None))
        self.license_enable_gpu.setText("")
        self.import_license_btn.setText(QCoreApplication.translate("MainWindow", u"\u5bfc\u5165", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"\u8def\u5f84", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u653e\u5bfc\u51fa", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setting_tab), QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
    # retranslateUi

