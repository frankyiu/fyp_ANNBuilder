from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QPen, QColor, QBrush
from PyQt5.QtCore import QMimeData, Qt, QPoint, QFile

"""
Inherit QLabel, inherited by DatasetIcon and ToolbarIcon
Provide supports to the hovering and pressing effect
"""
class QLabelEffect(QLabel):
    def __init__(self,parent):
        super(QLabel,self).__init__(parent)
        self.__initialize()

    def __initialize(self):
        self.rounded_rect_radius = None
        self.qpixmap_drawn = QLabelEffect.getDefaultPixmap()
        self.hover_color = QColor(255,255,255,128)
        self.press_color = QColor(0,0,0,128)

    def setRoundedRadius(self, radius):
        self.rounded_rect_radius = radius

    def setQPixmapDrawn(self, pix):
        self.qpixmap_drawn = pix

    def setHoverColor(self, qc):
        self.hover_color = qc

    def setPressColor(self, qc):
        self.press_color = qc

    def __drawRect(self, painter):
        if self.rounded_rect_radius is not None:
            radius = self.rounded_rect_radius
            painter.drawRoundedRect(self.qpixmap_drawn.rect(), radius, radius)
        else:
            painter.drawRect(self.qpixmap_drawn.rect())


    def __createPainter(self, empty_pix):
        painter = QPainter(empty_pix)
        painter.setBrush(QBrush(self.qpixmap_drawn))
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)
        return painter

    """
    render the image based on the hovering state and pressing state
    """
    def showImage(self, hover=False, press=False):
        tmp = QPixmap(self.qpixmap_drawn.size())
        tmp.fill(Qt.transparent)
        painter = self.__createPainter(tmp)
        self.__drawRect(painter)
        if hover:
            painter.setBrush(self.hover_color)
            self.__drawRect(painter)
        elif press:
            painter.setBrush(self.press_color)
            self.__drawRect(painter)
        self.setPixmap(tmp)
        painter.end()

    """
    use the default pixmap when the icon can not be loaded
    """
    @staticmethod
    def getDefaultPixmap():
        return QPixmap(600,600)
