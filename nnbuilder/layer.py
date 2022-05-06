from PyQt5.QtGui import QPainterPath, QFont, QFontMetricsF
from PyQt5.QtCore import QRectF
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsRectItem
from .base import _NNB1DAffineLayer, _NNB1DStackedLayer, _NNB2DConvLayer, _NNB2DPoolingLayer, _NNB2DFlattenLayer
from .form import NNB1DAffineLayerForm
from .config import *

'''

- resize a QGraphicsItem with the mouse:
    https://stackoverflow.com/questions/34429632/resize-a-qgraphicsitem-with-the-mouse

'''


class NNBContainableLayer(QGraphicsRectItem):
    class Handle:
        handleTopLeft = 1
        handleTopMiddle = 2
        handleTopRight = 3
        handleMiddleLeft = 4
        handleMiddleRight = 5
        handleBottomLeft = 6
        handleBottomMiddle = 7
        handleBottomRight = 8

        handleCursors = {  # TO-DO
            handleTopLeft: Qt.SizeFDiagCursor,
            handleTopMiddle: Qt.SizeVerCursor,
            handleTopRight: Qt.SizeBDiagCursor,
            handleMiddleLeft: Qt.SizeHorCursor,
            handleMiddleRight: Qt.SizeHorCursor,
            handleBottomLeft: Qt.SizeBDiagCursor,
            handleBottomMiddle: Qt.SizeVerCursor,
            handleBottomRight: Qt.SizeFDiagCursor,
        }

    class State:
        Normal = 1
        Moving = 2
        ShowingHandles = 3
        Resizing = 4

    def __init__(self, title, x, y):
        QGraphicsRectItem.__init__(self, x, y, LAYER_WIDTH, LAYER_HEIGHT)
        self.headerTitle = title
        self.headerBGColor = QColor(255, 255, 255, 128)
        self.bodyBGColor = QColor(200, 200, 200, 128)

        self.handles = {}
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressRect = None

        self.state = NNBContainableLayer.State.Normal
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable |
                      QGraphicsItem.ItemSendsGeometryChanges | QGraphicsItem.ItemIsFocusable)

        self.updateHandlesPos()

    def handleAt(self, point):
        for k, v, in self.handles.items():
            if v.contains(point):
                return k
        return None

    def mousePressEvent(self, event):
        if self.state == NNBContainableLayer.State.ShowingHandles:
            self.handleSelected = self.handleAt(event.pos())
            if self.handleSelected:
                self.mousePressRect = self.boundingRect()
        self.mousePressPos = event.pos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.state == NNBContainableLayer.State.Normal:
            if self.mousePressPos and \
                    (self.mousePressPos - event.pos()).manhattanLength() >= QApplication.startDragDistance():
                self.state = NNBContainableLayer.State.Moving
        elif self.state == NNBContainableLayer.State.ShowingHandles:
            if self.handleSelected:
                self.state = NNBContainableLayer.State.Resizing
            else:
                self.state = NNBContainableLayer.State.Moving
        elif self.state == NNBContainableLayer.State.Resizing:
            self.interactiveResize(event.pos())
            return
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.RightButton:
            super().mouseReleaseEvent(event)
            return
        if self.state == NNBContainableLayer.State.Normal:
            self.state = NNBContainableLayer.State.ShowingHandles
        elif self.state == NNBContainableLayer.State.ShowingHandles:
            self.state = NNBContainableLayer.State.Normal
        elif self.state == NNBContainableLayer.State.Moving or self.state == NNBContainableLayer.State.Resizing:
            self.state = NNBContainableLayer.State.Normal
            self.handleSelected = None
            self.mousePressRect = None
        self.update()
        self.mousePressPos = None
        super().mouseReleaseEvent(event)

    def mouseDoubleClickEvent(self, event):
        if self.scene().sceneMode != SceneMode.ConnectMode:
            self.handleMouseDoubleClickEvent()

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemSelectedChange:
            self.state = NNBContainableLayer.State.Normal
        if change == QGraphicsItem.ItemPositionChange:
            self.handleItemChanged()
        return super().itemChange(change, value)

    def boundingRect(self):
        o = LAYER_HANDLE_SIZE + LAYER_HANDLE_SPACE
        return self.rect().adjusted(-o, -o, o, o)

    def updateHandlesPos(self):
        s = LAYER_HANDLE_SIZE
        b = self.boundingRect()
        self.handles[NNBContainableLayer.Handle.handleTopLeft] = QRectF(b.left(), b.top(), s, s)
        self.handles[NNBContainableLayer.Handle.handleTopMiddle] = QRectF(b.center().x() - s / 2, b.top(), s, s)
        self.handles[NNBContainableLayer.Handle.handleTopRight] = QRectF(b.right() - s, b.top(), s, s)
        self.handles[NNBContainableLayer.Handle.handleMiddleLeft] = QRectF(b.left(), b.center().y() - s / 2, s, s)
        self.handles[NNBContainableLayer.Handle.handleMiddleRight] = QRectF(b.right() - s, b.center().y() - s / 2, s, s)
        self.handles[NNBContainableLayer.Handle.handleBottomLeft] = QRectF(b.left(), b.bottom() - s, s, s)
        self.handles[NNBContainableLayer.Handle.handleBottomMiddle] = QRectF(b.center().x() - s / 2,
                                                                             b.bottom() - s, s, s)
        self.handles[NNBContainableLayer.Handle.handleBottomRight] = QRectF(b.right() - s, b.bottom() - s, s, s)

    def findResizeScope(self):
        return float('inf'), -float('inf'), float('inf'), -float('inf')

    def interactiveResize(self, mousePos):
        offset = LAYER_HANDLE_SIZE + LAYER_HANDLE_SPACE
        boundingRect = self.boundingRect()
        rect = self.rect()
        self.prepareGeometryChange()
        # TO-DO
        neuronHighestPos, neuronLowestPos, neuronLeftmostPos, neuronRightmostPos = self.findResizeScope()
        dY = self.sceneBoundingRect().y() - boundingRect.y()
        dX = self.sceneBoundingRect().x() - boundingRect.x()
        if self.handleSelected == NNBContainableLayer.Handle.handleTopMiddle or \
                self.handleSelected == NNBContainableLayer.Handle.handleTopLeft or \
                self.handleSelected == NNBContainableLayer.Handle.handleTopRight:
            toY = self.mousePressRect.top() + mousePos.y() - self.mousePressPos.y()
            if boundingRect.bottom() - toY < LAYER_MIN_HEIGHT:
                toY = boundingRect.bottom() - LAYER_MIN_HEIGHT
            if toY + dY > neuronHighestPos:
                toY = neuronHighestPos - dY
            rect.setTop(toY + offset)
        elif self.handleSelected == NNBContainableLayer.Handle.handleBottomMiddle or \
                self.handleSelected == NNBContainableLayer.Handle.handleBottomLeft or \
                self.handleSelected == NNBContainableLayer.Handle.handleBottomRight:
            toY = self.mousePressRect.bottom() + mousePos.y() - self.mousePressPos.y()
            if toY - boundingRect.top() < LAYER_MIN_HEIGHT:
                toY = boundingRect.top() + LAYER_MIN_HEIGHT
            if toY + dY < neuronLowestPos:
                toY = neuronLowestPos - dY
            rect.setBottom(toY - offset)

        if self.handleSelected == NNBContainableLayer.Handle.handleMiddleLeft or \
                self.handleSelected == NNBContainableLayer.Handle.handleBottomLeft or \
                self.handleSelected == NNBContainableLayer.Handle.handleTopLeft:
            toX = self.mousePressRect.left() + mousePos.x() - self.mousePressPos.x()
            if boundingRect.right() - toX < LAYER_MIN_WIDTH:
                toX = boundingRect.right() - LAYER_MIN_WIDTH
            if toX + dX > neuronLeftmostPos:
                toX = neuronLeftmostPos - dX
            rect.setLeft(toX + offset)
        elif self.handleSelected == NNBContainableLayer.Handle.handleMiddleRight or \
                self.handleSelected == NNBContainableLayer.Handle.handleBottomRight or \
                self.handleSelected == NNBContainableLayer.Handle.handleTopRight:
            toX = self.mousePressRect.right() + mousePos.x() - self.mousePressPos.x()
            if toX - boundingRect.left() < LAYER_MIN_WIDTH:
                toX = boundingRect.left() + LAYER_MIN_WIDTH
            if toX + dX < neuronRightmostPos:
                toX = neuronRightmostPos - dX
            rect.setRight(toX - offset)

        self.setRect(rect)
        self.updateHandlesPos()
        self.handleItemChanged()

    def shape(self):
        path = QPainterPath()
        path.addRect(self.rect())
        if self.state == NNBContainableLayer.State.ShowingHandles or self.state == NNBContainableLayer.State.Resizing:
            for handle, rect in self.handles.items():
                if self.state == NNBContainableLayer.State.ShowingHandles or handle == self.handleSelected:
                    path.addEllipse(rect)
        return path

    def paint(self, painter, option, widget=None):
        if self.isSelected() or self.hoveredOnConnectMode:
            painter.setBrush(NNB_FOCUS_BRUSH)
            painter.setPen(NNB_FOCUS_PEN)
            painter.drawRoundedRect(self.rect(), LAYER_CORNER_RADIUS, LAYER_CORNER_RADIUS)

        # draw body part
        painter.setBrush(LAYER_BODY_COLOR)
        painter.setPen(NNB_PEN)
        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)

        path.addRoundedRect(self.rect().x(), self.rect().y() + LAYER_HEADER_HEIGHT,
                            self.rect().width(), self.rect().height() - LAYER_HEADER_HEIGHT,
                            LAYER_CORNER_RADIUS, LAYER_CORNER_RADIUS)
        path.addRect(QRectF(self.rect().x(), self.rect().y() + LAYER_HEADER_HEIGHT, 10, 10))
        path.addRect(QRectF(self.rect().right() - 10, self.rect().y() + LAYER_HEADER_HEIGHT, 10, 10))
        painter.drawPath(path.simplified())

        # draw the header with a title
        painter.setBrush(QColor(255, 255, 255, 128))
        painter.setPen(QColor(0, 0, 0, 255))
        path = QPainterPath()
        path.setFillRule(Qt.WindingFill)
        path.addRoundedRect(self.rect().x(), self.rect().y(),
                            self.rect().width(), LAYER_HEADER_HEIGHT,
                            LAYER_CORNER_RADIUS, LAYER_CORNER_RADIUS)
        path.addRect(QRectF(self.rect().x(), self.rect().y() + LAYER_HEADER_HEIGHT - 10, 10, 10))
        path.addRect(QRectF(self.rect().right() - 10, self.rect().y() + LAYER_HEADER_HEIGHT - 10, 10, 10))
        painter.drawPath(path.simplified())

        font = QFont()
        font.setPointSize(8)
        font.setBold(True)
        painter.setFont(font)
        fontMetrics = QFontMetricsF(font)
        text = self.headerTitle
        rectMidX = self.rect().x() + self.rect().width() / 2
        rectMidY = self.rect().y() + LAYER_HEADER_HEIGHT / 2
        while True:
            fontWidth = fontMetrics.width(text)
            if self.rect().width() >= fontWidth:
                break
            text = text[:-1]
        fontHeight = fontMetrics.height()
        painter.drawText(int(rectMidX - fontWidth / 2),
                         int(rectMidY + fontHeight / 3), text)
        painter.drawLine(int(self.rect().x()), int(self.rect().y() + LAYER_HEADER_HEIGHT),
                         int(self.rect().right()), int(self.rect().y() + LAYER_HEADER_HEIGHT))
        painter.drawLine(int(self.rect().x()), int(self.rect().y() + LAYER_HEADER_HEIGHT - 2),
                         int(self.rect().right()), int(self.rect().y() + LAYER_HEADER_HEIGHT - 2))

        # Draw Handles
        if self.state == NNBContainableLayer.State.ShowingHandles or \
                self.state == NNBContainableLayer.State.Resizing:
            painter.setBrush(QBrush(Qt.white))
            painter.setPen(QPen(QColor(0, 0, 0, 255), 1.0, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            for handle, rect in self.handles.items():
                if self.state == NNBContainableLayer.State.ShowingHandles or handle == self.handleSelected:
                    painter.drawEllipse(rect)


class NNB1DLayer(NNBContainableLayer):
    def __init__(self, name, x, y):
        NNBContainableLayer.__init__(self, name, x, y)

    def findResizeScope(self):
        neuronHighestPos, neuronLowestPos, neuronLeftmostPos, neuronRightmostPos = super().findResizeScope()
        for neuron in self.neurons:
            neuronBR = neuron.sceneBoundingRect()
            if neuronBR.y() - 5 < neuronHighestPos:
                neuronHighestPos = neuronBR.y() - LAYER_HEADER_HEIGHT - 5
            if neuronBR.y() + 5 + NEURON_1D_DIAMETER > neuronLowestPos:
                neuronLowestPos = neuronBR.y() + NEURON_1D_DIAMETER + 5
            if neuronBR.x() - 5 < neuronLeftmostPos:
                neuronLeftmostPos = neuronBR.x() - 5
            if neuronBR.x() + NEURON_1D_DIAMETER + 5 > neuronRightmostPos:
                neuronRightmostPos = neuronBR.x() + NEURON_1D_DIAMETER + 5
        return neuronHighestPos, neuronLowestPos, neuronLeftmostPos, neuronRightmostPos


class NNB1DAffineLayer(_NNB1DAffineLayer, NNB1DLayer):
    def __init__(self, name, x, y):
        _NNB1DAffineLayer.__init__(self, name)
        NNB1DLayer.__init__(self, name, x, y)

    def createForm(self):
        return NNB1DAffineLayerForm(self, self.scene().activeWindow())


class NNB1DStackedAffineLayer(_NNB1DStackedLayer, NNB1DLayer):
    def __init__(self, name, x, y, numNeurons=-1):
        _NNB1DStackedLayer.__init__(self, name, numNeurons)
        NNB1DLayer.__init__(self, name, x, y)
        self.neuronHeight = 0
        self.neuronStartX = 0
        self.neuronStartY = 0
        self.neuronLayouts = None
        self.skipDotLayouts = None
        self.findNeuronLayout()

    def createForm(self):
        return NNB1DAffineLayerForm(self, self.scene().activeWindow())

    def changeNumNeurons(self, numNeurons):
        if numNeurons == self.numNeurons:
            return
        self.numNeurons = numNeurons
        self.findNeuronLayout()
        for connection in self.neurons[0].connectionsFrom.values():
            connection.updateConnectionPos()
            if isinstance(connection, _NNBTrainableConnection):
                connection.initializeWeight()
        for connection in self.neurons[0].connectionsTo.values():
            connection.updateConnectionPos()
            if isinstance(connection, _NNBTrainableConnection):
                connection.initializeWeight()
        self.update()

    def findNeuronLayout(self):
        neuronLayouts = []
        skipDotLayouts = []
        rect = self.rect()
        n = self.numNeurons
        if n == -1:
            n = 10000
        maxNumNeurons = int((rect.height() - LAYER_HEADER_HEIGHT - STACKED_AFF_1D_LAYER_SPACE) /
                            (STACKED_AFF_1D_LAYER_SPACE + NEURON_1D_DIAMETER))
        if n > maxNumNeurons:
            numNeuronsExceeded = True
            n = maxNumNeurons
        else:
            numNeuronsExceeded = False

        s = (rect.height() - LAYER_HEADER_HEIGHT - n * NEURON_1D_DIAMETER) / (n + 1)
        dotS = 0
        if numNeuronsExceeded:
            dotS = (2 * s + NEURON_1D_DIAMETER - 3 * STACKED_AFF_1D_SKIP_DOT_SIZE) / 4
        x = rect.x() + (rect.width() - NEURON_1D_DIAMETER) / 2
        y = rect.y() + LAYER_HEADER_HEIGHT + s
        yBase = y
        self.neuronStartX = x
        self.neuronStartY = y

        if numNeuronsExceeded:
            for i in range(n):
                if i == n - 3:
                    xDot = x + NEURON_1D_RADIUS - STACKED_AFF_1D_SKIP_DOT_SIZE / 2
                    yDot = y + dotS
                    for j in range(3):
                        skipDotLayouts.append((xDot, yDot))
                        yDot += dotS
                else:
                    if i != 0:
                        y += s
                    neuronLayouts.append((x, y))
                y += NEURON_1D_DIAMETER
        else:
            for i in range(n):
                neuronLayouts.append((x, y))
                y += (NEURON_1D_DIAMETER + s)
        self.neuronLayouts = neuronLayouts
        self.skipDotLayouts = skipDotLayouts
        self.neuronHeight = y - yBase

    def interactiveResize(self, mousePos):
        super().interactiveResize(mousePos)
        self.findNeuronLayout()
        if self.nextLayer:
            stackedNeuron = self.neurons[0]
            for connectionTo in stackedNeuron.connectionsTo.values():
                connectionTo.updateConnectionPos()
        if self.prevLayer:
            stackedNeuron = self.neurons[0]
            for connectionFrom in stackedNeuron.connectionsFrom.values():
                connectionFrom.updateConnectionPos()


class NNB2DConvLayer(_NNB2DConvLayer, NNBContainableLayer):
    def __init__(self, name, x, y):
        _NNB2DConvLayer.__init__(self, name)
        NNBContainableLayer.__init__(self, name, x, y)

    def createForm(self):
        return NNB1DAffineLayerForm(self, self.scene().activeWindow())
        # return NNB2DConvLayerForm(self)

    def findResizeScope(self):
        neuronHighestPos, neuronLowestPos, neuronLeftmostPos, neuronRightmostPos = super().findResizeScope()
        for neuron in self.neurons:
            neuronBR = neuron.sceneBoundingRect()
            if neuronBR.y() < neuronHighestPos:
                neuronHighestPos = neuronBR.y() - NEURON_2D_SIZE - 5
            if neuronBR.y() > neuronLowestPos:
                neuronLowestPos = neuronBR.y() + NEURON_2D_SIZE + 5
            if neuronBR.x() < neuronLeftmostPos:
                neuronLeftmostPos = neuronBR.x() - 5
            if neuronBR.x() > neuronRightmostPos:
                neuronRightmostPos = neuronBR.x() + NEURON_2D_SIZE + 5
        return neuronHighestPos, neuronLowestPos, neuronLeftmostPos, neuronRightmostPos

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            self.handleItemChanged()
        return super().itemChange(change, value)


class NNB2DPoolingLayer(_NNB2DPoolingLayer, NNBContainableLayer):
    def __init__(self, name, x, y):
        _NNB2DPoolingLayer.__init__(self, name)
        NNBContainableLayer.__init__(self, name, x, y)

    def createForm(self):
        return NNB1DAffineLayerForm(self, self.scene().activeWindow())

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            self.handleItemChanged()
        return super().itemChange(change, value)


class NNB2DFlattenLayer(_NNB2DFlattenLayer, NNBContainableLayer):
    def __init__(self, name, x, y):
        _NNB2DFlattenLayer.__init__(self, name)
        NNBContainableLayer.__init__(self, name, x, y)

    def createForm(self):
        return NNB1DAffineLayerForm(self, self.scene().activeWindow())

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            self.handleItemChanged()
        return super().itemChange(change, value)
