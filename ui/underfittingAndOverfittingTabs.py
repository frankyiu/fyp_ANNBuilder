import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class UnderfittingAndOverfittingTabs(QTabWidget):               # geeksforgeeks.org
    def __init__(self, parent = None):
        super(UnderfittingAndOverfittingTabs, self).__init__(parent)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        self.addTab(self.tab1, 'Overview')
        self.addTab(self.tab2, 'Why Underfitting')
        self.addTab(self.tab3, 'Solutions To Underfitting')
        self.addTab(self.tab4, 'Why Overfitting')
        self.addTab(self.tab5, 'Solutions To Overfitting')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Underfitting: The training accuracy is poor, i.e. the model has not learnt much meaningful information from the training dataset.'))
        layout.addWidget(QLabel('Overfitting: The trained model has a low accuracy, in comparison to the training result, when it is generalized to the test set.'))
        layout.addWidget(QLabel('Here is an example illustrating different scenarios of which a model learns a decision boundary to classify points in a training dataset into 2 groups using 2 features.'))

        underfitting_and_overfitting_graph = QLabel()
        underfitting_and_overfitting_graph.setPixmap(QPixmap('./png/UnderfittingAndOverfitting/Overview/underfitting_and_overfitting.png'))
        layout.addWidget(underfitting_and_overfitting_graph)
        
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
                
        layout.addWidget(QLabel('The reasons of underfitting could be:'))
        layout.addWidget(QLabel('1. not enough training with the dataset'))
        layout.addWidget(QLabel('2. the dataset has a poor quality, eg. sigificant background noise, the size is too small, etc.'))
        layout.addWidget(QLabel('3. the number of features involved in consideration is too small'))
        layout.addWidget(QLabel('4. the model is too simple to deal with the hypothesis'))

        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Here are the common solutions to underfitting:'))
        layout.addWidget(QLabel('1. Increase the number of training epochs, i.e. the number of passes over the entire dataset'))
        layout.addWidget(QLabel('2. Remove background noise from the dataset'))
        layout.addWidget(QLabel('3. Expand the dataset by data collection or data augmentation'))
        layout.addWidget(QLabel('4. Consider factoring in more features'))
        layout.addWidget(QLabel('5. Enhance the model\'s complexity'))

        self.tab3.setLayout(layout)

    def tab4UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('The reasons of overfitting could be:'))
        layout.addWidget(QLabel('1. the training time is too long with a relatively small dataset'))
        layout.addWidget(QLabel('2. the model is too complicated to deal with the simple hypothesis'))
        layout.addWidget(QLabel('3. the number of features involved in consideration is too big'))
        
        self.tab4.setLayout(layout)
    
    def tab5UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Here are the common solutions to overfitting:'))
        layout.addWidget(QLabel('1. Stop early and appropriately in the training phase'))
        layout.addWidget(QLabel('2. Expand the dataset by data collection or data augmentation'))
        layout.addWidget(QLabel('3. Use a simpler model'))
        layout.addWidget(QLabel('4. Adopt regularization'))
        layout.addWidget(QLabel('5. Dropout out certain units in the neural network'))

        self.tab5.setLayout(layout)
