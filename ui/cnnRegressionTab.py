import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CNNRegressionTab(QTabWidget):
    def __init__(self, parent = None):
        super(CNNRegressionTab, self).__init__(parent)

        self.tab1 = QWidget()

        self.addTab(self.tab1, 'CNN Regression')
        
        style = """
        QWidget{
            background-color: rgb(40, 44, 52);
        }
        QLabel{
            font-size: 16pt;
        }
        """
        self.setStyleSheet(style)
        
        self.tab1UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('In the case of regression, a function of the score vector, the weights of each line connecting the score nodes and the output node, as well as the bias, needs to be defined.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('In the training phase, the output is passed into a loss function and backpropagation will then be conducted as per the calculated loss.')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        label3 = QLabel('Mean-squared error, MSE, is the most common loss function used in CNN regression. Some other functions, like mean-absolute error, can be used as substitutes.')
        label3.setWordWrap(True)
        layout.addWidget(label3)
        
        label4 = QLabel('Here is an illustration of the very last stage of CNN regression adpoting MSE as its loss function:')
        label4.setWordWrap(True)
        layout.addWidget(label4)

        cnnRegression_gif = QLabel()
        cnnRegression_gif.setAlignment(Qt.AlignCenter)
        cnnRegression_movie = QMovie('./gifs/CNNRegression/cnnRegression.gif')
        cnnRegression_gif.setMovie(cnnRegression_movie)
        cnnRegression_movie.start()
        layout.addWidget(cnnRegression_gif)
        
        label5 = QLabel('f(x) is defined as needed. For example, the function for linear regression is defined as f(x) = Bias 2 + Score 1 * W1 + Score 2 * W2 + ... + Score m * Wm')
        label5.setWordWrap(True)
        layout.addWidget(label5)
        
        self.tab1.setLayout(layout)
