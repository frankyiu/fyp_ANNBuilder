# TEMP
from PyQt5.QtGui import QPainter, QDrag, QPixmap, QPolygonF
from PyQt5.QtCore import QMimeData, QPoint, QPointF
from PyQt5.QtWidgets import QApplication, QGraphicsRectItem, QGraphicsEllipseItem, QGraphicsPolygonItem
from .config import *


class NNBIcon:
    def __init__(self):
        self.st_pos = None
        self.minedataText = ""

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.st_pos = event.pos()

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        if (event.pos() - self.st_pos).manhattanLength() < QApplication.startDragDistance():
            return
        drag = QDrag(event.widget())
        minedata = QMimeData()
        minedata.setText(self.minedataText)
        drag.setMimeData(minedata)

        drag.setPixmap(self.drawPixmap())
        drag.setHotSpot(QPoint(ICON_OFFSET_X, ICON_OFFSET_Y))
        Qt.DropAction = drag.exec_(Qt.CopyAction | Qt.MoveAction)

    def drawPixmap(self):
        return QPixmap()


class NNB1DNeuronIcon(NNBIcon, QGraphicsEllipseItem):
    def __init__(self, x, y):
        NNBIcon.__init__(self)
        QGraphicsEllipseItem.__init__(self, x, y, NEURON_1D_ICON_SIZE, NEURON_1D_ICON_SIZE)
        self.minedataText = "neuron_1D"

    def drawPixmap(self):
        pixmap = QPixmap(NEURON_1D_DIAMETER + 2, NEURON_1D_DIAMETER + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.drawEllipse(0, 0, NEURON_1D_DIAMETER, NEURON_1D_DIAMETER)
        painter.end()
        return pixmap


class NNB1DBiasNeuronIcon(NNBIcon, QGraphicsEllipseItem):
    def __init__(self, x, y):
        NNBIcon.__init__(self)
        QGraphicsEllipseItem.__init__(self, x, y, NEURON_1D_ICON_SIZE, NEURON_1D_ICON_SIZE)
        self.minedataText = "neuron_bias_1D"

    def drawPixmap(self):
        pixmap = QPixmap(NEURON_1D_DIAMETER + 2, NEURON_1D_DIAMETER + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.drawEllipse(0, 0, NEURON_1D_DIAMETER, NEURON_1D_DIAMETER)
        painter.end()
        return pixmap


class NNB2DNeuronIcon(NNBIcon, QGraphicsRectItem):
    def __init__(self, x, y):
        NNBIcon.__init__(self)
        QGraphicsRectItem.__init__(self, x, y, NEURON_2D_ICON_SIZE, NEURON_2D_ICON_SIZE)
        self.minedataText = "neuron_2D"

    def drawPixmap(self):
        pixmap = QPixmap(NEURON_2D_SIZE + 2, NEURON_2D_SIZE + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.drawRect(0, 0, NEURON_2D_SIZE, NEURON_2D_SIZE)
        painter.end()
        return pixmap


class NNB2DBiasNeuronIcon(NNBIcon, QGraphicsRectItem):
    def __init__(self, x, y):
        NNBIcon.__init__(self)
        QGraphicsRectItem.__init__(self, x, y, NEURON_2D_ICON_SIZE, NEURON_2D_ICON_SIZE)
        self.minedataText = "neuron_bias_2D"

    def drawPixmap(self):
        pixmap = QPixmap(NEURON_2D_SIZE + 2, NEURON_2D_SIZE + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.drawRect(0, 0, NEURON_2D_SIZE, NEURON_2D_SIZE)
        painter.end()
        return pixmap


class NNBAffineLayerIcon(NNBIcon, QGraphicsRectItem):
    def __init__(self, x, y):
        NNBIcon.__init__(self)
        QGraphicsRectItem.__init__(self, x, y, AFFINE_LAYER_ICON_WIDTH, AFFINE_LAYER_ICON_HEIGHT)
        self.minedataText = "affine_layer"

    def drawPixmap(self):
        pixmap = QPixmap(LAYER_WIDTH + 2, LAYER_HEIGHT + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.setBrush(LAYER_BODY_COLOR)
        painter.drawRect(0, 0, LAYER_WIDTH, LAYER_HEIGHT)
        painter.end()
        return pixmap


class NNBConvLayerIcon(NNBIcon, QGraphicsRectItem):
    def __init__(self, x, y):
        NNBIcon.__init__(self)
        QGraphicsRectItem.__init__(self, x, y, CONV_LAYER_ICON_WIDTH, CONV_LAYER_ICON_HEIGHT)
        self.minedataText = "conv_layer"

    def drawPixmap(self):
        pixmap = QPixmap(LAYER_WIDTH + 2, LAYER_HEIGHT + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.setBrush(LAYER_BODY_COLOR)
        painter.drawRect(0, 0, LAYER_WIDTH, LAYER_HEIGHT)
        painter.end()
        return pixmap


class NNBLostFuncBlock(NNBIcon, QGraphicsRectItem):
    def __init__(self, x, y):
        NNBIcon.__init__(self)
        QGraphicsRectItem.__init__(self, x, y, LFB_ICON_WIDTH, LFB_ICON_HEIGHT)
        self.minedataText = "loss_func_block"

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


class NNBRegularizerIcon(NNBIcon, QGraphicsPolygonItem):
    def __init__(self, x, y):
        NNBIcon.__init__(self)
        QGraphicsPolygonItem.__init__(self)
        p1 = QPointF(x + REGULARIZER_ICON_WIDTH / 2, y)
        p2 = QPointF(x + REGULARIZER_ICON_WIDTH, y + REGULARIZER_ICON_HEIGHT / 2)
        p3 = QPointF(x + REGULARIZER_ICON_WIDTH / 2, y + REGULARIZER_ICON_HEIGHT)
        p4 = QPointF(x, y + REGULARIZER_ICON_HEIGHT / 2)
        self.romb = QPolygonF([p1, p2, p3, p4])
        self.setPolygon(self.romb)
        self.minedataText = "regularizer"

    def paint(self, painter, option, widget=None):
        painter.setPen(NNB_PEN)
        painter.setBrush(QBrush(REGULARIZER_BODY_COLOR))
        painter.drawPolygon(self.romb)

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


class NNBStacked1DAffLayerIcon(NNBIcon, QGraphicsRectItem):
    def __init__(self, x, y):
        NNBIcon.__init__(self)
        QGraphicsRectItem.__init__(self, x, y, CONV_LAYER_ICON_WIDTH, CONV_LAYER_ICON_HEIGHT)
        self.minedataText = "stacked_affine_layer"

    def drawPixmap(self):
        pixmap = QPixmap(LAYER_WIDTH + 2, LAYER_HEIGHT + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.setBrush(LAYER_BODY_COLOR)
        painter.drawRect(0, 0, LAYER_WIDTH, LAYER_HEIGHT)
        painter.end()
        return pixmap


class NNBPoolingLayerIcon(NNBIcon, QGraphicsRectItem):
    def __init__(self, x, y):
        NNBIcon.__init__(self)
        QGraphicsRectItem.__init__(self, x, y, CONV_LAYER_ICON_WIDTH, CONV_LAYER_ICON_HEIGHT)
        self.minedataText = "pooling_layer"

    def drawPixmap(self):
        pixmap = QPixmap(LAYER_WIDTH + 2, LAYER_HEIGHT + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.setBrush(LAYER_BODY_COLOR)
        painter.drawRect(0, 0, LAYER_WIDTH, LAYER_HEIGHT)
        painter.end()
        return pixmap


class NNBFlattenLayerIcon(NNBIcon, QGraphicsRectItem):
    def __init__(self, x, y):
        NNBIcon.__init__(self)
        QGraphicsRectItem.__init__(self, x, y, CONV_LAYER_ICON_WIDTH, CONV_LAYER_ICON_HEIGHT)
        self.minedataText = "flatten_layer"

    def drawPixmap(self):
        pixmap = QPixmap(LAYER_WIDTH + 2, LAYER_HEIGHT + 2)
        pixmap.fill(WHITE_TRANSPARENT)
        painter = QPainter(pixmap)
        painter.setBrush(LAYER_BODY_COLOR)
        painter.drawRect(0, 0, LAYER_WIDTH, LAYER_HEIGHT)
        painter.end()
        return pixmap
