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
        self.addTab(self.tab3, 'Illustration of Backpropagation 1')
        self.addTab(self.tab4, 'Illustration of Backpropagation 2')
        self.addTab(self.tab5, 'Exercise')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Feedforward is the process of feeding in an item to an artificial neural network, in order to obtain a predicition.'))
        layout.addWidget(QLabel('In supervised learning, a loss function is defined to compute the accuracy of each prediction based on the corresponding gruth truth.'))
        layout.addWidget(QLabel('Backpropagation is the process of adjusting the weights of a neural network according to the loss given by the loss function.\nThe weight updates in the process are guided by the application of the chain rule of differentiation, starting from the loss given by the loss function and traversing the network in a reverse orde back to the input layer.'))
        
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('The application of the chain rule of differentiation on an arbitrary node of a neural network is illustrated as below:'))

        chainRuleInBackpropagation_gif = QLabel()
        chainRuleInBackpropagation_movie = QMovie('./gifs/FeedforwardAndBackpropagation/ChainRuleInBackpropagation/chainRuleInBackpropagation.gif')
        chainRuleInBackpropagation_gif.setMovie(chainRuleInBackpropagation_movie)
        chainRuleInBackpropagation_movie.start()
        layout.addWidget(chainRuleInBackpropagation_gif)
        
        layout.addWidget(QLabel('Note that, all the activation functions in a nerual network must be differentiable; otherwise, backpropagation does not work.'))

        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('A simple illustration of backpropagation:'))

        demonstrationOfBackpropagation1_gif = QLabel()
        demonstrationOfBackpropagation1_movie = QMovie('./gifs/FeedforwardAndBackpropagation/DemonstrationOfBackpropagation1/demonstrationOfBackpropagation1.gif')
        demonstrationOfBackpropagation1_gif.setMovie(demonstrationOfBackpropagation1_movie)
        demonstrationOfBackpropagation1_movie.start()
        layout.addWidget(demonstrationOfBackpropagation1_gif)

        self.tab3.setLayout(layout)
    
    def tab4UI(self):
        layout = QVBoxLayout()
                
        layout.addWidget(QLabel('A more complicated illustration of backpropagation:'))

        demonstrationOfBackpropagation2_gif = QLabel()
        demonstrationOfBackpropagation2_movie = QMovie('./gifs/FeedforwardAndBackpropagation/DemonstrationOfBackpropagation2/demonstrationOfBackpropagation2.gif')
        demonstrationOfBackpropagation2_gif.setMovie(demonstrationOfBackpropagation2_movie)
        demonstrationOfBackpropagation2_movie.start()
        layout.addWidget(demonstrationOfBackpropagation2_gif)
        
        layout.addWidget(QLabel('Pay attention to the end of the illustration, of how backpropagation goes through the sigmoid function!'))

        self.tab4.setLayout(layout)

    def tab5UI(self):
        layout = QVBoxLayout()
     
        exercise_graph = QLabel()
        exercise_graph.setPixmap(QPixmap('./png/FeedforwardAndBackpropagation/Exercise/exercise.png'))
        layout.addWidget(exercise_graph)
        
        qna_layout1 = QHBoxLayout()
        qna_layout1.addWidget(QLabel('Please Input the Value of X:'))
        qna_case1_lineedit = QLineEdit()
        qna_case1_lineedit.setObjectName('Line1')
        qna_layout1.addWidget(qna_case1_lineedit)
        qna_layout1_widget = QWidget()
        qna_layout1_widget.setLayout(qna_layout1)
        layout.addWidget(qna_layout1_widget)
        
        qna_layout2 = QHBoxLayout()
        qna_layout2.addWidget(QLabel('Please Input the Value of Y:'))
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
