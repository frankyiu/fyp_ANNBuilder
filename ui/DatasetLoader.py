import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QImage, QPixmap, QPainter, QCursor, QPen, QColor, QBrush
from PyQt5.QtCore import QMimeData, Qt, QPoint
from ui.DatasetPopup import *
from ui.DatasetIcon import *
from dataset.DatasetObject import *

#This is the widget attched to the main canvas
#when click on this widget, it pop up another widget to select data set
#get the data (ndarray, (N, n_features) for features, (N, ) for label) using obj.getFeature(), and obj.getLabel()
#return None if data set is not found
class DatasetLoader(DatasetIcon):
    def __init__(self,parent, popUpParent, loaderQRect):
        default_dataset = 'bi_moon'
        super().__init__(parent, default_dataset)
        self.setGeometry(loaderQRect)
        self.setAcceptDrops(False)
        self.dataset_object = DatasetObject()       #The dataset object this loader owns
        self.selected_dataset_widget = None
        self.popup = DatasetPopup(popUpParent,self) #The popup this loader owns
        self.getPopupWidget().updateDatasetPlotPixmap()
        self.loadDataset(self.getPopupWidget().getDatasetIconWidget(default_dataset))
        self.getPopupWidget().showDatasetInfo(self.getDatasetName())
        self.getPopupWidget().toggle(False)
        self.show()

    def writeSettingToDict(self):
        setting = {}
        setting["dataset"] = self.getDatasetName()
        setting["split"] = self.getPopupWidget().getTrainTestSplitValue()
        setting["noise"] = self.getPopupWidget().getNoiseValue()
        return setting

    def readSettingFromDict(self, setting):
        self.loadDataset(self.getPopupWidget().getDatasetIconWidget(setting["dataset"]))
        self.getPopupWidget().resetSplit(setting["split"])
        self.getPopupWidget().resetNoise(setting["noise"])
        self.showImage(hover=False)

    #override the DatasetIcon
    #When user press the dataloader icon, it shows the pressing effect
    def mousePressEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        if event.button() == Qt.LeftButton:
            self.showImage(press=True)

        #Sample use of saving and loading the setting
        import pickle
        path_to_save_folder = ""
        if event.button() == Qt.RightButton:
            setting = self.writeSettingToDict()
            with open(path_to_save_folder+"tmpsetting.ds", "wb") as f:
                pickle.dump(setting, f)
            print("Setting Saved")
        elif event.button() == Qt.MidButton:
            with open(path_to_save_folder+"tmpsetting.ds", "rb") as f:
                setting = pickle.load(f)
            self.readSettingFromDict(setting)
            print("Setting Loaded")

    #override the DatasetIcon
    #When user release the button, it show/hide the popup panel
    #followed by the release effect
    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)
        self.getPopupWidget().toggle()
        self.showImage(hover=True)

    #load the image and csv file to the program
    #accept a DatasetIcon object
    #invoked only after click and release an icon on popup widget, and the first time the program runs
    def loadDataset(self, selected):
        self.getPopupWidget().resetNoise()                              #this will trigger the redraw function, reset it first
        has_loaded_once = self.isDatasetLoaded()
        if has_loaded_once:
            self.getSelectedDatasetWidget().showImage(press=False)
        path = DatasetIcon.dataset_directory
        load_success = self.getDatasetObject().loadDataset(path, selected.getDatasetName())
        if load_success:
            self.setSelectedDatasetWidget(selected)
            self.setSelectedDatasetName(selected.getDatasetName())          #set the selected dataset
            self.setDatasetPixmap(selected.getDatasetPixmap())              #use the pixmap of the DatasetIcon object
            self.setLastLoadedDatasetPixmap(self.getDatasetPixmap())        #keep a copy every time it load a pixmap
            self.showImage(hover=has_loaded_once)                           #The loader wont show hovering effect the first time
            self.getSelectedDatasetWidget().showImage(press=True)
            self.getPopupWidget().updateDatasetPlotPixmap()
            self.getPopupWidget().showDatasetInfo()
        else:
            print("Load Dataset Failed:", selected.getDatasetName())
            self.setSelectedDatasetWidget(None)
            self.setSelectedDatasetName(None)
            self.setDatasetPixmap(QPixmap(600,600))
            self.setLastLoadedDatasetPixmap(self.getDatasetPixmap())
            self.showImage(hover=True)
            self.getPopupWidget().updateDatasetPlotPixmap()
            self.getPopupWidget().showDatasetInfo()


    #Set the icon image using the icon image in datasetIcon object
    #if the passed argument is itself, it change back the icon image to the previously loaded icon
    def changeIconImg(self, datasetIcon, hover):
        if self != datasetIcon:
            self.setDatasetPixmap(datasetIcon.getDatasetPixmap())
        else:
            self.setDatasetPixmap(self.getLastLoadedDatasetPixmap())
        self.getPopupWidget().updateDatasetPlotPixmap()
        self.showImage(hover=hover)

    def plotData(self, isClassify=True):
        tmpfile = "tmp"
        filename = DatasetIcon.dataset_directory+'img/'+tmpfile+'.png'
        self.getDatasetObject().plotData(filename, isClassify)
        self.loadDatasetImg(tmpfile)
        self.getPopupWidget().updateDatasetPlotPixmap()
        self.showImage(hover=True)

    def addNoiseToData(self, val):
        if self.getDatasetObject().isCNNData():
            self.getDatasetObject().doVariation(val)
            self.plotData()
        else:
            dataset_name = self.getDatasetName()
            is_gaussian = self.getPopupWidget().isGaussian(self.getDatasetName())
            is_regression = self.getPopupWidget().isRegression(self.getDatasetName())
            self.getDatasetObject().addNoiseToData(val, is_gaussian, is_regression)
            self.plotData(not is_regression)

    def isDatasetLoaded(self):
        return self.getSelectedDatasetWidget() != None and self.getDatasetObject().hasData()

    def isDataLoader(self):
        return True

    def isDatasetIcon(self):
        return False

    def getTrainData(self):
        return self.getDatasetObject().getTrainData()

    def getTestData(self):
        return self.getDatasetObject().getTestData()

    def getTrainingSetRatio(self):
        return self.getDatasetObject().getTrainingSetRatio()

    def getDatasetObject(self):
        return self.dataset_object

    def getPopupWidget(self):
        return self.popup

    def getLastLoadedDatasetPixmap(self):
        return self.last_loaded_piximg

    def getSelectedDatasetWidget(self):
        return self.selected_dataset_widget

    def setTrainingSetRatio(self, val):
        self.getDatasetObject().setTrainingSetRatio(val)

    def setLastLoadedDatasetPixmap(self, pixmap):
        self.last_loaded_piximg = pixmap

    def setSelectedDatasetName(self, name):
        self.dataset_name = name

    def setSelectedDatasetWidget(self, widget):
        self.selected_dataset_widget = widget
