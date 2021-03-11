import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MLPApplicationTab(QTabWidget):
    def __init__(self, parent = None):
        super(MLPApplicationTab, self).__init__(parent)

        self.tab1 = QWidget()

        self.addTab(self.tab1, 'Application of MLP')

        self.tab1UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Multi-layer perceptron (MLP) is widely used to deal with classification problems and regression problems.'))
        layout.addWidget(QLabel('Common applications of MLP include speech recognition, customers\' behaviours prediction and many more.'))        
        layout.addWidget(QLabel('MLP can also be incorporated into a more complex neural network architecture as one of its key components.'))

        self.tab1.setLayout(layout)
