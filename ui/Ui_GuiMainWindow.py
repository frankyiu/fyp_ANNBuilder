# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GuiMainWindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from .Ui_tutorialsWindow import Ui_tutorialsWindow
from .DraggableLabel import NNB1DNeuronIcon
from .DraggableLabel import NNB1DBiasNeuronIcon
from .DraggableLabel import NNB2DNeuronIcon
from .DraggableLabel import NNB2DBiasNeuronIcon
from .DraggableLabel import NNBAffineLayerIcon
from .DraggableLabel import NNBConvLayerIcon
from .DraggableLabel import NNBLostFuncBlock
from .DraggableLabel import NNBRegularizerIcon
from .DraggableLabel import NNBStacked1DAffLayerIcon
from .DraggableLabel import NNBPoolingLayerIcon
from .DraggableLabel import NNBFlattenLayerIcon
from .ResultDashBoard import ScrollableResultDashBoard

import files_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.resize(1300, 740)
        MainWindow.setMinimumSize(QSize(1300, 740))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/basic/icons/basic/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        self.centralwidget.setFont(font1)
        self.centralwidget.setStyleSheet(u"color: rgb(210, 210, 210);\n"
"background:transparent;\n"
"font-family:Segoe UI;\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        self.frame_main.setCursor(QCursor(Qt.ArrowCursor))
        self.frame_main.setStyleSheet(u"QToolTip { color: #fff; background-color: #000; border: none; }\n"
"\n"
"QScrollBar:horizontal\n"
"{\n"
"    border: 1px solid #222222;\n"
"    background-color: #3d3d3d;\n"
"    height: 15px;\n"
"    margin: 0px 16px 0px 16px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(150, 150, 150, 255),stop:1 rgba(107, 107, 107, 255));\n"
"	border-radius: 6px;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:horizontal\n"
"{\n"
"    background-color: #3d3d3d;\n"
"    width: 17px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::sub-line:horizontal\n"
"{\n"
"    border: 1px solid #3d3d3d;\n"
"    background-color: #3d3d3d;\n"
"    width: 17px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::right-arrow:horizontal\n"
"{\n"
"    image: url(\":/basic/icons/basic/right-arrow.png\""
                        ");\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::left-arrow:horizontal\n"
"{\n"
"    image: url(\":/basic/icons/basic/left-arrow.png\");\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"    background: none;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"    background-color: #3d3d3d;\n"
"    width: 15px;\n"
"    border: 1px solid #222222;\n"
"    margin: 16px 0px 16px 0px;\n"
"}\n"
"\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"    background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(150, 150, 150, 255),stop:1 rgba(107, 107, 107, 255));\n"
"	border-radius: 3px;\n"
"    min-height: 20px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"    border: 1px solid #3d3d3d;\n"
"    background-color: #3d3d3d;\n"
"    height: 15px;\n"
"    subcontrol-position: bottom;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::su"
                        "b-line:vertical\n"
"{\n"
"    border: 1px solid #3d3d3d;\n"
"    background-color: #3d3d3d;\n"
"    height: 15px;\n"
"    subcontrol-position: top;\n"
"    subcontrol-origin: margin;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::up-arrow:vertical\n"
"{\n"
"    image: url(\":/basic/icons/basic/up-arrow.png\");\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::down-arrow:vertical\n"
"{\n"
"    image: url(\":/basic/icons/basic/down-arrow.png\");\n"
"    width: 6px;\n"
"    height: 6px;\n"
"\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"    background: none;\n"
"\n"
"}")
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
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
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
        self.label_logo = QLabel(self.frame_label_top_btns)
        self.label_logo.setObjectName(u"label_logo")
        sizePolicy.setHeightForWidth(self.label_logo.sizePolicy().hasHeightForWidth())
        self.label_logo.setSizePolicy(sizePolicy)
        self.label_logo.setMaximumSize(QSize(24, 24))
        self.label_logo.setPixmap(QPixmap(u":/basic/icons/basic/logo.png"))
        self.label_logo.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.label_logo)

        self.label_title_bar_top = QLabel(self.frame_label_top_btns)
        self.label_title_bar_top.setObjectName(u"label_title_bar_top")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_title_bar_top.sizePolicy().hasHeightForWidth())
        self.label_title_bar_top.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(10)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_title_bar_top.setFont(font2)
        self.label_title_bar_top.setStyleSheet(u"background: transparent;\n"
"")
        self.label_title_bar_top.setMargin(10)

        self.horizontalLayout_10.addWidget(self.label_title_bar_top)


        self.horizontalLayout_4.addWidget(self.frame_label_top_btns)

        self.frame_btns_right = QFrame(self.frame_top_btns)
        self.frame_btns_right.setObjectName(u"frame_btns_right")
        sizePolicy1.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy1)
        self.frame_btns_right.setMaximumSize(QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_btns_right)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.btn_minimize = QPushButton(self.frame_btns_right)
        self.btn_minimize.setObjectName(u"btn_minimize")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy2)
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
        icon1 = QIcon()
        icon1.addFile(u":/basic/icons/basic/minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_minimize.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.btn_minimize)

        self.btn_maximize_restore = QPushButton(self.frame_btns_right)
        self.btn_maximize_restore.setObjectName(u"btn_maximize_restore")
        sizePolicy2.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        self.btn_maximize_restore.setSizePolicy(sizePolicy2)
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
        icon2 = QIcon()
        icon2.addFile(u":/basic/icons/basic/maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_maximize_restore.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.btn_maximize_restore)

        self.btn_close = QPushButton(self.frame_btns_right)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
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
        icon3 = QIcon()
        icon3.addFile(u":/basic/icons/basic/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.btn_close)


        self.horizontalLayout_4.addWidget(self.frame_btns_right, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frame_top_btns)


        self.horizontalLayout_3.addWidget(self.frame_title_bar)


        self.verticalLayout.addWidget(self.frame_top)

        self.frame_center = QFrame(self.frame_main)
        self.frame_center.setObjectName(u"frame_center")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy3)
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
        sizePolicy.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy)
        self.frame_left_menu.setMinimumSize(QSize(60, 0))
        self.frame_left_menu.setMaximumSize(QSize(60, 16777215))
        self.frame_left_menu.setLayoutDirection(Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet(u"QFrame {\n"
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
        self.btn_expand.setStyleSheet(u"padding-left: 19px;\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/basic/icons/basic/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_expand.setIcon(icon4)
        self.btn_expand.setIconSize(QSize(22, 22))

        self.verticalLayout_5.addWidget(self.btn_expand)

        self.btn_home = QPushButton(self.frame_left_menu)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(60, 60))
        self.btn_home.setFont(font1)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u":/basic/icons/basic/house.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon5)
        self.btn_home.setIconSize(QSize(30, 30))
        self.btn_home.setCheckable(False)
        self.btn_home.setFlat(False)

        self.verticalLayout_5.addWidget(self.btn_home)

        self.btn_tutorial = QPushButton(self.frame_left_menu)
        self.btn_tutorial.setObjectName(u"btn_tutorial")
        self.btn_tutorial.setMinimumSize(QSize(60, 60))
        self.btn_tutorial.setFont(font1)
        self.btn_tutorial.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/basic/icons/basic/book.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_tutorial.setIcon(icon6)
        self.btn_tutorial.setIconSize(QSize(30, 30))

        self.verticalLayout_5.addWidget(self.btn_tutorial)

        self.btn_draw = QPushButton(self.frame_left_menu)
        self.btn_draw.setObjectName(u"btn_draw")
        self.btn_draw.setMinimumSize(QSize(60, 60))
        self.btn_draw.setFont(font1)
        self.btn_draw.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/basic/icons/basic/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_draw.setIcon(icon7)
        self.btn_draw.setIconSize(QSize(30, 43))

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
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.page_home.sizePolicy().hasHeightForWidth())
        self.page_home.setSizePolicy(sizePolicy4)
        self.verticalLayout_10 = QVBoxLayout(self.page_home)
        self.verticalLayout_10.setSpacing(20)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(50, 50, 50, 50)
        self.frame_20 = QFrame(self.page_home)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy4.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy4)
        self.frame_20.setStyleSheet(u"#frame_20{\n"
"border-bottom: 2px solid;\n"
"border-color: #3d3d3d;\n"
"}")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.label_24 = QLabel(self.frame_20)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setMinimumSize(QSize(100, 100))
        self.label_24.setMaximumSize(QSize(100, 100))
        self.label_24.setPixmap(QPixmap(u":/basic/icons/basic/logo.png"))
        self.label_24.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.label_24)

        self.label_6 = QLabel(self.frame_20)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 120))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(40)
        self.label_6.setFont(font3)
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.label_6.setWordWrap(False)

        self.horizontalLayout_21.addWidget(self.label_6)


        self.verticalLayout_10.addWidget(self.frame_20)

        self.frame_5 = QFrame(self.page_home)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 0))
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_14 = QFrame(self.frame_5)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy4.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy4)
        self.frame_14.setMaximumSize(QSize(350, 16777215))
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_14)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.btn_gotoTutorial = QToolButton(self.frame_14)
        self.btn_gotoTutorial.setObjectName(u"btn_gotoTutorial")
        sizePolicy.setHeightForWidth(self.btn_gotoTutorial.sizePolicy().hasHeightForWidth())
        self.btn_gotoTutorial.setSizePolicy(sizePolicy)
        self.btn_gotoTutorial.setMaximumSize(QSize(400, 16777215))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(15)
        self.btn_gotoTutorial.setFont(font4)
        self.btn_gotoTutorial.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gotoTutorial.setLayoutDirection(Qt.LeftToRight)
        self.btn_gotoTutorial.setStyleSheet(u"color: rgb(235, 186, 22);")
        self.btn_gotoTutorial.setIcon(icon6)
        self.btn_gotoTutorial.setIconSize(QSize(100, 100))
        self.btn_gotoTutorial.setAutoRepeat(False)
        self.btn_gotoTutorial.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_17.addWidget(self.btn_gotoTutorial, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.label_5 = QLabel(self.frame_14)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 0))
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_5.setWordWrap(True)

        self.verticalLayout_17.addWidget(self.label_5, 0, Qt.AlignHCenter|Qt.AlignTop)

        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setMinimumSize(QSize(0, 205))
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_16)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_8 = QLabel(self.frame_16)
        self.label_8.setObjectName(u"label_8")
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setMaximumSize(QSize(16777215, 39))
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"background-color: #3d3d3d;")
        self.label_8.setMargin(10)

        self.verticalLayout_19.addWidget(self.label_8, 0, Qt.AlignVCenter)

        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_17)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.btn_gotoBasicCon = QPushButton(self.frame_17)
        self.btn_gotoBasicCon.setObjectName(u"btn_gotoBasicCon")
        self.btn_gotoBasicCon.setFont(font)
        self.btn_gotoBasicCon.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_29.addWidget(self.btn_gotoBasicCon, 0, Qt.AlignLeft)

        self.btn_gotoMLP = QPushButton(self.frame_17)
        self.btn_gotoMLP.setObjectName(u"btn_gotoMLP")
        self.btn_gotoMLP.setFont(font)
        self.btn_gotoMLP.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_29.addWidget(self.btn_gotoMLP, 0, Qt.AlignLeft)

        self.btn_gotoCNN = QPushButton(self.frame_17)
        self.btn_gotoCNN.setObjectName(u"btn_gotoCNN")
        self.btn_gotoCNN.setFont(font)
        self.btn_gotoCNN.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_29.addWidget(self.btn_gotoCNN)


        self.verticalLayout_19.addWidget(self.frame_17, 0, Qt.AlignLeft)


        self.verticalLayout_17.addWidget(self.frame_16)


        self.horizontalLayout_8.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.frame_5)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy4.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy4)
        self.frame_15.setMaximumSize(QSize(350, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_15)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.btn_gotoBuilder = QToolButton(self.frame_15)
        self.btn_gotoBuilder.setObjectName(u"btn_gotoBuilder")
        sizePolicy.setHeightForWidth(self.btn_gotoBuilder.sizePolicy().hasHeightForWidth())
        self.btn_gotoBuilder.setSizePolicy(sizePolicy)
        self.btn_gotoBuilder.setMaximumSize(QSize(400, 16777215))
        self.btn_gotoBuilder.setFont(font4)
        self.btn_gotoBuilder.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_gotoBuilder.setStyleSheet(u"color: rgb(235, 186, 22);")
        self.btn_gotoBuilder.setIcon(icon7)
        self.btn_gotoBuilder.setIconSize(QSize(100, 100))
        self.btn_gotoBuilder.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.verticalLayout_18.addWidget(self.btn_gotoBuilder)

        self.label_7 = QLabel(self.frame_15)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 0))
        self.label_7.setFont(font)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)

        self.verticalLayout_18.addWidget(self.label_7)

        self.frame_18 = QFrame(self.frame_15)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMinimumSize(QSize(0, 205))
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_18)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")

        self.verticalLayout_18.addWidget(self.frame_18)


        self.horizontalLayout_8.addWidget(self.frame_15)


        self.verticalLayout_10.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.page_home)
        self.page_tutorial = QWidget()
        self.page_tutorial.setObjectName(u"page_tutorial")
        self.verticalLayout_6 = QVBoxLayout(self.page_tutorial)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.page_tutorial)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 40))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(16)
        self.label_2.setFont(font5)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_2)

        self.widget_tutorial = Ui_tutorialsWindow(self.page_tutorial)
        self.widget_tutorial.setObjectName(u"widget_tutorial")
        self.widget_tutorial.setFont(font1)

        self.verticalLayout_6.addWidget(self.widget_tutorial)

        self.stackedWidget.addWidget(self.page_tutorial)
        self.page_draw = QWidget()
        self.page_draw.setObjectName(u"page_draw")
        self.horizontalLayout_6 = QHBoxLayout(self.page_draw)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.draw_left = QFrame(self.page_draw)
        self.draw_left.setObjectName(u"draw_left")
        self.draw_left.setMinimumSize(QSize(200, 0))
        self.draw_left.setMaximumSize(QSize(200, 16777215))
        self.draw_left.setStyleSheet(u"\n"
"#frame_component{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(35, 36, 40);\n"
"}\n"
"#frame_dataset{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(35, 36, 40);\n"
"}\n"
"\n"
"")
        self.draw_left.setFrameShape(QFrame.StyledPanel)
        self.draw_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.draw_left)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 10, 0)
        self.frame_dataset = QFrame(self.draw_left)
        self.frame_dataset.setObjectName(u"frame_dataset")
        sizePolicy4.setHeightForWidth(self.frame_dataset.sizePolicy().hasHeightForWidth())
        self.frame_dataset.setSizePolicy(sizePolicy4)
        self.frame_dataset.setMaximumSize(QSize(16777215, 16777215))
        self.frame_dataset.setFrameShape(QFrame.StyledPanel)
        self.frame_dataset.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_dataset)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_dataset = QLabel(self.frame_dataset)
        self.label_dataset.setObjectName(u"label_dataset")
        self.label_dataset.setMaximumSize(QSize(16777215, 30))
        self.label_dataset.setFont(font1)
        self.label_dataset.setStyleSheet(u"background-color: rgb(27, 31, 38);\n"
"border-top-left-radius: 10px;\n"
"border-top-right-radius: 10px;\n"
"")
        self.label_dataset.setMargin(5)

        self.verticalLayout_12.addWidget(self.label_dataset)

        self.frame_dataloader = QFrame(self.frame_dataset)
        self.frame_dataloader.setObjectName(u"frame_dataloader")
        self.frame_dataloader.setMinimumSize(QSize(0, 150))
        self.frame_dataloader.setMaximumSize(QSize(16777215, 16777215))
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
        self.label_component.setFont(font1)
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
        self.verticalLayout_14 = QVBoxLayout(self.frame_9)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.frame_9)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea{\n"
"border:None;\n"
"}\n"
"\n"
"QScrollBar:vertical{\n"
"border:None;\n"
"}\n"
"\n"
"")
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 169, 718))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(169, 16777215))
        self.horizontalLayout_12 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.widget_7 = QWidget(self.scrollAreaWidgetContents)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setMinimumSize(QSize(0, 700))
        self.label_14 = QLabel(self.widget_7)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 9, 41, 16))
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setFont(font1)
        self.widget = QWidget(self.widget_7)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-5, 30, 161, 199))
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy5)
        self.widget.setStyleSheet(u"color: rgb(235, 186, 22);")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_20 = QVBoxLayout(self.widget_4)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(4, 4, 4, 4)
        self.neuron_2D = NNB2DNeuronIcon(self.widget_4)
        self.neuron_2D.setObjectName(u"neuron_2D")
        self.neuron_2D.setCursor(QCursor(Qt.PointingHandCursor))
        self.neuron_2D.setStyleSheet(u"")
        self.neuron_2D.setPixmap(QPixmap(u":/component/icons/component/2D_Neuron.png"))
        self.neuron_2D.setScaledContents(True)
        self.neuron_2D.setAlignment(Qt.AlignCenter)
        self.neuron_2D.setMargin(7)

        self.verticalLayout_20.addWidget(self.neuron_2D)

        self.label_9 = QLabel(self.widget_4)
        self.label_9.setObjectName(u"label_9")
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(8)
        self.label_9.setFont(font6)
        self.label_9.setTextFormat(Qt.AutoText)
        self.label_9.setAlignment(Qt.AlignCenter)
        self.label_9.setWordWrap(False)

        self.verticalLayout_20.addWidget(self.label_9)


        self.gridLayout_2.addWidget(self.widget_4, 1, 0, 1, 1)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_21 = QVBoxLayout(self.widget_5)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(4, 4, 4, 4)
        self.neuron_bias_1D = NNB1DBiasNeuronIcon(self.widget_5)
        self.neuron_bias_1D.setObjectName(u"neuron_bias_1D")
        self.neuron_bias_1D.setCursor(QCursor(Qt.PointingHandCursor))
        self.neuron_bias_1D.setStyleSheet(u"")
        self.neuron_bias_1D.setPixmap(QPixmap(u":/component/icons/component/1D_Bias.png"))
        self.neuron_bias_1D.setScaledContents(True)
        self.neuron_bias_1D.setAlignment(Qt.AlignCenter)
        self.neuron_bias_1D.setMargin(7)

        self.verticalLayout_21.addWidget(self.neuron_bias_1D)

        self.label_10 = QLabel(self.widget_5)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font6)
        self.label_10.setTextFormat(Qt.AutoText)
        self.label_10.setAlignment(Qt.AlignCenter)
        self.label_10.setWordWrap(False)

        self.verticalLayout_21.addWidget(self.label_10)


        self.gridLayout_2.addWidget(self.widget_5, 0, 1, 1, 1)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_22 = QVBoxLayout(self.widget_6)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(4, 4, 4, 4)
        self.neuron_1D = NNB1DNeuronIcon(self.widget_6)
        self.neuron_1D.setObjectName(u"neuron_1D")
        self.neuron_1D.setCursor(QCursor(Qt.PointingHandCursor))
        self.neuron_1D.setStyleSheet(u"")
        self.neuron_1D.setPixmap(QPixmap(u":/component/icons/component/1D_Neuron.png"))
        self.neuron_1D.setScaledContents(True)
        self.neuron_1D.setAlignment(Qt.AlignCenter)
        self.neuron_1D.setMargin(7)

        self.verticalLayout_22.addWidget(self.neuron_1D)

        self.label_11 = QLabel(self.widget_6)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font6)
        self.label_11.setTextFormat(Qt.AutoText)
        self.label_11.setAlignment(Qt.AlignCenter)
        self.label_11.setWordWrap(False)

        self.verticalLayout_22.addWidget(self.label_11)


        self.gridLayout_2.addWidget(self.widget_6, 0, 0, 1, 1)

        self.widget_8 = QWidget(self.widget)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_23 = QVBoxLayout(self.widget_8)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(4, 4, 4, 4)
        self.neuron_bias_2D = NNB2DBiasNeuronIcon(self.widget_8)
        self.neuron_bias_2D.setObjectName(u"neuron_bias_2D")
        self.neuron_bias_2D.setCursor(QCursor(Qt.PointingHandCursor))
        self.neuron_bias_2D.setStyleSheet(u"")
        self.neuron_bias_2D.setPixmap(QPixmap(u":/component/icons/component/1D_Bias.png"))
        self.neuron_bias_2D.setScaledContents(True)
        self.neuron_bias_2D.setAlignment(Qt.AlignCenter)
        self.neuron_bias_2D.setMargin(7)

        self.verticalLayout_23.addWidget(self.neuron_bias_2D)

        self.label_15 = QLabel(self.widget_8)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font6)
        self.label_15.setTextFormat(Qt.AutoText)
        self.label_15.setAlignment(Qt.AlignCenter)
        self.label_15.setWordWrap(False)

        self.verticalLayout_23.addWidget(self.label_15)


        self.gridLayout_2.addWidget(self.widget_8, 1, 1, 1, 1)

        self.label_20 = QLabel(self.widget_7)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(0, 238, 35, 16))
        sizePolicy.setHeightForWidth(self.label_20.sizePolicy().hasHeightForWidth())
        self.label_20.setSizePolicy(sizePolicy)
        self.label_20.setFont(font1)
        self.widget_2 = QWidget(self.widget_7)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(-5, 259, 161, 291))
        sizePolicy5.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy5)
        self.widget_2.setStyleSheet(u"color: rgb(235, 186, 22);")
        self.gridLayout_3 = QGridLayout(self.widget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widget_9 = QWidget(self.widget_2)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_24 = QVBoxLayout(self.widget_9)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(4, 4, 4, 4)
        self.conv_layer = NNBConvLayerIcon(self.widget_9)
        self.conv_layer.setObjectName(u"conv_layer")
        self.conv_layer.setCursor(QCursor(Qt.PointingHandCursor))
        self.conv_layer.setStyleSheet(u"")
        self.conv_layer.setPixmap(QPixmap(u":/component/icons/component/Conv_Layer.png"))
        self.conv_layer.setScaledContents(True)
        self.conv_layer.setAlignment(Qt.AlignCenter)
        self.conv_layer.setMargin(0)

        self.verticalLayout_24.addWidget(self.conv_layer)

        self.label_16 = QLabel(self.widget_9)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font6)
        self.label_16.setTextFormat(Qt.AutoText)
        self.label_16.setAlignment(Qt.AlignCenter)
        self.label_16.setWordWrap(False)

        self.verticalLayout_24.addWidget(self.label_16)


        self.gridLayout_3.addWidget(self.widget_9, 1, 0, 1, 1)

        self.widget_10 = QWidget(self.widget_2)
        self.widget_10.setObjectName(u"widget_10")
        self.verticalLayout_25 = QVBoxLayout(self.widget_10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(4, 4, 4, 4)
        self.stacked_affine_layer = NNBStacked1DAffLayerIcon(self.widget_10)
        self.stacked_affine_layer.setObjectName(u"stacked_affine_layer")
        self.stacked_affine_layer.setCursor(QCursor(Qt.PointingHandCursor))
        self.stacked_affine_layer.setStyleSheet(u"")
        self.stacked_affine_layer.setPixmap(QPixmap(u":/component/icons/component/StackAffine_Layer.png"))
        self.stacked_affine_layer.setScaledContents(True)
        self.stacked_affine_layer.setAlignment(Qt.AlignCenter)
        self.stacked_affine_layer.setMargin(0)

        self.verticalLayout_25.addWidget(self.stacked_affine_layer)

        self.label_17 = QLabel(self.widget_10)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font6)
        self.label_17.setTextFormat(Qt.AutoText)
        self.label_17.setAlignment(Qt.AlignCenter)
        self.label_17.setWordWrap(False)

        self.verticalLayout_25.addWidget(self.label_17)


        self.gridLayout_3.addWidget(self.widget_10, 0, 1, 1, 1)

        self.widget_12 = QWidget(self.widget_2)
        self.widget_12.setObjectName(u"widget_12")
        self.verticalLayout_27 = QVBoxLayout(self.widget_12)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(4, 4, 4, 4)
        self.pooling_layer = NNBPoolingLayerIcon(self.widget_12)
        self.pooling_layer.setObjectName(u"pooling_layer")
        self.pooling_layer.setCursor(QCursor(Qt.PointingHandCursor))
        self.pooling_layer.setStyleSheet(u"")
        self.pooling_layer.setPixmap(QPixmap(u":/component/icons/component/Pooling_Layer.png"))
        self.pooling_layer.setScaledContents(True)
        self.pooling_layer.setAlignment(Qt.AlignCenter)
        self.pooling_layer.setMargin(0)

        self.verticalLayout_27.addWidget(self.pooling_layer)

        self.label_19 = QLabel(self.widget_12)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font6)
        self.label_19.setTextFormat(Qt.AutoText)
        self.label_19.setAlignment(Qt.AlignCenter)
        self.label_19.setWordWrap(False)

        self.verticalLayout_27.addWidget(self.label_19)


        self.gridLayout_3.addWidget(self.widget_12, 1, 1, 1, 1)

        self.widget_11 = QWidget(self.widget_2)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_26 = QVBoxLayout(self.widget_11)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(4, 4, 4, 4)
        self.affine_layer = NNBAffineLayerIcon(self.widget_11)
        self.affine_layer.setObjectName(u"affine_layer")
        self.affine_layer.setCursor(QCursor(Qt.PointingHandCursor))
        self.affine_layer.setStyleSheet(u"")
        self.affine_layer.setPixmap(QPixmap(u":/component/icons/component/Affine_Layer.png"))
        self.affine_layer.setScaledContents(True)
        self.affine_layer.setAlignment(Qt.AlignCenter)
        self.affine_layer.setMargin(0)

        self.verticalLayout_26.addWidget(self.affine_layer)

        self.label_18 = QLabel(self.widget_11)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font6)
        self.label_18.setTextFormat(Qt.AutoText)
        self.label_18.setAlignment(Qt.AlignCenter)
        self.label_18.setWordWrap(False)

        self.verticalLayout_26.addWidget(self.label_18)


        self.gridLayout_3.addWidget(self.widget_11, 0, 0, 1, 1)

        self.widget_13 = QWidget(self.widget_2)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_28 = QVBoxLayout(self.widget_13)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(4, 4, 4, 4)
        self.flatten_layer = NNBFlattenLayerIcon(self.widget_13)
        self.flatten_layer.setObjectName(u"flatten_layer")
        self.flatten_layer.setCursor(QCursor(Qt.PointingHandCursor))
        self.flatten_layer.setStyleSheet(u"")
        self.flatten_layer.setPixmap(QPixmap(u":/component/icons/component/Flatten_Layer.png"))
        self.flatten_layer.setScaledContents(True)
        self.flatten_layer.setAlignment(Qt.AlignCenter)
        self.flatten_layer.setMargin(0)

        self.verticalLayout_28.addWidget(self.flatten_layer)

        self.label_21 = QLabel(self.widget_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font6)
        self.label_21.setTextFormat(Qt.AutoText)
        self.label_21.setAlignment(Qt.AlignCenter)
        self.label_21.setWordWrap(False)

        self.verticalLayout_28.addWidget(self.label_21)


        self.gridLayout_3.addWidget(self.widget_13, 2, 0, 1, 1)

        self.label_22 = QLabel(self.widget_7)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(0, 559, 61, 16))
        sizePolicy.setHeightForWidth(self.label_22.sizePolicy().hasHeightForWidth())
        self.label_22.setSizePolicy(sizePolicy)
        self.label_22.setFont(font1)
        self.widget_3 = QWidget(self.widget_7)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(-5, 580, 161, 106))
        sizePolicy5.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy5)
        self.widget_3.setStyleSheet(u"color: rgb(235, 186, 22);")
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.widget_16 = QWidget(self.widget_3)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_31 = QVBoxLayout(self.widget_16)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(4, 4, 4, 4)
        self.loss_func_block = NNBLostFuncBlock(self.widget_16)
        self.loss_func_block.setObjectName(u"loss_func_block")
        self.loss_func_block.setCursor(QCursor(Qt.PointingHandCursor))
        self.loss_func_block.setStyleSheet(u"")
        self.loss_func_block.setPixmap(QPixmap(u":/component/icons/component/LossFuction.png"))
        self.loss_func_block.setScaledContents(True)
        self.loss_func_block.setAlignment(Qt.AlignCenter)
        self.loss_func_block.setMargin(7)

        self.verticalLayout_31.addWidget(self.loss_func_block)

        self.label_25 = QLabel(self.widget_16)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font6)
        self.label_25.setTextFormat(Qt.AutoText)
        self.label_25.setAlignment(Qt.AlignCenter)
        self.label_25.setWordWrap(False)

        self.verticalLayout_31.addWidget(self.label_25)


        self.gridLayout_4.addWidget(self.widget_16, 0, 1, 1, 1)

        self.widget_18 = QWidget(self.widget_3)
        self.widget_18.setObjectName(u"widget_18")
        self.verticalLayout_33 = QVBoxLayout(self.widget_18)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(4, 4, 4, 4)
        self.regularizer = NNBRegularizerIcon(self.widget_18)
        self.regularizer.setObjectName(u"regularizer")
        self.regularizer.setCursor(QCursor(Qt.PointingHandCursor))
        self.regularizer.setStyleSheet(u"")
        self.regularizer.setPixmap(QPixmap(u":/component/icons/component/Regularizer.png"))
        self.regularizer.setScaledContents(True)
        self.regularizer.setAlignment(Qt.AlignCenter)
        self.regularizer.setMargin(7)

        self.verticalLayout_33.addWidget(self.regularizer)

        self.label_27 = QLabel(self.widget_18)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font6)
        self.label_27.setTextFormat(Qt.AutoText)
        self.label_27.setAlignment(Qt.AlignCenter)
        self.label_27.setWordWrap(False)

        self.verticalLayout_33.addWidget(self.label_27)


        self.gridLayout_4.addWidget(self.widget_18, 0, 0, 1, 1)


        self.horizontalLayout_12.addWidget(self.widget_7)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_14.addWidget(self.scrollArea)


        self.verticalLayout_13.addWidget(self.frame_9)


        self.verticalLayout_7.addWidget(self.frame_component)


        self.horizontalLayout_6.addWidget(self.draw_left)

        self.draw_main = QFrame(self.page_draw)
        self.draw_main.setObjectName(u"draw_main")
        self.draw_main.setFrameShape(QFrame.StyledPanel)
        self.draw_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.draw_main)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(4, 0, 4, 0)
        self.draw_content = QWidget(self.draw_main)
        self.draw_content.setObjectName(u"draw_content")
        self.horizontalLayout_13 = QHBoxLayout(self.draw_content)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, 0)
        self.draw_build = QWidget(self.draw_content)
        self.draw_build.setObjectName(u"draw_build")
        self.verticalLayout_16 = QVBoxLayout(self.draw_build)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.draw_build)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 30))
        self.frame_2.setMaximumSize(QSize(16777215, 30))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 0, 5, 0)
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        sizePolicy1.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy1)
        self.label_3.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.btn_message = QPushButton(self.frame_2)
        self.btn_message.setObjectName(u"btn_message")
        self.btn_message.setFont(font1)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/basic/icons/basic/warning.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_message.setIcon(icon8)
        self.btn_message.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.btn_message)

        self.widget_toolbar = QWidget(self.frame_2)
        self.widget_toolbar.setObjectName(u"widget_toolbar")
        sizePolicy.setHeightForWidth(self.widget_toolbar.sizePolicy().hasHeightForWidth())
        self.widget_toolbar.setSizePolicy(sizePolicy)
        self.widget_toolbar.setAutoFillBackground(False)
        self.widget_toolbar.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.widget_toolbar)


        self.verticalLayout_16.addWidget(self.frame_2)

        self.frame = QFrame(self.draw_build)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.graphicsView = QGraphicsView(self.frame)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setToolTipDuration(8)
        self.graphicsView.setStyleSheet(u"QGraphicsView{\n"
"border: 2px solid;\n"
"border-radius: 10px;\n"
"border-color: rgba(84, 84, 84, 200);\n"
"}")

        self.horizontalLayout_20.addWidget(self.graphicsView)


        self.verticalLayout_16.addWidget(self.frame)


        self.horizontalLayout_13.addWidget(self.draw_build)

        self.frame_3 = QFrame(self.draw_content)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(180, 0))
        self.frame_3.setMaximumSize(QSize(180, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_3)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.btn_guide = QPushButton(self.frame_3)
        self.btn_guide.setObjectName(u"btn_guide")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.btn_guide.sizePolicy().hasHeightForWidth())
        self.btn_guide.setSizePolicy(sizePolicy6)
        self.btn_guide.setMinimumSize(QSize(0, 30))
        self.btn_guide.setMaximumSize(QSize(24, 16777215))
        self.btn_guide.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/basic/icons/basic/suggestion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_guide.setIcon(icon9)
        self.btn_guide.setIconSize(QSize(20, 20))

        self.verticalLayout_15.addWidget(self.btn_guide, 0, Qt.AlignRight)

        self.widget_dashboard = ScrollableResultDashBoard(self.frame_3)
        self.widget_dashboard.setObjectName(u"widget_dashboard")

        self.verticalLayout_15.addWidget(self.widget_dashboard)


        self.horizontalLayout_13.addWidget(self.frame_3)


        self.verticalLayout_8.addWidget(self.draw_content)

        self.draw_bottom = QWidget(self.draw_main)
        self.draw_bottom.setObjectName(u"draw_bottom")
        self.draw_bottom.setMinimumSize(QSize(0, 100))
        self.draw_bottom.setMaximumSize(QSize(16777215, 110))
        self.draw_bottom.setStyleSheet(u"#draw_bottom{\n"
"border-radius: 10px;\n"
"background-color: rgb(35, 36, 40);\n"
"}")
        self.horizontalLayout_14 = QHBoxLayout(self.draw_bottom)
        self.horizontalLayout_14.setSpacing(3)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, -1)
        self.frame_optimi = QFrame(self.draw_bottom)
        self.frame_optimi.setObjectName(u"frame_optimi")
        sizePolicy7 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_optimi.sizePolicy().hasHeightForWidth())
        self.frame_optimi.setSizePolicy(sizePolicy7)
        self.frame_optimi.setMinimumSize(QSize(665, 0))
        self.frame_optimi.setFrameShape(QFrame.StyledPanel)
        self.frame_optimi.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_optimi)
        self.horizontalLayout_16.setSpacing(20)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_11 = QFrame(self.frame_optimi)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(300, 0))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(100, 16777215))
        self.label_12.setFont(font1)

        self.horizontalLayout_19.addWidget(self.label_12)

        self.frame_12 = QFrame(self.frame_11)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFont(font1)
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.radio_momentum = QRadioButton(self.frame_12)
        self.radio_momentum.setObjectName(u"radio_momentum")
        self.radio_momentum.setFont(font1)

        self.gridLayout.addWidget(self.radio_momentum, 0, 1, 1, 1)

        self.radio_rmsProp = QRadioButton(self.frame_12)
        self.radio_rmsProp.setObjectName(u"radio_rmsProp")
        self.radio_rmsProp.setFont(font1)

        self.gridLayout.addWidget(self.radio_rmsProp, 2, 0, 1, 1)

        self.radio_adam = QRadioButton(self.frame_12)
        self.radio_adam.setObjectName(u"radio_adam")
        self.radio_adam.setFont(font1)

        self.gridLayout.addWidget(self.radio_adam, 2, 1, 1, 1)

        self.radio_adaDelta = QRadioButton(self.frame_12)
        self.radio_adaDelta.setObjectName(u"radio_adaDelta")
        self.radio_adaDelta.setFont(font1)

        self.gridLayout.addWidget(self.radio_adaDelta, 1, 0, 1, 1)

        self.radio_sgd = QRadioButton(self.frame_12)
        self.radio_sgd.setObjectName(u"radio_sgd")
        self.radio_sgd.setFont(font1)

        self.gridLayout.addWidget(self.radio_sgd, 0, 0, 1, 1)

        self.radio_adaGrad = QRadioButton(self.frame_12)
        self.radio_adaGrad.setObjectName(u"radio_adaGrad")
        self.radio_adaGrad.setFont(font1)

        self.gridLayout.addWidget(self.radio_adaGrad, 1, 1, 1, 1)


        self.horizontalLayout_19.addWidget(self.frame_12)


        self.horizontalLayout_16.addWidget(self.frame_11)

        self.frame_22 = QFrame(self.frame_optimi)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setMinimumSize(QSize(150, 0))
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_23.setSpacing(6)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, -1, 0, -1)
        self.label_28 = QLabel(self.frame_22)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setMaximumSize(QSize(80, 16777215))
        self.label_28.setFont(font1)

        self.horizontalLayout_23.addWidget(self.label_28)

        self.spin_batchSize = QDoubleSpinBox(self.frame_22)
        self.spin_batchSize.setObjectName(u"spin_batchSize")
        self.spin_batchSize.setMinimumSize(QSize(0, 25))
        self.spin_batchSize.setMaximumSize(QSize(100, 16777215))
        self.spin_batchSize.setFont(font)
        self.spin_batchSize.setStyleSheet(u"background-color: transparent;\n"
"border:None\n"
"")
        self.spin_batchSize.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spin_batchSize.setDecimals(0)
        self.spin_batchSize.setMaximum(1000.000000000000000)
        self.spin_batchSize.setSingleStep(1.000000000000000)
        self.spin_batchSize.setValue(32.000000000000000)

        self.horizontalLayout_23.addWidget(self.spin_batchSize)


        self.horizontalLayout_16.addWidget(self.frame_22)

        self.frame_21 = QFrame(self.frame_optimi)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(0, 0))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.frame_21)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_21)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(160, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 16777215))
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.label)

        self.spin_learningRate = QDoubleSpinBox(self.frame_6)
        self.spin_learningRate.setObjectName(u"spin_learningRate")
        sizePolicy4.setHeightForWidth(self.spin_learningRate.sizePolicy().hasHeightForWidth())
        self.spin_learningRate.setSizePolicy(sizePolicy4)
        self.spin_learningRate.setMinimumSize(QSize(0, 25))
        self.spin_learningRate.setMaximumSize(QSize(16777215, 16777215))
        self.spin_learningRate.setFont(font)
        self.spin_learningRate.setStyleSheet(u"background-color: transparent;\n"
"border:None\n"
"")
        self.spin_learningRate.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spin_learningRate.setDecimals(3)
        self.spin_learningRate.setMaximum(100.000000000000000)
        self.spin_learningRate.setSingleStep(0.001000000000000)
        self.spin_learningRate.setValue(0.000000000000000)

        self.horizontalLayout_17.addWidget(self.spin_learningRate)


        self.verticalLayout_34.addWidget(self.frame_6)

        self.frame_10 = QFrame(self.frame_21)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(150, 0))
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_10)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(80, 16777215))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_18.addWidget(self.label_4)

        self.spin_decayRate = QDoubleSpinBox(self.frame_10)
        self.spin_decayRate.setObjectName(u"spin_decayRate")
        self.spin_decayRate.setMinimumSize(QSize(0, 25))
        self.spin_decayRate.setMaximumSize(QSize(100, 16777215))
        self.spin_decayRate.setFont(font)
        self.spin_decayRate.setStyleSheet(u"background-color: transparent;\n"
"border:None\n"
"")
        self.spin_decayRate.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spin_decayRate.setDecimals(4)
        self.spin_decayRate.setMaximum(1.000000000000000)
        self.spin_decayRate.setSingleStep(0.000100000000000)
        self.spin_decayRate.setValue(0.900000000000000)

        self.horizontalLayout_18.addWidget(self.spin_decayRate)


        self.verticalLayout_34.addWidget(self.frame_10)


        self.horizontalLayout_16.addWidget(self.frame_21)


        self.horizontalLayout_14.addWidget(self.frame_optimi, 0, Qt.AlignLeft)

        self.frame_control = QFrame(self.draw_bottom)
        self.frame_control.setObjectName(u"frame_control")
        self.frame_control.setMinimumSize(QSize(0, 0))
        self.frame_control.setMaximumSize(QSize(290, 120))
        self.frame_control.setFrameShape(QFrame.StyledPanel)
        self.frame_control.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_control)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.frame_control)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMinimumSize(QSize(110, 0))
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_13)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, -1, -1, -1)
        self.label_13 = QLabel(self.frame_13)
        self.label_13.setObjectName(u"label_13")
        font7 = QFont()
        font7.setFamily(u"Segoe UI")
        font7.setPointSize(13)
        self.label_13.setFont(font7)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.verticalLayout_11.addWidget(self.label_13)


        self.horizontalLayout_15.addWidget(self.frame_13)

        self.frame_8 = QFrame(self.frame_control)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.btn_restart = QPushButton(self.frame_8)
        self.btn_restart.setObjectName(u"btn_restart")
        self.btn_restart.setMinimumSize(QSize(40, 40))
        self.btn_restart.setMaximumSize(QSize(40, 40))
        self.btn_restart.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_restart.setStyleSheet(u":hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton{border-radius: 20px;}\n"
"")
        icon10 = QIcon()
        icon10.addFile(u":/basic/icons/basic/005-return.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_restart.setIcon(icon10)
        self.btn_restart.setIconSize(QSize(24, 24))

        self.horizontalLayout_11.addWidget(self.btn_restart)


        self.horizontalLayout_15.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_control)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_train = QPushButton(self.frame_7)
        self.btn_train.setObjectName(u"btn_train")
        self.btn_train.setMinimumSize(QSize(64, 64))
        self.btn_train.setMaximumSize(QSize(70, 16777215))
        self.btn_train.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_train.setMouseTracking(False)
        icon11 = QIcon()
        icon11.addFile(u":/basic/icons/basic/001-play-button.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_train.setIcon(icon11)
        self.btn_train.setIconSize(QSize(60, 60))
        self.btn_train.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.btn_train)


        self.horizontalLayout_15.addWidget(self.frame_7)

        self.frame_4 = QFrame(self.frame_control)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_feedfor = QPushButton(self.frame_4)
        self.btn_feedfor.setObjectName(u"btn_feedfor")
        self.btn_feedfor.setMinimumSize(QSize(40, 40))
        self.btn_feedfor.setMaximumSize(QSize(40, 40))
        self.btn_feedfor.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_feedfor.setStyleSheet(u":hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton{border-radius: 20px;}")
        icon12 = QIcon()
        icon12.addFile(u":/basic/icons/basic/008-next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_feedfor.setIcon(icon12)
        self.btn_feedfor.setIconSize(QSize(20, 20))

        self.verticalLayout_3.addWidget(self.btn_feedfor)

        self.btn_backprop = QPushButton(self.frame_4)
        self.btn_backprop.setObjectName(u"btn_backprop")
        self.btn_backprop.setMinimumSize(QSize(40, 40))
        self.btn_backprop.setMaximumSize(QSize(40, 40))
        self.btn_backprop.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_backprop.setStyleSheet(u":hover {\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QPushButton{border-radius: 20px;}")
        icon13 = QIcon()
        icon13.addFile(u":/basic/icons/basic/007-backward-arrows-couple.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_backprop.setIcon(icon13)
        self.btn_backprop.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.btn_backprop)


        self.horizontalLayout_15.addWidget(self.frame_4)


        self.horizontalLayout_14.addWidget(self.frame_control)


        self.verticalLayout_8.addWidget(self.draw_bottom)


        self.horizontalLayout_6.addWidget(self.draw_main)

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

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ANNBuilder", None))
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
#if QT_CONFIG(tooltip)
        self.btn_home.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"     Home", None))
