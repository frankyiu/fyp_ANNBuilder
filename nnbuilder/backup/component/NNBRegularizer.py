from PyQt5.QtGui import QPolygonF
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsPolygonItem
from NNBBlock import NNBBlock
from NNBForm import NNBRegularizerForm
from config import *

class NNBRegularizer(NNBBlock, QGraphicsPolygonItem):
    def __init__(self, name, x, y):
        NNBBlock.__init__(self, name)
        QGraphicsPolygonItem.__init__(self)
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable |
                      QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemSendsGeometryChanges)

        #Set up the shape, which is a romb
        p1 = QPointF(x + REGULARIZER_WIDTH / 2, y)
        p2 = QPointF(x + REGULARIZER_WIDTH, y + REGULARIZER_HEIGHT / 2)
        p3 = QPointF(x + REGULARIZER_WIDTH / 2, y + REGULARIZER_HEIGHT)
        p4 = QPointF(x, y + REGULARIZER_HEIGHT / 2)
        self.romb = QPolygonF([p1, p2, p3, p4])
        self.setPolygon(self.romb)

        #?
        self.connections = {}

        # model hyper-parameters
        self.regularization = "L2"  # L1, L2, L0.5, L3, Lp, Elastic Net
        self.C = 1.0

    def createForm(self, window):
        return NNBRegularizerForm(self, window)

    def _connectLayer(self, layer):
        self.adjBlocks.append(layer)

    def _remove(self):
        pass
    #         for targetNeuron, connectionLine in self.connections.items():
    #             self.scene().removeItem(connectionLine)
    #             if self in targetNeuron.connections:
    #                 del targetNeuron.connections[self]
    #         if self.adjBlocks:
    #             self.adjBlocks[0].adjBlocks.remove(self)

    def paint(self, painter, option, widget=None):
        if self.isSelected() or self.hoveredOnConnectMode:
            painter.setBrush(NNB_FOCUS_BRUSH)
            painter.setPen(NNB_FOCUS_PEN)
            painter.drawPolygon(self.romb)
        painter.setPen(NNB_PEN)
        painter.setBrush(QBrush(REGULARIZER_BODY_COLOR))
        painter.drawPolygon(self.romb)

    def mouseDoubleClickEvent(self, event):
        if self.scene().sceneMode != SceneMode.ConnectMode:
            self.handleMouseDoubleClickEvent()

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange and self.connections:
            for connection in self.connections.values():
                connection.updateConnectionPos()
        return super().itemChange(change, value)

