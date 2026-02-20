from PyQt5.QtGui import QFont, QFontMetricsF, QPainterPath
from PyQt5.QtCore import QPointF, QRect, QRectF
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsEllipseItem, QGraphicsRectItem
from .base import _NNB1DInputNeuron, _NNB1DBiasNeuron, _NNB1DStackedNeuron, _NNB2DInputNeuron, _NNB2DBiasNeuron, \
    _NNB2DFlattenLayer, _NNBLossFuncBlock
from .config import *
from .form import NNB1DNeuronForm


def drawPlusOne(painter, rect):
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
    rectMidX = rect.x() + rect.width() / 2
    rectMidY = rect.y() + rect.height() / 2
    painter.drawText(int(rectMidX - fontWidth / 2), int(rectMidY + fontHeight / 3), plusOneText)


def draw1DNeuron(painter, rect, isSelected=False, isConnectedTo=False, isBias=False, hasSyn=True):
    if isSelected:
        painter.setBrush(NNB_FOCUS_BRUSH)
        painter.setPen(NNB_FOCUS_PEN)
        painter.drawEllipse(rect)

    if isConnectedTo:
        x = rect.x()
        y = rect.y()
        if hasSyn:
            startPt = QPointF(x + NEURON_1D_RADIUS + NEURON_1D_SYN_OFFSET_X,
                              y + NEURON_1D_RADIUS - NEURON_1D_SYN_OFFSET_Y)
            midPt = QPointF(x + NEURON_1D_DIAMETER + NEURON_1D_SYN_LENGTH,
                            y + NEURON_1D_RADIUS)
            endPt = QPointF(x + NEURON_1D_RADIUS + NEURON_1D_SYN_OFFSET_X,
                            y + NEURON_1D_RADIUS + NEURON_1D_SYN_OFFSET_Y)
            startingAngle = - NEURON_1D_SYN_THETA
            path = QPainterPath()
            path.moveTo(startPt)
            path.lineTo(midPt)
            path.lineTo(endPt)
            path.moveTo(midPt)
            path.arcTo(x, y, NEURON_1D_DIAMETER, NEURON_1D_DIAMETER, startingAngle, 2 * NEURON_1D_SYN_THETA)
            painter.drawPath(path)

    painter.setPen(NNB_PEN)
    painter.setBrush(NEURON_BODY_COLOR)
    painter.drawEllipse(rect)

    if isBias:
        drawPlusOne(painter, rect)


class NNB1DNeuron(QGraphicsEllipseItem):
    def __init__(self, x, y):
        QGraphicsEllipseItem.__init__(self, x, y, NEURON_1D_DIAMETER, NEURON_1D_DIAMETER)
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable |
                      QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemSendsGeometryChanges)

    def createForm(self):
        return NNB1DNeuronForm(self, self.scene().activeWindow())

    def boundingRect(self):
        if self.connectionsTo:
            return self.rect().adjusted(0, 0, NEURON_1D_SYN_LENGTH, 0)
        return self.rect()

    def paint(self, painter, option, widget=None):
        draw1DNeuron(painter, self.rect(),
                     self.isSelected() or self.hoveredOnConnectMode,
                     self.connectionsTo, hasSyn=not isinstance(self.layer.nextLayer, _NNBLossFuncBlock))

    def mouseDoubleClickEvent(self, event):
        if self.scene().sceneMode != SceneMode.ConnectMode:
            self.handleMouseDoubleClickEvent()

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            self.handleItemChanged()
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
        return QGraphicsEllipseItem.itemChange(self, change, value)


class NNB1DInputNeuron(_NNB1DInputNeuron, NNB1DNeuron):
    def __init__(self, name, x, y):
        _NNB1DInputNeuron.__init__(self, name)
        NNB1DNeuron.__init__(self, x, y)


class NNB1DBiasNeuron(_NNB1DBiasNeuron, NNB1DNeuron):
    def __init__(self, name, x, y):
        _NNB1DBiasNeuron.__init__(self, name)
        NNB1DNeuron.__init__(self, x, y)

    def paint(self, painter, option, widget=None):
        draw1DNeuron(painter, self.rect(),
                     self.isSelected() or self.hoveredOnConnectMode,
                     self.connectionsTo, hasSyn=not isinstance(self.layer.nextLayer, _NNBLossFuncBlock), isBias=True)


