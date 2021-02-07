import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QPen, QColor, QBrush
from PyQt5.QtCore import QMimeData, Qt, QPoint
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.ToolBarIcon import *

#This is the widget attached to the program UI
#All the switch tool logic is implemented here
#This includes: control the mode flag, control the press effect of icons
class ToolBarWidget(QWidget):
    def __init__(self, parent=None):
        super(QWidget,self).__init__(parent)
        self.toolbar = {}   #use dict to track the icons, regardless the order of object creation
        self.setupUi()
        self.addTools()

    #helper function to ensure 1 and only 1 button is pressed
    def controlPressEffect(self, selected_idx):
        for k,v in self.toolbar.items():
            if k == selected_idx:
                v.press=True
            else:
                v.press=False
            v.showImage()
        return

    #call the api
    def toolSelect(self):
        self.controlPressEffect(0)
        print(ToolBarIcon.tool_name[self.toolbar[0].tool])
        pass

    #call the api
    def toolConnect(self):
        self.controlPressEffect(1)
        print(ToolBarIcon.tool_name[self.toolbar[1].tool])
        pass

    #call the api
    def toolTrain(self):
        self.controlPressEffect(2)
        print(ToolBarIcon.tool_name[self.toolbar[2].tool])
        pass

    #control the display size of widget
    def setupUi(self):
        n_tools = len(ToolBarIcon.tool_name)
        size = 30
        self.setGeometry(QtCore.QRect(0, 0, n_tools * size, size))
        self.setObjectName("ToolBarhorizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("ToolBarhorizontalLayout")

    #add the tools qlabel to the widget
    def addTools(self):
        #expandable
        SelectTool = ToolBarIcon(self, 0)
        SelectTool.setObjectName("ToolBarSelectTool")
        self.horizontalLayout.addWidget(SelectTool)
        ConnectTool = ToolBarIcon(self, 1)
        ConnectTool.setObjectName("ToolBarConnectTool")
        self.horizontalLayout.addWidget(ConnectTool)
        TrainTool = ToolBarIcon(self, 2)
        TrainTool.setObjectName("ToolBarTrainTool")
        self.horizontalLayout.addWidget(TrainTool)
