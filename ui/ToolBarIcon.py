import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QPen, QColor, QBrush
from PyQt5.QtCore import QMimeData, Qt, QPoint


#This is the class for the icon in tool bar
class ToolBarIcon(QLabel):
    img_directory = u':/toolbar/icons/toolbar/'
    tool_name = ["selecttool", "connecttool", "traintool"]  #expandable

    def __init__(self, parent, tool_idx):
        super(QLabel,self).__init__(parent)
        if tool_idx >= len(ToolBarIcon.tool_name):
            raise Exception("Tool Bar Item Index out of range")
        self.parent().toolbar[tool_idx] = self
        self.tool = tool_idx    #index to indicate what tool this icon represent
        self.press = False      #for press effect
        self.configureIcon()
        self.setToolTips()
        self.defaultTool()
        self.show()

    #select tool is used by default
    def defaultTool(self):
        if self.tool == 0:
            self.parent().toolSelect()

    #shows the hovering effect
    def enterEvent(self, event):
        self.showImage(hover=True)

    #revert the hovering effect
    def leaveEvent(self, event):
        self.showImage(hover=False)

    #When user press the icon, the icon shows a pressing effect
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.press = True
            self.showImage()

    #When user release the press, it switch the tool
    def mouseReleaseEvent(self, event):
        #expandable
        if self.tool == 0:
            self.parent().toolSelect()
        elif self.tool == 1:
            self.parent().toolConnect()
        elif  self.tool == 2:
            self.parent().toolTrain()

    #This function handles the tool tips text
    def setToolTips(self):
        #expandable
        if self.tool == 0:
            self.setToolTip("Select Object")
        elif self.tool == 1:
            self.setToolTip("Connect Object")
        elif  self.tool == 2:
            self.setToolTip("Train Network")

    #This function handles the hovering and pressing effect of the icon and draw it
    def showImage(self, hover=False):
        tmp = QPixmap(self.tool_piximg.size())
        tmp.fill(Qt.transparent)
        painter = QPainter(tmp)
        painter.setBrush(QBrush(self.tool_piximg))
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.drawRect(self.tool_piximg.rect())
        if hover:
            painter.setBrush(QColor(255,255,255,128))
            painter.drawRect(self.tool_piximg.rect())
            pass
        elif self.press:    #hovering effect should overwrite the press effect
            painter.setBrush(QColor(0,0,0,128))
            painter.drawRect(self.tool_piximg.rect())
            pass
        self.setPixmap(tmp)
        painter.end()

    #edit the property and load the image file from the system
    def configureIcon(self):
        #self.resize(size,size)
        self.setMaximumWidth(30)
        self.setScaledContents(True)
        self.setStyleSheet("background:transparent;")
        self.tool_piximg = QPixmap(ToolBarIcon.img_directory+ToolBarIcon.tool_name[self.tool]+'.png')
        self.showImage()
