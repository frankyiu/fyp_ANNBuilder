import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CNNArchitectureTab(QTabWidget):
    def __init__(self, parent = None):
        super(CNNArchitectureTab, self).__init__(parent)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, 'The Critical Components of A CNN')
        self.addTab(self.tab2, 'The Typical Setup of A CNN')
        self.addTab(self.tab3, 'Further Remarks')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('CNN is characterized by several critical components listed as below:'))
        layout.addWidget(QLabel('1. Convolutional layer'))
        layout.addWidget(QLabel('2. Pooling Layer'))
        layout.addWidget(QLabel('3. Flattening Layer'))
        layout.addWidget(QLabel('4. Fully-connected Layer'))
        
        self.tab1.setLayout(layout)
        
    def tab2UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Here is the typical setup and the feedforword illustration of a simple CNN:'))

        cnnFeedforward_gif = QLabel()
        cnnFeedforward_movie = QMovie('./gifs/CNN/ArchitectureOfCNN/cnnFeedforward.gif')
        cnnFeedforward_gif.setMovie(cnnFeedforward_movie)
        cnnFeedforward_movie.start()
        layout.addWidget(cnnFeedforward_gif)

        layout.addWidget(QLabel('Check out the detailed operation of each component by visiting its own section.'))

        self.tab2.setLayout(layout)
        
    def tab3UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Note that, convolutional layer and pooling layer could be taken as a combination and be generalized to a more complicated structure with more layers.'))
        layout.addWidget(QLabel('After convolution and pooling, a flattening layer usually follows to reshape the output feature map into a feature vector and to feed the feature vector into the following fully-connected layer/layers.'))
        layout.addWidget(QLabel('The fully-connected layer/layers digest the information carried by the above feature vector and pass the output along for further processing.'))
        layout.addWidget(QLabel('The task objtective, i.e. classification or regression, determines how the output of its fully-connected layer would be further processed (refer to "CNN Classification" and "CNN Regression" for more details).'))
        layout.addWidget(QLabel('In the training phase, backpropagation is conducted as per the loss given by the loss function right after feedforward.'))

        self.tab3.setLayout(layout)

