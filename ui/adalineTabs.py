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
        self.addTab(self.tab2, 'Typical Setup')
        
        self.tab1UI()
        self.tab2UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Adaptive Linear Element, namely Adaline, contains a single layer of adjustable weights on the lines connecting the input nodes and the processing unit.'))
        layout.addWidget(QLabel('The output is generally the weighted sum of the input values.'))
        layout.addWidget(QLabel('Under supervised learning, a loss function (will be introduced later) would be applied to determine how close is each prediction to the labeled ground truth of the corresponding fed-in training example and then makes adjustments accordingly to the weights in the hope that it will enhance the accuracy of future prediction.'))
        
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel('Here is the typical setup of an Adaline:'))

        adaline_gif = QLabel()
        movie_adaline = QMovie('./gifs/Adaline/Overview/adaline.gif')
        adaline_gif.setMovie(movie_adaline)
        movie_adaline.start()
        layout.addWidget(adaline_gif)
        
        self.tab2.setLayout(layout)
