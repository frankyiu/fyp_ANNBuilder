from PyQt5 import QtWidgets,  QtCore
from PyQt5.QtWidgets import  QWidget
from PyQt5.QtCore import QPoint, QRect

class PopUpGuide():
    
    size = QPoint(250, 120)
    
    def __init__(self, offset, text, targetWidget, backWidget,  factory):
        self.pos = targetWidget.pos()+offset
        self.factory = factory
        self.targetWidget = targetWidget
        self.backWidget = backWidget
        self.setUpUI()
        self.setText(text)
        self.setUpButton()
        self.show()
        
    def setText(self, text):
        self.guide.textBrowser.append(text)
    
    def show(self):
        self.guide.show()
        self.shadow.show()
        
    def transulateBack(self):
        posOnBack = self.targetWidget.mapTo(self.backWidget, QPoint(0, 0))
        self.shadow.setGeometry(QRect(0, 0, self.backWidget.width(), self.backWidget.height()))
        self.shadow.setStyleSheet("border-color: rgba(0, 0, 0,0.3);\n"
        f"border-width: {posOnBack.y()}px {self.backWidget.width()-self.targetWidget.width()-posOnBack.x()}px {self.backWidget.height()-self.targetWidget.height()-posOnBack.y()}px {posOnBack.x()}px;\n"
        "border-style: solid;\n")

        
    def refresh(self):
        self.transulateBack()
        
    def setUpUI(self):
        #transulateBackground
        self.shadow = QtWidgets.QWidget(self.backWidget)
        self.transulateBack()
        #CreatePopUpGuide
        
        self.guide= QtWidgets.QWidget(self.backWidget)
        self.guide.setGeometry(QRect(self.pos.x(), self.pos.y(), PopUpGuide.size.x(), PopUpGuide.size.y()))
        self.guide.setStyleSheet("QWidget#widget{\n"
"border: 1px solid;\n"
"border-radius: 10px;\n"
"background-color: rgb(81, 90, 106);\n"
"}\n"
"")
        self.guide.setObjectName('widget')
        self.guide.verticalLayout = QtWidgets.QVBoxLayout(self.guide)
        self.guide.verticalLayout.setObjectName("verticalLayout")
        self.guide.textBrowser = QtWidgets.QTextBrowser(self.guide)
        self.guide.textBrowser.setObjectName("textBrowser")
        self.guide.verticalLayout.addWidget(self.guide.textBrowser)
        self.guide.frame = QtWidgets.QFrame(self.guide)
        self.guide.frame.setMinimumSize(QtCore.QSize(0, 30))
        self.guide.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.guide.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.guide.frame.setObjectName("frame")
        self.guide.horizontalLayout = QtWidgets.QHBoxLayout(self.guide.frame)
        self.guide.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.guide.horizontalLayout.setObjectName("horizontalLayout")
        self.guide.frame_2 = QtWidgets.QFrame(self.guide.frame)
        self.guide.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.guide.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.guide.frame_2.setObjectName("frame_2")
        self.guide.horizontalLayout.addWidget(self.guide.frame_2)
        
        self.guide.btn_skip = QtWidgets.QPushButton(self.guide.frame)
        self.guide.btn_skip.setMaximumSize(QtCore.QSize(100, 16777215))
        self.guide.btn_skip.setObjectName("btn_skip")
        self.guide.btn_skip.setText('Skip')
        self.guide.horizontalLayout.addWidget(self.guide.btn_skip)
        
        self.guide.btn_next = QtWidgets.QPushButton(self.guide.frame)
        self.guide.btn_next.setMaximumSize(QtCore.QSize(100, 16777215))
        self.guide.btn_next.setObjectName("btn_next")
        self.guide.btn_next.setText('Next')

        self.guide.horizontalLayout.addWidget(self.guide.btn_next)
        self.guide.verticalLayout.addWidget(self.guide.frame)
        
        
    def setUpButton(self):
        self.guide.btn_skip.clicked.connect(self.factory.skip)
        self.guide.btn_next.clicked.connect(self.factory.next)
        
        
    def close(self):
        self.shadow.hide()
        self.guide.hide()
        self.guide.close()
        self.shadow.close()
