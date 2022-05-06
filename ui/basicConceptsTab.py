import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BasicConceptsTab(QTabWidget):
    def __init__(self, parent = None):
        super(BasicConceptsTab, self).__init__(parent)

        self.tab1 = QWidget()

        self.addTab(self.tab1, 'Basic Concepts')
        
        style = """
        QWidget{
            background-color: rgb(40, 44, 52);
        }
        QLabel{
            font-size: 12pt;
        }
        QTabBar::tab{
            background: lightgray;
            color: black;
            border: 3;
            padding: 5px;
            max-width: 300px;
            height: 15px;
            border: 1px solid;
        }
        QTabBar::tab:selected {
            background: gray;
            color: white;
        }
        """
        self.setStyleSheet(style)
        
        self.tabBar().setAutoHide(True)

        self.tab1UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        label = QLabel('Basic Concepts')
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        label.setStyleSheet("QLabel{font-size: 40pt;}")

        layout.addWidget(label)

        self.tab1.setLayout(layout)
