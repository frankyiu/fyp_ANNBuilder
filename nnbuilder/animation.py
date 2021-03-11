from PyQt5.QtGui import QPolygonF
from PyQt5.QtCore import QObject, QPointF, QLineF, QPropertyAnimation, pyqtProperty
from PyQt5.QtWidgets import QGraphicsPolygonItem
from .config import *

class NNTrainArrowFlowAnimation(QObject):
    def __init__(self, lineItem, forward=True, parent=None):
        super().__init__(parent)
        self.arrowlineItem = lineItem
        self.arrowline = lineItem.line()
        self.forward = forward
        self.arrowhead = QGraphicsPolygonItem()
        self.arrowhead.setBrush(QBrush(Qt.black))
        if not self.forward:
            self.arrowline = QLineF(self.arrowline.x2(), self.arrowline.y2(),
                                    self.arrowline.x1(), self.arrowline.y1())
        self.setUp()
        self.fAnimation = QPropertyAnimation(self, b"p1",
                                             parent=self,
                                             startValue=self.startValue,
                                             endValue=self.endValue,
                                             duration=ANIMATION_DURATION)

    def onAnimationFinished(self):
        self.arrowlineItem.scene().finishOneLayerFlowAnimation()

    def start(self):
        self.arrowlineItem.scene().addItem(self.arrowhead)
        self.fAnimation.start()

    def vanish(self):
        self.arrowlineItem.scene().removeItem(self.arrowhead)

    def setDir(self, forward=True):
        if self.forward != forward:
            self.arrowline = QLineF(self.arrowline.x2(), self.arrowline.y2(),
                                    self.arrowline.x1(), self.arrowline.y1())
            self.forward = forward
            self.reset()

    def reset(self):
        self.setUp()
        self.fAnimation.setStartValue(self.startValue)
        self.fAnimation.setEndValue(self.endValue)

    def setUp(self):
        self.vLine = self.arrowline.unitVector()
        self.vLine.setLength(ANIMATION_ARROWHEAD_LENGTH)
        self.vLineDx = self.vLine.dx()
        self.vLineDy = self.vLine.dy()
        self.startValue = self.arrowline.p1()
        self.endValue = QPointF(self.arrowline.p2().x() - self.vLineDx,
                                self.arrowline.p2().y() - self.vLineDy)
        self.arrowhead.setPolygon(self.findArrowhead())

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