#if QT_CONFIG(tooltip)
        self.btn_tutorial.setToolTip(QCoreApplication.translate("MainWindow", u"Tutorial", None))
#endif // QT_CONFIG(tooltip)
        self.btn_tutorial.setText(QCoreApplication.translate("MainWindow", u"     Tutorial", None))
#if QT_CONFIG(tooltip)
        self.btn_draw.setToolTip(QCoreApplication.translate("MainWindow", u"Builder", None))
#endif // QT_CONFIG(tooltip)
        self.btn_draw.setText(QCoreApplication.translate("MainWindow", u"     Builder", None))
        self.label_24.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Welcome to ANN Builder", None))
        self.btn_gotoTutorial.setText(QCoreApplication.translate("MainWindow", u"Explore the Tutorial", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Check out our neural network tutorials, learn the curial concept, and pratise the exercise", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tutorials", None))
        self.btn_gotoBasicCon.setText(QCoreApplication.translate("MainWindow", u"Basic Concept", None))
        self.btn_gotoMLP.setText(QCoreApplication.translate("MainWindow", u"Multi-Layer Perceptron", None))
        self.btn_gotoCNN.setText(QCoreApplication.translate("MainWindow", u"Convolutional Neural Network", None))
        self.btn_gotoBuilder.setText(QCoreApplication.translate("MainWindow", u"Create a new Model", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Create a neural network model from scatch, visualize and train the model", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Tutorial", None))
        self.label_dataset.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_component.setText(QCoreApplication.translate("MainWindow", u"Component", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Neuron", None))
#if QT_CONFIG(tooltip)
        self.neuron_2D.setToolTip(QCoreApplication.translate("MainWindow", u"2D Neuron", None))
#endif // QT_CONFIG(tooltip)
        self.neuron_2D.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"2D_Neuron", None))
