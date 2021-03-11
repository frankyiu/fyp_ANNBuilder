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
        
        layout.addWidget(QLabel('Regularization is a common strategy used to mitigate overfitting.'))
        layout.addWidget(QLabel('Say, we have a simple linear regression model as below:'))
        
        linear_regression_model_graph = QLabel()
        linear_regression_model_graph.setPixmap(QPixmap('./png/Regularization/Introduction/linear_regression_model.png'))
        layout.addWidget(linear_regression_model_graph)
        
        linear_regression_model__notations_graph = QLabel()
        linear_regression_model__notations_graph.setPixmap(QPixmap('./png/Regularization/Introduction/linear_regression_model_notations.png'))
        layout.addWidget(linear_regression_model__notations_graph)
        
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('L1 Regularization, namely Lasso Regression, puts a constraint on the summation of the absolute values of the weights by adding the penalty term below to Error(y, ŷ):'))
        
        l1PenaltyTerm_graph = QLabel()
        l1PenaltyTerm_graph.setPixmap(QPixmap('./png/Regularization/L1Regularization/l1penaltyterm.png'))
        layout.addWidget(l1PenaltyTerm_graph)
        
        l1PenaltyTermNotation_graph = QLabel()
        l1PenaltyTermNotation_graph.setPixmap(QPixmap('./png/Regularization/L1Regularization/l1penaltyterm_notation.png'))
        layout.addWidget(l1PenaltyTermNotation_graph)
        
        layout.addWidget(QLabel('The objective of training becomes minimizing the loss function:'))
        
        l1LossFunction_graph = QLabel()
        l1LossFunction_graph.setPixmap(QPixmap('./png/Regularization/L1Regularization/l1LossFunction.png'))
        layout.addWidget(l1LossFunction_graph)
        
        l1LossFunctionNotation_graph = QLabel()
        l1LossFunctionNotation_graph.setPixmap(QPixmap('./png/Regularization/L1Regularization/l1lossfunction_notation.png'))
        layout.addWidget(l1LossFunctionNotation_graph)
        
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('L2 Regularization,  namely Ridge Regression, puts a constraint on the summation of the square of the weights by adding the penalty term below to Error(y, ŷ):'))
                
        l2PenaltyTerm_graph = QLabel()
        l2PenaltyTerm_graph.setPixmap(QPixmap('./png/Regularization/L2Regularization/l2penaltyterm.png'))
        layout.addWidget(l2PenaltyTerm_graph)
        
        l2PenaltyTermNotation_graph = QLabel()
        l2PenaltyTermNotation_graph.setPixmap(QPixmap('./png/Regularization/L2Regularization/l2penaltyterm_notation.png'))
        layout.addWidget(l2PenaltyTermNotation_graph)
        
        layout.addWidget(QLabel('The objective of training becomes minimizing the loss function:'))

        l2LossFunction_graph = QLabel()
        l2LossFunction_graph.setPixmap(QPixmap('./png/Regularization/L2Regularization/l2LossFunction.png'))
        layout.addWidget(l2LossFunction_graph)
        
        l2LossFunctionNotation_graph = QLabel()
        l2LossFunctionNotation_graph.setPixmap(QPixmap('./png/Regularization/L2Regularization/l2lossfunction_notation.png'))
        layout.addWidget(l2LossFunctionNotation_graph)
                
        self.tab3.setLayout(layout)

    def tab4UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('L3 Regularization puts a constraint on the summation of the cube of the weights by adding the penalty term below to Error(y, ŷ):'))
                
        l3PenaltyTerm_graph = QLabel()
        l3PenaltyTerm_graph.setPixmap(QPixmap('./png/Regularization/L3Regularization/l3penaltyterm.png'))
        layout.addWidget(l3PenaltyTerm_graph)
        
        l3PenaltyTermNotation_graph = QLabel()
        l3PenaltyTermNotation_graph.setPixmap(QPixmap('./png/Regularization/L3Regularization/l3penaltyterm_notation.png'))
        layout.addWidget(l3PenaltyTermNotation_graph)
        
        layout.addWidget(QLabel('The objective of training becomes minimizing the loss function:'))

        l3LossFunction_graph = QLabel()
        l3LossFunction_graph.setPixmap(QPixmap('./png/Regularization/L3Regularization/l3lossfunction.png'))
        layout.addWidget(l3LossFunction_graph)

        l3LossFunctionNotation_graph = QLabel()
        l3LossFunctionNotation_graph.setPixmap(QPixmap('./png/Regularization/L3Regularization/l3lossfunction_notation.png'))
        layout.addWidget(l3LossFunctionNotation_graph)
        
        self.tab4.setLayout(layout)
    
    def tab5UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('L0.5 Regularization puts a constraint on the summation of the square root of the weights by adding the penalty term below to Error(y, ŷ):'))
        
        l0_5PenaltyTerm_graph = QLabel()
        l0_5PenaltyTerm_graph.setPixmap(QPixmap('./png/Regularization/L0_5Regularization/l0_5penaltyterm.png'))
        layout.addWidget(l0_5PenaltyTerm_graph)
        
        l0_5PenaltyTermNotation_graph = QLabel()
        l0_5PenaltyTermNotation_graph.setPixmap(QPixmap('./png/Regularization/L0_5Regularization/l0_5penaltyterm_notation.png'))
        layout.addWidget(l0_5PenaltyTermNotation_graph)
        
        layout.addWidget(QLabel('The objective of training becomes minimizing the loss function:'))

        l0_5LossFunction_graph = QLabel()
        l0_5LossFunction_graph.setPixmap(QPixmap('./png/Regularization/L0_5Regularization/l0_5lossfunction.png'))
        layout.addWidget(l0_5LossFunction_graph)
        
        l0_5LossFunctionNotation_graph = QLabel()
        l0_5LossFunctionNotation_graph.setPixmap(QPixmap('./png/Regularization/L0_5Regularization/l0_5lossfunction_notation.png'))
        layout.addWidget(l0_5LossFunctionNotation_graph)
        
        self.tab5.setLayout(layout)
    
    def tab6UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Lp Regularization puts a constraint on the summation of the weights to the power p by adding the penalty term below to Error(y, ŷ):'))
        
        lpPenaltyTerm_graph = QLabel()
        lpPenaltyTerm_graph.setPixmap(QPixmap('./png/Regularization/LpRegularization/lppenaltyterm.png'))
        layout.addWidget(lpPenaltyTerm_graph)
        
        lpPenaltyTermNotation_graph = QLabel()
        lpPenaltyTermNotation_graph.setPixmap(QPixmap('./png/Regularization/LpRegularization/lppenaltyterm_notation.png'))
        layout.addWidget(lpPenaltyTermNotation_graph)
        
        layout.addWidget(QLabel('The objective of training becomes minimizing the loss function:'))

        lpLossFunction_graph = QLabel()
        lpLossFunction_graph.setPixmap(QPixmap('./png/Regularization/LpRegularization/lplossfunction.png'))
        layout.addWidget(lpLossFunction_graph)
        
        lpLossFunctionNotation_graph = QLabel()
        lpLossFunctionNotation_graph.setPixmap(QPixmap('./png/Regularization/LpRegularization/lplossfunction_notation.png'))
        layout.addWidget(lpLossFunctionNotation_graph)

        self.tab6.setLayout(layout)    
    
    def tab7UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Elastic Net Regularization is a combination of L1 and L2 regularization by adding the 2 penalty terms below to Error(y, ŷ):'))
        
        elasticNetPenaltyTerms_graph = QLabel()
        elasticNetPenaltyTerms_graph.setPixmap(QPixmap('./png/Regularization/ElasticNetRegularization/elasticnetpenaltyterms.png'))
        layout.addWidget(elasticNetPenaltyTerms_graph)
        
        elasticNetPenaltyTermsNotations_graph = QLabel()
        elasticNetPenaltyTermsNotations_graph.setPixmap(QPixmap('./png/Regularization/ElasticNetRegularization/elasticnetpenaltyterms_notations.png'))
        layout.addWidget(elasticNetPenaltyTermsNotations_graph)
        
        layout.addWidget(QLabel('The objective of training becomes minimizing the loss function:'))

        elasticNetLossFunction_graph = QLabel()
        elasticNetLossFunction_graph.setPixmap(QPixmap('./png/Regularization/ElasticNetRegularization/elasticnetlossfunction.png'))
        layout.addWidget(elasticNetLossFunction_graph) 
        
        elasticNetLossFunctionNotation_graph = QLabel()
        elasticNetLossFunctionNotation_graph.setPixmap(QPixmap('./png/Regularization/ElasticNetRegularization/elasticnetlossfunction_notation.png'))
        layout.addWidget(elasticNetLossFunctionNotation_graph)
        
        self.tab7.setLayout(layout)
