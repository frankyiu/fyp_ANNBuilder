import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class ConvolutionalLayerTabs(QTabWidget):
    def __init__(self, parent = None):
        super(ConvolutionalLayerTabs, self).__init__(parent)

        self.tabBar().setElideMode(Qt.ElideNone)
        self.tabBar().setUsesScrollButtons(True)
        
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tab7 = QWidget()
        
        self.addTab(self.tab1, 'Introduction')
        self.addTab(self.tab2, '2D Convolution')
        self.addTab(self.tab3, 'Different Types of Filters')
        self.addTab(self.tab4, 'Stride')
        self.addTab(self.tab5, 'Padding')
        self.addTab(self.tab6, 'A Convolutional Layer In A Neural Network')
        self.addTab(self.tab7, '2D Convolution On Multiple-channel Input Feature Maps')
        
        style = """
        QWidget{
            background-color: rgb(40, 44, 52);
        }
        QLabel{
            font-size: 12pt;
        }
        QPushButton{
            border: 2px solid black;
            background-color: lightgray;
            color: black;
            border-radius : 12px;
            padding: 4px;
            font-size: 12pt;
        }
        QPushButton::hover{
            background-color: gray;
            color: white;
        }
        QTabBar::tab{
            background: lightgray;
            color: black;
            border: 3;
            padding: 5px;
            max-width: 500px;
            height: 15px;
            border: 1px solid;
        }
        QTabBar::tab:selected {
            background: gray;
            color: white;
        }
        QTabBar QToolButton{
            background: rgb(40, 44, 52);
            color: lightgray;
            border-width: 5px;
        }
        QTabBar QToolButton:hover{
            color: white;
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

    def tab1UI(self):
        layout = QVBoxLayout() 
        
        label1 = QLabel('Convolution layer is one of the critical components of convolutional neural networks, which are mostly used for feature extraction from images.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('It uses and learns a set of kernels, also known as filters, to extract features from input images and generates a self-defined number of corresponding feature maps.')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        label3 = QLabel('The mathematical operation, namely convolution, taking place in a convolutional layer can either be 1D, 2D or 3D.')
        label3.setWordWrap(True)
        layout.addWidget(label3)
        
        label4 = QLabel('As 2D convolution is the most common form, the following discussion will focus on it.')
        label4.setWordWrap(True)
        layout.addWidget(label4)
        
        self.tab1.setLayout(layout)

    def tab2UI(self):               # https://www.deeplearningbook.org/contents/convnets.html
        layout = QVBoxLayout()
        
        label1 = QLabel('With a 3x4 input matrix, a 2x2 kernel, and stride = 1, 2D convolution will generate a 2x3 feature map as illustrated below:')
        label1.setWordWrap(True)
        layout.addWidget(label1)
                
        conv_gif = QLabel()
        conv_gif.setAlignment(Qt.AlignCenter)
        conv_movie = QMovie('./gifs/ConvolutionalLayer/2DConvolution/convolution.gif')
        conv_gif.setMovie(conv_movie)
        conv_movie.start()
        layout.addWidget(conv_gif)
        
        self.tab2.setLayout(layout)
        
    def tab3UI(self):               # Jame's Notes
        layout = QVBoxLayout()
        
        label4 = QLabel('The parameters of a kernel matrix, aka filter, determines how its ouput feature maps look like.')
        label4.setWordWrap(True)
        layout.addWidget(label4)
        
        label5 = QLabel('Here are the 3x3 examples of some frequently used filters:')
        label5.setWordWrap(True)
        layout.addWidget(label5)
                
        label1 = QLabel('1. vertical edge detector, used to detect vertical edges in input images')
        label1.setAlignment(Qt.AlignCenter)
        label1.setWordWrap(True)
        
        verticalEdgeDetector_graph = QLabel()
        verticalEdgeDetector_graph.setAlignment(Qt.AlignCenter)
        verticalEdgeDetector_graph.setPixmap(QPixmap('./png/ConvolutionalLayer/DifferentTypesOfFilters/verticalEdgeDetector.png'))
        
        layout1 = QHBoxLayout()
        layout1.addWidget(label1)
        layout1.addWidget(verticalEdgeDetector_graph)
        
        layout1Widget = QWidget()
        layout1Widget.setLayout(layout1)
        layout.addWidget(layout1Widget)
        
        label2 = QLabel('2. horizontal edge detector, used to detect horizontal edges in input images')
        label2.setAlignment(Qt.AlignCenter)
        label2.setWordWrap(True)
                
        horizontalEdgeDetector_graph = QLabel()
        horizontalEdgeDetector_graph.setAlignment(Qt.AlignCenter)
        horizontalEdgeDetector_graph.setPixmap(QPixmap('./png/ConvolutionalLayer/DifferentTypesOfFilters/horizontalEdgeDetector.png'))
        
        layout2 = QHBoxLayout()
        layout2.addWidget(label2)
        layout2.addWidget(horizontalEdgeDetector_graph)
        
        layout2Widget = QWidget()
        layout2Widget.setLayout(layout2)
        layout.addWidget(layout2Widget)
        
        label3 = QLabel('3. smoothing filter, used to blur input images')
        label3.setAlignment(Qt.AlignCenter)
        label3.setWordWrap(True)
        
        smoothingFilter_graph = QLabel()
        smoothingFilter_graph.setAlignment(Qt.AlignCenter)
        smoothingFilter_graph.setPixmap(QPixmap('./png/ConvolutionalLayer/DifferentTypesOfFilters/smoothingFilter.png'))

        layout3 = QHBoxLayout()
        layout3.addWidget(label3)
        layout3.addWidget(smoothingFilter_graph)
        
        layout3Widget = QWidget()
        layout3Widget.setLayout(layout3)
        layout.addWidget(layout3Widget)
        
        self.tab3.setLayout(layout)
    
    def tab4UI(self):              
        layout = QVBoxLayout()
     
        label1 = QLabel('"Stride" controls how a kernel steps through input matrices.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('Here is the setup of a 5x5 input matrix:')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        setup_graph = QLabel()
        setup_graph.setAlignment(Qt.AlignCenter)
        setup_graph.setObjectName('setup_graph')
        setup_graph.setPixmap(QPixmap('./png/ConvolutionalLayer/Stride/setup.png'))
        layout.addWidget(setup_graph)
        
        label3 = QLabel('Click one of the buttons below to see how a 3x3 kernel sweeps through the input matrix in each case:')
        label3.setWordWrap(True)
        layout.addWidget(label3)
        
        btn_layout = QHBoxLayout()
        
        btn_stride1 = QPushButton('Case 1: Stride = 1')
        btn_layout.addWidget(btn_stride1)
        btn_stride1.clicked.connect(self.switch_to_stride1_gif)
        
        btn_stride2 = QPushButton('Case 2: Stride = 2')
        btn_layout.addWidget(btn_stride2)
        btn_stride2.clicked.connect(self.switch_to_stride2_gif)
        
        btn_layout_widget = QWidget()
        btn_layout_widget.setLayout(btn_layout)
        
        layout.addWidget(btn_layout_widget)
        
        label4 = QLabel('Note that a corresponding cell is generated in the respective output matrix at each step of sweeping.\nThe sizes of the output matrices in Case 1 and Case 2 hence are 3x3 and 2x2 respectively.')
        label4.setWordWrap(True)
        layout.addWidget(label4)
        
        self.tab4.setLayout(layout)
        
    def switch_to_stride1_gif(self):
        stride1_movie = QMovie('./gifs/ConvolutionalLayer/Stride/stride1.gif')
        self.tab4.findChild(QLabel, 'setup_graph').setMovie(stride1_movie)
        stride1_movie.start()
        
    def switch_to_stride2_gif(self):
        stride2_movie = QMovie('./gifs/ConvolutionalLayer/Stride/stride2.gif')
        self.tab4.findChild(QLabel, 'setup_graph').setMovie(stride2_movie)
        stride2_movie.start()
        
    def tab5UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('"Padding" is a necessary measure to prevent the output matrices from shrinkage, i.e. align the sizes of the input matrices and the output matrices in convolution.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('It does so by adding a 1-unit wide frame to the original input matrices before starting any convolution.')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        label3 = QLabel('Zero-padding, i.e. all the padding cells are 0s, is the most common form of padding.')
        label3.setWordWrap(True)
        layout.addWidget(label3)
        
        label4 = QLabel('A zero-padded 2x2 input matrix has a size of 4x4 and looks like below:')
        label4.setWordWrap(True)
        layout.addWidget(label4)

        matrices_layout = QHBoxLayout()
        
        inputMatrix_graph = QLabel()
        inputMatrix_graph.setPixmap(QPixmap('./png/ConvolutionalLayer/Padding/inputMatrix.png'))
        matrices_layout.addWidget(inputMatrix_graph)
        
        zeroPaddedMatrix_graph = QLabel()
        zeroPaddedMatrix_graph.setPixmap(QPixmap('./png/ConvolutionalLayer/Padding/zeroPaddedMatrix.png'))
        matrices_layout.addWidget(zeroPaddedMatrix_graph)
        
        matrices_layout_widget = QWidget()
        matrices_layout_widget.setLayout(matrices_layout)
        
        layout.addWidget(matrices_layout_widget)
        
        self.tab5.setLayout(layout)
        
    def tab6UI(self):               # https://www.researchgate.net/figure/Input-and-output-feature-maps-of-a-convolutional-layer_fig1_334819564
        layout = QVBoxLayout()
                
        label1 = QLabel('A convolutional layer in a neural network often needs to handle fed-in data in multiple channels and output processed data in multiple channels as well.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('For example, the convolutional layer below has the number of input channels and the number of output channels both equal to 6:')
        label2.setWordWrap(True)
        layout.addWidget(label2)
                 
        example_graph = QLabel()
        example_graph.setAlignment(Qt.AlignCenter)
        example_graph.setPixmap(QPixmap('./png/ConvolutionalLayer/AConvolutionalLayerInANeuralNetwork/example.png'))
        layout.addWidget(example_graph)
        
        label3 = QLabel('Note that, the number of input channels and the number of output channels in a convolutional layer are not necessarily equal.')
        label3.setWordWrap(True)
        layout.addWidget(label3)
        
        label4 = QLabel('Besides, each output feature map, i.e. the output matrix of a certain channel, is generated by a unique kernel.\nThat is:\n1. The red output feature map above is generated by Kernel 1 by sweeping through all the input feature maps.\n2. The green output feature map above is generated by Kernel 2 by sweeping through all the input feature maps.')
        label4.setWordWrap(True)
        layout.addWidget(label4)
        
        label5 = QLabel('In addition, sizes of output feature maps are usually identical. This is also the case with input feature maps.')
        label5.setWordWrap(True)
        layout.addWidget(label5)
        
        self.tab6.setLayout(layout)
        
    def tab7UI(self):               # predictiveprogrammer.com
        layout = QVBoxLayout()
     
        label1 = QLabel('Let see how a kernel performs 2D convolution on a RGB input image and generates a corresponding output feature map:')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        demo_gif = QLabel()
        demo_gif.setAlignment(Qt.AlignCenter)
        demo_movie = QMovie('./gifs/ConvolutionalLayer/2DConvolutionOnMultichannelInputFeatureMaps/demo.gif')
        demo_gif.setMovie(demo_movie)
        demo_movie.start()
        layout.addWidget(demo_gif)
            
        label2 = QLabel('To generate n output feature maps, we use n kernels, each performs the above operation once to produce its respective output feature map.')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        self.tab7.setLayout(layout)
