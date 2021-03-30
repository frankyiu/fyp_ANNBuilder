from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QPen, QColor, QBrush
from PyQt5.QtCore import QMimeData, Qt, QPoint
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.ToolBarIcon import ToolBarIcon
from ui.ToolBarIconSelect import ToolBarIconSelect
from ui.ToolBarIconConnect import ToolBarIconConnect
from ui.ToolBarIconTrain import ToolBarIconTrain

"""
A widget that contains all the ToolBarIcon Object
Implement the switch tool logic
"""
class ToolBarWidget(QWidget):
    def __init__(self, parent=None):
        super(QWidget,self).__init__(parent)
        self.toolbar_dict = {}
        self.selected_tool = None
        self.setupUi()
        self.addTools()
        self.setTool(self.toolbar_dict["select"])

    """
    Implement the switch tool logic, it
    - first remove the press effect of the previously selected tool
    - then add the press effect of the new one and switch the mode
    """
    def setTool(self, selected):
        if self.selected_tool is not None:
            self.__setToolPressEffect(self.selected_tool, False)
        self.selected_tool = selected
        self.__setToolPressEffect(self.selected_tool, True)
        self.selected_tool.switchMode()

    def __setToolPressEffect(self, tool_widget, press):
        tool_widget.press = press
        tool_widget.showImage()

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
        SelectTool = ToolBarIconSelect(self)
        SelectTool.setObjectName("ToolBarSelectTool")
        self.horizontalLayout.addWidget(SelectTool)
        self.toolbar_dict["select"] = SelectTool
        ConnectTool = ToolBarIconConnect(self)
        ConnectTool.setObjectName("ToolBarConnectTool")
        self.horizontalLayout.addWidget(ConnectTool)
        self.toolbar_dict["connect"] = ConnectTool
        TrainTool = ToolBarIconTrain(self)
        TrainTool.setObjectName("ToolBarTrainTool")
        self.horizontalLayout.addWidget(TrainTool)
        self.toolbar_dict["train"] = TrainTool
