from PyQt5.QtGui import QPainterPath, QPainterPathStroker
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPathItem
from NNBConnection import NNBConnection
from config import *

class NNBRegConnection(NNBConnection, QGraphicsPathItem):
    def __init__(self, name, block, regularizer):
        '''
        :param name:
        :param block: component1
        :param regularizer: component2
        '''
        NNBConnection.__init__(self, name, block, regularizer)
        QGraphicsPathItem.__init__(self)
        # note that since a connection line can only be created on connect mode, so set it to be unselectable
        self.setFlags(QGraphicsItem.ItemIsFocusable)
        self.updateConnectionPos()

    def paint(self, painter, option, widget=None):
        if self.isSelected():
            painter.setBrush(NNB_FOCUS_BRUSH)
            painter.setPen(NNB_FOCUS_PEN)
            painter.drawPath(self.path)
        painter.setBrush(QBrush(QColor(255, 255, 255, 0)))
        painter.setPen(NNB_PEN)
        painter.drawPath(self.path)

    def updateConnectionPos(self):
        blockRect = self.component1.sceneBoundingRect()
        regularizerRect = self.component2.sceneBoundingRect()
        x1 = regularizerRect.x()
        y1 = regularizerRect.y() + regularizerRect.height() / 2
        x2 = blockRect.x() + blockRect.width() / 2
        y2 = blockRect.y()
        c1 = x2
        c2 = y1
        if regularizerRect.x() + regularizerRect.width() < x2:
            x1 += regularizerRect.width()
        if y1 > blockRect.y() + blockRect.height() / 2:
            y2 += blockRect.height()
        if y1 > blockRect.y() and y1 < blockRect.bottom():
            c1 = x1
            c2 = y2
        self.fromPt = QPointF(x1, y1)
        self.ctrlPt = QPointF(c1, c2)
        self.toPt = QPointF(x2, y2)
        self.path = QPainterPath()
        self.path.moveTo(self.fromPt)
        self.path.quadTo(self.ctrlPt, self.toPt)
        self.setPath(self.path)

    def shape(self):
        path = QPainterPath()
        path.moveTo(self.fromPt)
        path.quadTo(self.ctrlPt, self.toPt)
        stroker = QPainterPathStroker()
        return stroker.createStroke(path).simplified()

    def mouseDoubleClickEvent(self, event):
        if self.scene().sceneMode != SceneMode.ConnectMode:
            self.handleMouseDoubleClickEvent()

    def createForm(self, window):
        pass
        # return NNBRegConnectionForm(self, window)

    def _removeWithoutCheckConnectivity(self):
        pass

    def _remove(self):
        pass