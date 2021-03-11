import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MLPClassificationTab(QTabWidget):
    def __init__(self, parent = None):
        super(MLPClassificationTab, self).__init__(parent)

        self.tab1 = QWidget()

        self.addTab(self.tab1, 'MLP Classification')

        self.tab1UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('For classification problems, the value of each node in the output layer can be interpreted as the likelihood of the fed-in example having the correponding class label.'))
        layout.addWidget(QLabel('But more generally, the output vector would be fed into a softmax function to obtain a probability vector, which would in turn be fed into a cross-entropy function to calculate the loss.'))
        layout.addWidget(QLabel('Here is a simple illustration of how the value of each output node would be further treated by a softmax function and a cross entropy loss function in MLP classification:'))

        mlpClassification_gif = QLabel()
        mlpClassification_movie = QMovie('./gifs/MLPClassification/mlpClassification.gif')
        mlpClassification_gif.setMovie(mlpClassification_movie)
        mlpClassification_movie.start()
        layout.addWidget(mlpClassification_gif)

        layout.addWidget(QLabel('In the training phase, backpropagation is conducted as per the loss given by the loss function after each feedforward.'))

        self.tab1.setLayout(layout)