#if QT_CONFIG(tooltip)
        self.neuron_bias_1D.setToolTip(QCoreApplication.translate("MainWindow", u"1D Bias", None))
#endif // QT_CONFIG(tooltip)
        self.neuron_bias_1D.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"1D_Bias", None))
#if QT_CONFIG(tooltip)
        self.neuron_1D.setToolTip(QCoreApplication.translate("MainWindow", u"1D Neuron", None))
#endif // QT_CONFIG(tooltip)
        self.neuron_1D.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"1D_Neuron", None))
#if QT_CONFIG(tooltip)
        self.neuron_bias_2D.setToolTip(QCoreApplication.translate("MainWindow", u"2D Bias", None))
#endif // QT_CONFIG(tooltip)
        self.neuron_bias_2D.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"2D_Bias", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Layer", None))
#if QT_CONFIG(tooltip)
        self.conv_layer.setToolTip(QCoreApplication.translate("MainWindow", u"Convuntional Layer", None))
#endif // QT_CONFIG(tooltip)
        self.conv_layer.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Conv", None))
#if QT_CONFIG(tooltip)
        self.stacked_affine_layer.setToolTip(QCoreApplication.translate("MainWindow", u"Stacked Affine Layer", None))
#endif // QT_CONFIG(tooltip)
        self.stacked_affine_layer.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"StackAffine", None))
