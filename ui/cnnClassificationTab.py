import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CNNClassificationTab(QTabWidget):
    def __init__(self, parent = None):
        super(CNNClassificationTab, self).__init__(parent)

        self.tab1 = QWidget()

        self.addTab(self.tab1, 'CNN Classification')
        
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
        
        label1 = QLabel('In the case of classification, each entry of the score vector returned by the fully-connect layer can be taken as the likelihood of the fed-in example having a specific label.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('But more generally, the score vector would be fed into a softmax function to obtain a probability vector, which would then be fed into a cross-entropy function to obtain the loss.')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        label3 = QLabel('Take a CNN used to predict the income level of an individual by his/her personal particulars as an example, the illustration below clearly shows the workflow of the neural network at the very last stage:')
        label3.setWordWrap(True)
        layout.addWidget(label3)

        cnnClassification_gif = QLabel()
        cnnClassification_gif.setAlignment(Qt.AlignCenter)
        cnnClassification_movie = QMovie('./gifs/CNNClassification/cnnClassification.gif')
        cnnClassification_gif.setMovie(cnnClassification_movie)
        cnnClassification_movie.start()
        layout.addWidget(cnnClassification_gif)

        self.tab1.setLayout(layout)
