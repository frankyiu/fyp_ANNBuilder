from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow,  QButtonGroup, QDialog
from PyQt5.QtCore import Qt, QPropertyAnimation
from PyQt5.QtGui import QCursor
from ui.Ui_GuiMainWindow import *
from ui.DatasetLoader import *
from ui.Guide import *
from ui.PopUpGuideFactory import *

class MainWindow(QMainWindow):
    
    
    def __init__(self):
        QMainWindow.__init__(self)
        self.firstTimeGuide = True
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.isMaxWindow = False
        self.setupMenu()
        self.setupTitleBar()
        self.setupTutorial()
        self.setupBuilder()
        self.show()
        self.resizeEvent(None)
        
    def resizeEvent(self, event):
        self.ui.btn_viewer.setMinimumHeight(self.ui.tab_viewer.height())
        if(self.popUpGuide.isStarted):
            self.popUpGuide.refreshUI()
        
    def setupBuilder(self):
        self.ui.dataloader = DatasetLoader(self.ui.frame_dataloader, self.ui.page_draw, QtCore.QRect(0, 0, 120, 120))    
        #setting Tour
        self.popUpGuide = PopUpGuideFactory(self.ui.page_draw)
        self.popUpGuide.append(self.ui.frame_dataset, QPoint(150, 0), 'This is the Dataset Panel\nYou can choose the dataset by clicking the picture')
        self.popUpGuide.append(self.ui.frame_component, QPoint(150, 0), 'This is the Component Panel\nYou can drag and drop the component to the drawing panel to build the model')
        self.popUpGuide.append(self.ui.frame_control, QPoint(150, 0), 'This is the Control Panel\nClick the Play button the train the model')
        self.popUpGuide.append(self.ui.graphicsView, QPoint(0, 0), 'This is the Drawing Panel\nDrag the component to it to build your own model')
        self.ui.btn_guide.clicked.connect(self.guideOnclickEvent)
        
        #setting Viewer
        self.ui.btn_viewer.clicked.connect(self.viewerOnclickEvent)
        
    def viewerOnclickEvent(self):
        icon = QIcon()
        if(self.ui.tab_viewer.isHidden()):
            self.ui.tab_viewer.show()
            self.ui.draw_right.setMinimumWidth(200)
            icon.addFile(u":/basic/icons/basic/next-1.png", QSize(), QIcon.Normal, QIcon.Off)
        else:
            self.ui.tab_viewer.hide()
            self.ui.draw_right.setMinimumWidth(self.ui.btn_viewer.width()+10)
            icon.addFile(u":/basic/icons/basic/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_viewer.setIcon(icon)
        
    def setupTitleBar(self):
        #remove title bar
#        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.ui.btn_minimize.clicked.connect(self.showMinimized)
        self.ui.btn_maximize_restore.clicked.connect(self.maxOrRestore)
        self.ui.btn_close.clicked.connect(self.close)
    
    def setupTutorial(self):
        return 
        
    def setupMenu(self):
        #set up expand btn
        self.expandOrgWidth = self.ui.frame_left_menu.width()
        self.ui.btn_expand.clicked.connect(lambda: self.ExpandOnclickEvent(200))
        #set up meunu btn
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
        if (width == maxWidth):
            targetWidth = self.expandOrgWidth
            icon.addFile(u":/basic/icons/basic/next-1.png", QSize(), QIcon.Normal, QIcon.Off)
        else:
            targetWidth = maxWidth
            icon.addFile(u":/basic/icons/basic/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_expand.setIcon(icon)
        self.animation = QPropertyAnimation(self.ui.frame_left_menu, b"minimumWidth")
        self.animation.setDuration(350)
        self.animation.setStartValue(width)
        self.animation.setEndValue(targetWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()
        
        
    def maxOrRestore(self):
        if(self.isMaxWindow):
            self.showNormal()
            self.isMaxWindow = False
        else:
            self.showMaximized()
            self.isMaxWindow = True
    
    
    def backOnclickEvent(self):
        print(btn = self.sender())
        if(btn.objectName()== 'btn_back'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_tutorial)
            
    def menuOnclickEvent(self, btn):
        if (btn.objectName() == 'btn_home'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_home)
            
        if (btn.objectName() == 'btn_tutorial'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_tutorial)
            
        if (btn.objectName() == 'btn_draw'):
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_draw)
            if(self.firstTimeGuide):
                self.guideOnclickEvent()

    def guideOnclickEvent(self):
        self.popUpGuide.start()
        self.firstTimeGuide = False

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
