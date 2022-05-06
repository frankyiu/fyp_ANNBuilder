from PyQt5.QtGui import QPainterPath, QPainterPathStroker
from PyQt5.QtCore import QPointF
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsLineItem, QGraphicsPathItem
from .base import _NNB1DLinearConnection, _NNB1DStackedLinConnection, \
    _NNB2DConvConnection, _NNBLFBConnection, _NNBRegConnection, \
    _NNB2DFlattenConnection, _NNB2DPoolingConnection, _NNB1DStackedNeuron, _NNB1DBiasNeuron, \
    _NNB2DNeuron, _NNBRegularizer
from .form import NNB1DLinearConnectionForm
from .config import *


def findBlockLayout(block):
    blockLayouts = []
    if isinstance(block, _NNB1DStackedNeuron):
        layerSBR = block.layer.sceneBoundingRect()
        layerBR = block.layer.boundingRect()
        dx = layerSBR.x() - layerBR.x()
        dy = layerSBR.y() - layerBR.y()
        for neuronLayout in block.layer.neuronLayouts:
            blockLayouts.append((neuronLayout[0] + dx, neuronLayout[1] + dy))
    else:
        blockSBR = block.sceneBoundingRect()
        blockLayouts = [(blockSBR.x(), blockSBR.y())]
    return blockLayouts


def find1DLinLineGeometry(xFrom, yFrom, xTo, yTo, hasSYN=True):
    x1 = xFrom + NEURON_1D_DIAMETER + NEURON_1D_SYN_LENGTH if hasSYN else xFrom + NEURON_1D_DIAMETER
    y1 = yFrom + NEURON_1D_RADIUS
    x2 = xTo
    y2 = yTo + NEURON_1D_RADIUS
    return x1, y1, x2, y2


class NNB1DLinearConnection(_NNB1DLinearConnection, QGraphicsLineItem):
    def __init__(self, name, blockFrom, blockTo):
        _NNB1DLinearConnection.__init__(self, name, blockFrom, blockTo)
        QGraphicsLineItem.__init__(self)
        # note that since a connection line can only be created on connect mode, so set it to be unselectable
        self.setFlags(QGraphicsItem.ItemIsFocusable)
        self.fromPts = []
        self.toPts = []

    def createForm(self):
        return NNB1DLinearConnectionForm(self, self.scene().activeWindow())

    def updateConnectionPos(self):
        rectFrom = self.blockFrom.sceneBoundingRect()
        rectTo = self.blockTo.sceneBoundingRect()
        x1, y1, x2, y2 = find1DLinLineGeometry(rectFrom.x(), rectFrom.y(), rectTo.x(), rectTo.y())
        self.setLine(x1, y1, x2, y2)
        self.fromPts = [(x1, y1)]
        self.toPts = [(x2, y2)]

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


class NNB1DStackedLinConnection(_NNB1DStackedLinConnection, QGraphicsPathItem):
    def __init__(self, name, blockFrom, blockTo):
        _NNB2DConvConnection.__init__(self, name, blockFrom, blockTo)
        QGraphicsPathItem.__init__(self)
        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable)
        self.fromPts = []
        self.toPts = []

    def createForm(self):
        return NNB1DLinearConnectionForm(self, self.scene().activeWindow())

    def updateConnectionPos(self):
        neuronFromLayouts = findBlockLayout(self.blockFrom)
        neuronToLayouts = findBlockLayout(self.blockTo)
        self.fromPts = []
        self.toPts = []
        for neuronFromLayout in neuronFromLayouts:
            for i, neuronToLayout in enumerate(neuronToLayouts):
                if i == len(neuronToLayouts) - 1:
                    if isinstance(self.blockTo, _NNB1DStackedNeuron) and self.blockTo.layer.hasBias:
                        continue
                    elif isinstance(self.blockTo, _NNB1DBiasNeuron):
                        continue
                x1, y1, x2, y2 = find1DLinLineGeometry(*neuronFromLayout, *neuronToLayout)
                self.fromPts.append((x1, y1))
                self.toPts.append((x2, y2))
        self.setPath(self.makeLines())
        self.update()

    def makeLines(self):
        path = QPainterPath()
        for fromPt, toPt in zip(self.fromPts, self.toPts):
            path.moveTo(*fromPt)
            path.lineTo(*toPt)
        return path

    def shape(self):
        path = self.makeLines()
        return QPainterPathStroker().createStroke(path).simplified()

    def paint(self, painter, option, widget=None):
        path = self.makeLines()
        if self.isSelected():
            painter.setBrush(NNB_FOCUS_BRUSH)
            painter.setPen(NNB_FOCUS_PEN)
            painter.drawPath(path)
        painter.setBrush(NNB_BRUSH)
        painter.setPen(NNB_PEN)
        painter.drawPath(path)


