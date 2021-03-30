from PyQt5 import QtCore
from PyQt5.QtWidgets import QWidget
from ui.ResultDashBoardConstant import *
from dataset.generator import plot_np
import matplotlib
#matplotlib.use('Agg') #This line avoid multithreding runtime error
matplotlib.use('QT5Agg')
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.colors import ListedColormap
from ml.Utility import reverse_one_hot
import time


class HeatmapCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=CONTOUR_DEFAULT_WIDTH,
                 height=CONTOUR_DEFAULT_HEIGHT, dpi=CONTOUR_DEFAULT_DPI):
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.figure.add_axes([0, 0, 1, 1])
        super(HeatmapCanvas, self).__init__(self.figure)
        self.setParent(parent)

"""
The heatmap graph on the dashboard are drawn using matplotlib backend
Other alternative frameworks include: pyqtgraph, matplotlib animation
"""
class ResultHeatmap(QWidget):
    def __init__(self,parent=None):
        super(ResultHeatmap,self).__init__(parent)
        self.setParent(parent)
        self.setMinimumSize(QtCore.QSize(WIDGET_WIDTH, WIDGET_WIDTH))
        self.setMaximumSize(QtCore.QSize(WIDGET_WIDTH, WIDGET_WIDTH))
        self.setObjectName("Heatmap")
        self.canvas = HeatmapCanvas(self)
        self.cmap  = CONTOUR_CMAP_COLOR
        self.resetAll()
        parent.verticalLayout.addWidget(self)

    """
    keep a reference of the test set data and model for future prediction
    scatter the data points on the graph once during the whole training
    """
    def cacheData(self, X, y, model, isClassify):
        self.X = X
        self.model = model
        data = np.concatenate((self.X, y.reshape(-1,1)), axis=1)
        plot_np(data, None, isClassify, self.canvas.figure, self.canvas.axes, CONTOUR_DOT_SIZE)

    """
    Precompute and store the meshgrid for future contour graph prediction
    """
    def createCopy(self, X, y, model, grid_size):
        f1_min, f1_max = X[:, 0].min()-1, X[:, 0].max()+1    #+-1 for the margin
        f2_min, f2_max = X[:, 1].min()-1, X[:, 1].max()+1    #+-1 for the margin
        f1 = np.arange(f1_min, f1_max, grid_size)
        f2 = np.arange(f2_min, f2_max, grid_size)
        xx, yy = np.meshgrid(f1, f2)
        grid = np.hstack((xx.reshape((-1,1)), yy.reshape((-1,1))))
        self.xx = xx
        self.yy = yy
        self.grid = grid
        self.grid_n = grid.shape[0]
        self.n_classes = len(np.unique(y))
        self.lst_cmp = ListedColormap(self.cmap[:self.n_classes])
        self.cacheData(X, y, model, isClassify=True)

    """
    Reset all the reference to the dataset
    and all precomputed data in the previous training
    """
    def resetAll(self):
        self.xx = None
        self.yy = None
        self.grid = None
        self.grid_n = None
        self.n_classes = None
        self.lst_cmp = None
        self.X = None
        self.model = None
        self.contour = None
        self.reg_line = None
        self.y_pred = None  #prediction of test set is done together

    """
    Only redraw the contour graph during training
    test set prediction is done together with the contour graph
    feed the data directly to the model without calling predict() for performance purpose
    """
    def updateContour(self):
        self.clearContor()
        pred_m = self.model(np.concatenate([self.grid, self.X], axis=0)).numpy()
        self.y_pred = reverse_one_hot(pred_m[self.grid_n:, :])
        self.zz = reverse_one_hot(pred_m[:self.grid_n, :]).reshape(self.xx.shape).astype(int)    #cast as integer
        self.contour = self.canvas.axes.contourf(self.xx, self.yy, self.zz, cmap=self.lst_cmp, \
                                                 zorder=0, vmin=0, vmax=self.n_classes-1) #set vmin vmax for norm pipeline

    """
    Main flow to create the heatmap for math dataset classification
    grid_size affect the stretching of the plotted data
    """
    def generateHeatmapClassify(self, X, y, model, grid_size=0.3):
        #First call
        if self.n_classes is None:
            self.clearPlot()
            self.setHidden(False)
            self.createCopy(X, y, model, grid_size)

        self.updateContour()
        self.canvas.draw_idle() #draw_idle() spent less time than draw()
        return self.y_pred

    """
    Main flow to create the heatmap for math dataset regression
    feed the data directly to the model without calling predict() for performance purpose
    """
    def generateHeatmapRegression(self, X, y, model, grid_size=None):
        #First call
        if self.model is None:
            self.clearPlot()
            self.setHidden(False)
            self.cacheData(X, y, model, isClassify=False)

        #only need to draw a line to show the fitting of model
        self.clearLinePlot()
        y_pred = self.model(self.X)
        self.reg_line = self.canvas.axes.plot(self.X, y_pred, \
                        color=CONTOUR_REGRESSION_LINE_COLOR, linewidth=CONTOUR_REGRESSION_LINE_WIDTH)
        self.canvas.draw_idle()  #draw_idle() spent less time than draw()

    """
    For Contour graph in Classification
    """
    def clearContor(self):
        if self.contour is not None:
            for coll in self.contour.collections:
                coll.remove()

    """
    For the regression line
    """
    def clearLinePlot(self):
        if self.reg_line is not None:
            for coll in self.reg_line:
                coll.remove()

    """
    Clear the scatter and all others drawn
    Used for CNN dataset, and first call for Math dataset
    """
    def clearPlot(self):
        if not self.isHidden():
            self.canvas.axes.clear()
            self.setHidden(True)

    """
    Clear the plot and show on GUI to signal the user the dataset is reset
    """
    def resetPlot(self):
        self.canvas.axes.clear()
        self.canvas.draw()
