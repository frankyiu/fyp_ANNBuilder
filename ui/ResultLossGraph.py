# Import libraries
import numpy as np
from ml.Utility import average_every
from pyqtgraph.Qt import QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPen, QColor
import pyqtgraph as pg
from ui.ResultDashBoardConstant import *

"""
The loss graph shown in the dashboard
"""
class ResultLossGraph(QWidget):
    def __init__(self,parent=None):
        super(ResultLossGraph,self).__init__(parent)
        self.__setQAttribute()
        self.__setPlotWidget()
        self.reset()
        parent.verticalLayout.addWidget(self.getPlotWidget())
    pass

    def __setQAttribute(self):
        #self.setGeometry(QtCore.QRect(0, 0, 150, 150))
        self.setMinimumSize(QtCore.QSize(WIDGET_WIDTH, WIDGET_WIDTH))
        self.setMaximumSize(QtCore.QSize(WIDGET_WIDTH, WIDGET_WIDTH))
        self.setObjectName("LossGraphWidget")

    def __setPlotWidget(self):
        self.setPlotWidgetColor((37, 37, 49))
        self.plot_widget = pg.PlotWidget()
        self.plot_widget.plotItem.setMouseEnabled(x=False, y=False)
        self.plot_widget.plotItem.hideAxis('bottom')
        self.plot_widget.plotItem.hideAxis('left')
        self.plot_widget.addLegend(offset=(0,1))
        self.train_loss_graph = self.plot_widget.plot(name="Train")
        self.test_loss_graph = self.plot_widget.plot(name="Test")
        train_pen = self.makePen(LOSS_GRAPH_LINE_WIDTH, LOSS_GRAPH_COLOR_TRAIN)
        test_pen = self.makePen(LOSS_GRAPH_LINE_WIDTH, LOSS_GRAPH_COLOR_TEST)
        self.setPlotWidgetPens(train_pen, test_pen)
        self.setPlotWidgetSize(WIDGET_WIDTH, WIDGET_WIDTH)

    """
    Plot a default loss graph on GUI
    """
    def reset(self, train_losses=None, test_losses=None):
        self.train_losses = [1 for i in range(100)] if train_losses is None else train_losses   #HARDCODED
        self.test_losses = [0.5 for i in range(100)] if test_losses is None else test_losses    #HARDCODED
        self.train_loss_graph.setData(self.train_losses)
        self.test_loss_graph.setData(self.test_losses)

    def setPlotWidgetSize(self, w, h):
        self.plot_widget.setMaximumSize(w,h)
        self.plot_widget.setMinimumSize(w,h)

    def setPlotWidgetColor(self, bg_color):
        if bg_color is not None:
            pg.setConfigOption('background', bg_color)

    def setPlotWidgetPens(self, train_pen, test_pen):
        self.train_loss_graph.setPen(train_pen)
        self.test_loss_graph.setPen(test_pen)

    def makePen(self, width, color):
        return pg.mkPen(width=width,color=color)

    def getPlotWidget(self):
        return self.plot_widget

    """
    set a reference to the list object
    and use this reference to update the loss graph
    """
    def setLossesReference(self, train_losses, test_losses):
        self.train_losses = train_losses
        self.test_losses = test_losses
        self.train_loss_graph.setData(self.train_losses)
        self.test_loss_graph.setData(self.test_losses)
        #self.plot_widget.clear()

    """
    remove the reference to free the memory
    """
    def resetLossesReference(self):
        self.train_losses = []
        self.test_losses = []

    """
    update the loss graph through the list references
    disable auto range while drawing to optimize
    """
    def updateGraph(self):
        self.plot_widget.plotItem.disableAutoRange()    #faster render
        """
        n_avg = 5
        train_pad = np.pad(self.train_losses, (n_avg//2, n_avg-1-n_avg//2), mode='edge')
        test_pad = np.pad(self.test_losses, (n_avg//2, n_avg-1-n_avg//2), mode='edge')
        self.train_loss_graph.setData(np.convolve(train_pad, np.ones((n_avg,))/n_avg, mode='valid'))
        self.test_loss_graph.setData(np.convolve(test_pad, np.ones((n_avg,))/n_avg, mode='valid'))
        """
        self.train_loss_graph.setData(self.train_losses)
        self.test_loss_graph.setData(self.test_losses)
        self.plot_widget.plotItem.autoRange()           #faster render