class NNB2DConvConnection(_NNB2DConvConnection, QGraphicsPathItem):
    def __init__(self, name, neuron2DFrom, neuron2DTo):
        _NNB2DConvConnection.__init__(self, name, neuron2DFrom, neuron2DTo)
        QGraphicsPathItem.__init__(self)
        self.setFlags(QGraphicsItem.ItemIsSelectable | QGraphicsItem.ItemIsFocusable)
        self.lkr, self.lkt, self.lkb = 0, 0, 0
        self.rmx, self.rmy = 0, 0

    def createForm(self):
        return NNB1DLinearConnectionForm(self, self.scene().activeWindow())

    def updateConnectionPos(self):
        kernelSize = self.blockFrom.kernelSize()
        leftSceneBRect = self.blockFrom.sceneBoundingRect()
        rightSceneBRect = self.blockTo.sceneBoundingRect()

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
        return QPainterPathStroker().createStroke(path).simplified()

    def paint(self, painter, option, widget=None):
        path = self.makeLines()
        if self.isSelected():
            painter.setBrush(QColor(128, 128, 128, 128))
            path.lineTo(self.lkr, self.lkt)
            painter.drawPath(path)
        painter.setBrush(NNB_BRUSH)
        painter.drawPath(path)


class NNBRegConnection(_NNBRegConnection, QGraphicsPathItem):
    def __init__(self, name, block, regularizer):
        '''
        :param name:
        :param block: component1
        :param regularizer: component2
        '''
        _NNBRegConnection.__init__(self, name, block, regularizer)
        QGraphicsPathItem.__init__(self)
        # note that since a connection line can only be created on connect mode, so set it to be unselectable
        self.setFlags(QGraphicsItem.ItemIsFocusable | QGraphicsItem.ItemIsFocusable)

    def createForm(self):
        return NNB1DLinearConnectionForm(self, self.scene().activeWindow())
        # return NNBRegConnectionForm(self, window)

    def paint(self, painter, option, widget=None):
        if self.isSelected():
            painter.setBrush(NNB_FOCUS_BRUSH)
            painter.setPen(NNB_FOCUS_PEN)
            painter.drawPath(self.path)
        painter.setBrush(QBrush(QColor(255, 255, 255, 0)))
        painter.setPen(NNB_PEN)
        painter.drawPath(self.path)

    def updateConnectionPos(self):
        blockFromSBF = self.blockFrom.sceneBoundingRect()
        blockToSBF = self.blockTo.sceneBoundingRect()
        if isinstance(self.blockFrom, _NNBRegularizer):
            x1 = blockFromSBF.x() + blockFromSBF.width()
            y1 = blockFromSBF.y() + blockFromSBF.height() / 2
            x2 = blockToSBF.x() + blockToSBF.width() / 2
            y2 = blockToSBF.y() + blockToSBF.height()
            c1, c2 = x2, y1
            if blockToSBF.x() + blockToSBF.width() < x1:
                x1 = blockFromSBF.x()
            if y1 < blockToSBF.y() + blockToSBF.height() / 2:
                y2 = blockToSBF.y()
        else:
            x1 = blockFromSBF.x() + blockFromSBF.width() / 2
            y1 = blockFromSBF.y() + blockFromSBF.height() - (LAYER_HANDLE_SIZE + LAYER_HANDLE_SPACE)
            x2 = blockToSBF.x()
            y2 = blockToSBF.y() + blockToSBF.height() / 2
            c1, c2 = x1, y2
            if blockToSBF.x() + blockToSBF.width() < x1:
                x2 = blockToSBF.x() + blockToSBF.width()
            if y2 < blockFromSBF.y() + blockFromSBF.height() / 2:
                y1 = blockFromSBF.y() + (LAYER_HANDLE_SIZE + LAYER_HANDLE_SPACE)
            if blockFromSBF.y() < y2 < blockFromSBF.bottom():
                c1 = x2
                c2 = y1

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


