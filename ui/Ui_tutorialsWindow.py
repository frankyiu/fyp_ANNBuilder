#### -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/cad/Desktop/eric6IDEWorkingDir/Tutorials/ui/tutorialsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from .basicConceptsTab import BasicConceptsTab
from .artificialNeuronTabs import ArtificialNeuronTabs
from .activationFunctionsTabs import ActivationFunctionsTabs
from .perceptronTabs import PerceptronTabs
from .adalineTabs import AdalineTabs
from .feedforwardAndBackpropagationTabs import FeedforwardAndBackpropagationTabs
from .lossFunctionsTabs import LossFunctionsTabs
from .optimizersTabs import OptimizersTabs
from .underfittingAndOverfittingTabs import UnderfittingAndOverfittingTabs
from .regularizationTabs import RegularizationTabs
from .mlpTabs import MLPTabs
from .mlpApplicationTab import MLPApplicationTab
from .mlpArchitectureTab import MLPArchitectureTab
from .mlpClassificationTab import MLPClassificationTab
from .mlpRegressionTab import MLPRegressionTab
from .cnnTabs import CNNTabs
from .cnnApplicationTab import CNNApplicationTab
from .cnnArchitectureTab import CNNArchitectureTab
from .convolutionalLayerTabs import ConvolutionalLayerTabs
from .poolingLayerTabs import PoolingLayerTabs
from .flatteningLayerTabs import FlatteningLayerTabs
from .fullyconnectedLayerTabs import FullyconnectedLayerTabs
from .cnnClassificationTab import CNNClassificationTab
from .cnnRegressionTab import CNNRegressionTab

