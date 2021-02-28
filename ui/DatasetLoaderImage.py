import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QPen, QColor, QBrush
from PyQt5.QtCore import QMimeData, Qt, QPoint


class DatasetLoaderImage(QLabel):
    def __init__(self,parent):
        super(QLabel,self).__init__(parent)
        self.setScaledContents(True)
        self.setStyleSheet("background:transparent;")
        self.show()

    def showImage(self):
        tmp = QPixmap(self.pixmap_img.size())
        tmp.fill(Qt.transparent)
        painter = QPainter(tmp)
        painter.setBrush(QBrush(self.pixmap_img))
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)
        radius = 25
        painter.drawRoundedRect(self.pixmap_img.rect(), radius, radius)
        self.setPixmap(tmp)
        painter.end()

    def updateReferenceImg(self, pixmap):
        self.pixmap_img = pixmap
        self.showImage()
