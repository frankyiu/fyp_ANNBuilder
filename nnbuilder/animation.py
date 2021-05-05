from PyQt5.QtGui import QPolygonF
from PyQt5.QtCore import QObject, QPointF, QLineF, QPropertyAnimation, pyqtProperty
from PyQt5.QtWidgets import QGraphicsPolygonItem
from .config import *
from .utils import *

def findArrowhead(vLine):
    nLine = vLine.normalVector()
    nLine.setLength(nLine.length() * ANIMATION_ARROWHEAD_FACTOR)
    n2Line = nLine.normalVector().normalVector()
    p1 = vLine.p2()
    p2 = nLine.p2()
    p3 = n2Line.p2()
    return QPolygonF([p1, p2, p3])


class NNBLineTrainArrowFlowAnimation(QObject):
    def __init__(self, connection, idx, forward=True, parent=None):
        super().__init__(parent)
        self.connection = connection
        self.forward = forward
        self.arrowhead = QGraphicsPolygonItem()
        self.arrowhead.setBrush(QBrush(Qt.black))
        if not self.forward:
            self.arrowline = QLineF(*connection.toPts[idx], *connection.fromPts[idx])
        else:
            self.arrowline = QLineF(*connection.fromPts[idx], *connection.toPts[idx])
        self.vLine = self.arrowline.unitVector()
        self.vLine.setLength(ANIMATION_ARROWHEAD_LENGTH)
        self.vLineDx = self.vLine.dx()
        self.vLineDy = self.vLine.dy()
        self.startValue = self.arrowline.p1()
        self.endValue = QPointF(self.arrowline.p2().x() - self.vLineDx,
                                self.arrowline.p2().y() - self.vLineDy)
        self.arrowhead.setPolygon(self.findArrowhead())
        self.fAnimation = QPropertyAnimation(self, b"p1",
                                             parent=self,
                                             startValue=self.startValue,
                                             endValue=self.endValue,
                                             duration=ANIMATION_DURATION)

    def onAnimationFinished(self):
        self.connection.scene().finishOneLayerFlowAnimation()

    def finishedConnect(self):
        self.fAnimation.finished.connect(self.onAnimationFinished)

    def start(self):
        self.connection.scene().addItem(self.arrowhead)
        self.fAnimation.start()

    def stop(self):
        self.fAnimation.stop()

    def vanish(self):
        self.connection.scene().removeItem(self.arrowhead)

    def destroy(self):
        del self.fAnimation

    def findArrowhead(self):
        nLine = self.vLine.normalVector()
        nLine.setLength(nLine.length() * ANIMATION_ARROWHEAD_FACTOR)
        n2Line = nLine.normalVector().normalVector()
        p1 = self.vLine.p2()
        p2 = nLine.p2()
        p3 = n2Line.p2()
        return QPolygonF([p1, p2, p3])

    def p1(self):
        return self.vLine.p1()

    def setP1(self, p1):
        self.vLine.setP1(p1)
        self.vLine.setP2(QPointF(p1.x() + self.vLineDx, p1.y() + self.vLineDy))
        self.arrowhead.setPolygon(self.findArrowhead())

    p1 = pyqtProperty(QPointF, fget=p1, fset=setP1)


class NNBPathTrainArrowFlowAnimation:
    def __init__(self, connection, forward=True):
        # super().__init__(parent)
        self.connection = connection
        self.forward = forward
        self.animations = []
        for i in range(len(self.connection.fromPts)):
            self.animations.append(NNBLineTrainArrowFlowAnimation(connection, i, forward))

    def finishedConnect(self):
        if self.animations:
            self.animations[0].finishedConnect()

    def start(self):
        for animation in self.animations:
            animation.start()

    def stop(self):
        for animation in self.animations:
            animation.stop()

    def vanish(self):
        for animation in self.animations:
            animation.vanish()

    def destroy(self):
        for animation in self.animations:
            animation.destroy()


class NNBCurveTrainArrowFlowAnimation(QObject):
    def __init__(self, connection, forward=True, parent=None):
        super().__init__(parent)
        self.connection = connection
        self.forward = forward
        if self.forward:
            self.x1, self.y1 = connection.fromPt.x(), connection.fromPt.y()
            self.x2, self.y2 = connection.toPt.x(), connection.toPt.y()
        else:
            self.x1, self.y1 = connection.toPt.x(), connection.toPt.y()
            self.x2, self.y2 = connection.fromPt.x(), connection.fromPt.y()
        self.cx, self.cy = connection.ctrlPt.x(), connection.ctrlPt.y()
        self.currX = self.x1
        self.vLine = None

        self.arrowhead = QGraphicsPolygonItem()
        self.arrowhead.setBrush(QBrush(Qt.black))
        self.fAnimation = QPropertyAnimation(self, b"p1",
                                              # parent = self,
                                              startValue = self.x1,
                                              endValue = self.x2,
                                              duration = ANIMATION_DURATION)

    def onAnimationFinished(self):
        self.toLFBAnimation.start()

    def finishedConnect(self):
        self.fAnimation.finished.connect(self.onAnimationFinished)

    def start(self):
        self.connection.scene().addItem(self.arrowhead)
        self.fAnimation.start()

    def stop(self):
        self.fAnimation.stop()

    def vanish(self):
        self.connection.scene().removeItem(self.arrowhead)

    def destroy(self):
        del self.fAnimation

    def findArrowhead(self):
        nLine = self.vLine.normalVector()
        nLine.setLength(nLine.length() * ANIMATION_ARROWHEAD_FACTOR)
        n2Line = nLine.normalVector().normalVector()
        p1 = self.vLine.p2()
        p2 = nLine.p2()
        p3 = n2Line.p2()
        return QPolygonF([p1, p2, p3])

    def p1(self):
        return self.currX

    def setP1(self, p1):
        t = self.fAnimation.currentTime() / ANIMATION_DURATION
        xt, yt = findPt(self.x1, self.y1, self.x2, self.y2, self.cx, self.cy, t)
        xt_, yt_ = findDerPt(self.x1, self.y1, self.x2, self.y2, self.cx, self.cy, t)
        self.currX = xt

        xt_next = xt
        yt_next = yt + 1
        if xt_ != 0:
            m = yt_ / xt_
            c = -m * xt + yt
            xt_next = xt + 1
            yt_next = m * (xt + 1) + c
        if self.forward:
            arrowline = QLineF(xt, yt, xt_next, yt_next)
        else:
            arrowline = QLineF(xt_next, yt_next, xt, yt)

        self.vLine = arrowline.unitVector()
        self.vLine.setLength(ANIMATION_ARROWHEAD_LENGTH)
        vLineDx = self.vLine.dx()
        vLineDy = self.vLine.dy()
        p = QPointF(xt, yt)
        self.vLine.setP1(p)
        self.vLine.setP2(QPointF(p.x() + vLineDx, p.y() + vLineDy))
        self.arrowhead.setPolygon(self.findArrowhead())

    p1 = pyqtProperty(float, fget=p1, fset=setP1)

