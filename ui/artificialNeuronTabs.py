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
        
        lb = QLabel()
        movie = QMovie('./gifs/ArtificialNeuron/Introduction/introduction.gif')
        lb.setMovie(movie)
        movie.start()
        layout.addWidget(lb)
        
        layout.addWidget(QLabel('Artficial neuron is one of the basic building blocks of nearly all of the complicated artificial neural networks.'))
        layout.addWidget(QLabel('It mimics a biological neuron by the 3 critical components listed below:\n1. The weight of each line\n2. The mathematical function adopted by the processing unit\n3. The bias node'))
        
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('1. The weight of each line connecting the input nodes and the processing unit serves the purpose to scale the respective input.'))
 
        lb = QLabel()
        movie = QMovie('./gifs/ArtificialNeuron/TheWeightOfEachLine/theWeightOfEachLine.gif')
        lb.setMovie(movie)
        movie.start()
        layout.addWidget(lb)
        
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('2. The activation funtion, i.e. the mathematical function adopted by the processing unit, determines how the processing unit would handle the input data.'))

        lb = QLabel()
        movie = QMovie('./gifs/ArtificialNeuron/TheProcessingUnit/theProcessingUnit.gif')
        lb.setMovie(movie)
        movie.start()
        layout.addWidget(lb)
                
        self.tab3.setLayout(layout)

    def tab4UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('3. A bias node, a node apart from the input nodes, that would influence the input to the processing unit.'))
     
        lb = QLabel()
        movie = QMovie('./gifs/ArtificialNeuron/TheBias/theBias.gif')
        lb.setMovie(movie)
        movie.start()
        layout.addWidget(lb)
        
        self.tab4.setLayout(layout)
    
    def tab5UI(self):
        layout = QVBoxLayout()
        
        conclusion_graph = QLabel()
        conclusion_graph.setPixmap(QPixmap('./png/ArtificialNeuron/Conclusion/conclusion.png'))
        layout.addWidget(conclusion_graph)
        
        layout.addWidget(QLabel('Therefore, artificial neurons for various purposes can be constructed easily by altering\n1. the weights\n2. the activation function\n3. the bias value'))

        self.tab5.setLayout(layout)
            
