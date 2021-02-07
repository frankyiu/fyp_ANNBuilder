import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QPen
from PyQt5.QtCore import QMimeData, Qt, QPoint



class DraggableLabel(QLabel):


    def __init__(self, parent):
        super().__init__(parent)
        self.rPos = None #for window resizing

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
        mimedata.setText(self.objectName())
        drag.setMimeData(mimedata)
        drag.setPixmap(self.grab())
        drag.setHotSpot(event.pos())
        Qt.DropAction = drag.exec_(Qt.CopyAction | Qt.MoveAction)


    #get the absolute position of a child label based on frame's position
    def globalPos(self):
        return self.parent().pos() + self.relativePos()

    #get the relative position of the label relative to the parent frame
    #should be the same as pos(), but will update when resize
    def relativePos(self):
        p_w, p_h = self.parent().size().width(), self.parent().size().height()
        return QPoint(self.rPos[0] * p_w, self.rPos[1] * p_h) - self.radius

    #connect nodes in neighbor frame
    def connectNeighborFrameNodes(self, list, painter):
        for l in list:
            dist = l.globalPos()-self.globalPos()
            painter.drawLine(self.relativePos()+self.radius, dist+self.relativePos()+self.radius) #draw on local frame

