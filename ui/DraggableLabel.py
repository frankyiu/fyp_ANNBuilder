import sys

from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QPen, QPolygonF
from PyQt5.QtCore import QMimeData, Qt, QPoint, QPointF
from nnbuilder.config import *


class DraggableLabel(QLabel):

    def __init__(self, parent):
        super().__init__(parent)
        self.mimedatatext = ''

    def setObjectName(self, name):
        super().setObjectName(name)
        self.mimedatatext = name

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.st_pos = event.pos()


    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.st_pos).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(self)
        mimedata = QMimeData()
        mimedata.setText(self.mimedatatext)
        drag.setMimeData(mimedata)
        drag.setPixmap(self.drawPixmap())
        drag.setHotSpot(QPoint(ICON_OFFSET_X, ICON_OFFSET_Y))
        Qt.DropAction = drag.exec_(Qt.CopyAction | Qt.MoveAction)

    def drawPixmap(self):
        return self.grab()



class NNB1DNeuronIcon(DraggableLabel):
    def __init__(self,parent):
        DraggableLabel.__init__(self,parent)

        self.mimedataText = "neuron_1D"

    def drawPixmap(self):
        pixmap = QPixmap(NEURON_1D_DIAMETER + 2, NEURON_1D_DIAMETER + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.drawEllipse(0, 0, NEURON_1D_DIAMETER, NEURON_1D_DIAMETER)
        painter.end()
        return pixmap


class NNB1DBiasNeuronIcon(DraggableLabel):
    def __init__(self,parent):
        DraggableLabel.__init__(self,parent)
        self.mimedataText = "neuron_bias_1D"

    def drawPixmap(self):
        pixmap = QPixmap(NEURON_1D_DIAMETER + 2, NEURON_1D_DIAMETER + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.drawEllipse(0, 0, NEURON_1D_DIAMETER, NEURON_1D_DIAMETER)
        painter.end()
        return pixmap


class NNB2DNeuronIcon(DraggableLabel):
    def __init__(self,parent):
        DraggableLabel.__init__(self,parent)
        self.mimedataText = "neuron_2D"

    def drawPixmap(self):
        pixmap = QPixmap(NEURON_2D_SIZE + 2, NEURON_2D_SIZE + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.drawRect(0, 0, NEURON_2D_SIZE, NEURON_2D_SIZE)
        painter.end()
        return pixmap


class NNB2DBiasNeuronIcon(DraggableLabel):
    def __init__(self,parent):
        DraggableLabel.__init__(self,parent)
        self.mimedataText = "neuron_bias_2D"

    def drawPixmap(self):
        pixmap = QPixmap(NEURON_2D_SIZE + 2, NEURON_2D_SIZE + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.drawRect(0, 0, NEURON_2D_SIZE, NEURON_2D_SIZE)
        painter.end()
        return pixmap


class NNBAffineLayerIcon(DraggableLabel):
    def __init__(self,parent):
        DraggableLabel.__init__(self,parent)
        self.mimedataText = "affine_layer"

    def drawPixmap(self):
        pixmap = QPixmap(LAYER_WIDTH + 2, LAYER_HEIGHT + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.setBrush(LAYER_BODY_COLOR)
        painter.drawRect(0, 0, LAYER_WIDTH, LAYER_HEIGHT)
        painter.end()
        return pixmap


class NNBConvLayerIcon(DraggableLabel):
    def __init__(self,parent):
        DraggableLabel.__init__(self,parent)
        self.mimedataText = "conv_layer"

    def drawPixmap(self):
        pixmap = QPixmap(LAYER_WIDTH + 2, LAYER_HEIGHT + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.setBrush(LAYER_BODY_COLOR)
        painter.drawRect(0, 0, LAYER_WIDTH, LAYER_HEIGHT)
        painter.end()
        return pixmap


class NNBLostFuncBlock(DraggableLabel):
    def __init__(self,parent):
        DraggableLabel.__init__(self,parent)
        self.mimedataText = "loss_func_block"

    def paint(self, painter, option, widget=None):
        painter.setPen(NNB_PEN)
        painter.setBrush(QBrush(LFB_BODY_COLOR))
        painter.drawRect(self.rect())

    def drawPixmap(self):
        pixmap = QPixmap(LFB_WIDTH + 2, LFB_HEIGHT + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.setBrush(LFB_BODY_COLOR)
        painter.drawRect(0, 0, LFB_WIDTH, LFB_HEIGHT)
        painter.end()
        return pixmap


class NNBRegularizerIcon(DraggableLabel):
    def __init__(self,parent):
        DraggableLabel.__init__(self,parent)
        self.mimedataText = "regularizer"


    def drawPixmap(self):
        pixmap = QPixmap(REGULARIZER_WIDTH, REGULARIZER_WIDTH)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.setBrush(REGULARIZER_BODY_COLOR)
        p1 = QPointF(REGULARIZER_WIDTH / 2, 0)
        p2 = QPointF(REGULARIZER_WIDTH, REGULARIZER_HEIGHT / 2)
        p3 = QPointF(REGULARIZER_WIDTH / 2, REGULARIZER_HEIGHT)
        p4 = QPointF(0, REGULARIZER_HEIGHT / 2)
        painter.drawPolygon(QPolygonF([p1, p2, p3, p4]))
        painter.end()
        return pixmap


class NNBStacked1DAffLayerIcon(DraggableLabel):
    def __init__(self,parent):
        DraggableLabel.__init__(self,parent)
        self.mimedataText = "stacked_affine_layer"

    def drawPixmap(self):
        pixmap = QPixmap(LAYER_WIDTH + 2, LAYER_HEIGHT + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.setBrush(LAYER_BODY_COLOR)
        painter.drawRect(0, 0, LAYER_WIDTH, LAYER_HEIGHT)
        painter.end()
        return pixmap


class NNBPoolingLayerIcon(DraggableLabel):
    def __init__(self,parent):
        DraggableLabel.__init__(self,parent)
        self.mimedataText = "pooling_layer"

    def drawPixmap(self):
        pixmap = QPixmap(LAYER_WIDTH + 2, LAYER_HEIGHT + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.setBrush(LAYER_BODY_COLOR)
        painter.drawRect(0, 0, LAYER_WIDTH, LAYER_HEIGHT)
        painter.end()
        return pixmap


class NNBFlattenLayerIcon(DraggableLabel):
    def __init__(self,parent):
        DraggableLabel.__init__(self,parent)
        self.mimedataText = "flatten_layer"

    def drawPixmap(self):
        pixmap = QPixmap(LAYER_WIDTH + 2, LAYER_HEIGHT + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.setBrush(LAYER_BODY_COLOR)
        painter.drawRect(0, 0, LAYER_WIDTH, LAYER_HEIGHT)
        painter.end()
        return pixmap
