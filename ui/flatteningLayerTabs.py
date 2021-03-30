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
        self.addTab(self.tab2, 'Demonstration')
        
        self.tab1UI()
        self.tab2UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Flattening layer transforms multi-dimensional feature maps into one-dimensional feature vectors, for the purpose of facilitating the classification taking place in the fully-connected layers afterwards.'))
        layout.addWidget(QLabel('In a convolutional neural network, flattening layer usually comes after a convolutional layer or a pooling layer, and before a fully-connected layer.'))

        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel('Here is the demonstration of how a flattening layer transforms a 3x3 input feature map into a 1D feature vector:'))
        
        flattening_graph = QLabel()
        flattening_graph.setPixmap(QPixmap('./png/FlatteningLayer/Demonstration/flattening.png'))
        layout.addWidget(flattening_graph)

        self.tab2.setLayout(layout)
