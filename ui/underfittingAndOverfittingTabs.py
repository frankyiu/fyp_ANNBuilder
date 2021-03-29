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

    def tab1UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('Underfitting: The training accuracy is poor, i.e. the model has not learnt much meaningful information from the training dataset.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('Overfitting: The trained model has a low accuracy, in comparison to the training result, when it is generalized to the test set.')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        label3 = QLabel('Here is an example illustrating different scenarios of which a model learns a decision boundary to classify points in a training dataset into 2 groups using 2 features.')
        label3.setWordWrap(True)
        layout.addWidget(label3)

        underfitting_and_overfitting_graph = QLabel()
        underfitting_and_overfitting_graph.setAlignment(Qt.AlignCenter)
        underfitting_and_overfitting_graph.setPixmap(QPixmap('./png/UnderfittingAndOverfitting/Overview/underfitting_and_overfitting.png').scaled(underfitting_and_overfitting_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
        layout.addWidget(underfitting_and_overfitting_graph)
        
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
                
        label1 = QLabel('The reasons of underfitting could be:')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('1. not enough training with the dataset')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        label3 = QLabel('2. the dataset has a poor quality, eg. sigificant background noise, the size is too small, etc.')
        label3.setWordWrap(True)
        layout.addWidget(label3) 
    
        label4 = QLabel('3. the number of features involved in consideration is too small')
        label4.setWordWrap(True)
        layout.addWidget(label4)
        
        label5 = QLabel('4. the model is too simple to deal with the hypothesis')
        label5.setWordWrap(True)
        layout.addWidget(label5)

        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('Here are the common solutions to underfitting:')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('1. Increase the number of training epochs, i.e. the number of passes over the entire dataset')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        label3 = QLabel('2. Remove background noise from the dataset')
        label3.setWordWrap(True)
        layout.addWidget(label3) 
    
        label4 = QLabel('3. Expand the dataset by data collection or data augmentation')
        label4.setWordWrap(True)
        layout.addWidget(label4)
        
        label5 = QLabel('4. Consider factoring in more features')
        label5.setWordWrap(True)
        layout.addWidget(label5)
        
        label6 = QLabel('5. Enhance the model\'s complexity')
        label6.setWordWrap(True)
        layout.addWidget(label6)
        
        self.tab3.setLayout(layout)

    def tab4UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('The reasons of overfitting could be:')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('1. the training time is too long with a relatively small dataset')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        label3 = QLabel('2. the model is too complicated to deal with the simple hypothesis')
        label3.setWordWrap(True)
        layout.addWidget(label3) 
    
        label4 = QLabel('3. the number of features involved in consideration is too big')
        label4.setWordWrap(True)
        layout.addWidget(label4)
        
        self.tab4.setLayout(layout)
    
    def tab5UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('Here are the common solutions to overfitting:')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('1. Stop early and appropriately in the training phase')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        label3 = QLabel('2. Expand the dataset by data collection or data augmentation')
        label3.setWordWrap(True)
        layout.addWidget(label3) 
    
        label4 = QLabel('3. Use a simpler model')
        label4.setWordWrap(True)
        layout.addWidget(label4)
        
        label5 = QLabel('4. Adopt regularization')
        label5.setWordWrap(True)
        layout.addWidget(label5)
        
        label6 = QLabel('5. Dropout out certain units in the neural network')
        label6.setWordWrap(True)
        layout.addWidget(label6)

        self.tab5.setLayout(layout)
