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
        
        layout.addWidget(QLabel('In supervised learning, an artificial neural network is usually connectd to a loss function.'))
        layout.addWidget(QLabel('In each prediction made, the loss function takes the outcome and the ground truth of the fed-in example as input and indicates the loss, i.e. accuracy, of the prediction.'))
        layout.addWidget(QLabel('In the learning process, the objective is to minimize the loss in predictions.'))
        layout.addWidget(QLabel('There are many loss functions available for neural network construction and they serve different purposes.'))
        layout.addWidget(QLabel('The most common three are going to be introduced in the following tabs.'))
        
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
                
        mae_graph = QLabel()
        mae_graph.setPixmap(QPixmap('./png/LossFunctions/mae.png'))
        layout.addWidget(mae_graph)
        
        mae_notations_graph = QLabel()
        mae_notations_graph.setPixmap(QPixmap('./png/LossFunctions/mae_notations.png'))
        layout.addWidget(mae_notations_graph)
              
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QVBoxLayout()
        
        mse_graph = QLabel()
        mse_graph.setPixmap(QPixmap('./png/LossFunctions/mse.png'))
        layout.addWidget(mse_graph)
        
        mse_notations_graph = QLabel()
        mse_notations_graph.setPixmap(QPixmap('./png/LossFunctions/mse_notations.png'))
        layout.addWidget(mse_notations_graph)
        
        self.tab3.setLayout(layout)
    
    def tab4UI(self):
        layout = QVBoxLayout()
                        
        ce_graph = QLabel()
        ce_graph.setPixmap(QPixmap('./png/LossFunctions/ce.png'))
        layout.addWidget(ce_graph)
        
        ce_notations_graph = QLabel()
        ce_notations_graph.setPixmap(QPixmap('./png/LossFunctions/ce_notations.png'))
        layout.addWidget(ce_notations_graph)
        
        self.tab4.setLayout(layout)
