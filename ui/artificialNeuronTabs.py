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
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('Artficial neuron is the basic building block of many advanced artificial neural networks.\nIt mimics a biological neuron by a general architecture as below:')
        label1.setWordWrap(True)
        layout.addWidget(label1)

        artificialNeuronArchitecture_graph = QLabel()
        artificialNeuronArchitecture_graph.setPixmap(QPixmap('./png/ArtificialNeuron/Introduction/artificialNeuronArchitecture.png').scaled(artificialNeuronArchitecture_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        artificialNeuronArchitecture_graph.setAlignment(Qt.AlignCenter)
        layout.addWidget(artificialNeuronArchitecture_graph)
        
        label2 = QLabel('An artificial neuron is characterized by 3 critical components:\n1. The weight of each line connecting the input nodes and the processing unit\n2. The activation function adopted by the processing unit\n3. The bias node')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('The weight of each line connecting the input nodes and the processing unit serves the purpose to scale the respective input.')
        label1.setWordWrap(True)
        layout.addWidget(label1)

        lb = QLabel()
        lb.setAlignment(Qt.AlignCenter)
        movie = QMovie('./gifs/ArtificialNeuron/TheWeightOfEachLine/theWeights.gif')
        lb.setMovie(movie)
        movie.start()
        layout.addWidget(lb)
        
        label2 = QLabel('The weights are usually adjustable to enable the neuron to learn to make more precise predictions.')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QVBoxLayout()
        
        label = QLabel('The activation funtion, i.e. the mathematical function adopted by the processing unit, determines how the processing unit handles the input data.')
        label.setWordWrap(True)
        layout.addWidget(label)

        lb = QLabel()
        lb.setAlignment(Qt.AlignCenter)
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
        
        label = QLabel('A bias node, a node apart from the input nodes, that adjusts the input value to the processing unit.')
        label.setWordWrap(True)
        layout.addWidget(label)
     
        lb = QLabel()
        lb.setAlignment(Qt.AlignCenter)
        movie = QMovie('./gifs/ArtificialNeuron/TheBias/theBias.gif')
        lb.setMovie(movie)
        movie.start()
        layout.addWidget(lb)
        
        self.tab4.setLayout(layout)
    
    def tab5UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('Putting all the pieces together, an artificial neuron generally operates as below:')
        label1.setWordWrap(True)
        layout.addWidget(label1)

        artificialNeuronDemo_gif = QLabel()
        artificialNeuronDemo_gif.setAlignment(Qt.AlignCenter)
        artificialNeuronDemo_movie = QMovie('./gifs/ArtificialNeuron/Conclusion/artificialNeuronDemo.gif')
        artificialNeuronDemo_gif.setMovie(artificialNeuronDemo_movie)
        artificialNeuronDemo_movie.start()
        layout.addWidget(artificialNeuronDemo_gif)
        
        label2 = QLabel('Different types of artificial neurons hence can be constructed easily by altering\n1. the weights\n2. the activation function\n3. the bias value')
        label2.setWordWrap(True)
        layout.addWidget(label2)

        self.tab5.setLayout(layout)
            
