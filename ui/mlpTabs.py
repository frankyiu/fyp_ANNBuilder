import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MLPTabs(QTabWidget):                
    def __init__(self, parent = None):
        super(MLPTabs, self).__init__(parent)

        self.tab1 = QWidget()

        self.addTab(self.tab1, '')
        self.setStyleSheet("background-color: rgb(40, 44, 52);")

        self.tab1UI()


    def tab1UI(self):
        layout = QVBoxLayout()

        label = QLabel('Multi-layer Perceptron - MLP')
        label.setAlignment(Qt.AlignCenter)
        label.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        label.setStyleSheet("QLabel{font-size: 40pt;}")
        layout.addWidget(label)

        self.tab1.setLayout(layout)

