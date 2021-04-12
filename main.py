from PyQt5.QtWidgets import QMainWindow, QButtonGroup
from PyQt5.QtCore import QPropertyAnimation, QSize
from PyQt5.QtGui import QIcon
from ui.Ui_GuiMainWindow import *
from ui.DatasetLoader import *
from ui.PopUpGuideFactory import *
from builderui import BuilderUI


class MainWindow(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        self.setupFont()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.isMaxWindow = False
        self.borderHit = None
        self.dragPos = None
        self.setupMenu()
        self.setupTitleBar()
        self.setupWindow()
        self.setupHome()
        self.builder = BuilderUI(self.ui)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        self.show()
        self.resizeEvent(None)

    def setupFont(self):
        QFontDatabase.addApplicationFont(":/font/fonts/DroidSansMono.ttf")
        QFontDatabase.addApplicationFont(":/font/fonts/SegoeUIMono.ttf")

    def setupWindow(self):
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(17)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.ui.centralwidget.setGraphicsEffect(self.shadow)
        self.ui.centralwidget.setMouseTracking(True)
        self.ui.centralwidget.mouseMoveEvent = self.mouseMoveEvent
        self.ui.frame_top.mouseMoveEvent = self.moveWindowEvent
        self.ui.frame_top.mouseDoubleClickEvent = self.titleDoubleClickEvent
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def setupHome(self):
        self.ui.btn_gotoTutorial.clicked.connect(self.ui.btn_tutorial.click)
        self.ui.btn_gotoBuilder.clicked.connect(self.ui.btn_draw.click)

        self.ui.btn_gotoBasicCon.clicked.connect(lambda: self.ui.widget_tutorial.leftlist.setCurrentRow(0))
        self.ui.btn_gotoBasicCon.clicked.connect(self.ui.btn_tutorial.click)

        self.ui.btn_gotoMLP.clicked.connect(lambda: self.ui.widget_tutorial.leftlist.setCurrentRow(10))
        self.ui.btn_gotoMLP.clicked.connect(self.ui.btn_tutorial.click)

        self.ui.btn_gotoCNN.clicked.connect(lambda: self.ui.widget_tutorial.leftlist.setCurrentRow(15))
        self.ui.btn_gotoCNN.clicked.connect(self.ui.btn_tutorial.click)



    def resizeEvent(self, event):
        self.builder.resizeEvent(event)

    def setupTitleBar(self):
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        self.ui.btn_maximize_restore.clicked.connect(self.maxOrRestore)
        self.ui.btn_close.clicked.connect(self.close)

    def setupMenu(self):
        # set up expand btn
        self.expandOrgWidth = self.ui.frame_left_menu.width()
        self.ui.btn_expand.clicked.connect(lambda: self.ExpandOnclickEvent(150))
        # set up meunu btn
        self.menuButtons = QButtonGroup()
        self.menuButtons.addButton(self.ui.btn_home)
        self.menuButtons.addButton(self.ui.btn_tutorial)
        self.menuButtons.addButton(self.ui.btn_draw)
        for btn in self.menuButtons.buttons():
            btn.setCheckable(True)
            btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.ui.btn_home.setChecked(True)
        self.menuButtons.buttonClicked.connect(self.menuOnclickEvent)

    def ExpandOnclickEvent(self, maxWidth):
        icon = QIcon()
        width = self.ui.frame_left_menu.width()
        if width == maxWidth:
            targetWidth = self.expandOrgWidth
        else:
            targetWidth = maxWidth
        self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
        self.animation.setDuration(350)
        self.animation.setStartValue(width)
        self.animation.setEndValue(targetWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

    def maxOrRestore(self):
        if (self.isMaxWindow):
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.showNormal()
            self.isMaxWindow = False
        else:
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.showMaximized()
            self.isMaxWindow = True
        self.resizeEvent(None)

    def menuOnclickEvent(self, btn):
        if (btn.objectName() == 'btn_home'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)

        if (btn.objectName() == 'btn_tutorial'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_tutorial)

        if (btn.objectName() == 'btn_draw'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_draw)
            self.builder.menuclicked()

    def mouseMoveEvent(self, event):
        # drag and move
        if event.buttons() & Qt.LeftButton:
            nGeo = self.geometry()
            if self.borderHit == 'left':
                nGeo.setLeft(event.globalPos().x())
            elif self.borderHit == 'right':
                nGeo.setRight(event.globalPos().x())
            elif self.borderHit == 'top':
                nGeo.setTop(event.globalPos().y())
            elif self.borderHit == 'bottom':
                nGeo.setBottom(event.globalPos().y())
            elif self.borderHit == 'top-left':
                nGeo.setTopLeft(event.globalPos())
            elif self.borderHit == 'top-right':
                nGeo.setTopRight(event.globalPos())
            elif self.borderHit == 'bottom-left':
                nGeo.setBottomLeft(event.globalPos())
            elif self.borderHit == 'bottom-right':
                nGeo.setBottomRight(event.globalPos())

            condx = nGeo.x() > self.x() and nGeo.width() <= self.minimumWidth()
            condy = nGeo.y() > self.y() and nGeo.height() <= self.minimumHeight()
            if (condx and condy):
                return
            elif condx:
                self.setGeometry(self.x(), nGeo.y(), self.width(), nGeo.height())
            elif condy:
                self.setGeometry(nGeo.x(), self.y(), nGeo.width(), self.height())
            else:
                self.setGeometry(nGeo)
        else:
            # only move
            margin = 10
            width, height = self.ui.centralwidget.width(), self.ui.centralwidget.height()
            x, y = event.pos().x(), event.pos().y()
            if x <= margin and y <= margin:
                self.setCursor(Qt.SizeFDiagCursor)
                self.borderHit = 'top-left'
            elif x <= margin and y >= height - margin:
                self.setCursor(Qt.SizeBDiagCursor)
                self.borderHit = 'bottom-left'
            elif x >= width - margin and y <= margin:
                self.setCursor(Qt.SizeBDiagCursor)
                self.borderHit = 'top-right'
            elif x >= width - margin and y >= height - margin:
                self.setCursor(Qt.SizeFDiagCursor)
                self.borderHit = 'bottom-right'
            elif x <= margin:
                self.setCursor(Qt.SizeHorCursor)
                self.borderHit = 'left'
            elif y <= margin:
                self.setCursor(Qt.SizeVerCursor)
                self.borderHit = 'top'
            elif x >= width - margin:
                self.setCursor(Qt.SizeHorCursor)
                self.borderHit = 'right'
            elif y >= height - margin:
                self.setCursor(Qt.SizeVerCursor)
                self.borderHit = 'bottom'

    def mousePressEvent(self,event):
        self.dragPos = event.globalPos()
    def mouseReleaseEvent(self, event):
        self.borderHit = None

    def moveWindowEvent(self,event):
        if self.isMaxWindow:
            return
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos()- self.dragPos)
            self.dragPos = event.globalPos()

    def titleDoubleClickEvent(self,event):
        self.maxOrRestore()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