class NNBLFBConnection(_NNBLFBConnection, QGraphicsPathItem):
    def __init__(self, name, blockFrom, blockTo):
        _NNBLFBConnection.__init__(self, name, blockFrom, blockTo)
        QGraphicsPathItem.__init__(self)
        # note that since a connection line can only be created on connect mode, so set it to be unselectable
        self.fromPts = []
        self.toPts = []
        self.setFlags(QGraphicsItem.ItemIsFocusable)

    def createForm(self):
        return NNB1DLinearConnectionForm(self, self.scene().activeWindow())
        # return NNBLFBConnectionForm(self, window)

    def updateConnectionPos(self):
        neuronFromLayouts = findBlockLayout(self.blockFrom)
        lbfPos = findBlockLayout(self.blockTo)[0]
        self.fromPts = []
        self.toPts = []
        for neuronFromLayout in neuronFromLayouts:
            x1, y1, x2, y2 = find1DLinLineGeometry(*neuronFromLayout, *lbfPos, hasSYN=False)
            self.fromPts.append((x1, y1))
            self.toPts.append((x2, y2))
        self.setPath(self.makeLines())
        self.update()

    def makeLines(self):
        path = QPainterPath()
        for fromPt, toPt in zip(self.fromPts, self.toPts):
            path.moveTo(*fromPt)
            path.lineTo(*toPt)
        return path

    def shape(self):
        path = self.makeLines()
        return QPainterPathStroker().createStroke(path).simplified()

    def paint(self, painter, option, widget=None):
        path = self.makeLines()
        if self.isSelected():
            painter.setBrush(NNB_FOCUS_BRUSH)
            painter.setPen(NNB_FOCUS_PEN)
            painter.drawPath(path)
        painter.setBrush(NNB_BRUSH)
        painter.setPen(NNB_PEN)
        painter.drawPath(path)

    def mouseDoubleClickEvent(self, event):
        if self.scene().sceneMode != SceneMode.ConnectMode:
            self.handleMouseDoubleClickEvent()


class NNB2DFlattenConnection(_NNB2DFlattenConnection, QGraphicsPathItem):
    def __init__(self, name, blockFrom, blockTo):
        _NNB2DFlattenConnection.__init__(self, name, blockFrom, blockTo)
        QGraphicsLineItem.__init__(self)
        self.setFlags(QGraphicsItem.ItemIsFocusable)
        self.fromPts = []
        self.toPts = []
        self.updateConnectionPos()

    def createForm(self):
        return NNB1DLinearConnectionForm(self, self.scene().activeWindow())

    def updateConnectionPos(self):
        self.fromPts = []
        self.toPts = []
        if isinstance(self.blockFrom, _NNB2DNeuron):
            blockFromSBR = self.blockFrom.sceneBoundingRect()
            blockToSBR = self.blockTo.sceneBoundingRect()
            self.fromPts.append((blockFromSBR.x() + NEURON_2D_SIZE, blockFromSBR.y()))
            self.fromPts.append((blockFromSBR.x() + NEURON_2D_SIZE, blockFromSBR.y() + NEURON_2D_SIZE))
            self.toPts.append((blockToSBR.x() + blockToSBR.width() / 2,
                               blockToSBR.y() + blockToSBR.height() / 2))
        else:
            blockFromSBR = self.blockFrom.sceneBoundingRect()
            layerToSBR = self.blockTo.layer.sceneBoundingRect()
            layerToBR = self.blockTo.layer.boundingRect()
            dx = layerToSBR.x() - layerToBR.x()
            dy = layerToSBR.y() - layerToBR.y()
            self.fromPts.append((blockFromSBR.x() + blockFromSBR.width() / 2,
                                 blockFromSBR.y() + blockFromSBR.height() / 2))
            for neuronLayout in self.blockTo.layer.neuronLayouts:
                self.toPts.append((neuronLayout[0] + dx, neuronLayout[1] + dy + NEURON_1D_RADIUS))

        self.setPath(self.makeLines())
        self.update()

    def makeLines(self):
        path = QPainterPath()
        for fromPt in self.fromPts:
            for toPt in self.toPts:
                path.moveTo(*fromPt)
                path.lineTo(*toPt)
        return path

    def shape(self):
        path = self.makeLines()
        return QPainterPathStroker().createStroke(path).simplified()

    def paint(self, painter, option, widget=None):
        path = self.makeLines()
        if self.isSelected():
            painter.setBrush(NNB_FOCUS_BRUSH)
            painter.setPen(NNB_FOCUS_PEN)
            painter.drawPath(path)
        painter.setBrush(NNB_BRUSH)
        painter.setPen(NNB_PEN)
        painter.drawPath(path)


class NNB2DPoolingConnection(_NNB2DPoolingConnection, QGraphicsLineItem):
    def __init__(self, name, blockLeft, blockRight):
        _NNB2DPoolingConnection.__init__(self, name, blockLeft, blockRight)
        QGraphicsLineItem.__init__(self)
        # note that since a connection line can only be created on connect mode, so set it to be unselectable
        self.setFlags(QGraphicsItem.ItemIsFocusable)

    def createForm(self):
        return NNB1DLinearConnectionForm(self, self.scene().activeWindow())