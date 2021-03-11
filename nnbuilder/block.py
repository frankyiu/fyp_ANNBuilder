from PyQt5.QtGui import QPolygonF
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsRectItem, QGraphicsPolygonItem
from .base import _NNBLossFuncBlock, _NNBRegularizer
from .form import NNBLFBForm, NNBRegularizerForm
from .config import *


class NNBLossFuncBlock(_NNBLossFuncBlock, QGraphicsRectItem):
    def __init__(self, name, x, y):
        _NNBLossFuncBlock.__init__(self, name)
        QGraphicsRectItem.__init__(self, x, y, LFB_WIDTH, LFB_HEIGHT)
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable |
                      QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemSendsGeometryChanges)

    def createForm(self, window):
        return NNBLFBForm(self, window)

    def paint(self, painter, option, widget=None):
        if self.isSelected() or self.hoveredOnConnectMode:
            painter.setBrush(NNB_FOCUS_BRUSH)
            painter.setPen(NNB_FOCUS_PEN)
            painter.drawRect(self.rect())
        painter.setPen(NNB_PEN)
        painter.setBrush(QBrush(LFB_BODY_COLOR))
        painter.drawRect(self.rect())

    def mouseDoubleClickEvent(self, event):
        if self.scene().sceneMode != SceneMode.ConnectMode:
            self.handleMouseDoubleClickEvent()

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            self.handleItemChanged()
        return super().itemChange(change, value)


class NNBRegularizer(_NNBRegularizer, QGraphicsPolygonItem):
    def __init__(self, name, x, y):
        _NNBRegularizer.__init__(self, name)
        QGraphicsPolygonItem.__init__(self)
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable |
                      QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemSendsGeometryChanges)

        # Set up the shape, which is a romb
        p1 = QPointF(x + REGULARIZER_WIDTH / 2, y)
        p2 = QPointF(x + REGULARIZER_WIDTH, y + REGULARIZER_HEIGHT / 2)
        p3 = QPointF(x + REGULARIZER_WIDTH / 2, y + REGULARIZER_HEIGHT)
        p4 = QPointF(x, y + REGULARIZER_HEIGHT / 2)
        self.romb = QPolygonF([p1, p2, p3, p4])
        self.setPolygon(self.romb)

    def createForm(self, window):
        return NNBRegularizerForm(self, window)

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
        if change == QGraphicsItem.ItemPositionChange:
            self.handleItemChanged()
        return super().itemChange(change, value)