#if QT_CONFIG(tooltip)
        self.pooling_layer.setToolTip(QCoreApplication.translate("MainWindow", u"Pooling Layer", None))
#endif // QT_CONFIG(tooltip)
        self.pooling_layer.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Pooling", None))
#if QT_CONFIG(tooltip)
        self.affine_layer.setToolTip(QCoreApplication.translate("MainWindow", u"Affine Layer", None))
#endif // QT_CONFIG(tooltip)
        self.affine_layer.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Affine", None))
#if QT_CONFIG(tooltip)
        self.flatten_layer.setToolTip(QCoreApplication.translate("MainWindow", u"Flatten Layer", None))
#endif // QT_CONFIG(tooltip)
        self.flatten_layer.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Flatten", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"Other", None))
#if QT_CONFIG(tooltip)
        self.loss_func_block.setToolTip(QCoreApplication.translate("MainWindow", u"Loss Function", None))
#endif // QT_CONFIG(tooltip)
        self.loss_func_block.setText("")
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"LossFunc", None))
#if QT_CONFIG(tooltip)
        self.regularizer.setToolTip(QCoreApplication.translate("MainWindow", u"Regularizer", None))
#endif // QT_CONFIG(tooltip)
        self.regularizer.setText("")
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Regularizer", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Building Panel", None))
#if QT_CONFIG(tooltip)
        self.btn_message.setToolTip(QCoreApplication.translate("MainWindow", u"Warning Message", None))
