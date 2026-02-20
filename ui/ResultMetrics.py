from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from ui.ResultMetric import ResultMetric
from ui.ResultDashBoardConstant import *

"""
The metric class for precision, recall and f1score
for each metric, show the value class by class
the label names are obtained from ResultLabels class
"""
class ResultMetrics(ResultMetric):
    f_string_by_class = "\n{:<11}{:.2%}"
    def __init__(self, metric_type, parent=None):
        super().__init__(metric_type, parent)
        self.f_string = metric_type + ":"
        self.updateLabel()
        self.showMetrics()

    def _setSize(self, num_classes=2):
        height = METRICS_WIDGET_BASE_HEIGHT + num_classes * METRICS_WIDGET_VAR_HEIGHT
        self.setMinimumSize(QtCore.QSize(WIDGET_WIDTH, height))
        self.setMaximumSize(QtCore.QSize(WIDGET_WIDTH, height))

    def updateLabel(self):
        label_widget = self.parent().findChild(QLabel, "Result DashBoard Labels")
        self.label = label_widget.getLabel()
        self.num_classes = label_widget.getNumClass()
        self._setSize(self.num_classes)

    def showMetrics(self, metrics=None):
        if metrics is None:
            metrics = [0 for i in range(self.num_classes)]
        self.setHidden(False)
        tar_string = self.f_string
        for idx in range(len(metrics)):
            tar_string = tar_string + ResultMetrics.f_string_by_class.format(
                                      self.label[idx], metrics[idx])
        self.setText(tar_string)

    def hideMetrices(self):
        self.setHidden(True)
