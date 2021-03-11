import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CNNRegressionTab(QTabWidget):
    def __init__(self, parent = None):
        super(CNNRegressionTab, self).__init__(parent)

        self.tab1 = QWidget()

        self.addTab(self.tab1, 'CNN Regression')

        self.tab1UI()

    def tab1UI(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel('In the case of regression, a function of the score vector, the weights of each line connecting the score nodes and the output node, as well as the bias, needs to be defined.'))
        layout.addWidget(QLabel('In the training phase, the output is passed into a loss function and backpropagation will then be conducted as per the calculated loss.'))
        layout.addWidget(QLabel('Mean-squared error, MSE, is the most common loss function used in CNN regression. Some other functions, like mean-absolute error, can be used as substitutes.'))
        layout.addWidget(QLabel('Here is an illustration of the very last stage of CNN regression adpoting MSE as its loss function:'))

        cnnRegression_gif = QLabel()
        cnnRegression_movie = QMovie('./gifs/CNNRegression/cnnRegression.gif')
        cnnRegression_gif.setMovie(cnnRegression_movie)
        cnnRegression_movie.start()
        layout.addWidget(cnnRegression_gif)
        
        layout.addWidget(QLabel('f(x) is defined as needed. For example, the function for linear regression is defined as f(x) = Bias 2 + Score 1 * W1 + Score 2 * W2 + ... + Score m * Wm'))

        self.tab1.setLayout(layout)
