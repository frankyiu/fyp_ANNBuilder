from PyQt5 import QtGui
from PyQt5.QtCore import QRect, QSize, QPoint, Qt
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QSizePolicy, QVBoxLayout, QPushButton, QTextBrowser


class Message(QWidget):
    warningStyle = 'background-color: rgb(254,239,179);\ncolor: rgb(159,96,0);\nborder-radius:5px;'
    errorStyle = 'background-color: rgb(254,239,179);\ncolor: rgb(159,96,0);'
    scrollBarStyle = \
"QScrollBar:vertical {\
background-color: transparent;\
width: 10px;\
border: none;\
margin: 0;\
}\
QScrollBar::handle:vertical {\
background: rgb(235, 186, 22);\
}\
\
QScrollBar::add-line:vertical {\
height: -1px;\
border: none;\
background-color: transparent;\
}\
\
QScrollBar::sub-line:vertical {\
height: -1px;\
border: none;\
background-color: transparent;\
}\
\
QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\
height: -1px;\
border: none;\
}"

    def __init__(self, targetWidget, size, message, parent):
        super().__init__(parent)
        self.targetWidget = targetWidget
        self.message = message
        self.size = size
        self.setupUi()
        self.setMessage()
        self.setupEvent()
        self.hide()

    def setMessage(self, nMessage=None):
        if nMessage is not None:
            self.message = nMessage
        self.textbrowser.setText(self.message)
        self.show()

    def setupUi(self):
        pos = self.targetWidget.mapTo(self.parent(), QPoint(0, 0))
        self.setGeometry(QRect(pos.x(), pos.y(), self.size.x(), self.size.y()))
        self.widget = QWidget(self)
        self.verticalLayout = QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.addWidget(self.widget)
        self.widget.setObjectName('widget')
        self.widget.setStyleSheet(f'QWidget{{{Message.warningStyle}}} {Message.scrollBarStyle}')

        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.icon = QLabel(self.widget)
        self.icon.setObjectName(u"icon")

        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon.sizePolicy().hasHeightForWidth())
        self.icon.setSizePolicy(sizePolicy)
        self.icon.setMinimumSize(QSize(0, 0))
        self.icon.setMaximumSize(QSize(40, 40))
        self.icon.setPixmap(QPixmap(u":/basic/icons/basic/warning.png"))
        self.icon.setScaledContents(True)

        self.horizontalLayout.addWidget(self.icon)

        self.textbrowser = QTextBrowser(self.widget)
        self.textbrowser.setObjectName(u"textbrowser")

        self.horizontalLayout.addWidget(self.textbrowser)

        self.btn_close = QPushButton(self.widget)
        self.btn_close.setObjectName(u"btn_close")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy2)
        self.btn_close.setMaximumSize(QSize(10, 10))
        self.btn_close.setStyleSheet(u"background:transparent;")
        icon = QIcon()
        icon.addFile(u":/basic/icons/basic/close-1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_close, 0, Qt.AlignTop)

        self.retranslateUi()

    def setupEvent(self):
        self.btn_close.clicked.connect(self.hide)

    def retranslateUi(self):
        self.icon.setText("")
        self.textbrowser.setText("Test Message")

    def refreshUi(self):
        pos = self.targetWidget.mapTo(self.parent(), QPoint(0, 0))
        # move to bottom-right
        self.move(pos.x() + self.targetWidget.width() - self.width() - 10,
                  pos.y() + self.targetWidget.height() - self.height() - 10)

    def toggleEvent(self, checked):
        self.refreshUi()
        self.hide() if self.isVisible() else self.show()
