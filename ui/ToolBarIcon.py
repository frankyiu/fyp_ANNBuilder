import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QPen, QColor, QBrush
from PyQt5.QtCore import QMimeData, Qt, QPoint
from ui.QLabelEffect import QLabelEffect
from nnbuilder.config import *


"""
Parent class for other toolbaricon widget
Reuse the hovering and pressing effect
"""
class ToolBarIcon(QLabelEffect):
    img_directory = u':/toolbar/icons/toolbar/'
    tool_name = {"select":"selecttool", "connect":"connecttool", "train":"traintool"}  #expandable

    def __init__(self, parent, api):
        super().__init__(parent)
        self.press = False      #for press effect
        self.api = api
        self.configureIcon()
        self.setToolTips()
        self.show()

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

    """
    Call the Parent (the widget that contains all Icon)
    setTool method to set the selected tool as self
    """
    def mouseReleaseEvent(self, event):
        self.parent().setTool(self)

    #handles the tool tips text
    def setToolTips(self):
        self.setToolTip(self.getToolTipString())

    #This function handles the hovering and pressing effect of the icon and draw it
    def showImage(self, hover=False):
        super().showImage(hover, self.press)

    #edit the property and load the image file from the system
    def configureIcon(self):
        self.setMaximumWidth(30)
        self.setScaledContents(True)
        self.setStyleSheet("background:transparent;")
        self.tool_piximg = QPixmap(ToolBarIcon.img_directory+self.getToolName()+'.png')
        self.setQPixmapDrawn(self.tool_piximg)
        self.showImage()
