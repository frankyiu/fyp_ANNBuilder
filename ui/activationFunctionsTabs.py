import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ActivationFunctionsTabs(QTabWidget):
    def __init__(self, parent = None):
        super(ActivationFunctionsTabs, self).__init__(parent)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tab7 = QWidget()
        self.tab8 = QWidget()
        self.tab9 = QWidget()
        self.tab10 = QWidget()
        self.tab11 = QWidget()

        self.addTab(self.tab1, 'Introduction')        
        self.addTab(self.tab2, 'Step Function')
        self.addTab(self.tab3, 'Linear Function')
        self.addTab(self.tab4, 'Sigmoid')
        self.addTab(self.tab5, 'tanh - Hyperbolic Tangent')
        self.addTab(self.tab6, 'ReLU - Rectified Linear Unit')
        self.addTab(self.tab7, 'Leakky ReLU - Leaky Rectified Linear Unit')
        self.addTab(self.tab8, 'ELU - Exponential Linear Unit')
        self.addTab(self.tab9, 'Softmax')
        self.addTab(self.tab10, 'Gaussian')
        self.addTab(self.tab11, 'Sine')
        
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
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()
        self.tab6UI()
        self.tab7UI()
        self.tab8UI()
        self.tab9UI()
        self.tab10UI()
        self.tab11UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('Activation function is the mathematical function adopted by the processing unit of an artificial neuron.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('It dictates how the incoming data from the previous layer of nodes would be handled by the processing unit.')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        label3 = QLabel('The input to the processing unit is generally the weighted sum of the input values to the previous layer of nodes.')
        label3.setWordWrap(True)
        layout.addWidget(label3)
        
        label4 = QLabel('Several common activation functions will be introduced in the following tabs.')
        label4.setWordWrap(True)
        layout.addWidget(label4)
        
        self.tab1.setLayout(layout)
    
    def tab2UI(self):
        layout = QVBoxLayout()
    
        label1 = QLabel('Step function gives discrete outputs.\nThe threshold of a step function defines most of its properties.\n')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('Here is the typical setup of a step function:')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        stepFunction_graph = QLabel()
        stepFunction_graph.setPixmap(QPixmap('./png/ActivationFunctions/StepFunction/stepFunction.png').scaled(stepFunction_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(stepFunction_graph)
        
        label3 = QLabel('Pros: efficient computation\nCons: not compatible with backpropagation')
        label3.setWordWrap(True)
        layout.addWidget(label3)
        
        self.tab2.setLayout(layout)

    def tab3UI(self): 
        layout = QVBoxLayout()

        linearFunction_graph = QLabel()
        linearFunction_graph.setPixmap(QPixmap('./png/ActivationFunctions/LinearFunction/linearFunction1.png'))
        layout.addWidget(linearFunction_graph)
        
        linearFunction_graph2 = QLabel()
        linearFunction_graph2.setPixmap(QPixmap('./png/ActivationFunctions/LinearFunction/linearFunction2.png'))
        layout.addWidget(linearFunction_graph2)
        
        label1 = QLabel('x: (-∞, ∞)\nRange: (-∞, ∞)\nPros: efficient computation\nCons: not compatible with backpropagation')
        label1.setWordWrap(True)
        layout.addWidget(label1)

        self.tab3.setLayout(layout)
        
    def tab4UI(self):               # medium.com
        layout = QVBoxLayout()
        
        sigmoid_graph = QLabel()
        sigmoid_graph.setPixmap(QPixmap('./png/ActivationFunctions/Sigmoid/Sigmoid.png').scaled(sigmoid_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(sigmoid_graph)
        
        label = QLabel('x: (-∞, ∞)\nRange: [0, 1]\nNon-zero-centered\nPros: efficient backpropagation\nCons: computationally expensive, could lead to saturated gradients')
        label.setWordWrap(True)
        layout.addWidget(label)
        
        self.tab4.setLayout(layout)

    def tab5UI(self):               #  medium.com
        layout = QVBoxLayout()
        
        tanh_graph = QLabel()
        tanh_graph.setPixmap(QPixmap('./png/ActivationFunctions/tanh/tanh.png').scaled(tanh_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(tanh_graph)
        
        label = QLabel('x: (-∞, ∞)\nRange: [-1, 1]\nZero-centered\nPros: efficient back propagation\nCons: could lead to saturated gradients')
        label.setWordWrap(True)
        layout.addWidget(label)
        
        self.tab5.setLayout(layout)
    
    def tab6UI(self):               # medium.com
        layout = QVBoxLayout()
                
        ReLU_graph = QLabel()
        ReLU_graph.setPixmap(QPixmap('./png/ActivationFunctions/ReLU/ReLU.png').scaled(ReLU_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(ReLU_graph)
        
        label = QLabel('x: (-∞, ∞)\nRange: [0, ∞)\nPros: quickly converges, low cost of computation, would not saturate, efficient backpropagation\nCons: will lead to dead ReLU, i.e. gradient = 0, if the input is negative or equal to 0')
        label.setWordWrap(True)
        layout.addWidget(label)
        
        self.tab6.setLayout(layout)

    def tab7UI(self):               #  medium.com
        layout = QVBoxLayout()
     
        LeakyReLU_graph = QLabel()
        LeakyReLU_graph.setPixmap(QPixmap('./png/ActivationFunctions/LeakyReLU/LeakyReLU.png').scaled(LeakyReLU_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(LeakyReLU_graph)
        
        label = QLabel('A variant of ReLU\nx: (-∞, ∞)\nRange: (-∞, ∞)\nPros: same as ReLU but has rectified the dead ReLU issue\nCons: computationally more expensive than ReLU')
        label.setWordWrap(True)
        layout.addWidget(label)

        self.tab7.setLayout(layout)
        
    def tab8UI(self):               #  medium.com
        layout = QVBoxLayout()
     
        ELU_graph = QLabel()
        ELU_graph.setPixmap(QPixmap('./png/ActivationFunctions/ELU/ELU.png').scaled(ELU_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(ELU_graph)
        
        label = QLabel('Another variant of ReLU\nx: (-∞, ∞)\nRange: [-a, ∞)\nPros: same as ReLU but has rectified the dead ReLU issue\nCons: computationally more expensive than ReLU and Leaky ReLU')
        label.setWordWrap(True)
        layout.addWidget(label)
        
        self.tab8.setLayout(layout)
        
        
    def tab9UI(self):
        layout = QVBoxLayout()
     
        softmax_gif = QLabel()
        softmax_movie = QMovie('./gifs/ActivationFunctions/softmax.gif')
        softmax_gif.setMovie(softmax_movie)
        softmax_movie.start()
        layout.addWidget(softmax_gif)
        
        label = QLabel('Softmax function is generally applied on the last layer of nodes of a neural network, indicated by the "Z"s above.\nEach of the eventual outputs, indicated by the "O"s above, would be normalized to [0, 1] and the values sum up to 1.')
        label.setWordWrap(True)
        layout.addWidget(label)
        
        self.tab9.setLayout(layout) 
        
    def tab10UI(self):              # Wiki
        layout = QVBoxLayout()
     
        label1 = QLabel('Gaussian function has a general form as below, which a, b, c are real constants and c is not equal to 0:')
        label1.setWordWrap(True)
        layout.addWidget(label1)

        gaussian_eq = QLabel()
        gaussian_eq.setPixmap(QPixmap('./png/ActivationFunctions/Gaussian/gaussian_eq.png').scaled(gaussian_eq.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(gaussian_eq)
        
        label2 = QLabel('The graph of the Gaussian function with a = 1, b = 0 and c = 1/sqrt(2):')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        gaussian_graph = QLabel()
        gaussian_graph.setPixmap(QPixmap('./png/ActivationFunctions/Gaussian/gaussian_graph.png').scaled(gaussian_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(gaussian_graph)
        
        label3 = QLabel('x: (-∞, ∞)\nRange: (0, 1]')
        label3.setWordWrap(True)
        layout.addWidget(label3)
        
        self.tab10.setLayout(layout)
    
    def tab11UI(self):          # Varsity Tutors
        layout = QVBoxLayout()
     
        sine_graph = QLabel()
        sine_graph.setPixmap(QPixmap('./png/ActivationFunctions/Sine/sinGraph.png').scaled(sine_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(sine_graph)
        
        label = QLabel('Sine function is a periodic function with a period = 2π radian, ie. sin(x) = sin(2nπ + x) where n is an integer.\nx: (-∞, ∞)\nRange: [-1, 1]\nApart from the simple sine function, there are some other activation functions derived from sin(x), eg. sin(x)/x.')
        label.setWordWrap(True)
        layout.addWidget(label)
        
        self.tab11.setLayout(layout)
