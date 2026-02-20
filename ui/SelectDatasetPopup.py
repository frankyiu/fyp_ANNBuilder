import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QPen, QColor, QBrush
from PyQt5.QtCore import QMimeData, Qt, QPoint, QEvent
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.DatasetIcon import *


class SelectDatasetPopup(QWidget):
    #List of prepared datasets
    datasets = ['bi_linear', 'bi_moon', 'bi_circle', 'bi_xor', 'bi_spiral', 'multi_three', 'multi_four', 'multi_circles']

    def __init__(self,parent, loader):
        super(QWidget,self).__init__(parent)
        self.loader = loader
        self.elementSize = QtCore.QSize(100, 100)
        self.setupUI()
        self.displaying = True

    #This function handles the display of popup widget
    #Use this show/hide the popup
    def toggle(self, state=None):
        if state is not None:
            self.displaying = not state
        if self.displaying:
            self.hide()
            self.displaying = False
        else:
            self.show()
            self.displaying = True
        return self.displaying

    #When user move the cursor from icon to panel, the loader icon keeps the hovering effect
    def enterEvent(self, event):
        self.loader.showImage(hover=True)

    #When user does not select any data set and leave the panel, change back the loader icon and close popup
    def leaveEvent(self, event):
        self.loader.setDataSetImg(self.loader)
        self.loader.showImage()
        self.toggle(False)

    def setupUI(self):
#        topleft = self.loader.qrect.topLeft()
        r_topleft = self.loader.mapTo(self.parent(),  QtCore.QPoint(0, 0))
        self.setGeometry(QtCore.QRect(r_topleft.x()+80, r_topleft.y()+30, 260, 500))
        self.setStyleSheet("background:rgba(255,255,255,80);border-radius: 10px")
        i = 0
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 260, 500))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Dataset1 = DatasetIcon(self.verticalLayoutWidget, SelectDatasetPopup.datasets[i], self.loader)
        i += 1
        self.Dataset1.setEnabled(True)
        self.Dataset1.setMinimumSize(self.elementSize)
        self.Dataset1.setMaximumSize(self.elementSize)
        self.Dataset1.setObjectName("Dataset1")
        self.horizontalLayout.addWidget(self.Dataset1)
        self.Dataset2 = DatasetIcon(self.verticalLayoutWidget, SelectDatasetPopup.datasets[i], self.loader)
        i += 1
        self.Dataset2.setEnabled(True)
        self.Dataset2.setMinimumSize(self.elementSize)
        self.Dataset2.setMaximumSize(self.elementSize)
        self.Dataset2.setObjectName("Dataset2")
        self.horizontalLayout.addWidget(self.Dataset2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Dataset3 = DatasetIcon(self.verticalLayoutWidget, SelectDatasetPopup.datasets[i], self.loader)
        i += 1
        self.Dataset3.setEnabled(True)
        self.Dataset3.setMinimumSize(self.elementSize)
        self.Dataset3.setMaximumSize(self.elementSize)
        self.Dataset3.setObjectName("Dataset3")
        self.horizontalLayout_3.addWidget(self.Dataset3)
        self.Dataset4 = DatasetIcon(self.verticalLayoutWidget, SelectDatasetPopup.datasets[i], self.loader)
        i += 1
        self.Dataset4.setEnabled(True)
        self.Dataset4.setMinimumSize(self.elementSize)
        self.Dataset4.setMaximumSize(self.elementSize)
        self.Dataset4.setObjectName("Dataset4")
        self.horizontalLayout_3.addWidget(self.Dataset4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Dataset5 = DatasetIcon(self.verticalLayoutWidget, SelectDatasetPopup.datasets[i], self.loader)
        i += 1
        self.Dataset5.setEnabled(True)
        self.Dataset5.setMinimumSize(self.elementSize)
        self.Dataset5.setMaximumSize(self.elementSize)
        self.Dataset5.setObjectName("Dataset5")
        self.horizontalLayout_4.addWidget(self.Dataset5)
        self.Dataset6 = DatasetIcon(self.verticalLayoutWidget, SelectDatasetPopup.datasets[i], self.loader)
        i += 1
        self.Dataset6.setEnabled(True)
        self.Dataset6.setMinimumSize(self.elementSize)
        self.Dataset6.setMaximumSize(self.elementSize)
        self.Dataset6.setObjectName("Dataset6")
        self.horizontalLayout_4.addWidget(self.Dataset6)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Dataset7 = DatasetIcon(self.verticalLayoutWidget, SelectDatasetPopup.datasets[i], self.loader)
        i += 1
        self.Dataset7.setEnabled(True)
        self.Dataset7.setMinimumSize(self.elementSize)
        self.Dataset7.setMaximumSize(self.elementSize)
        self.Dataset7.setObjectName("Dataset7")
        self.horizontalLayout_5.addWidget(self.Dataset7)
        self.Dataset8 = DatasetIcon(self.verticalLayoutWidget, SelectDatasetPopup.datasets[i], self.loader)
        self.Dataset8.setEnabled(True)
        self.Dataset8.setMinimumSize(self.elementSize)
        self.Dataset8.setMaximumSize(self.elementSize)
        self.Dataset8.setObjectName("Dataset8")
        self.horizontalLayout_5.addWidget(self.Dataset8)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        #self.resize(self.verticalLayoutWidget.geometry())
