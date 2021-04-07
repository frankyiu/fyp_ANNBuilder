import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MLPApplicationTab(QTabWidget):
    def __init__(self, parent = None):
        super(MLPApplicationTab, self).__init__(parent)

        self.tab1 = QWidget()

        self.addTab(self.tab1, 'Application of MLP')
        
        self.tabBar().setAutoHide(True)
        
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
            border-radius: 12px;
            font-size: 12pt;
        }
        QTabBar::tab:selected {
            background: gray;
            color: white;
        }
        """
        self.setStyleSheet(style)

        self.tab1UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel("Multi-layer perceptron (MLP) is widely used to deal with classification problems and regression problems.")
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('Common applications of MLP include speech recognition, customers\' behaviours prediction and many more.')
        label2.setWordWrap(True)    
        layout.addWidget(label2)
        
        label3 = QLabel('MLP can also be incorporated into a more complex neural network architecture as one of its key components.')
        label3.setWordWrap(True)
        layout.addWidget(label3)

        self.tab1.setLayout(layout)
