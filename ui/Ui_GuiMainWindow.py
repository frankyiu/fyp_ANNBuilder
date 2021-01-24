# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GuiMainWindowlvJTWT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from ui.DraggableLabel import DraggableLabel
from ui.Ui_tutorialsWindow import Ui_tutorialsWindow

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1268, 737)
        MainWindow.setMinimumSize(QSize(1024, 720))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(27, 29, 35, 160);\n"
"	border: 1px solid rgb(40, 40, 40);\n"
"	border-radius: 2px;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"color: rgb(210, 210, 210);")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setFrameShape(QFrame.NoFrame)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_top = QFrame(self.frame_main)
        self.frame_top.setObjectName(u"frame_top")
        self.frame_top.setMinimumSize(QSize(0, 35))
        self.frame_top.setMaximumSize(QSize(16777215, 35))
        self.frame_top.setStyleSheet(u"background-color: transparent;")
        self.frame_top.setFrameShape(QFrame.NoFrame)
        self.frame_top.setFrameShadow(QFrame.Raised)
        self.frame_top.setLineWidth(1)
        self.frame_top.setMidLineWidth(0)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_top)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_toggle = QFrame(self.frame_top)
        self.frame_toggle.setObjectName(u"frame_toggle")
        self.frame_toggle.setMaximumSize(QSize(70, 16777215))
        self.frame_toggle.setStyleSheet(u"background-color: rgb(27, 31, 38);")
        self.frame_toggle.setFrameShape(QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_toggle)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_3.addWidget(self.frame_toggle)

        self.frame_title_bar = QFrame(self.frame_top)
        self.frame_title_bar.setObjectName(u"frame_title_bar")
        self.frame_title_bar.setStyleSheet(u"background: transparent;")
        self.frame_title_bar.setFrameShape(QFrame.NoFrame)
        self.frame_title_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_title_bar)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_top_btns = QFrame(self.frame_title_bar)
        self.frame_top_btns.setObjectName(u"frame_top_btns")
        self.frame_top_btns.setMaximumSize(QSize(16777215, 16777215))
        self.frame_top_btns.setStyleSheet(u"background-color: rgb(35, 36, 40);")
        self.frame_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_top_btns)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_top_btns = QFrame(self.frame_top_btns)
        self.frame_label_top_btns.setObjectName(u"frame_label_top_btns")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy)
        self.frame_label_top_btns.setFrameShape(QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_label_top_btns)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 0, 10, 0)
        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_title_bar_top.setFont(font1)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")
        self.label_title_bar_top.setMargin(10)

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy1)
        self.btn_minimize.setMinimumSize(QSize(35, 0))
        self.btn_minimize.setMaximumSize(QSize(35, 16777215))
        self.btn_minimize.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/16x16/icons/16x16/cil-window-minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy1.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy1)
        self.btn_maximize_restore.setMinimumSize(QSize(35, 0))
        self.btn_maximize_restore.setMaximumSize(QSize(35, 16777215))
        self.btn_maximize_restore.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/16x16/icons/16x16/cil-window-maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy1.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy1)
        self.btn_close.setMinimumSize(QSize(35, 0))
        self.btn_close.setMaximumSize(QSize(35, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:pressed {	\n"
"	background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/16x16/icons/16x16/cil-x.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)


        self.horizontalLayout_3.addWidget(self.frame_title_bar)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy2)
        self.frame_center.setStyleSheet(u"background-color: rgb(40, 44, 52);\n"
"")
        self.frame_center.setFrameShape(QFrame.NoFrame)
        self.frame_center.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_center)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_left_menu = QFrame(self.frame_center)
        self.frame_left_menu.setObjectName(u"frame_left_menu")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy3)
        self.frame_left_menu.setMinimumSize(QSize(60, 0))
        self.frame_left_menu.setMaximumSize(QSize(60, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"QFrame {\n"
"	padding-top: 10px;\n"
"	background-color: rgb(27, 31, 38);\n"
"	box-shadow: 2px 0px 2px red;\n"
"}\n"
"QPushButton {	\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	padding-left: 15px;\n"
"	text-align: left;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton:checked {\n"
"	background-color: rgb(80, 91, 111);\n"
"}\n"
"\n"
"\n"
"")
        self.frame_left_menu.setFrameShape(QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_menu)
        self.verticalLayout_5.setSpacing(1)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_expand = QPushButton(self.frame_left_menu)
        self.btn_expand.setObjectName(u"btn_expand")
        self.btn_expand.setMinimumSize(QSize(0, 40))
        self.btn_expand.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_expand.setStyleSheet(u"padding-left: 18px;\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/basic/icons/basic/next-1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_expand.setIcon(icon3)
        self.btn_expand.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.btn_expand)

        self.btn_home = QPushButton(self.frame_left_menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(60, 60))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        self.btn_home.setFont(font2)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        icon4 = QIcon()
        icon4.addFile(u":/basic/icons/basic/house.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon4)
        self.btn_home.setIconSize(QSize(30, 30))
        self.btn_home.setCheckable(False)
        self.btn_home.setFlat(False)

        self.verticalLayout_5.addWidget(self.btn_home)

        self.btn_tutorial = QPushButton(self.frame_left_menu)
        self.btn_tutorial.setObjectName(u"btn_tutorial")
        self.btn_tutorial.setMinimumSize(QSize(60, 60))
        self.btn_tutorial.setFont(font2)
        self.btn_tutorial.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/basic/icons/basic/book.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_tutorial.setIcon(icon5)
        self.btn_tutorial.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.btn_tutorial)

        self.btn_draw = QPushButton(self.frame_left_menu)
        self.btn_draw.setObjectName(u"btn_draw")
        self.btn_draw.setMinimumSize(QSize(60, 60))
        self.btn_draw.setFont(font2)
        self.btn_draw.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/basic/icons/basic/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_draw.setIcon(icon6)
        self.btn_draw.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.btn_draw)

        self.frame_menus = QFrame(self.frame_left_menu)
        self.frame_menus.setObjectName(u"frame_menus")
        self.frame_menus.setFrameShape(QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QFrame.Raised)
        self.layout_menus = QVBoxLayout(self.frame_menus)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName(u"layout_menus")
        self.layout_menus.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_5.addWidget(self.frame_menus)


        self.horizontalLayout_2.addWidget(self.frame_left_menu)

        self.frame_content_right = QFrame(self.frame_center)
        self.frame_content_right.setObjectName(u"frame_content_right")
        self.frame_content_right.setStyleSheet(u"")
        self.frame_content_right.setFrameShape(QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_content_right)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_content = QFrame(self.frame_content_right)
        self.frame_content.setObjectName(u"frame_content")
        self.frame_content.setAutoFillBackground(False)
        self.frame_content.setStyleSheet(u"")
        self.frame_content.setFrameShape(QFrame.NoFrame)
        self.frame_content.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_content)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(5, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_content)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_6 = QLabel(self.page_home)
        self.label_6.setObjectName(u"label_6")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(40)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_6)

        self.frame_5 = QFrame(self.page_home)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")

        self.horizontalLayout_8.addWidget(self.label)


        self.verticalLayout_10.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.page_home)
        self.page_tutorial = QWidget()
        self.page_tutorial.setObjectName(u"page_tutorial")
        self.verticalLayout_6 = QVBoxLayout(self.page_tutorial)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.page_tutorial)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 40))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(16)
        self.label_2.setFont(font4)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.widget_tutorial = Ui_tutorialsWindow(self.page_tutorial)
        self.widget_tutorial.setObjectName(u"widget_tutorial")

        self.verticalLayout_6.addWidget(self.widget_tutorial)

        self.stackedWidget.addWidget(self.page_tutorial)
        self.page_draw = QWidget()
        self.page_draw.setObjectName(u"page_draw")
        self.page_draw.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.page_draw)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.draw_left = QFrame(self.page_draw)
        self.draw_left.setObjectName(u"draw_left")
        self.draw_left.setMinimumSize(QSize(200, 0))
        self.draw_left.setMaximumSize(QSize(200, 16777215))
        self.draw_left.setStyleSheet(u"\n"
"\n"
"#frame_component{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(35, 36, 40);\n"
"}\n"
"#frame_dataset{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(35, 36, 40);\n"
"}\n"
"#frame_control{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(35, 36, 40);\n"
"}\n"
"")
        self.draw_left.setFrameShape(QFrame.StyledPanel)
        self.draw_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.draw_left)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 10, 0)
        self.frame_dataset = QFrame(self.draw_left)
        self.frame_dataset.setObjectName(u"frame_dataset")
        self.frame_dataset.setMaximumSize(QSize(200, 150))
        self.frame_dataset.setFrameShape(QFrame.StyledPanel)
        self.frame_dataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_dataset)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_dataset = QLabel(self.frame_dataset)
        self.label_dataset.setObjectName(u"label_dataset")
        self.label_dataset.setMaximumSize(QSize(16777215, 30))
        self.label_dataset.setFont(font2)
        self.label_dataset.setStyleSheet(u"background-color: rgb(27, 31, 38);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"")
        self.label_dataset.setMargin(5)

        self.verticalLayout_12.addWidget(self.label_dataset)

        self.frame_dataloader = QFrame(self.frame_dataset)
        self.frame_dataloader.setObjectName(u"frame_dataloader")
        self.frame_dataloader.setFrameShape(QFrame.StyledPanel)
        self.frame_dataloader.setFrameShadow(QFrame.Raised)

        self.verticalLayout_12.addWidget(self.frame_dataloader)


        self.verticalLayout_7.addWidget(self.frame_dataset)

        self.frame_component = QFrame(self.draw_left)
        self.frame_component.setObjectName(u"frame_component")
        self.frame_component.setFrameShape(QFrame.StyledPanel)
        self.frame_component.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_component)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.label_component = QLabel(self.frame_component)
        self.label_component.setObjectName(u"label_component")
        self.label_component.setMaximumSize(QSize(16777215, 30))
        self.label_component.setFont(font2)
        self.label_component.setStyleSheet(u"background-color: rgb(27, 31, 38);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"")
        self.label_component.setMargin(5)

        self.verticalLayout_13.addWidget(self.label_component)

        self.frame_9 = QFrame(self.frame_component)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame_9)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 20, 81, 101))
        self.verticalLayout_17 = QVBoxLayout(self.widget)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_neuron_2 = DraggableLabel(self.widget)
        self.label_neuron_2.setObjectName(u"label_neuron_2")
        self.label_neuron_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_neuron_2.setStyleSheet(u"")
        self.label_neuron_2.setPixmap(QPixmap(u":/basic/icons/basic/004-circle.png"))
        self.label_neuron_2.setScaledContents(True)
        self.label_neuron_2.setAlignment(Qt.AlignCenter)
        self.label_neuron_2.setMargin(5)

        self.verticalLayout_17.addWidget(self.label_neuron_2)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_7)

        self.widget_2 = QWidget(self.frame_9)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 130, 81, 101))
        self.verticalLayout_18 = QVBoxLayout(self.widget_2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_layer = DraggableLabel(self.widget_2)
        self.label_layer.setObjectName(u"label_layer")
        self.label_layer.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_layer.setPixmap(QPixmap(u":/basic/icons/basic/003-layers.png"))
        self.label_layer.setScaledContents(True)
        self.label_layer.setAlignment(Qt.AlignCenter)
        self.label_layer.setMargin(5)

        self.verticalLayout_18.addWidget(self.label_layer)

        self.label_5 = QLabel(self.widget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_5)

        self.widget_3 = QWidget(self.frame_9)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 20, 81, 101))
        self.verticalLayout_19 = QVBoxLayout(self.widget_3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_neuron_3 = DraggableLabel(self.widget_3)
        self.label_neuron_3.setObjectName(u"label_neuron_3")
        self.label_neuron_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_neuron_3.setStyleSheet(u"")
        self.label_neuron_3.setPixmap(QPixmap(u":/basic/icons/basic/004-circle.png"))
        self.label_neuron_3.setScaledContents(True)
        self.label_neuron_3.setAlignment(Qt.AlignCenter)
        self.label_neuron_3.setMargin(5)

        self.verticalLayout_19.addWidget(self.label_neuron_3)

        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_8)

        self.widget_4 = QWidget(self.frame_9)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(80, 130, 81, 101))
        self.verticalLayout_20 = QVBoxLayout(self.widget_4)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_layer_2 = DraggableLabel(self.widget_4)
        self.label_layer_2.setObjectName(u"label_layer_2")
        self.label_layer_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_layer_2.setPixmap(QPixmap(u":/basic/icons/basic/003-layers.png"))
        self.label_layer_2.setScaledContents(True)
        self.label_layer_2.setAlignment(Qt.AlignCenter)
        self.label_layer_2.setMargin(5)

        self.verticalLayout_20.addWidget(self.label_layer_2)

        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_9)

        self.widget_5 = QWidget(self.frame_9)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setGeometry(QRect(0, 240, 81, 101))
        self.verticalLayout_21 = QVBoxLayout(self.widget_5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_layer_3 = DraggableLabel(self.widget_5)
        self.label_layer_3.setObjectName(u"label_layer_3")
        self.label_layer_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_layer_3.setPixmap(QPixmap(u":/basic/icons/basic/003-layers.png"))
        self.label_layer_3.setScaledContents(True)
        self.label_layer_3.setAlignment(Qt.AlignCenter)
        self.label_layer_3.setMargin(5)

        self.verticalLayout_21.addWidget(self.label_layer_3)

        self.label_10 = QLabel(self.widget_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_10)

        self.widget_6 = QWidget(self.frame_9)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setGeometry(QRect(80, 240, 81, 101))
        self.verticalLayout_22 = QVBoxLayout(self.widget_6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_layer_4 = DraggableLabel(self.widget_6)
        self.label_layer_4.setObjectName(u"label_layer_4")
        self.label_layer_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_layer_4.setPixmap(QPixmap(u":/basic/icons/basic/003-layers.png"))
        self.label_layer_4.setScaledContents(True)
        self.label_layer_4.setAlignment(Qt.AlignCenter)
        self.label_layer_4.setMargin(5)

        self.verticalLayout_22.addWidget(self.label_layer_4)

        self.label_11 = QLabel(self.widget_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_11)


        self.verticalLayout_13.addWidget(self.frame_9)


        self.verticalLayout_7.addWidget(self.frame_component)

        self.frame_control = QFrame(self.draw_left)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setMinimumSize(QSize(0, 120))
        self.frame_control.setMaximumSize(QSize(16777215, 120))
        self.frame_control.setFrameShape(QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_control)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.frame_control)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.frame_7)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(64, 64))
        self.pushButton_2.setMaximumSize(QSize(70, 16777215))
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setMouseTracking(False)
        icon7 = QIcon()
        icon7.addFile(u":/basic/icons/basic/001-play-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon7)
        self.pushButton_2.setIconSize(QSize(60, 60))

        self.horizontalLayout_9.addWidget(self.pushButton_2)


        self.verticalLayout_11.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_control)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_3 = QPushButton(self.frame_8)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 20))
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_8)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(0, 20))
        self.pushButton_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_11.addWidget(self.pushButton_4)


        self.verticalLayout_11.addWidget(self.frame_8)


        self.verticalLayout_7.addWidget(self.frame_control)


        self.horizontalLayout_6.addWidget(self.draw_left)

        self.draw_main = QFrame(self.page_draw)
        self.draw_main.setObjectName(u"draw_main")
        self.draw_main.setFrameShape(QFrame.StyledPanel)
        self.draw_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.draw_main)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(4, 0, 4, -1)
        self.frame_2 = QFrame(self.draw_main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 30))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setAutoFillBackground(False)
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.frame_3)

        self.btn_guide = QPushButton(self.frame_2)
        self.btn_guide.setObjectName(u"btn_guide")
        self.btn_guide.setMaximumSize(QSize(24, 16777215))
        self.btn_guide.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_7.addWidget(self.btn_guide)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.graphicsView = QGraphicsView(self.draw_main)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setStyleSheet(u"\n"
"border: 2px solid;\n"
"border-radius: 10px;\n"
"border-color: rgba(84, 84, 84, 200);\n"
"")

        self.verticalLayout_8.addWidget(self.graphicsView)

        self.tabWidget = QTabWidget(self.draw_main)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(16777215, 120))
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(u"background-color: 0;")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_8.addWidget(self.tabWidget)


        self.horizontalLayout_6.addWidget(self.draw_main)

        self.draw_right = QFrame(self.page_draw)
        self.draw_right.setObjectName(u"draw_right")
        self.draw_right.setMinimumSize(QSize(200, 0))
        self.draw_right.setMaximumSize(QSize(0, 16777215))
        self.draw_right.setFrameShape(QFrame.StyledPanel)
        self.draw_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.draw_right)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, -1, 9)
        self.btn_viewer = QPushButton(self.draw_right)
        self.btn_viewer.setObjectName(u"btn_viewer")
        self.btn_viewer.setMinimumSize(QSize(20, 100))
        self.btn_viewer.setMaximumSize(QSize(20, 16777215))
        self.btn_viewer.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_viewer.setStyleSheet(u"background-color: rgb(27, 31, 38);\n"
"border: none;\n"
"\n"
"")
        self.btn_viewer.setIcon(icon3)

        self.horizontalLayout_12.addWidget(self.btn_viewer)

        self.tab_viewer = QTabWidget(self.draw_right)
        self.tab_viewer.setObjectName(u"tab_viewer")
        self.tab_viewer.setEnabled(True)
        self.tab_viewer.setMaximumSize(QSize(16777215, 16777215))
        self.tab_viewer.setAutoFillBackground(False)
        self.tab_viewer.setStyleSheet(u"background-color: 0;")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tab_viewer.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tab_viewer.addTab(self.tab_4, "")

        self.horizontalLayout_12.addWidget(self.tab_viewer)


        self.horizontalLayout_6.addWidget(self.draw_right)

        self.stackedWidget.addWidget(self.page_draw)

        self.verticalLayout_9.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_content)


        self.horizontalLayout_2.addWidget(self.frame_content_right)


        self.verticalLayout.addWidget(self.frame_center)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        QWidget.setTabOrder(self.btn_maximize_restore, self.btn_close)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        self.tab_viewer.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_title_bar_top.setText(QCoreApplication.translate("MainWindow", u"ANN Builder ", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize_restore.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize_restore.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.btn_expand.setText("")
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"     Home", None))
        self.btn_tutorial.setText(QCoreApplication.translate("MainWindow", u"     Tutorial", None))
        self.btn_draw.setText(QCoreApplication.translate("MainWindow", u"     Builder", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Welcome to ANN Builder", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tutorial", None))
        self.label_dataset.setText(QCoreApplication.translate("MainWindow", u"Dataset", None))
        self.label_component.setText(QCoreApplication.translate("MainWindow", u"Component", None))
        self.label_neuron_2.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"2D-Neuron", None))
        self.label_layer.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Layer", None))
        self.label_neuron_3.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Neuron", None))
        self.label_layer_2.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"2D-Layer", None))
        self.label_layer_3.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Regularizer", None))
        self.label_layer_4.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Cost Func", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Feed-Forwrd", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Back-Pop", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Building Panel", None))
        self.btn_guide.setText(QCoreApplication.translate("MainWindow", u"?", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.btn_viewer.setText("")
        self.tab_viewer.setTabText(self.tab_viewer.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tab_viewer.setTabText(self.tab_viewer.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Tab 2", None))
    # retranslateUi

