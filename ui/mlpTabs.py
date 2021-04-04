import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MLPTabs(QTabWidget):                
    def __init__(self, parent = None):
        super(MLPTabs, self).__init__(parent)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, 'The Structure Of A Multi-layer Perceptron')
        self.addTab(self.tab2, 'Training A Multi-layer Perceptron')
        self.addTab(self.tab3, 'Application Of Multi-layer Perceptrons')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Here is the general structure of a multi-layer perceptron containing just 1 hidden layer:'))
        
        mlpStructure_graph = QLabel()
        mlpStructure_graph.setPixmap(QPixmap('./png/MultilayerPerceptron/StructureOfAMultilayerPerceptron/mlpStructure.png'))
        layout.addWidget(mlpStructure_graph)
        
        layout.addWidget(QLabel('Notice that, the number of the hidden layers can be incremented arbitrarily as needed.'))
        layout.addWidget(QLabel('In addition, the activation function of the hidden units must be non-linear and differentiable, as to enable backpropagation in training.'))

        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Consider a simple multi-layer perceptron illustrated as below:'))
              
        lb = QLabel()
        movie = QMovie('./gifs/MultilayerPerceptron/TrainingOfAMultilayerPerceptron/trainingOfAMlp.gif')
        lb.setMovie(movie)
        movie.start()
        layout.addWidget(lb)
        
        layout.addWidget(QLabel('Training of a multi-layer perceptron with 1 fed-in example involves 3 steps:\n1. feeding forward the pre-processed data of the fed-in example\n2. call the loss function with the predicted outcome, ŷ, and the ground truth, y, to determine the accuracy\n3. adjust the weight of each line accordingly in backpropagation'))
        layout.addWidget(QLabel('Note that, the training purpose is to minimize the loss function by finding the optimal weight for each line in the neural network.'))
        
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QVBoxLayout()
                
        layout.addWidget(QLabel('Multi-layer Perceptrons are well-suited to classification tasks involving categorical items.'))
        layout.addWidget(QLabel('Examples of real-world application of multi-layer perceptrons involve:\n1. speech recognition\n2. image recognition'))
        
        self.tab3.setLayout(layout)
