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
        
        style = """
        QWidget{
            background-color: rgb(40, 44, 52);
        }
        QLabel{
            font-size: 16pt;
        }
        QPushButton{
            border: 2px solid black;
            background-color: #F9F7ED;
            color: black;
            border-radius : 12px;
            padding: 2px 4px 2px 4px;
            font-size: 16pt;
        }
        QPushButton::hover
        {
            background-color : #24a0ed;
            color: white;
        }
        QLineEdit::hover
        {
            background-color : white;
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
        
        label1 = QLabel('Feedforward is the process of feeding in an item to an artificial neural network, in order to obtain a predicition.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('In supervised learning, a loss function is defined to compute the accuracy of each prediction based on the corresponding gruth truth.')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        label3 = QLabel('Backpropagation is the process of adjusting the weights of a neural network according to the loss given by the loss function. The weight updates in the process are guided by the application of the chain rule of differentiation, starting from the loss given by the loss function and traversing the network in a reverse orde back to the input layer.')
        label3.setWordWrap(True)
        layout.addWidget(label3)
        
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('The application of the chain rule of differentiation on an arbitrary node of a neural network is illustrated as below:')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        chainRuleInBackpropagation_gif = QLabel()
        chainRuleInBackpropagation_gif.setScaledContents(True)
        chainRuleInBackpropagation_movie = QMovie('./gifs/FeedforwardAndBackpropagation/ChainRuleInBackpropagation/chainRuleInBackpropagation.gif')
        chainRuleInBackpropagation_movie.setScaledSize(chainRuleInBackpropagation_gif.size())
        chainRuleInBackpropagation_gif.setMovie(chainRuleInBackpropagation_movie)
        chainRuleInBackpropagation_movie.start()
        layout.addWidget(chainRuleInBackpropagation_gif)
        
        label2 = QLabel('Note that, all the activation functions in a nerual network must be differentiable; otherwise, backpropagation does not work.')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        self.tab2.setLayout(layout)

    def tab3UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('A simple illustration of backpropagation:')
        label1.setWordWrap(True)
        layout.addWidget(label1)       

        demonstrationOfBackpropagation1_gif = QLabel()
        demonstrationOfBackpropagation1_gif.setScaledContents(True)
        demonstrationOfBackpropagation1_movie = QMovie('./gifs/FeedforwardAndBackpropagation/DemonstrationOfBackpropagation1/demonstrationOfBackpropagation1.gif')
        demonstrationOfBackpropagation1_movie.setScaledSize(demonstrationOfBackpropagation1_gif.size())
        demonstrationOfBackpropagation1_gif.setMovie(demonstrationOfBackpropagation1_movie)
        demonstrationOfBackpropagation1_movie.start()
        layout.addWidget(demonstrationOfBackpropagation1_gif)

        self.tab3.setLayout(layout)
    
    def tab4UI(self):
        layout = QVBoxLayout()
                
        label1 = QLabel('A more complicated illustration of backpropagation:')
        label1.setWordWrap(True)
        layout.addWidget(label1)

        demonstrationOfBackpropagation2_gif = QLabel()
        demonstrationOfBackpropagation2_gif.setScaledContents(True)
        demonstrationOfBackpropagation2_movie = QMovie('./gifs/FeedforwardAndBackpropagation/DemonstrationOfBackpropagation2/demonstrationOfBackpropagation2.gif')
        demonstrationOfBackpropagation2_movie.setScaledSize(demonstrationOfBackpropagation2_gif.size())
        demonstrationOfBackpropagation2_gif.setMovie(demonstrationOfBackpropagation2_movie)
        demonstrationOfBackpropagation2_movie.start()
        layout.addWidget(demonstrationOfBackpropagation2_gif)
        
        label2 = QLabel('Pay attention to the end of the illustration, of how backpropagation goes through the sigmoid function!')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        self.tab4.setLayout(layout)

    def tab5UI(self):
        layout = QVBoxLayout()
     
        exercise_graph = QLabel()
        exercise_graph.setAlignment(Qt.AlignCenter)
        exercise_graph.setPixmap(QPixmap('./png/FeedforwardAndBackpropagation/Exercise/exercise.png').scaled(exercise_graph.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation))
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
        
        snr_layout = QHBoxLayout()
        
        btn_sub = QPushButton('Submit')
        btn_sub.clicked.connect(self.submission)
        snr_layout.addWidget(btn_sub)
        
        lb_result = QLabel('')
        lb_result.setObjectName('lb_result')
        lb_result.setAlignment(Qt.AlignCenter)
        snr_layout.addWidget(lb_result)
        
        snr_layout_widget = QWidget()
        snr_layout_widget.setLayout(snr_layout)
        layout.addWidget(snr_layout_widget)

        self.tab5.setLayout(layout)
        
    def submission(self):
        input_X = self.tab5.findChild(QLineEdit, 'Line1').text()
        input_Y = self.tab5.findChild(QLineEdit, 'Line2').text()
        if ((input_X == '-0.4' or input_X == '-0.40') and (input_Y == '-0.6' or input_Y == '-0.60')):
            self.tab5.findChild(QLabel, 'lb_result').setText('True!\nYou now have at least a basic understanding of backpropagation!')
        else:
            self.tab5.findChild(QLabel, 'lb_result').setText('False! Please try again!')