class Ui_tutorialsWindow(QWidget):
    def __init__(self, parent):
        super(Ui_tutorialsWindow, self).__init__(parent)
        self.setGeometry(300,50,10,10)
        self.setWindowTitle('Tutorials')

        self.leftlist = QListWidget()
        self.leftlist.setMinimumSize(QSize(200, 0))
        self.leftlist.insertItem(0, 'Basic Concepts')
        self.leftlist.insertItem(1, '       Artificial Neuron')
        self.leftlist.insertItem(2, '       Perceptron')
        self.leftlist.insertItem(3, '       Adaline')
        self.leftlist.insertItem(4, '       Activation Functions')
        self.leftlist.insertItem(5, '       Feedforward and Backpropagation')
        self.leftlist.insertItem(6, '       Loss Functions')
        self.leftlist.insertItem(7, '       Optimizers')
        self.leftlist.insertItem(8, '       Underfitting and Overfitting')
        self.leftlist.insertItem(9, '       Regularization')
        self.leftlist.insertItem(10, 'Multi-layer Perceptron')
        self.leftlist.insertItem(11, '      Application of MLP')
        self.leftlist.insertItem(12, '      Architecture of MLP')
        self.leftlist.insertItem(13, '      MLP Classification')
        self.leftlist.insertItem(14, '      MLP Regression')
        self.leftlist.insertItem(15, 'Convolutional Neural Network')
        self.leftlist.insertItem(16, '      Application of CNN')
        self.leftlist.insertItem(17, '      Architecture of CNN')
        self.leftlist.insertItem(18, '      Convolutional Layer')
        self.leftlist.insertItem(19, '      Pooling Layer')
        self.leftlist.insertItem(20, '      Flattening Layer')
        self.leftlist.insertItem(21, '      Fully-connected Layer')
        self.leftlist.insertItem(22, '      CNN Classification')
        self.leftlist.insertItem(23, '      CNN Regression')

        self.stack1 = QWidget()
        self.stack2 = QWidget()
        self.stack3 = QWidget()
        self.stack4 = QWidget()
        self.stack5 = QWidget()
        self.stack6 = QWidget()
        self.stack7 = QWidget()
        self.stack8 = QWidget()
        self.stack9 = QWidget()
        self.stack10 = QWidget()
        self.stack11 = QWidget()
        self.stack12 = QWidget()
        self.stack13 = QWidget()
        self.stack14 = QWidget()
        self.stack15 = QWidget()
        self.stack16 = QWidget()
        self.stack17 = QWidget()
        self.stack18 = QWidget()
        self.stack19 = QWidget()
        self.stack20 = QWidget()
        self.stack21 = QWidget()
        self.stack22 = QWidget()
        self.stack23 = QWidget()
        self.stack24 = QWidget()

        self.stack1UI()
        self.stack2UI()
        self.stack3UI()
        self.stack4UI()
        self.stack5UI()
        self.stack6UI()
        self.stack7UI()
        self.stack8UI()     
        self.stack9UI()
        self.stack10UI()
        self.stack11UI()
        self.stack12UI()
        self.stack13UI()
        self.stack14UI()        
        self.stack15UI()
        self.stack16UI()
        self.stack17UI()
        self.stack18UI()
        self.stack19UI()
        self.stack20UI()        
        self.stack21UI()
        self.stack22UI()
        self.stack23UI()
        self.stack24UI()

        self.stack = QStackedWidget(self)

        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        self.stack.addWidget(self.stack3)
        self.stack.addWidget(self.stack4)
        self.stack.addWidget(self.stack5)
        self.stack.addWidget(self.stack6)
        self.stack.addWidget(self.stack7)
        self.stack.addWidget(self.stack8)   
        self.stack.addWidget(self.stack9)
        self.stack.addWidget(self.stack10)
        self.stack.addWidget(self.stack11)
        self.stack.addWidget(self.stack12)
        self.stack.addWidget(self.stack13)
        self.stack.addWidget(self.stack14)
        self.stack.addWidget(self.stack15)
        self.stack.addWidget(self.stack16)
        self.stack.addWidget(self.stack17)
        self.stack.addWidget(self.stack18)
        self.stack.addWidget(self.stack19)
        self.stack.addWidget(self.stack20)
        self.stack.addWidget(self.stack21)
        self.stack.addWidget(self.stack22)
        self.stack.addWidget(self.stack23)
        self.stack.addWidget(self.stack24)

        HBox = QHBoxLayout()
        HBox.addWidget(self.leftlist)
        HBox.addWidget(self.stack)

        self.setLayout(HBox)

        self.leftlist.currentRowChanged.connect(self.display)
        
    def stack1UI(self):
        layout = QHBoxLayout()
        
        basicConceptsTab = BasicConceptsTab()
        layout.addWidget(basicConceptsTab)
        
        self.stack1.setLayout(layout)
        
    def stack2UI(self):
        layout = QHBoxLayout()
        
        artificialNeuronTabs = ArtificialNeuronTabs()
        layout.addWidget(artificialNeuronTabs)
        
        self.stack2.setLayout(layout)

    def stack3UI(self):
        layout = QHBoxLayout()
        
        perceptronTabs = PerceptronTabs()
        perceptronTabs.setObjectName('perceptronTabs')
        layout.addWidget(perceptronTabs)

        self.stack3.setLayout(layout)

    def stack4UI(self):
        layout = QVBoxLayout()

        adalineTabs = AdalineTabs()        
        layout.addWidget(adalineTabs)
        
        self.stack4.setLayout(layout)
        
    def stack5UI(self):
        layout = QVBoxLayout()
        
        activationFunctionsTabs = ActivationFunctionsTabs()        
        layout.addWidget(activationFunctionsTabs)

        self.stack5.setLayout(layout)

    def stack6UI(self):
        layout = QVBoxLayout()
        
        feedforwardAndBackpropagationTabs = FeedforwardAndBackpropagationTabs()        
        layout.addWidget(feedforwardAndBackpropagationTabs)

        self.stack6.setLayout(layout)

    def stack7UI(self):
        layout = QVBoxLayout()
        
        lossFunctionsTabs = LossFunctionsTabs()        
        layout.addWidget(lossFunctionsTabs)

        self.stack7.setLayout(layout)
        
    def stack8UI(self):
        layout = QVBoxLayout()
        
        optimizersTabs = OptimizersTabs()        
        layout.addWidget(optimizersTabs)

        self.stack8.setLayout(layout)
        
    def stack9UI(self):
        layout = QVBoxLayout()
                
        underfittingAndOverfittingTabs = UnderfittingAndOverfittingTabs()        
        layout.addWidget(underfittingAndOverfittingTabs)
        
        self.stack9.setLayout(layout)
        
    def stack10UI(self):
        layout = QVBoxLayout()
        
        regularizationTabs = RegularizationTabs()        
        layout.addWidget(regularizationTabs)

        self.stack10.setLayout(layout)
    
    def stack11UI(self):
        layout = QVBoxLayout()
           
        mlpTabs = MLPTabs()        
        layout.addWidget(mlpTabs)
        
        self.stack11.setLayout(layout)    
        
    def stack12UI(self):
        layout = QVBoxLayout()
           
        mlpApplicationTab = MLPApplicationTab()        
        layout.addWidget(mlpApplicationTab)
        
        self.stack12.setLayout(layout)    
        
    def stack13UI(self):
        layout = QVBoxLayout()
           
        mlpArchitectureTab = MLPArchitectureTab()        
        layout.addWidget(mlpArchitectureTab)
        
        self.stack13.setLayout(layout)    
        
    def stack14UI(self):
        layout = QVBoxLayout()
           
        mlpClassificationTab = MLPClassificationTab()        
        layout.addWidget(mlpClassificationTab)
    
        self.stack14.setLayout(layout) 
        
    def stack15UI(self):
        layout = QVBoxLayout()
           
        mlpRegressionTab = MLPRegressionTab()        
        layout.addWidget(mlpRegressionTab)
        
        self.stack15.setLayout(layout) 
        
    def stack16UI(self):
        layout = QVBoxLayout()
           
        cnnTabs = CNNTabs()        
        layout.addWidget(cnnTabs)
        
        self.stack16.setLayout(layout)    
        
    def stack17UI(self):
        layout = QVBoxLayout()
           
        cnnApplicationTab = CNNApplicationTab()        
        layout.addWidget(cnnApplicationTab)
        
        self.stack17.setLayout(layout)   
        
    def stack18UI(self):
        layout = QVBoxLayout()
           
        cnnArchitectureTab = CNNArchitectureTab()        
        layout.addWidget(cnnArchitectureTab)
        
        self.stack18.setLayout(layout)    
    
    def stack19UI(self):
        layout = QVBoxLayout()
        
        convolutionalLayerTabs = ConvolutionalLayerTabs()        
        layout.addWidget(convolutionalLayerTabs)
        
        self.stack19.setLayout(layout)
        
    def stack20UI(self):
        layout = QVBoxLayout()
        
        poolingLayerTabs = PoolingLayerTabs()        
        layout.addWidget(poolingLayerTabs)
        
        self.stack20.setLayout(layout)    
    
    def stack21UI(self):
        layout = QVBoxLayout()
        
        flatteningLayerTabs = FlatteningLayerTabs()        
        layout.addWidget(flatteningLayerTabs)
        
        self.stack21.setLayout(layout)
    
    def stack22UI(self):
        layout = QVBoxLayout()
        
        fullyconnectedLayerTabs = FullyconnectedLayerTabs()        
        layout.addWidget(fullyconnectedLayerTabs)
        
        self.stack22.setLayout(layout)
        
    def stack23UI(self):
        layout = QVBoxLayout()
        
        cnnClassificationTab = CNNClassificationTab()        
        layout.addWidget(cnnClassificationTab)
        
        self.stack23.setLayout(layout)
        
    def stack24UI(self):
        layout = QVBoxLayout()
        
        cnnRegressionTab = CNNRegressionTab()        
        layout.addWidget(cnnRegressionTab)
        
        self.stack24.setLayout(layout)
        
    def display(self, i):
        self.stack.setCurrentIndex(i)
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Ui_tutorialsWindow = Ui_tutorialsWindow()
    Ui_tutorialsWindow.show()
    sys.exit(app.exec_())

