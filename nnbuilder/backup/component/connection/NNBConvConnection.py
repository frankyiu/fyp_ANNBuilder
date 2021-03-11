from PyQt5.QtGui import QPainterPath, QPainterPathStroker
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPathItem
from NNBConnection import NNBConnection
from config import *

class NNBConvConnection(NNBConnection, QGraphicsPathItem):
    '''
    component1 and component2 must be of type "NNBneuron2D"

    '''
    def __init__(self, name, neuron2DLeft, neuron2DRight):
        NNBConnection.__init__(self, name, neuron2DLeft, neuron2DRight)
        QGraphicsPathItem.__init__(self)
        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsFocusable)
        self.updateConnectionPos()

    def updateConnectionPos(self):
        kernelSize = self.component1.kernelSize()
        leftSceneBRect = self.component1.sceneBoundingRect()
        rightSceneBRect = self.component2.sceneBoundingRect()

        self.lkr = leftSceneBRect.x() + (leftSceneBRect.width() + kernelSize) / 2
        self.lkt = leftSceneBRect.y() + (leftSceneBRect.height() - kernelSize) / 2
        self.lkb = leftSceneBRect.y() + (leftSceneBRect.height() + kernelSize) / 2
        self.rmx = rightSceneBRect.x() + rightSceneBRect.width() / 2
        self.rmy = rightSceneBRect.y() + rightSceneBRect.height() / 2
        self.setPath(self.makeLines())
        self.update()

    def makeLines(self):
        path = QPainterPath()
        path.moveTo(self.lkr, self.lkt)
        path.lineTo(self.rmx, self.rmy)
        path.moveTo(self.lkr, self.lkb)
        path.lineTo(self.rmx, self.rmy)
        return path

    def shape(self):
        path = self.makeLines()
        stroker = QPainterPathStroker()
        return stroker.createStroke(path).simplified()

    def paint(self, painter, option, widget=None):
        path = self.makeLines()
        if self.isSelected():
            painter.setBrush(QColor(128, 128, 128, 128))
            path.lineTo(self.lkr, self.lkt)
            painter.drawPath(path)
            # small rects also get highlightened
        painter.setBrush(NNB_BRUSH)
        painter.drawPath(path)



