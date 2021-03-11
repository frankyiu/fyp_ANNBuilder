import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ArtificialNeuronTabs(QTabWidget):
    def __init__(self, parent = None):
        super(ArtificialNeuronTabs, self).__init__(parent)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        self.addTab(self.tab1, 'Introduction')
        self.addTab(self.tab2, 'The Weight Of Each Line')
        self.addTab(self.tab3, 'The Processing Unit')
        self.addTab(self.tab4, 'The Bias')
        self.addTab(self.tab5, 'Conclusion')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Artficial neuron is the basic building block of many advanced artificial neural networks.'))
        layout.addWidget(QLabel('It mimics a biological neuron by a general architecture as below:'))

        artificialNeuronArchitecture_graph = QLabel()
        artificialNeuronArchitecture_graph.setPixmap(QPixmap('./png/ArtificialNeuron/Introduction/artificialNeuronArchitecture.png'))
        layout.addWidget(artificialNeuronArchitecture_graph)
        
        layout.addWidget(QLabel('An artificial neuron is characterized by 3 critical components:\n1. The weight of each line connecting the input nodes and the processing unit\n2. The activation function adopted by the processing unit\n3. The bias node'))
        
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('The weight of each line connecting the input nodes and the processing unit serves the purpose to scale the respective input.'))
 
        lb = QLabel()
        movie = QMovie('./gifs/ArtificialNeuron/TheWeightOfEachLine/theWeights.gif')
        lb.setMovie(movie)
        movie.start()
        layout.addWidget(lb)
        
        layout.addWidget(QLabel('The weights are usually adjustable to enable the neuron to learn to make more precise predictions.'))
        
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('The activation funtion, i.e. the mathematical function adopted by the processing unit, determines how the processing unit handles the input data.'))

        lb = QLabel()
        movie = QMovie('./gifs/ArtificialNeuron/TheProcessingUnit/theActivationFunction.gif')
        lb.setMovie(movie)
        movie.start()
        layout.addWidget(lb)
        
        activationFunction_graph = QLabel()
        activationFunction_graph.setPixmap(QPixmap('./png/ArtificialNeuron/TheProcessingUnit/theActivationFunction.png'))
        layout.addWidget(activationFunction_graph)        
        self.tab3.setLayout(layout)

    def tab4UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('A bias node, a node apart from the input nodes, that adjusts the input value to the processing unit.'))
     
        lb = QLabel()
        movie = QMovie('./gifs/ArtificialNeuron/TheBias/theBias.gif')
        lb.setMovie(movie)
        movie.start()
        layout.addWidget(lb)
        
        self.tab4.setLayout(layout)
    
    def tab5UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Putting all the pieces together, an artificial neuron generally operates as below:'))

        artificialNeuronDemo_gif = QLabel()
        artificialNeuronDemo_movie = QMovie('./gifs/ArtificialNeuron/Conclusion/artificialNeuronDemo.gif')
        artificialNeuronDemo_gif.setMovie(artificialNeuronDemo_movie)
        artificialNeuronDemo_movie.start()
        layout.addWidget(artificialNeuronDemo_gif)
        
        layout.addWidget(QLabel('Different types of artificial neurons hence can be constructed easily by altering\n1. the weights\n2. the activation function\n3. the bias value'))

        self.tab5.setLayout(layout)
            
