from PyQt5 import QtCore, QtGui, QtWidgets
from ui.ResultLosses import *
from ui.ResultMetric import *
from ui.ResultMetrics import *
from ui.ResultLabels import *
from ui.ResultLossGraph import *
from ui.ResultHeatmap import *
from ui.ResultDashBoardConstant import *
from ml.UpdateDashBoard import *

class ScrollableResultDashBoard(QtWidgets.QScrollArea):
    def __init__(self, parent=None):
        super(ScrollableResultDashBoard, self).__init__(parent)
        self.setWidgetResizable(True)
        self.setGeometry(QtCore.QRect(0, 0, WIDGET_WIDTH, 450))
        self.dashboard_widget = ResultDashBoard(self)
        dashboard_stylesheet = " \
                                #widget_dashboard {\
                                background:rgb(35, 36, 40); \
                                border: 0px;\
                                border-radius: 10px;\
                                padding: 5px;\
                                }\
                                QWidget{font-family:SegoeUIMonoW01-Regular;\
                                }"
        self.setStyleSheet(dashboard_stylesheet)
        self.setWidget(self.dashboard_widget)


"""
The widget that contains all the parts shown on dashboard, including
- losses, loss graph, contour graph, accuracy, and classfication metrics
"""
class ResultDashBoard(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(ResultDashBoard,self).__init__(parent)
        self.setObjectName("ResultDashBoard")
        self.setupUi()
        UpdateDashBoard.setResultDashBoard(self)

    def setupUi(self):
        self.verticalLayout = QtWidgets.QVBoxLayout(self)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("ResultDashBoardVerticalLayout")
        self.TrainLoss = ResultLosses("Training Loss", self)
        self.TestLoss = ResultLosses("Testing Loss", self)
        self.LossGraph = ResultLossGraph(self)
        self.LossGraph.updateGraph()
        self.Heatmap = ResultHeatmap(self)
        self.Accuracy = ResultMetric("Accuracy", self)
        self.label = ResultLabels(self)
        self.Precision = ResultMetrics("Precision", self)
        self.Recall = ResultMetrics("Recall", self)
        self.F1Score = ResultMetrics("F1 Score", self)
        font = QtGui.QFont()
        font.setFamily("SegoeUIMonoW01-Regular") #Fixed width font family to render the result
        font.setStyleHint(QtGui.QFont.TypeWriter)
        font.setPointSize(TEXT_FONT_SIZE)
        self.TrainLoss.setFont(font)
        self.TestLoss.setFont(font)
        self.Accuracy.setFont(font)
        self.Precision.setFont(font)
        self.Recall.setFont(font)
        self.F1Score.setFont(font)
