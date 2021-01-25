import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class RegularizationTabs(QTabWidget):           # ml-cheatsheet.readthedocs.io
    def __init__(self, parent = None):
        super(RegularizationTabs, self).__init__(parent)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tab6 = QWidget()
        self.tab7 = QWidget()

        self.addTab(self.tab1, 'Introduction')
        self.addTab(self.tab2, 'L1 Regularization')
        self.addTab(self.tab3, 'L2 Regularization')
        self.addTab(self.tab4, 'L3 Regularization')
        self.addTab(self.tab5, 'L0.5 Regularization')
        self.addTab(self.tab6, 'Lp Regularization')
        self.addTab(self.tab7, 'Elastic Net Regularization')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()
        self.tab6UI()
        self.tab7UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Regularization is a common strategy used in regression models to mitigate overfitting.'))
        layout.addWidget(QLabel('Say, we have a simple linear regression model as below:'))
        
        simpleRegressionModel_graph = QLabel()
        simpleRegressionModel_graph.setPixmap(QPixmap('./png/Regularization/Introduction/simpleRegressionModel.png'))
        layout.addWidget(simpleRegressionModel_graph)
        
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('L1 Regularization, namely Lasso Regression, puts a constraint on the summation of the absolute values of the weights by adding the penalty term below to Error(y, ŷ):'))
        
        penaltyTerm_graph = QLabel()
        penaltyTerm_graph.setPixmap(QPixmap('./png/Regularization/L1Regularization/penaltyTerm.png'))
        layout.addWidget(penaltyTerm_graph)
        
        layout.addWidget(QLabel('The objective of training becomes minimizing the loss function:'))
        
        l1LossFunction_graph = QLabel()
        l1LossFunction_graph.setPixmap(QPixmap('./png/Regularization/L1Regularization/l1LossFunction.png'))
        layout.addWidget(l1LossFunction_graph)
        
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('L2 Regularization,  namely Ridge Regression, puts a constraint on the summation of the square of the weights by adding the penalty term below to Error(y, ŷ):'))
                
        penaltyTerm_graph = QLabel()
        penaltyTerm_graph.setPixmap(QPixmap('./png/Regularization/L2Regularization/penaltyTerm.png'))
        layout.addWidget(penaltyTerm_graph)
        
        layout.addWidget(QLabel('The objective of training becomes minimizing the loss function:'))

        l2LossFunction_graph = QLabel()
        l2LossFunction_graph.setPixmap(QPixmap('./png/Regularization/L2Regularization/l2LossFunction.png'))
        layout.addWidget(l2LossFunction_graph)
                
        self.tab3.setLayout(layout)

    def tab4UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('L3 Regularization puts a constraint on the summation of the cube of the weights by adding the penalty term below to Error(y, ŷ):'))
                
        penaltyTerm_graph = QLabel()
        penaltyTerm_graph.setPixmap(QPixmap('./png/Regularization/L3Regularization/penaltyTerm.png'))
        layout.addWidget(penaltyTerm_graph)
        
        layout.addWidget(QLabel('The objective of training becomes minimizing the loss function:'))

        l3LossFunction_graph = QLabel()
        l3LossFunction_graph.setPixmap(QPixmap('./png/Regularization/L3Regularization/l3LossFunction.png'))
        layout.addWidget(l3LossFunction_graph)

        self.tab4.setLayout(layout)
    
    def tab5UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('L0.5 Regularization puts a constraint on the summation of the square root of the weights by adding the penalty term below to Error(y, ŷ):'))
        
        penaltyTerm_graph = QLabel()
        penaltyTerm_graph.setPixmap(QPixmap('./png/Regularization/L0_5Regularization/penaltyTerm.png'))
        layout.addWidget(penaltyTerm_graph)
        
        layout.addWidget(QLabel('The objective of training becomes minimizing the loss function:'))

        l0_5LossFunction_graph = QLabel()
        l0_5LossFunction_graph.setPixmap(QPixmap('./png/Regularization/L0_5Regularization/l0_5LossFunction.png'))
        layout.addWidget(l0_5LossFunction_graph)
        
        self.tab5.setLayout(layout)
    
    def tab6UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Lp Regularization puts a constraint on the summation of the weights to the power p by adding the penalty term below to Error(y, ŷ):'))
        
        penaltyTerm_graph = QLabel()
        penaltyTerm_graph.setPixmap(QPixmap('./png/Regularization/LpRegularization/penaltyTerm.png'))
        layout.addWidget(penaltyTerm_graph)
        
        layout.addWidget(QLabel('The objective of training becomes minimizing the loss function:'))

        lpLossFunction_graph = QLabel()
        lpLossFunction_graph.setPixmap(QPixmap('./png/Regularization/LpRegularization/lpLossFunction.png'))
        layout.addWidget(lpLossFunction_graph)

        self.tab6.setLayout(layout)    
    
    def tab7UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Elastic Net Regularization is a combination of L1 and L2 regularization by adding the 2 penalty terms below to Error(y, ŷ):'))
        
        penaltyTerm1_graph = QLabel()
        penaltyTerm1_graph.setPixmap(QPixmap('./png/Regularization/ElasticNetRegularization/penaltyTerm1.png'))
        layout.addWidget(penaltyTerm1_graph)
        
        penaltyTerm2_graph = QLabel()
        penaltyTerm2_graph.setPixmap(QPixmap('./png/Regularization/ElasticNetRegularization/penaltyTerm2.png'))
        layout.addWidget(penaltyTerm2_graph)
        
        layout.addWidget(QLabel('The objective of training becomes minimizing the loss function:'))

        elasticNet_graph = QLabel()
        elasticNet_graph.setPixmap(QPixmap('./png/Regularization/ElasticNetRegularization/elasticNet.png'))
        layout.addWidget(elasticNet_graph)
        
        self.tab7.setLayout(layout)
