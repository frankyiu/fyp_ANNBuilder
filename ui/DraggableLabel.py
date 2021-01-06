import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QPen
from PyQt5.QtCore import QMimeData, Qt


class DraggableLabel(QLabel):
    
    deletable = False
    
    def __init__(self, parent):
        super().__init__(parent)
        self.deletable = False
        
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.st_pos = event.pos()


    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.st_pos).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.text())
        drag.setMimeData(mimedata)
        pixmap = QPixmap(self.size())
        painter = QPainter(pixmap)
        painter.drawPixmap(self.rect(), self.grab())
        painter.end()

        drag.setPixmap(pixmap)
        drag.setHotSpot(event.pos())
        Qt.DropAction = drag.exec_(Qt.CopyAction | Qt.MoveAction)
        
    def connectRight(self,  list):
        for l in list:
            painter = QPainter(self)
            painter.setPen(QPen())
            painter.drawLine(self.pos().x(), self.pos().y(), 200, 200);
    
    def connectLeft(self,  list):
        for l in list:
            painter = QPainter(self.parent().parent())
            painter.setPen(QPen())
            painter.drawLine(0, 0, 200, 200);






