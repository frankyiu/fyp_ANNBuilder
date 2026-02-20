from PyQt5.QtGui import QFont, QFontMetricsF
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem
from config import *
from NNBNeuron import NNBNeuron

class NNB2DNeuron(NNBNeuron, QGraphicsRectItem):
    def __init__(self, name, x, y):
        NNBNeuron.__init__(self, name)
        QGraphicsRectItem.__init__(self, x, y, NEURON_2D_SIZE, NEURON_2D_SIZE)
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable |
                      QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemSendsGeometryChanges)
        self.connectionsFrom = {}

    # def connectTo(self, neuron2D):
    #     # Check if connection is valid...
    #     #connection = NNBConvConnection(self, neuron2D)
    #     #self.scene().addItem(connection)
    #     self.connections[neuron2D] = connection
    #     neuron2D.connectionFrom[self] = connection

    def kernelSize(self):
        return NEURON_2D_SIZE // 4

    def paint(self, painter, option, widget = None):
        if self.isSelected():
            painter.setBrush(NNB_FOCUS_BRUSH)
            painter.setPen(NNB_FOCUS_PEN)
            painter.drawRect(self.rect())
        painter.setBrush(NEURON_BODY_COLOR)
        painter.setPen(NNB_PEN)
        painter.drawRect(self.rect())
        if self.connections:
            painter.setPen(QPen(Qt.DotLine))
            kernelSize = NEURON_2D_SIZE // 4
            kX = int(self.rect().x() + (self.rect().width() - kernelSize) / 2)
            kY = int(self.rect().y() + (self.rect().height() - kernelSize) / 2)
            painter.drawRect(kX, kY, kernelSize, kernelSize)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            for connection in self.connections.values():
                connection.updateConnectionPos()
            for connection in self.connectionsFrom.values():
                connection.updateConnectionPos()
        return super().itemChange(change, value)