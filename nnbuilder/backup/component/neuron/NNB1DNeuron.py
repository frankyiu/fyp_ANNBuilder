from PyQt5.QtGui import QFont, QFontMetricsF
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QGraphicsEllipseItem, QGraphicsItem
from config import *
from NNBNeuron import NNBNeuron
from NNBForm import NNB1DNeuronForm

class NNB1DNeuron(NNBNeuron, QGraphicsEllipseItem):
    '''

    '''
    def __init__(self, name, x, y):
        NNBNeuron.__init__(self, name)
        QGraphicsEllipseItem.__init__(self, x, y, NEURON_1D_DIAMETER, NEURON_1D_DIAMETER)
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable |
                      QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemSendsGeometryChanges)

    def createForm(self, window):
        return NNB1DNeuronForm(self, window)

    def _removeWithoutCheckConnectivity(self):
        for targetNeuron, connectionLine in self.connections.items():
            if self in targetNeuron.connections:
                del targetNeuron.connections[self]
        self.connections = {}

    def _remove(self):
        self.layer._removeNeuron(self)
        self._removeWithoutCheckConnectivity()

        # special case: when this connection is the only one within two layers, cancel their linking relation
        toBeRemovedAdjBlocks = []
        for adjBlock in self.layer.adjBlocks:
            shouldKeepAdjRelation = self.scene().checkConnectivity(self.layer, adjBlock)
            if not shouldKeepAdjRelation:
                toBeRemovedAdjBlocks.append(adjBlock)
                adjBlock.adjBlocks.remove(self.layer)
        for toBeRemovedAdjBlock in toBeRemovedAdjBlocks:
            self.layer.adjBlocks.remove(toBeRemovedAdjBlock)

    def preventGettingOutOfBox(self):
        rect = self.layer.rect()
        posX = self.rect().x()
        posY = self.rect().y()
        if posX < rect.left():
            self.setX(rect.left())
            self.update()
        elif posX + self.rect().width() > rect.right():
            self.setX(rect.right() - self.rect().width())
            self.update()
        if posY < rect.top() + LAYER_HEADER_HEIGHT:
            self.setY(rect.top() + LAYER_HEADER_HEIGHT)
            self.update()
        elif posY + self.rect().height() > rect.bottom():
            self.setY(rect.bottom() - self.rect().height())
            self.update()

    def paint(self, painter, option, widget=None):
        if self.isSelected() or self.hoveredOnConnectMode:
            painter.setBrush(NNB_FOCUS_BRUSH)
            painter.setPen(NNB_FOCUS_PEN)
            painter.drawEllipse(self.rect())

        painter.setPen(NNB_PEN)
        if self.isBias:
            painter.setBrush(QBrush(NEURON_BODY_COLOR))
            plusOneText = "+1"
            font = QFont()
            font.setPointSize(20)
            font.setFamily("courier new")
            font.setBold(True)
            font.setLetterSpacing(QFont.AbsoluteSpacing, 1)
            painter.setFont(font)
            fontMetrics = QFontMetricsF(font)
            fontWidth = fontMetrics.width(plusOneText)
            fontHeight = fontMetrics.height()
            rectMidX = self.rect().x() + self.rect().width() / 2
            rectMidY = self.rect().y() + self.rect().height() / 2
            painter.drawEllipse(self.rect())
            painter.drawText(int(rectMidX - fontWidth / 2),
                             int(rectMidY + fontHeight / 3), plusOneText)
        else:
            #painter.setBrush(NNB_BRUSH)
            painter.setBrush(QBrush(QColor(255, 255, 255, 128)))
            painter.drawEllipse(self.rect())

    def mouseDoubleClickEvent(self, event):
        if self.scene().sceneMode != SceneMode.ConnectMode:
            self.handleMouseDoubleClickEvent()

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            for connection in self.connections.values():
                connection.updateConnectionPos()
            newPos = QPointF(value.x(), value.y())
            rect = self.layer.rect()
            offsetX = self.rect().x()
            offsetY = self.rect().y()
            if newPos.x() + offsetX < rect.left():
                newPos.setX(rect.left() - offsetX)
            elif newPos.x() + offsetX + self.rect().width() > rect.right():
                newPos.setX(rect.right() - offsetX - self.rect().width())
            if newPos.y() + offsetY < rect.top() + LAYER_HEADER_HEIGHT:
                newPos.setY(rect.top() + LAYER_HEADER_HEIGHT - offsetY)
            elif newPos.y() + offsetY + self.rect().height() > rect.bottom():
                newPos.setY(rect.bottom() - offsetY - self.rect().height())

            return newPos
        return super().itemChange(change, value)






