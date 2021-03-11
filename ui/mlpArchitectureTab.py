import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MLPArchitectureTab(QTabWidget):
    def __init__(self, parent = None):
        super(MLPArchitectureTab, self).__init__(parent)

        self.tab1 = QWidget()

        self.addTab(self.tab1, 'Architecture of MLP')

        self.tab1UI()

    def tab1UI(self):
        layout = QVBoxLayout()
            
        layout.addWidget(QLabel('MLP is one of the simplest forms of deep learning neural networks.'))
        layout.addWidget(QLabel('Here is the general architecture of a MLP containing just 1 hidden layer:'))
        
        mlpArchitecture_graph = QLabel()
        mlpArchitecture_graph.setPixmap(QPixmap('./png/ArchitectureofMLP/mlpArchitecture.png'))
        layout.addWidget(mlpArchitecture_graph)
        
        layout.addWidget(QLabel('Notice that, the number of hidden layers can be incremented arbitrarily as needed.'))
        layout.addWidget(QLabel('In addition, the activation function of the hidden units must be non-linear and differentiable, so as to enable backpropagation in supervised training.'))
        layout.addWidget(QLabel('Classification tasks and regression tasks interpret and treat the output from the output layer differently, more details can be found in "MLP Classification" and "MLP Regression".'))

        self.tab1.setLayout(layout)