#endif // QT_CONFIG(tooltip)
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Warning: 0", None))
#if QT_CONFIG(tooltip)
        self.btn_guide.setToolTip(QCoreApplication.translate("MainWindow", u"Helper", None))
#endif // QT_CONFIG(tooltip)
        self.btn_guide.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Optrimization :", None))
        self.radio_momentum.setText(QCoreApplication.translate("MainWindow", u"Momentum", None))
        self.radio_rmsProp.setText(QCoreApplication.translate("MainWindow", u"RMSProp", None))
        self.radio_adam.setText(QCoreApplication.translate("MainWindow", u"Adam", None))
        self.radio_adaDelta.setText(QCoreApplication.translate("MainWindow", u"AdaDelta", None))
        self.radio_sgd.setText(QCoreApplication.translate("MainWindow", u"SGD", None))
        self.radio_adaGrad.setText(QCoreApplication.translate("MainWindow", u"AdaGrad", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Batch Size :", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Learning Rate :", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Decay Rate :", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Epoch: 0", None))
#if QT_CONFIG(tooltip)
        self.btn_restart.setToolTip(QCoreApplication.translate("MainWindow", u"Restart", None))
#endif // QT_CONFIG(tooltip)
        self.btn_restart.setText("")
#if QT_CONFIG(tooltip)
        self.btn_train.setToolTip(QCoreApplication.translate("MainWindow", u"Train", None))
#endif // QT_CONFIG(tooltip)
        self.btn_train.setText("")
#if QT_CONFIG(tooltip)
        self.btn_feedfor.setToolTip(QCoreApplication.translate("MainWindow", u"Feed Forward", None))
#endif // QT_CONFIG(tooltip)
        self.btn_feedfor.setText("")
#if QT_CONFIG(tooltip)
        self.btn_backprop.setToolTip(QCoreApplication.translate("MainWindow", u"Backpropagation", None))
#endif // QT_CONFIG(tooltip)
        self.btn_backprop.setText("")
    # retranslateUi

