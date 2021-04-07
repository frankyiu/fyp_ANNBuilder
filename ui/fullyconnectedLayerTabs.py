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
        self.tab2UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('A fully-connected layer is defined as a structure that every node of a layer is connected to every node of another layer.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('Here is the typical setup of a fully-connected layer:')
        label2.setWordWrap(True)
        layout.addWidget(label2)
   
        fullyconnectedLayer_graph = QLabel()
        fullyconnectedLayer_graph.setAlignment(Qt.AlignCenter)
        fullyconnectedLayer_graph.setPixmap(QPixmap('./png/FullyConnectedLayer/TheTypicalSetupOfAFullyConnectedLayer/fullyconnectedLayer.png'))
        layout.addWidget(fullyconnectedLayer_graph)

        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('A fully-connected layer is usually placed after a flattening layer.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('The purpose of deploying a fully-connected layer is to convert the information carried by every input feature vector to a corresponding score vector.')
        label2.setWordWrap(True)
        layout.addWidget(label2)

        label3 = QLabel('The score vector would then be interpreted differently, depending on the nature of the task, i.e. classification or regression.')
        label3.setWordWrap(True)
        layout.addWidget(label3)
       
        self.tab2.setLayout(layout)
