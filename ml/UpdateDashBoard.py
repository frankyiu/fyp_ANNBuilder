#from ui.ResultDashBoard import *
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
from dataset.DatasetMeta import DatasetMeta
from dataset.CNNDataset import CNNDataset
from ml.Utility import reverse_one_hot
import numpy as np
import time

"""
A wrapper class to the result dash board
All methods are static
Comments attached to important method
"""
class UpdateDashBoard():
    DashBoardObj = None
    IsDatasetCNN = False
    IsDatasetReg = False

    """
    keep track the dash board object
    fter it is created
    must be invoked, after the dash object is created
    """
    @staticmethod
    def setResultDashBoard(obj):
        UpdateDashBoard.DashBoardObj = obj

    """
    pass the reference of the losses history in Training module
    to the dash board object
    the loss graph updates based on these referenced lists
    must be invoked, before training
    """
    @staticmethod
    def connectLossGraph(train_losses, test_losses):
        UpdateDashBoard.DashBoardObj.LossGraph.setLossesReference(train_losses, test_losses)

    """
    pass the values of the losses of an iteration in training
    to the dash board object, and show the values in the QLabel
    must be invoked, during training, after an iteration of training
    """
    @staticmethod
    def updateLosses(train_loss, test_loss):
        UpdateDashBoard.DashBoardObj.TrainLoss.showMetric(train_loss)
        UpdateDashBoard.DashBoardObj.TestLoss.showMetric(test_loss)

    """
    update the loss graph after an iteration in training
    this invoked the updateGraph() function in the LossGraph object
    must be invoked, during training, after an iteration of training
    """
    @staticmethod
    def updateLossGraph():
        UpdateDashBoard.DashBoardObj.LossGraph.updateGraph()

    """
    update the visibility and the name of metrics in dash board
    e.g. shows Accuracy, Precision, ... for classification task
         and change the class label for each entry in Precision, ...
    must be invoked, before training
    """
    @staticmethod
    def updateMetricNames(dataset_name, variation):
        n_classes = UpdateDashBoard.__getClasses(dataset_name, variation)
        UpdateDashBoard.IsDatasetReg = DatasetMeta.isRegression(dataset_name)
        UpdateDashBoard.IsDatasetCNN = DatasetMeta.isCNN(dataset_name)

        if DatasetMeta.isRegression(dataset_name):
            UpdateDashBoard.__setMetricsVisible(False)
            return
        elif DatasetMeta.isMath(dataset_name):
            UpdateDashBoard.DashBoardObj.label.setLabelMath(n_classes)
        elif CNNDataset.isMNIST(dataset_name):
            UpdateDashBoard.DashBoardObj.label.setLabelMNIST(n_classes)
            UpdateDashBoard.DashBoardObj.Heatmap.clearPlot()
        elif CNNDataset.isCIFAR10(dataset_name):
            UpdateDashBoard.DashBoardObj.label.setLabelCIFAR10(n_classes)
            UpdateDashBoard.DashBoardObj.Heatmap.clearPlot()

        UpdateDashBoard.DashBoardObj.Precision.updateLabel()
        UpdateDashBoard.DashBoardObj.Recall.updateLabel()
        UpdateDashBoard.DashBoardObj.F1Score.updateLabel()
        UpdateDashBoard.__setMetricsVisible(True)

    def __setMetricsVisible(show):
        if show:
            UpdateDashBoard.DashBoardObj.Accuracy.showMetric()
            UpdateDashBoard.DashBoardObj.Precision.showMetrics()
            UpdateDashBoard.DashBoardObj.Recall.showMetrics()
            UpdateDashBoard.DashBoardObj.F1Score.showMetrics()
        else:
            UpdateDashBoard.DashBoardObj.Accuracy.hideMetrice()
            UpdateDashBoard.DashBoardObj.Precision.hideMetrices()
            UpdateDashBoard.DashBoardObj.Recall.hideMetrices()
            UpdateDashBoard.DashBoardObj.F1Score.hideMetrices()

    @staticmethod
    def __getClasses(dataset_name, variation):
        if DatasetMeta.isCNN(dataset_name):
            return DatasetMeta.getClasses(dataset_name, variation)
        elif dataset_name in ["multi_four", "multi_circles"]:
            n_class = 4
        elif dataset_name in ["multi_three"]:
            n_class = 3
        else:
            n_class = 2
        return [i for i in range(n_class)]


    """
    update the metrics value and heatmap in dash board
    the prediction of test set is perform together with the contour graph
    for performance purpose
    for CNN data, no contour graph will be computed so the prediction is
    done separately (tgt with the loss computation)
    feed the data directly to the model without calling predict() for performance purpose
    must be invoked, during training, after an iteration of training
    """
    @staticmethod
    def updatePredictionResult(X, y, model, pred=None):
        y_pred = UpdateDashBoard.updateHeatmap(X, y, model)
        if UpdateDashBoard.IsDatasetReg:
            return
        elif y_pred is None and pred is not None:
            y_pred = reverse_one_hot(pred)
        UpdateDashBoard.updateMetrics(y, y_pred)


    """
    reset all the references and data stored used in computing the contour graph
    must be invoked, before training
    """
    @staticmethod
    def resetHeatmapReference():
        UpdateDashBoard.DashBoardObj.Heatmap.resetAll()

    """
    reset all the references and data stored used in computing the loss graph
    must be invoked, before training
    """
    @staticmethod
    def resetLossGraphReference():
        UpdateDashBoard.DashBoardObj.LossGraph.resetLossesReference()

    """
    reset the dash board GUI, including
    - the metrics value
    - the drawing of loss graph and contour
    """
    @staticmethod
    def resetDashboardRendering():
        UpdateDashBoard.DashBoardObj.LossGraph.reset()
        UpdateDashBoard.DashBoardObj.Heatmap.resetPlot()
        UpdateDashBoard.resetMetrics()

    @staticmethod
    def resetMetrics():
        UpdateDashBoard.DashBoardObj.TrainLoss.showMetric()
        UpdateDashBoard.DashBoardObj.TestLoss.showMetric()
        UpdateDashBoard.DashBoardObj.Accuracy.showMetric()
        UpdateDashBoard.DashBoardObj.Precision.showMetrics()
        UpdateDashBoard.DashBoardObj.Recall.showMetrics()
        UpdateDashBoard.DashBoardObj.F1Score.showMetrics()

    @staticmethod
    def updateHeatmap(X, y, model):
        if UpdateDashBoard.IsDatasetReg:
            UpdateDashBoard.DashBoardObj.Heatmap.generateHeatmapRegression(X,y,model)
            return None
        elif UpdateDashBoard.IsDatasetCNN:
            UpdateDashBoard.DashBoardObj.Heatmap.clearPlot()
            return None
        else:
            return UpdateDashBoard.DashBoardObj.Heatmap.generateHeatmapClassify(X,y,model)

    @staticmethod
    def updateMetrics(y_true, y_pred):
        UpdateDashBoard.updateAccuracy(accuracy_score(y_true, y_pred))
        precision, recall, fscore, _ = precision_recall_fscore_support( \
                                        y_true, y_pred, average=None, warn_for=tuple())
        UpdateDashBoard.updatePrecision(precision)
        UpdateDashBoard.updateRecall(recall)
        UpdateDashBoard.updateF1Score(fscore)

    @staticmethod
    def updateAccuracy(acc):
        UpdateDashBoard.DashBoardObj.Accuracy.showMetric(acc)

    @staticmethod
    def updatePrecision(lst):
        UpdateDashBoard.DashBoardObj.Precision.showMetrics(lst)

    @staticmethod
    def updateRecall(lst):
        UpdateDashBoard.DashBoardObj.Recall.showMetrics(lst)

    @staticmethod
    def updateF1Score(lst):
        UpdateDashBoard.DashBoardObj.F1Score.showMetrics(lst)
