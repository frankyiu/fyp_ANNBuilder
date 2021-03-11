import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FullyconnectedLayerTabs(QTabWidget):
    def __init__(self, parent = None):
        super(FullyconnectedLayerTabs, self).__init__(parent)

        self.tab1 = QWidget()
        self.tab2 = QWidget()        

        self.addTab(self.tab1, 'The Definition Of A Fully-connected Layer')
        self.addTab(self.tab2, 'The Purpose Of Having A Fully-connected Layer')

        self.tab1UI()
        self.tab2UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('A fully-connected layer is defined as a structure that every node of a layer is connected to every node of another layer.'))
        layout.addWidget(QLabel('Here is the typical setup of a fully-connected layer:'))
   
        fullyconnectedLayer_graph = QLabel()
        fullyconnectedLayer_graph.setPixmap(QPixmap('./png/FullyConnectedLayer/TheTypicalSetupOfAFullyConnectedLayer/fullyconnectedLayer.png'))
        layout.addWidget(fullyconnectedLayer_graph)

        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel('A fully-connected layer is usually placed after a flattening layer.'))
        layout.addWidget(QLabel('The purpose of putting a fully-connected layer in place is to convert the information contained in every input feature vector to a corresponding score vector.'))
        layout.addWidget(QLabel('The score vector would then be interpreted differently, depending on the nature of the task, i.e. classification or regression.'))

        self.tab2.setLayout(layout)
