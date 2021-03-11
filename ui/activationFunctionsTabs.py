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
        
        layout.addWidget(QLabel('Activation function is the mathematical function adopted by the processing unit of an artificial neuron.'))
        layout.addWidget(QLabel('It dictates how the incoming data from the previous layer of nodes would be handled by the processing unit.'))
        layout.addWidget(QLabel('The input to the processing unit is generally the weighted sum of the input values to the previous layer of nodes.'))
        layout.addWidget(QLabel('Several common activation functions will be introduced in the following tabs.'))
        
        self.tab1.setLayout(layout)
    
    def tab2UI(self):
        layout = QVBoxLayout()
    
        layout.addWidget(QLabel('Step function only gives discrete outputs and needs a pre-defined threshold.\nIt is usually adopted to build perceptrons as illustrated previously.'))
        layout.addWidget(QLabel('Here is the typical setup of a step function with threshold = 2:'))

        stepFunction_graph = QLabel()
        stepFunction_graph.setPixmap(QPixmap('./png/ActivationFunctions/StepFunction/stepFunction.png'))
        layout.addWidget(stepFunction_graph)
        
        layout.addWidget(QLabel('The output is 1 if the input is equal to or larger than 2.\nOtherwise, the output is 0.'))
        layout.addWidget(QLabel('Pros: efficient computation'))
        layout.addWidget(QLabel('Cons: not compatible with backpropagation'))
        
        self.tab2.setLayout(layout)

    def tab3UI(self): 
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Linear function gives output proportional to the input.'))
        layout.addWidget(QLabel('Here is the typical setup of a linear function with slope = 1.'))

        linearFunction_graph = QLabel()
        linearFunction_graph.setPixmap(QPixmap('./png/ActivationFunctions/LinearFunction/linearFunction1.png'))
        layout.addWidget(linearFunction_graph)
        
        linearFunction_graph = QLabel()
        linearFunction_graph.setPixmap(QPixmap('./png/ActivationFunctions/LinearFunction/linearFunction2.png'))
        layout.addWidget(linearFunction_graph)
        
        layout.addWidget(QLabel('x: (-∞, ∞)'))
        layout.addWidget(QLabel('Range: (-∞, ∞)'))
        layout.addWidget(QLabel('Pros: efficient computation'))
        layout.addWidget(QLabel('Cons: not compatible with backpropagation'))
        
        self.tab3.setLayout(layout)
        
    def tab4UI(self):               # medium.com
        layout = QVBoxLayout()
        
        sigmoid_graph = QLabel()
        sigmoid_graph.setPixmap(QPixmap('./png/ActivationFunctions/Sigmoid/Sigmoid.png'))
        layout.addWidget(sigmoid_graph)
        
        layout.addWidget(QLabel('x: (-∞, ∞)'))
        layout.addWidget(QLabel('Range: [0, 1]'))
        layout.addWidget(QLabel('Non-zero-centered'))
        layout.addWidget(QLabel('Pros: efficient backpropagation'))
        layout.addWidget(QLabel('Cons: computationally expensive, could lead to saturated gradients'))
        
        self.tab4.setLayout(layout)

    def tab5UI(self):               #  medium.com
        layout = QVBoxLayout()
        
        tanh_graph = QLabel()
        tanh_graph.setPixmap(QPixmap('./png/ActivationFunctions/tanh/tanh.png'))
        layout.addWidget(tanh_graph)
        
        layout.addWidget(QLabel('x: (-∞, ∞)'))
        layout.addWidget(QLabel('Range: [-1, 1]'))
        layout.addWidget(QLabel('Zero-centered'))
        layout.addWidget(QLabel('Pros: efficient back propagation'))
        layout.addWidget(QLabel('Cons: could lead to saturated gradients'))
        
        self.tab5.setLayout(layout)
    
    def tab6UI(self):               # medium.com
        layout = QVBoxLayout()
                
        ReLU_graph = QLabel()
        ReLU_graph.setPixmap(QPixmap('./png/ActivationFunctions/ReLU/ReLU.png'))
        layout.addWidget(ReLU_graph)
        
        layout.addWidget(QLabel('x: (-∞, ∞)'))
        layout.addWidget(QLabel('Range: [0, ∞)'))
        layout.addWidget(QLabel('Pros: quickly converges, low cost of computation, would not saturate, efficient backpropagation'))
        layout.addWidget(QLabel('Cons: will lead to dead ReLU, i.e. gradient = 0, if the input is negative or equal to 0'))

        self.tab6.setLayout(layout)

    def tab7UI(self):               #  medium.com
        layout = QVBoxLayout()
     
        LeakyReLU_graph = QLabel()
        LeakyReLU_graph.setPixmap(QPixmap('./png/ActivationFunctions/LeakyReLU/LeakyReLU.png'))
        layout.addWidget(LeakyReLU_graph)
        
        layout.addWidget(QLabel('A variant of ReLU'))
        layout.addWidget(QLabel('x: (-∞, ∞)'))
        layout.addWidget(QLabel('Range: (-∞, ∞)'))
        layout.addWidget(QLabel('Pros: same as ReLU but has rectified the dead ReLU issue'))
        layout.addWidget(QLabel('Cons: computationally more expensive than ReLU'))

        self.tab7.setLayout(layout)
        
    def tab8UI(self):               #  medium.com
        layout = QVBoxLayout()
     
        ELU_graph = QLabel()
        ELU_graph.setPixmap(QPixmap('./png/ActivationFunctions/ELU/ELU.png'))
        layout.addWidget(ELU_graph)
        
        layout.addWidget(QLabel('Another variant of ReLU'))
        layout.addWidget(QLabel('x: (-∞, ∞)'))
        layout.addWidget(QLabel('Range: [-α, ∞)'))
        layout.addWidget(QLabel('Pros: same as ReLU but has rectified the dead ReLU issue'))
        layout.addWidget(QLabel('Cons: computationally more expensive than ReLU and Leaky ReLU'))
        
        self.tab8.setLayout(layout)
        
        
    def tab9UI(self):
        layout = QVBoxLayout()
     
        softmax_gif = QLabel()
        softmax_movie = QMovie('./gifs/ActivationFunctions/softmax.gif')
        softmax_gif.setMovie(softmax_movie)
        softmax_movie.start()
        layout.addWidget(softmax_gif)
        
        layout.addWidget(QLabel('Softmax function is generally applied on the last layer of nodes of a neural network, indicated by the "Z"s above.'))
        layout.addWidget(QLabel('Each of the eventual outputs, indicated by the "O"s above, would be normalized to [0, 1] and the "O"s sum up to 1.'))
        
        self.tab9.setLayout(layout) 
        
    def tab10UI(self):              # Wiki
        layout = QVBoxLayout()
     
        layout.addWidget(QLabel('Gaussian function has a general form as below, which a, b, c are real constants and c is not equal to 0:'))

        gaussian_eq = QLabel()
        gaussian_eq.setPixmap(QPixmap('./png/ActivationFunctions/Gaussian/gaussian_eq.png'))
        layout.addWidget(gaussian_eq)
        
        layout.addWidget(QLabel('The graph of the Gaussian function with a = 1, b = 0 and c = 1/sqrt(2):'))
        
        gaussian_graph = QLabel()
        gaussian_graph.setPixmap(QPixmap('./png/ActivationFunctions/Gaussian/gaussian_graph.png'))
        layout.addWidget(gaussian_graph)
        
        layout.addWidget(QLabel('x: (-∞, ∞)'))
        layout.addWidget(QLabel('Range: (0, 1]'))
        
        self.tab10.setLayout(layout)
    
    def tab11UI(self):          # Varsity Tutors
        layout = QVBoxLayout()
     
        sine_graph = QLabel()
        sine_graph.setPixmap(QPixmap('./png/ActivationFunctions/Sine/sineGraph.png'))
        layout.addWidget(sine_graph)
        
        layout.addWidget(QLabel('Sine function is a periodic function with a period = 2π, ie. sin(x) = sin(2nπ + x) where n is an integer.'))
        layout.addWidget(QLabel('x: (-∞, ∞)'))
        layout.addWidget(QLabel('Range: [-1, 1]'))
        layout.addWidget(QLabel('Apart from the simple sine function, there are some other activation functions derived from sin(x), eg. sin(x)/x.'))
        
        self.tab11.setLayout(layout)
