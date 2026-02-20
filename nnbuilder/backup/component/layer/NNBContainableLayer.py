'''

- resize a qgraphicsitem with the mouse:
    https://stackoverflow.com/questions/34429632/resize-a-qgraphicsitem-with-the-mouse

'''

from PyQt5.QtGui import QPainter, QPainterPath, QFont, QFontMetricsF
from PyQt5.QtCore import QRectF
from PyQt5.QtWidgets import QApplication, QGraphicsItem, QGraphicsRectItem
from config import *
from NNBLayer import NNBLayer


class NNBContainableLayer(NNBLayer, QGraphicsRectItem):
    class Handle:
        handleTopLeft = 1
        handleTopMiddle = 2
        handleTopRight = 3
        handleMiddleLeft = 4
        handleMiddleRight = 5
        handleBottomLeft = 6
        handleBottomMiddle = 7
        handleBottomRight = 8

        handleSize = +8.0
        handleSpace = -4.0

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

    def __init__(self, name, x, y):
        NNBLayer.__init__(self, name)
        QGraphicsRectItem.__init__(self, x, y, LAYER_WIDTH, LAYER_HEIGHT)
        self.headerTitle = name
        self.headerBGColor = QColor(255, 255, 255, 128)
        self.bodyBGColor = QColor(200, 200, 200, 128)

        self.handles = {}
        self.handleSelected = None
        self.mousePressPos = None
        self.mousePressRect = None

        self.minWidth = NEURON_1D_DIAMETER + 10
        self.minHeight = LAYER_HEADER_HEIGHT + NEURON_1D_DIAMETER + 10

        self.state = NNBResizableLayer.State.Normal
        self.setFlags(QGraphicsItem.ItemIsMovable | QGraphicsItem.ItemIsSelectable |
                      QGraphicsItem.ItemSendsGeometryChanges | QGraphicsItem.ItemIsFocusable)

        ###
        self.neurons = []

        self.updateHandlesPos()

    def handleAt(self, point):
        for k, v, in self.handles.items():
            if v.contains(point):
                return k
        return None

    def mousePressEvent(self, event):
        if self.state == NNBResizableLayer.State.ShowingHandles:
            self.handleSelected = self.handleAt(event.pos())
            if self.handleSelected:
                self.mousePressRect = self.boundingRect()
        self.mousePressPos = event.pos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if self.state == NNBResizableLayer.State.Normal:
            if (self.mousePressPos - event.pos()).manhattanLength() >= QApplication.startDragDistance():
                self.state = NNBResizableLayer.State.Moving
        elif self.state == NNBResizableLayer.State.ShowingHandles:
            if self.handleSelected:
                self.state = NNBResizableLayer.State.Resizing
            else:
                self.state = NNBResizableLayer.State.Moving
        elif self.state == NNBResizableLayer.State.Resizing:
            self.interactiveResize(event.pos())
            return
        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.state == NNBResizableLayer.State.Normal:
            self.state = NNBResizableLayer.State.ShowingHandles
        elif self.state == NNBResizableLayer.State.ShowingHandles:
            self.state = NNBResizableLayer.State.Normal
        elif self.state == NNBResizableLayer.State.Moving or self.state == NNBResizableLayer.State.Resizing:
            self.state = NNBResizableLayer.State.Normal
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
            self.state = NNBResizableLayer.State.Normal
        return super().itemChange(change, value)

    def boundingRect(self):
        o = NNBResizableLayer.Handle.handleSize + NNBResizableLayer.Handle.handleSpace
        return self.rect().adjusted(-o, -o, o, o)

    def updateHandlesPos(self):
        s = NNBResizableLayer.Handle.handleSize
        b = self.boundingRect()
        self.handles[NNBResizableLayer.Handle.handleTopLeft] = QRectF(b.left(), b.top(), s, s)
        self.handles[NNBResizableLayer.Handle.handleTopMiddle] = QRectF(b.center().x() - s / 2, b.top(), s, s)
        self.handles[NNBResizableLayer.Handle.handleTopRight] = QRectF(b.right() - s, b.top(), s, s)
        self.handles[NNBResizableLayer.Handle.handleMiddleLeft] = QRectF(b.left(), b.center().y() - s / 2, s, s)
        self.handles[NNBResizableLayer.Handle.handleMiddleRight] = QRectF(b.right() - s, b.center().y() - s / 2, s, s)
        self.handles[NNBResizableLayer.Handle.handleBottomLeft] = QRectF(b.left(), b.bottom() - s, s, s)
        self.handles[NNBResizableLayer.Handle.handleBottomMiddle] = QRectF(b.center().x() - s / 2, b.bottom() - s, s, s)
        self.handles[NNBResizableLayer.Handle.handleBottomRight] = QRectF(b.right() - s, b.bottom() - s, s, s)

    def interactiveResize(self, mousePos):
        offset = NNBResizableLayer.Handle.handleSize + NNBResizableLayer.Handle.handleSpace
        boundingRect = self.boundingRect()
        rect = self.rect()
        self.prepareGeometryChange()

        if self.handleSelected == NNBResizableLayer.Handle.handleTopMiddle or \
                self.handleSelected == NNBResizableLayer.Handle.handleTopLeft or \
                self.handleSelected == NNBResizableLayer.Handle.handleTopRight:
            toY = self.mousePressRect.top() + mousePos.y() - self.mousePressPos.y()
            if boundingRect.bottom() - toY < self.minHeight:
                toY = boundingRect.bottom() - self.minHeight
            boundingRect.setTop(toY)
            rect.setTop(boundingRect.top() + offset)
        elif self.handleSelected == NNBResizableLayer.Handle.handleBottomMiddle or \
                self.handleSelected == NNBResizableLayer.Handle.handleBottomLeft or \
                self.handleSelected == NNBResizableLayer.Handle.handleBottomRight:
            toY = self.mousePressRect.bottom() + mousePos.y() - self.mousePressPos.y()
            if toY - boundingRect.top() < self.minHeight:
                toY = boundingRect.top() + self.minHeight
            boundingRect.setBottom(toY)
            rect.setBottom(boundingRect.bottom() - offset)

        if self.handleSelected == NNBResizableLayer.Handle.handleMiddleLeft or \
                self.handleSelected == NNBResizableLayer.Handle.handleBottomLeft or \
                self.handleSelected == NNBResizableLayer.Handle.handleTopLeft:
            toX = self.mousePressRect.left() + mousePos.x() - self.mousePressPos.x()
            if boundingRect.right() - toX < self.minWidth:
                toX = boundingRect.right() - self.minWidth
            boundingRect.setLeft(toX)
            rect.setLeft(boundingRect.left() + offset)
        elif self.handleSelected == NNBResizableLayer.Handle.handleMiddleRight or \
                self.handleSelected == NNBResizableLayer.Handle.handleBottomRight or \
                self.handleSelected == NNBResizableLayer.Handle.handleTopRight:
            toX = self.mousePressRect.right() + mousePos.x() - self.mousePressPos.x()
            if toX - boundingRect.left() < self.minWidth:
                toX = boundingRect.left() + self.minWidth
            boundingRect.setRight(toX)
            rect.setRight(boundingRect.right() - offset)

        for neuron in self.neurons:
            neuron.preventGettingOutOfBox()

        self.setRect(rect)
        self.updateHandlesPos()

    def shape(self):
        path = QPainterPath()
        path.addRect(self.rect())
        if self.state == NNBResizableLayer.State.ShowingHandles or self.state == NNBResizableLayer.State.Resizing:
            for handle, rect in self.handles.items():
                if self.state == NNBResizableLayer.State.ShowingHandles or handle == self.handleSelected:
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
        if self.state == NNBResizableLayer.State.ShowingHandles or self.state == NNBResizableLayer.State.Resizing:
            painter.setBrush(QBrush(Qt.white))
            painter.setPen(QPen(QColor(0, 0, 0, 255), 1.0, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            for handle, rect in self.handles.items():
                if self.state == NNBResizableLayer.State.ShowingHandles or handle == self.handleSelected:
                    painter.drawEllipse(rect)


def main():
    import sys
    from PyQt5.QtWidgets import QGraphicsView, QGraphicsScene

    app = QApplication(sys.argv)
    QApplication.setStartDragDistance(1)  # TO-DO: NEED to seed this
    view = QGraphicsView()
    view.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing)
    scene = QGraphicsScene()

    scene.setSceneRect(0, 0, SCENE_DEFAULT_WIDTH, SCENE_DEFAULT_HEIGHT)
    view.setScene(scene)

    layer1 = NNBResizableLayer("Affine 1D Vec. Layer-1", 12, 20)
    layer2 = NNBResizableLayer("Conv. 1D Vec. Layer-1", 150, 30)
    scene.addItem(layer1)
    scene.addItem(layer2)
    view.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()