import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class BasicConceptsTab(QTabWidget):
    def __init__(self, parent = None):
        super(BasicConceptsTab, self).__init__(parent)

        self.tab1 = QWidget()

        self.addTab(self.tab1, 'Basic Concepts')

        self.tab1UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Basic Concepts'))

        self.tab1.setLayout(layout)
