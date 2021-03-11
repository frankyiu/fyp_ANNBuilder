import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MLPTabs(QTabWidget):                
    def __init__(self, parent = None):
        super(MLPTabs, self).__init__(parent)

        self.tab1 = QWidget()

        self.addTab(self.tab1, 'Multi-layer Perceptron')

        self.tab1UI()


    def tab1UI(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel('MLP'))

        self.tab1.setLayout(layout)

