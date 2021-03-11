import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class PerceptronTabs(QTabWidget):
    def __init__(self, parent = None):
        super(PerceptronTabs, self).__init__(parent)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()

        self.addTab(self.tab1, 'Introduction')
        self.addTab(self.tab2, 'Demonstration')
        self.addTab(self.tab3, 'Exercise')
        self.addTab(self.tab4, 'Perceptron Network')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Perceptron is a binary classifer, of which the processing unit adopts a step function with a given threshold.'))
        layout.addWidget(QLabel('Here is the typical setup of a simple perceptron:'))
        
        introduction_graph = QLabel()
        introduction_graph.setPixmap(QPixmap('./png/Perceptron/Introduction/perceptron.png'))
        layout.addWidget(introduction_graph)
        
        layout.addWidget(QLabel('It can be constructed to deal with many basic logical operations, like "AND" and "OR".'))

        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel('In this demonstration, a perceptron would be built to handle the logical operation "AND" between 2 inputs, each is either 0 or 1, with "1" representing "True" and "0" representing"False".'))
        layout.addWidget(QLabel('The threshold and the bias are both set to be 0.'))

        lb_gif = QLabel()
        lb_gif.setObjectName('lb_gif')
        movie_initialFrame = QMovie('./gifs/Perceptron/Demonstration/initialFrame.png')
        lb_gif.setMovie(movie_initialFrame)
        movie_initialFrame.start()
        layout.addWidget(lb_gif)
        
        lb_instruction = QLabel('Click 1 of the 4 buttons below to see how the perceptron works in each case.')
        layout.addWidget(lb_instruction)
        
        btn_layout = QHBoxLayout()
        
        btn_case1 = QPushButton('Case 1: X1 = 1, X2 = 1, bias = 0')
        btn_layout.addWidget(btn_case1)
        btn_case1.clicked.connect(self.switch_to_case1_gif)
        
        btn_case2 = QPushButton('Case 2: X1 = 1, X2 = 0, bias = 0')
        btn_layout.addWidget(btn_case2)
        btn_case2.clicked.connect(self.switch_to_case2_gif)
        
        btn_case3 = QPushButton('Case 3: X1 = 0, X2 = 1, bias = 0')
        btn_layout.addWidget(btn_case3)
        btn_case3.clicked.connect(self.switch_to_case3_gif)
        
        btn_case4 = QPushButton('Case 4: X1 = 0, X2 = 0, bias = 0')
        btn_layout.addWidget(btn_case4)
        btn_case4.clicked.connect(self.switch_to_case4_gif)
        
        btn_layout_widget = QWidget()
        btn_layout_widget.setLayout(btn_layout)
        
        layout.addWidget(btn_layout_widget)
        
        self.tab2.setLayout(layout)
        
    def switch_to_case1_gif(self):
        movie_case1 = QMovie('./gifs/Perceptron/Demonstration/case1.gif')
        self.tab2.findChild(QLabel, 'lb_gif').setMovie(movie_case1)
        movie_case1.start()
        
    def switch_to_case2_gif(self):
        movie_case2 = QMovie('./gifs/Perceptron/Demonstration/case2.gif')
        self.tab2.findChild(QLabel, 'lb_gif').setMovie(movie_case2)
        movie_case2.start()
        
    def switch_to_case3_gif(self):
        movie_case3 = QMovie('./gifs/Perceptron/Demonstration/case3.gif')
        self.tab2.findChild(QLabel, 'lb_gif').setMovie(movie_case3)
        movie_case3.start()
        
    def switch_to_case4_gif(self):
        movie_case4 = QMovie('./gifs/Perceptron/Demonstration/case4.gif')
        self.tab2.findChild(QLabel, 'lb_gif').setMovie(movie_case4)
        movie_case4.start()
    
    def tab3UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Take a look at the perceptron below and state the output in each of the 4 cases.'))
              
        exerciseSetup_graph = QLabel()
        exerciseSetup_graph.setPixmap(QPixmap('./png/Perceptron/Exercise/exerciseSetup.png'))
        layout.addWidget(exerciseSetup_graph)
        
        qna_layout1 = QHBoxLayout()
        qna_layout1.addWidget(QLabel('Case 1: X1 = 1, X2 = 1'))
        qna_case1_lineedit = QLineEdit()
        qna_case1_lineedit.setObjectName('Line1')
        qna_layout1.addWidget(qna_case1_lineedit)
        qna_layout1_widget = QWidget()
        qna_layout1_widget.setLayout(qna_layout1)
        layout.addWidget(qna_layout1_widget)
        
        qna_layout2 = QHBoxLayout()
        qna_layout2.addWidget(QLabel('Case 2: X1 = 1, X2 = 0'))
        qna_case2_lineedit = QLineEdit()
        qna_case2_lineedit.setObjectName('Line2')
        qna_layout2.addWidget(qna_case2_lineedit)
        qna_layout2_widget = QWidget()
        qna_layout2_widget.setLayout(qna_layout2)
        layout.addWidget(qna_layout2_widget)
        
        qna_layout3 = QHBoxLayout()
        qna_layout3.addWidget(QLabel('Case 3: X1 = 0, X2 = 1'))
        qna_case3_lineedit = QLineEdit()
        qna_case3_lineedit.setObjectName('Line3')
        qna_layout3.addWidget(qna_case3_lineedit)
        qna_layout3_widget = QWidget()
        qna_layout3_widget.setLayout(qna_layout3)
        layout.addWidget(qna_layout3_widget)
        
        qna_layout4 = QHBoxLayout()
        qna_layout4.addWidget(QLabel('Case 4: X1 = 0, X2 = 0'))
        qna_case4_lineedit = QLineEdit()
        qna_case4_lineedit.setObjectName('Line4')
        qna_layout4.addWidget(qna_case4_lineedit)
        qna_layout4_widget = QWidget()
        qna_layout4_widget.setLayout(qna_layout4)
        layout.addWidget(qna_layout4_widget)
        
        btn_sub = QPushButton('Submit')
        btn_sub.clicked.connect(self.submission)
        layout.addWidget(btn_sub)
        
        lb_result = QLabel('Result')
        lb_result.setObjectName('lb_result')
        layout.addWidget(lb_result)
        
        self.tab3.setLayout(layout)
    
    def submission(self):
        if self.tab3.findChild(QLineEdit, 'Line1').text() == self.tab3.findChild(QLineEdit, 'Line2').text() == self.tab3.findChild(QLineEdit, 'Line3').text() == '1' and self.tab3.findChild(QLineEdit, 'Line4').text() == '0':
            self.tab3.findChild(QLabel, 'lb_result').setText('True!\nIn fact, this perceptron is implemented to hanlde the "OR" logic.')
        else:
            self.tab3.findChild(QLabel, 'lb_result').setText('False')
            
    def tab4UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Multiple perceptrons can be grouped together to form a perceptron network.'))

        perceptronNetwork_graph = QLabel()
        perceptronNetwork_graph.setPixmap(QPixmap('./png/Perceptron/PerceptronNetwork/perceptronNetwork.png'))
        layout.addWidget(perceptronNetwork_graph)
        
        layout.addWidget(QLabel('The single layer perceptron network above can be generalized to a multi-layer structure, which is capable of handling more complicated tasks.'))
        layout.addWidget(QLabel('Details can be found in "Multi-layer Perceptron".'))

        self.tab4.setLayout(layout)
