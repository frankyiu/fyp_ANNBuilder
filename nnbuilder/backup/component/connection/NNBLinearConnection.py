from PyQt5.QtWidgets import QGraphicsItem, QGraphicsLineItem
from NNBConnection import NNBConnection
from NNBCostFuncBlock import NNBCostFuncBlock
from NNBForm import NNBSimConnectionForm
from config import *

class NNBSimConnection(NNBConnection, QGraphicsLineItem):
    '''
    Simple connection
    one single straight segment between two blocks

    '''
    def __init__(self, name, componentLeft, componentRight):
        NNBConnection.__init__(self, name, componentLeft, componentRight)
        QGraphicsLineItem.__init__(self)
        # note that since a connection line can only be created on connect mode, so set it to be unselectable
        self.setFlags(QGraphicsItem.ItemIsFocusable)
        self.updateConnectionPos()

        # training parameters
        self.weight = 0.0

    def createForm(self, window):
        return NNBSimConnectionForm(self, window)

    def updateConnectionPos(self):
        if self.component1.sceneBoundingRect().x() > self.component2.sceneBoundingRect().x():
            self.component1, self.component2 = self.component2, self.component1
        rectLeft = self.component1.sceneBoundingRect()
        rectRight = self.component2.sceneBoundingRect()
        x1 = rectLeft.x() + rectLeft.width()
        y1 = rectLeft.y() + rectLeft.height() / 2
        x2 = rectRight.x()
        y2 = rectRight.y() + rectRight.height() / 2
        self.setLine(x1, y1, x2, y2)

    def onWeightChangedOnTrainMode(self):
        if self.form:
            self.form.update()

    def _removeWithoutCheckConnectivity(self):
        if self.component2 in self.component1.connections:
            del self.component1.connections[self.component2]
        if self.component1 in self.component2.connections:
            del self.component2.connections[self.component1]

    def _remove(self):
        self._removeWithoutCheckConnectivity()

        # special case: when this connection is the only one within two layers, cancel their linking relation
        if isinstance(self.component1, NNBCostFuncBlock):
            layer1 = self.component1  # a costFuncBlock
            layer2 = self.component2.layer
        elif isinstance(self.component2, NNBCostFuncBlock):
            layer1 = self.component1.layer  # a costFuncBlock
            layer2 = self.component2
        else:
            layer1 = self.component1.layer
            layer2 = self.component2.layer
        shouldKeepAdjRelation = self.scene().checkConnectivity(layer1, layer2)
        if not shouldKeepAdjRelation:
            layer1.adjBlocks.remove(layer2)
            layer2.adjBlocks.remove(layer1)

    def paint(self, painter, option, widget=None):
        if self.isSelected():
            painter.setBrush(NNB_FOCUS_BRUSH)
            painter.setPen(NNB_FOCUS_PEN)
            painter.drawLine(self.line())
        painter.setBrush(NNB_BRUSH)
        painter.setPen(NNB_PEN)
        painter.drawLine(self.line())

    def mouseDoubleClickEvent(self, event):
        if self.scene().sceneMode != SceneMode.ConnectMode:
            self.handleMouseDoubleClickEvent()