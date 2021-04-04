from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtCore import QPoint, QRect

class FocusF():
    def __init__(self, parent, targetWidget):
        super().__init__(parent)
        self.targetWidget = targetWidget
        self.setupUI()
        self.show()
    
    def setupUI(self):
        posOnParent = self.targetWidget.mapTo(self.parent(), QPoint(0, 0))
        self.setGeometry(QRect(posOnParent.x(), posOnParent.y(), 300, 300))
        self.setStyleSheet("background-color: rgb(107, 203, 255);")
        self.setAutoFillBackground(True)
