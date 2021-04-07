import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MLPArchitectureTab(QTabWidget):
    def __init__(self, parent = None):
        super(MLPArchitectureTab, self).__init__(parent)

        self.tab1 = QWidget()

        self.addTab(self.tab1, 'Architecture of MLP')
        
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
            
        label1 = QLabel('MLP is one of the simplest forms of deep learning neural networks.\nHere is the general architecture of a MLP containing just 1 hidden layer:')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        mlpArchitecture_graph = QLabel()
        mlpArchitecture_graph.setAlignment(Qt.AlignCenter)
        mlpArchitecture_graph.setPixmap(QPixmap('./png/ArchitectureofMLP/mlpArchitecture.png').scaled(mlpArchitecture_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(mlpArchitecture_graph)

        label2 = QLabel('Notice that, the number of hidden layers can be incremented arbitrarily as needed.\nIn addition, the activation function of the hidden units must be non-linear and differentiable, so as to enable backpropagation in supervised training.\nClassification tasks and regression tasks interpret and treat the output from the output layer differently, more details can be found in "MLP Classification" and "MLP Regression".')
        label2.setWordWrap(True)
        layout.addWidget(label2)

        self.tab1.setLayout(layout)
