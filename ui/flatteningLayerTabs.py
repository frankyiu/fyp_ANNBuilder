import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FlatteningLayerTabs(QTabWidget):
    def __init__(self, parent = None):
        super(FlatteningLayerTabs, self).__init__(parent)

        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.addTab(self.tab1, 'The Purpose Of Flattening')
        self.addTab(self.tab2, 'Illustration')
        
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
        self.tab2UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('Flattening layer transforms multi-dimensional feature maps into one-dimensional feature vectors, for the purpose of facilitating the operation later taking place in the fully-connected layers.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('In a convolutional neural network, flattening layer usually comes after a convolutional layer or a pooling layer, and before a fully-connected layer.')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('Here is the illustration of how a flattening layer transforms a 3x3 input feature map into a 1D feature vector:')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        flattening_graph = QLabel()
        flattening_graph.setAlignment(Qt.AlignCenter)
        flattening_graph.setPixmap(QPixmap('./png/FlatteningLayer/Illustration/flattening.png'))
        layout.addWidget(flattening_graph)

        self.tab2.setLayout(layout)
