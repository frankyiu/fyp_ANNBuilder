from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem
from NNBComponent import NNBComponent
from ..NNBForm import NNBCFBForm
from config import *

class NNBCostFuncBlock(NNBComponent, QGraphicsRectItem):
    def __init__(self, name, x, y):
        NNBComponent.__init__(self, name)
        QGraphicsRectItem.__init__(self, x, y, CFB_WIDTH, CFB_HEIGHT)
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable |
                      QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemSendsGeometryChanges)
        # adjBlocks can only contain an output layer, so len(adjBlocks) >= 1
        self.connections = {}

        # model hyper-parameter
        self.costFunc = "MSE"  # MAE, MSE, CE

    def createForm(self, window):
        return NNBCFBForm(self, window)

    def _connectLayer(self, layer):
        self.adjBlocks = [layer]  # must be an output layer

    def _connectReg(self, reg):
        if reg not in self.regs:
            self.regs.append(reg)

    def _remove(self):
        for targetNeuron, connectionLine in self.connections.items():
            self.scene().removeItem(connectionLine)
            if self in targetNeuron.connections:
                del targetNeuron.connections[self]
        if self.adjBlocks:
            self.adjBlocks[0].adjBlocks.remove(self)
        # special case: when this connection is the only one within two layers, cancel their linking relation

    def paint(self, painter, option, widget=None):
        if self.isSelected() or self.hoveredOnConnectMode:
            painter.setBrush(NNB_FOCUS_BRUSH)
            painter.setPen(NNB_FOCUS_PEN)
            painter.drawRect(self.rect())
        painter.setPen(NNB_PEN)
        painter.setBrush(QBrush(CFB_BODY_COLOR))
        painter.drawRect(self.rect())

    def mouseDoubleClickEvent(self, event):
        if self.scene().sceneMode != SceneMode.ConnectMode:
            self.handleMouseDoubleClickEvent()

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            for connection in self.connections.values():
                connection.updateConnectionPos()
            for reg in self.regs:
                for connection in reg.connections.values():
                    connection.updateConnectionPos()
        return super().itemChange(change, value)