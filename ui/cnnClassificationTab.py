import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CNNClassificationTab(QTabWidget):
    def __init__(self, parent = None):
        super(CNNClassificationTab, self).__init__(parent)

        self.tab1 = QWidget()

        self.addTab(self.tab1, 'CNN Classification')

        self.tab1UI()

    def tab1UI(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel('In the case of classification, each entry of the score vector returned by the fully-connect layer can be taken as the likelihood of the fed-in example having a specific label.'))
        layout.addWidget(QLabel('But more generally, the score vector would be fed into a softmax function to obtain a probability vector, which would then be fed into a cross-entropy function to obtain the loss.'))
        layout.addWidget(QLabel('Take a CNN used to predict the income level of an individual by his/her personal particulars as an example, the illustration below clearly shows the workflow of the neural network at the very last stage:'))

        cnnClassification_gif = QLabel()
        cnnClassification_movie = QMovie('./gifs/CNNClassification/cnnClassification.gif')
        cnnClassification_gif.setMovie(cnnClassification_movie)
        cnnClassification_movie.start()
        layout.addWidget(cnnClassification_gif)

        self.tab1.setLayout(layout)
