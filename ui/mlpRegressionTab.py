import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MLPRegressionTab(QTabWidget):
    def __init__(self, parent = None):
        super(MLPRegressionTab, self).__init__(parent)

        self.tab1 = QWidget()

        self.addTab(self.tab1, 'MLP Regression')

        self.tab1UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('For regression problems, a function taking the the output values, the bias and the weight of each line connecting the output nodes and the function node as inputs, has to be defined.'))
        layout.addWidget(QLabel('The function gives the eventual output, which in turn will be fed into the loss function to calculate the loss.'))
        layout.addWidget(QLabel('Mean-squared error (MSE) and mean-absolute error (MAE) are two most commonly adopted loss functions in MLP regression. Other loss functions found suitable can also be applied as substitutes.'))
        layout.addWidget(QLabel('Here is the illustration of how the output values are further processed by a self-defined function f(x) in MLP regression:'))

        mlpRegression_gif = QLabel()
        mlpRegression_movie = QMovie('./gifs/MLPRegression/mlpRegression.gif')
        mlpRegression_gif.setMovie(mlpRegression_movie)
        mlpRegression_movie.start()
        layout.addWidget(mlpRegression_gif)

        layout.addWidget(QLabel('In the training phase, backpropagation is conducted as per the loss given by the loss function after each feedforward.'))

        self.tab1.setLayout(layout)
