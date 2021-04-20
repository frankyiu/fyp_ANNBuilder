import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class LossFunctionsTabs(QTabWidget):                # https://towardsdatascience.com/common-loss-functions-in-machine-learning-46af0ffc4d23
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

    def tab1UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('In supervised learning, an artificial neural network is usually connectd to a loss function.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('In each prediction made, the loss function takes the outcome and the ground truth of the fed-in example as input and indicates the loss, i.e. accuracy, of the prediction.')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        label3 = QLabel('In the learning process, the objective is to minimize the loss in predictions.')
        label3.setWordWrap(True)
        layout.addWidget(label3)
        
        label4 = QLabel('There are many loss functions available for neural network construction and they serve different purposes.')
        label4.setWordWrap(True)
        layout.addWidget(label4)
        
        label5 = QLabel('The most common three are going to be introduced in the following tabs.')
        label5.setWordWrap(True)
        layout.addWidget(label5)
        
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
                
        mae_graph = QLabel()
        mae_graph.setPixmap(QPixmap('./png/LossFunctions/mae.png').scaled(mae_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(mae_graph)
        
        mae_notations_graph = QLabel()
        mae_notations_graph.setPixmap(QPixmap('./png/LossFunctions/mae_notations.png').scaled(mae_notations_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(mae_notations_graph)
              
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QVBoxLayout()
        
        mse_graph = QLabel()
        mse_graph.setPixmap(QPixmap('./png/LossFunctions/mse.png').scaled(mse_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(mse_graph)
        
        mse_notations_graph = QLabel()
        mse_notations_graph.setPixmap(QPixmap('./png/LossFunctions/mse_notations.png').scaled(mse_notations_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(mse_notations_graph)
        
        self.tab3.setLayout(layout)
    
    def tab4UI(self):
        layout = QVBoxLayout()
                        
        ce_graph = QLabel()
        ce_graph.setPixmap(QPixmap('./png/LossFunctions/ce.png').scaled(ce_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(ce_graph)
        
        ce_notations_graph = QLabel()
        ce_notations_graph.setPixmap(QPixmap('./png/LossFunctions/ce_notations.png').scaled(ce_notations_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(ce_notations_graph)
        
        self.tab4.setLayout(layout)
