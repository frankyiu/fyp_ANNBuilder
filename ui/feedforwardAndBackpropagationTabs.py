import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FeedforwardAndBackpropagationTabs(QTabWidget):
    def __init__(self, parent = None):
        super(FeedforwardAndBackpropagationTabs, self).__init__(parent)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()

        self.addTab(self.tab1, 'Overview')
        self.addTab(self.tab2, 'Chain Rule In Backpropagation')
        self.addTab(self.tab3, 'Demonstration of Backpropagation 1')
        self.addTab(self.tab4, 'Demonstration of Backpropagation 2')
        self.addTab(self.tab5, 'Exercise')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Feedforward is the process of feeding in items of a preprocessed dataset into an artificial neural network one by one to obtain the predicted outcomes.'))
        layout.addWidget(QLabel('In supervised learning, a loss function is defined to compute the accuracy of each predicted outcome against the gruth truth of the fed-in labeled trainging example.'))
        layout.addWidget(QLabel('Backpropagation is the process of updating the weight of each line connecting the nodes in a neural network.\nThe weight updates in the process are guided by the application of chain rule of differentiation on the output of the loss function and it traverses the network in a reverse order, i.e. from the output layer back to the input layer.\nThe mechanism will be illustrated in the following tabs.'))
        layout.addWidget(QLabel('Stochastic Gradient descent - Weight updates are carried out for each training example'))
        layout.addWidget(QLabel('Batch Gradient descent - Weight updates are carried out for each batch of training examples, the adjustment to each weight is generally the accumulated value of the required change to the respective weight in each iteration of training among the bacth'))
        
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
        
        chainRuleInBackpropagation_gif = QLabel()
        chainRuleInBackpropagation_movie = QMovie('./gifs/FeedforwardAndBackpropagation/ChainRuleInBackpropagation/chainRuleInBackpropagation.gif')
        chainRuleInBackpropagation_gif.setMovie(chainRuleInBackpropagation_movie)
        chainRuleInBackpropagation_movie.start()
        layout.addWidget(chainRuleInBackpropagation_gif)
        
        layout.addWidget(QLabel('The application of the chain rule of differentiation on an arbitrary node in a neural network.\nNote that, as to enable backpropagation, all the activation functions of nodes in a nerual network must be differentiable.'))

        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('A simple demonstration:'))

        demonstrationOfBackpropagation1_gif = QLabel()
        demonstrationOfBackpropagation1_movie = QMovie('./gifs/FeedforwardAndBackpropagation/DemonstrationOfBackpropagation1/demonstrationOfBackpropagation1.gif')
        demonstrationOfBackpropagation1_gif.setMovie(demonstrationOfBackpropagation1_movie)
        demonstrationOfBackpropagation1_movie.start()
        layout.addWidget(demonstrationOfBackpropagation1_gif)

        self.tab3.setLayout(layout)
    
    def tab4UI(self):
        layout = QVBoxLayout()
                
        layout.addWidget(QLabel('A more complicated demonstration:'))

        demonstrationOfBackpropagation2_gif = QLabel()
        demonstrationOfBackpropagation2_movie = QMovie('./gifs/FeedforwardAndBackpropagation/DemonstrationOfBackpropagation2/demonstrationOfBackpropagation2.gif')
        demonstrationOfBackpropagation2_gif.setMovie(demonstrationOfBackpropagation2_movie)
        demonstrationOfBackpropagation2_movie.start()
        layout.addWidget(demonstrationOfBackpropagation2_gif)
        
        layout.addWidget(QLabel('Pay attention to how the backpropagation goes through the sigmoid function at the end of the illustration'))

        self.tab4.setLayout(layout)

    def tab5UI(self):
        layout = QVBoxLayout()
     
        exercise_graph = QLabel()
        exercise_graph.setPixmap(QPixmap('./png/FeedforwardAndBackpropagation/Exercise/exercise.png'))
        layout.addWidget(exercise_graph)
        
        qna_layout1 = QHBoxLayout()
        qna_layout1.addWidget(QLabel('Please Input The Value Of X:'))
        qna_case1_lineedit = QLineEdit()
        qna_case1_lineedit.setObjectName('Line1')
        qna_layout1.addWidget(qna_case1_lineedit)
        qna_layout1_widget = QWidget()
        qna_layout1_widget.setLayout(qna_layout1)
        layout.addWidget(qna_layout1_widget)
        
        qna_layout2 = QHBoxLayout()
        qna_layout2.addWidget(QLabel('Please Input The Value Of Y:'))
        qna_case2_lineedit = QLineEdit()
        qna_case2_lineedit.setObjectName('Line2')
        qna_layout2.addWidget(qna_case2_lineedit)
        qna_layout2_widget = QWidget()
        qna_layout2_widget.setLayout(qna_layout2)
        layout.addWidget(qna_layout2_widget)
        
        btn_sub = QPushButton('Submit')
        btn_sub.clicked.connect(self.submission)
        layout.addWidget(btn_sub)
        
        lb_result = QLabel('Result')
        lb_result.setObjectName('lb_result')
        layout.addWidget(lb_result)

        self.tab5.setLayout(layout)
        
    def submission(self):
        input_X = self.tab5.findChild(QLineEdit, 'Line1').text()
        input_Y = self.tab5.findChild(QLineEdit, 'Line2').text()
        if ((input_X == '-0.4' or input_X == '-0.40') and (input_Y == '-0.6' or input_Y == '-0.60')):
            self.tab5.findChild(QLabel, 'lb_result').setText('True!\nYou now have at least a basic understanding of backpropagation!')
        else:
            self.tab5.findChild(QLabel, 'lb_result').setText('False!\nPlease try again!')
