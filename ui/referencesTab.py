import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ReferencesTab(QTabWidget):
    def __init__(self, parent = None):
        super(ReferencesTab, self).__init__(parent)

        self.tab1 = QWidget()

        self.addTab(self.tab1, 'References')
        
        self.tabBar().setAutoHide(True)
        
        self.setStyleSheet("background-color: rgb(40, 44, 52); font-size: 8pt;")

        self.tab1UI()

    def tab1UI(self):
        layout = QVBoxLayout()

        label1 = QLabel('1. The “Perceptron” stack is based on: T. Y. Kwok, “Perceptrons,” lecture notes for COMP4211, Department of Computer Science and Engineering, Hong Kong University of Science and Technology, Sep. 1, 2020.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('2. The “Adaline” stack is based on: T. Y. Kwok, “Adaline,” lecture notes for COMP4211, Department of Computer Science and Engineering, Hong Kong University of Science and Technology, Sep. 1, 2020.')
        label2.setWordWrap(True)
        layout.addWidget(label2)

        label3 = QLabel('3. The “Feedforward and Backpropagation” stack is based on: F. F. Li, J. Johnson and S. Yeung, “CS231n Convolutional Neural Networks for Visual Recognition Lecture 4: Backpropagation and Neural Networks,” Stanford University, 2018. [Lecture slides]. Available: http://cs231n.stanford.edu/slides/2018/cs231n_2018_lecture04.pdf.')
        label3.setWordWrap(True)
        layout.addWidget(label3)
        
        label4 = QLabel('4. For the “Activation Functions” stack:\n- The “Sigmoid”, “tanh”, “ReLU”, “Leaky ReLU” tabs are based on: N. Kumar, “Deep Learning Best Practices: Activation Functions & Weight Initialization Methods – Part1,” May. 5, 2019. [Blog]. Available: https://medium.datadriveninvestor.com/deep-learning-best-practices-activation-functions-weight-initialization-methods-part-1-c235ff976ed [Accessed Jan. 20, 2021].\n\n- The “ELU” tab is based on: S. Jadon, “Introduction to Different Activation Functions for Deep Learning,” May. 16, 2018. [Blog]. Available: https://medium.com/@shrutijadon10104776/survey-on-activation-functions-for-deep-learning-9689331ba092 [Accessed Jan. 20, 2021].\n\n- The “Softmax” tab is based on: DeepAI, Softmax Function, 201?. [Online]. Available: https://deepai.org/machine-learning-glossary-and-terms/softmax-layer [Accessed Jan. 20, 2021].\n\n- The “Gaussian” tab is based on: Wikipedia, Gaussian function. [Online]. Available: https://en.wikipedia.org/wiki/Gaussian_function [Accessed Jan. 20, 2021].')
        label4.setWordWrap(True)
        layout.addWidget(label4)
        
        label5 = QLabel('5. The “Loss Functions” stack is based on: R. Parmar, “Common loss functions in machine learning,” Sep. 2, 2018. [Blog]. Available: https://towardsdatascience.com/common-loss-functions-in-machine-learning-46af0ffc4d23 [Accessed Jan. 20, 2021].')
        label5.setWordWrap(True)
        layout.addWidget(label5)
        
        label6 = QLabel('6. The “Optimizers” stack is based on: S. Patrikar, “Batch, Mini Batch & Stochastic Gradient Descent,” Oct. 1, 2019. [Blog]. Available: https://towardsdatascience.com/batch-mini-batch-stochastic-gradient-descent-7a62ecba642a [Accessed Jan. 20, 2021].')
        label6.setWordWrap(True)
        layout.addWidget(label6)
        
        label7 = QLabel('7. The “Underfitting and Overfitting” stack is based on: GeeksforGeeks, Underfitting and Overfitting in Machine Learning. [Online]. Available: https://www.geeksforgeeks.org/underfitting-and-overfitting-in-machine-learning/ [Accessed Jan. 20, 2021].')
        label7.setWordWrap(True)
        layout.addWidget(label7)
        
        label8 = QLabel('8. For the “Regularization” stack:\n- The “L1 Regularization” and “L2 Regularization” tabs are based on: ML Cheatsheet – Read the Docs, Regularization. [Online]. Available: https://ml-cheatsheet.readthedocs.io/en/latest/regularization.html#l1-regularization [Accessed Jan 20. 2021].\n\n- The “Elastic Net” tab is based on: Z. Hui, and T. Hastie, “Regularization and Variable Selection via the Elastic Net,” J. of the Royal Statistical Society: Series B (Statistical Methodology) 67 (2). pp. 301–20, Dec 2003.')
        label8.setWordWrap(True)
        layout.addWidget(label8)
        
        label9 = QLabel('9. For the “Convolutional Layer” stack:\n- The “2D Convolution” tab is based on: I. Goodfellow, Y. Bengio, and A. Courville, “9 Convolutional Networks,” in Deep Learning. Cambridge: The MIT Press, 2016, pp. 330. [ebook]. Available: https://www.deeplearningbook.org/ [Accessed Jan. 20, 2021].\n\n- The “A Convolutional Layer in a Neural Network” tab is based on: M. P. Véstias, “A Survey of Convolutional Neural Networks on Edge with Reconfigurable Computing,” Algorithms, vol. 12, no.8, p. 154, Jul. 2019.\n\n- The “2D Convolutional on Multiple-channel Input Features Maps” is based on: P. Malhotra, “Famous Convolutional Neural Network Architectures - #1,” 2018. [gif]. Available: https://predictiveprogrammer.com/famous-convolutional-neuralnetwork-architectures-1/ [Accessed Jan. 15, 2021].')
        label9.setWordWrap(True)
        layout.addWidget(label9)

        self.tab1.setLayout(layout)
        
