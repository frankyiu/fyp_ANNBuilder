import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CNNApplicationTab(QTabWidget):
    def __init__(self, parent = None):
        super(CNNApplicationTab, self).__init__(parent)

        self.tab1 = QWidget()

        self.addTab(self.tab1, 'Application of CNN')
        
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
            border: 1px solid;
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
        
        label1 = QLabel('Convolutional neural network (CNN) can be constructed to handle both classification tasks and regression tasks.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('Due to sparse connectivity and the weight-sharing scheme of convolution, the performance of CNN on image processing is highly effective and efficient.')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        label3 = QLabel('Therefore, CNN is widely used in image analysis, eg. object recognition, nowadays.')
        label3.setWordWrap(True)
        layout.addWidget(label3)
        
        self.tab1.setLayout(layout)
