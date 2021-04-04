import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class LossFunctionsTabs(QTabWidget):                # towardsdatascience
    def __init__(self, parent = None):
        super(LossFunctionsTabs, self).__init__(parent)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()

        self.addTab(self.tab1, 'Overview')
        self.addTab(self.tab2, 'MAE - Mean Absolute Error')
        self.addTab(self.tab3, 'MSE - Mean Squared Error')
        self.addTab(self.tab4, 'CE - Cross Entropy Loss')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('As illustrated in "Feedforward And Backpropagation", loss functions serve the purpose to guide the weight updates in backpropagation by indicating the accuracy of predictions against the corresponding ground truths.'))
        layout.addWidget(QLabel('There are many loss functions available for artificial neural network construction.'))
        layout.addWidget(QLabel('The most common three will be introduced in the following tabs.'))
        
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Mean Absolute Error'))
        
        mae_graph = QLabel()
        mae_graph.setPixmap(QPixmap('./png/LossFunctions/mae.png'))
        layout.addWidget(mae_graph)
        
        layout.addWidget(QLabel('n: the total number of training examples\nyi: the prediction on the i-th training example\nŷi: the ground truth of the i-th training example'))
      
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Mean Squared Error'))

        mse_graph = QLabel()
        mse_graph.setPixmap(QPixmap('./png/LossFunctions/mse.png'))
        layout.addWidget(mse_graph)
        
        layout.addWidget(QLabel('n: the total number of training examples\nyi: the prediction on the i-th training example\nŷi: the ground truth of the i-th training example'))

        self.tab3.setLayout(layout)
    
    def tab4UI(self):
        layout = QVBoxLayout()
                
        layout.addWidget(QLabel('Cross Entropy Loss'))
        
        ce_graph = QLabel()
        ce_graph.setPixmap(QPixmap('./png/LossFunctions/ce.png'))
        layout.addWidget(ce_graph)
        
        layout.addWidget(QLabel('n: the total number of training examples\nyi: the prediction on the i-th training example\nŷi: the ground truth of the i-th training example'))

        self.tab4.setLayout(layout)
