import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MLPRegressionTab(QTabWidget):
    def __init__(self, parent = None):
        super(MLPRegressionTab, self).__init__(parent)

        self.tab1 = QWidget()

        self.addTab(self.tab1, 'MLP Regression')
        
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
        
        label1 = QLabel('For regression problems, a function taking the the output values, the bias and the weight of each line connecting the output nodes and the function node as inputs, has to be defined.\nThe function gives the eventual output, which in turn will be fed into the loss function to calculate the loss.\nMean-squared error (MSE) and mean-absolute error (MAE) are two most commonly adopted loss functions in MLP regression. Other loss functions found suitable can also be applied as substitutes.\nHere is the illustration of how the output values are further processed by a self-defined function f(x) in MLP regression:')
        label1.setWordWrap(True)
        layout.addWidget(label1)

        mlpRegression_gif = QLabel()
        mlpRegression_gif.setAlignment(Qt.AlignCenter)
        mlpRegression_movie = QMovie('./gifs/MLPRegression/mlpRegression.gif')
        mlpRegression_gif.setMovie(mlpRegression_movie)
        mlpRegression_movie.start()
        layout.addWidget(mlpRegression_gif)
        
        label2 = QLabel('In the training phase, backpropagation is conducted as per the loss given by the loss function after each feedforward.')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        self.tab1.setLayout(layout)
