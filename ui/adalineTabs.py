import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class AdalineTabs(QTabWidget):
    def __init__(self, parent = None):
        super(AdalineTabs, self).__init__(parent)

        self.tab1 = QWidget()
        self.tab2 = QWidget()

        self.addTab(self.tab1, 'Overview')
        self.addTab(self.tab2, 'Illustration')
        
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

    def tab1UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('Adaptive Linear Element, namely Adaline, contains a single layer of adjustable weights on the lines connecting the input nodes and the processing unit.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('The output is generally the weighted sum of the input values.')
        label2.setWordWrap(True)
        layout.addWidget(label2)

        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()

        label1 = QLabel('Here is how a general Adaline works:')
        label1.setWordWrap(True)
        layout.addWidget(label1)

        adaline_gif = QLabel()
        adaline_gif.setAlignment(Qt.AlignCenter)
        movie_adaline = QMovie('./gifs/Adaline/Illustration/illustration.gif')
        adaline_gif.setMovie(movie_adaline)
        movie_adaline.start()
        layout.addWidget(adaline_gif)
        
        label2 = QLabel('Under supervised learning, a loss function (will be introduced later) is applied to the output to determine how close is the prediction to the labeled ground truth of the fed-in example.')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        label3 = QLabel('Backpropagation is then conducted to adjust the weights accordingly, so as to make more precise predictions in future rounds.')
        label3.setWordWrap(True)
        layout.addWidget(label3)
        
        self.tab2.setLayout(layout)
