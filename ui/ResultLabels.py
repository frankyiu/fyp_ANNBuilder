from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from ui.ResultDashBoardConstant import *

"""
This class contains all the label names used in the dashboard
for the ResultMetrics class
Methods are invoked by the UpdateDashBoard class to get the dataset information
"""
class ResultLabels(QLabel):
    Math    = ["BLUE", "ORANGE", "GREEN", "RED"]
    MNIST   = ["DIGIT 0", "DIGIT 1", "DIGIT 2", "DIGIT 3", "DIGIT 4", "DIGIT 5", "DIGIT 6", "DIGIT 7", "DIGIT 8", "DIGIT 9"]
    CIFAR10 = ["AIRPLANE", "AUTOMOBILE", "BIRD", "CAT" , "DEER", "DOG", "FROG", "HORSE", "SHIP", "TRUCK"]

    def __init__(self, parent=None):
        super(ResultLabels,self).__init__(parent)
        self.setObjectName("Result DashBoard Labels")
        self.setLabelMath([0,1])    #HARDCODED
        parent.verticalLayout.addWidget(self)
        self.setHidden(True)

    def setLabelMath(self, classes):
        self.updateLabel(classes, ResultLabels.Math)

    def setLabelMNIST(self, classes):
        self.updateLabel(classes, ResultLabels.MNIST)

    def setLabelCIFAR10(self, classes):
        self.updateLabel(classes, ResultLabels.CIFAR10)

    """
    classes: a list of integer indicating the unique set of label value of the current data set
    e.g. Cat and Dog in CIFAR10 with class label 3 and 5 => classes = [3, 5]
    name_lst: the list of string specified as static member of this class
    """
    def updateLabel(self, classes, name_lst):
        self.num_classes = len(classes)
        self.label = [label for idx,label in enumerate(name_lst) if idx in classes]

    def getLabel(self):
        return self.label

    def getNumClass(self):
        return self.num_classes