class NNB1DStackedNeuron(_NNB1DStackedNeuron, QGraphicsRectItem):
    def __init__(self, name, x, y):
        _NNB1DStackedNeuron.__init__(self, name)
        QGraphicsItem.__init__(self)
        self.setFlags(QGraphicsItem.ItemIsSelectable |
                      QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemSendsGeometryChanges)

    def createForm(self):
        return NNB1DNeuronForm(self, self.scene().activeWindow())

    def shape(self):
        path = QPainterPath()
        for i, neuronLayout in enumerate(self.layer.neuronLayouts):
            path.addEllipse(*neuronLayout, NEURON_1D_DIAMETER, NEURON_1D_DIAMETER)
        for skipDot in self.layer.skipDotLayouts:
            path.addEllipse(*skipDot, STACKED_AFF_1D_SKIP_DOT_SIZE, STACKED_AFF_1D_SKIP_DOT_SIZE)
        return path

    def boundingRect(self):
        rect = QRectF(self.layer.neuronStartX, self.layer.neuronStartY, NEURON_1D_DIAMETER, self.layer.neuronHeight)
        if self.connectionsTo:
            return rect.adjusted(-NEURON_1D_SYN_LENGTH, 0, NEURON_1D_SYN_LENGTH, 0)
        return rect

    def sceneBoundingRect(self):
        return self.boundingRect()

    def paint(self, painter, option, widget=None):
        hasSyn = not isinstance(self.layer.nextLayer, _NNBLossFuncBlock)
        for i, neuronLayout in enumerate(self.layer.neuronLayouts):
            draw1DNeuron(painter,
                         QRect(*neuronLayout, NEURON_1D_DIAMETER, NEURON_1D_DIAMETER),
                         self.isSelected() or self.hoveredOnConnectMode,
                         isConnectedTo=self.connectionsTo,
                         isBias=self.layer.hasBias and i == len(self.layer.neuronLayouts) - 1,
                         hasSyn=hasSyn
                         )
        for skipDot in self.layer.skipDotLayouts:
            if self.isSelected() or self.hoveredOnConnectMode:
                painter.setBrush(NNB_FOCUS_BRUSH)
                painter.setPen(NNB_FOCUS_PEN)
                painter.drawEllipse(*skipDot, STACKED_AFF_1D_SKIP_DOT_SIZE, STACKED_AFF_1D_SKIP_DOT_SIZE)
            painter.setPen(NNB_PEN)
            painter.setBrush(NEURON_BODY_COLOR)
            painter.drawEllipse(*skipDot, STACKED_AFF_1D_SKIP_DOT_SIZE, STACKED_AFF_1D_SKIP_DOT_SIZE)


class NNB2DNeuron(QGraphicsRectItem):
    def __init__(self, x, y):
        QGraphicsRectItem.__init__(self, x, y, NEURON_2D_SIZE, NEURON_2D_SIZE)
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable |
                      QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemSendsGeometryChanges)

    def createForm(self):
        return NNB1DNeuronForm(self, self.scene().activeWindow())

    def kernelSize(self):
        return NEURON_2D_SIZE // 4

    def paint(self, painter, option, widget=None):
        if self.isSelected():
            painter.setBrush(NNB_FOCUS_BRUSH)
            painter.setPen(NNB_FOCUS_PEN)
            painter.drawRect(self.rect())
        painter.setBrush(NEURON_BODY_COLOR)
        painter.setPen(NNB_PEN)
        painter.drawRect(self.rect())
        if self.connectionsTo and not isinstance(self.layer.nextLayer, _NNB2DFlattenLayer):
            painter.setPen(QPen(Qt.DotLine))
            kernelSize = NEURON_2D_SIZE // 4
            kX = int(self.rect().x() + (self.rect().width() - kernelSize) / 2)
            kY = int(self.rect().y() + (self.rect().height() - kernelSize) / 2)
            painter.drawRect(kX, kY, kernelSize, kernelSize)

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            self.handleItemChanged()
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
        return QGraphicsRectItem.itemChange(self, change, value)


class NNB2DInputNeuron(_NNB2DInputNeuron, NNB2DNeuron):
    def __init__(self, name, x, y):
        _NNB2DInputNeuron.__init__(self, name)
        NNB2DNeuron.__init__(self, x, y)


class NNB2DBiasNeuron(_NNB2DBiasNeuron, NNB2DNeuron):
    def __init__(self, name, x, y):
        _NNB2DBiasNeuron.__init__(self, name)
        NNB2DNeuron.__init__(self, x, y)

    def paint(self, painter, option, widget=None):
        super().paint(painter, option, widget)
        drawPlusOne(painter, self.rect())
