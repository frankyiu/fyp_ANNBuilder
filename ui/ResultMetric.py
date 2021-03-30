from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from ui.ResultDashBoardConstant import *

"""
Parent class of all textual label on dashboard
inheried by ResultLosses and ResultMetrics
Use a format string (with fixed width font) to render the result
"""
class ResultMetric(QLabel):
    def __init__(self, metric_type, parent=None):
        super(ResultMetric,self).__init__(parent)
        self.metric_type = metric_type
        self.f_string = metric_type + ":\n{: 17.3%}"
        self._setSize()
        self.setObjectName(metric_type)
        parent.verticalLayout.addWidget(self)
        self.showMetric()

    def _setSize(self):
        self.setMinimumSize(QtCore.QSize(WIDGET_WIDTH, METRIC_WIDGET_HEIGHT))
        self.setMaximumSize(QtCore.QSize(WIDGET_WIDTH, METRIC_WIDGET_HEIGHT))

    def showMetric(self, metric=0):
        self.setHidden(False)
        self.setText(self.f_string.format(metric))

    def hideMetrice(self):
        self.setHidden(True)
