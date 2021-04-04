import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QImage, QPixmap, QPainter, QCursor, QPen, QColor, QBrush
from PyQt5.QtCore import QMimeData, Qt, QPoint
from ui.DatasetPopup import *
from ui.DatasetIcon import *
from dataset.DatasetObject import *

"""
The QLabel shown on the main canvas
when user click on this widget, it shows the widget pop up
user can select the dataset on the pop up widget
provide access to the dataset object through the static method
    DatasetLoader.getDatasetObject()
"""
class DatasetLoader(DatasetIcon):
    dataset_object = DatasetObject()
    inTraining = False
    def __init__(self,parent, popUpParent, loaderQRect):
        default_dataset = 'bi_moon'
        super().__init__(parent, default_dataset)
        self.setGeometry(loaderQRect)
        self.setAcceptDrops(False)
        #self.dataset_object = DatasetObject()       #The dataset object this loader owns
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
        """
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
        """

    #override the DatasetIcon
    #When user release the button, it show/hide the popup panel
    #followed by the release effect
    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)
        if not DatasetLoader.inTraining:
            self.getPopupWidget().toggle()
        self.showImage(hover=True)

    #load the image and csv file to the program
    #accept a DatasetIcon object
    #invoked only after click and release an icon on popup widget, and the first time the program runs
    def loadDataset(self, selected):
        self.getPopupWidget().resetNoise()    #this will trigger the redraw function, reset it first
        has_loaded_once = self.isDatasetLoaded()
        if has_loaded_once:
            self.getSelectedDatasetWidget().showImage(press=False)
        load_success = DatasetLoader.getDatasetObject().loadDataset(dataset_name=selected.getDatasetName())
        if load_success:
            self.__setLoadedDatasetFromWidget(selected)
            self.getSelectedDatasetWidget().showImage(press=True)
            self.__updateStateAfterLoad(hover=has_loaded_once)
        else:
            print("Load Dataset Failed:", selected.getDatasetName())
            self.__setLoadedDatasetFromWidget(None)
            self.__updateStateAfterLoad()

    def __setLoadedDatasetFromWidget(self, widget=None):
        name = None if widget is None else widget.getDatasetName()
        pixmap = DatasetIcon.getDefaultPixmap() if widget is None else widget.getDatasetPixmap()
        self.__setSelectedDatasetWidget(widget)
        self.__setSelectedDatasetName(name)
        self._setDatasetPixmap(pixmap)
        self.__setLastLoadedDatasetPixmap(pixmap)

    def __updateStateAfterLoad(self, hover=True):
        self.showImage(hover=hover)
        self.getPopupWidget().updateDatasetPlotPixmap()
        self.getPopupWidget().showDatasetInfo()

    #Set the icon image using the icon image in datasetIcon object
    #if the passed argument is itself, it change back the icon image to the previously loaded icon
    #invoked when a dataset icon is clicked/hovered or leaving the popup widget
    def changeIconImg(self, datasetIcon, hover):
        if self != datasetIcon:
            self._setDatasetPixmap(datasetIcon.getDatasetPixmap())
        else:
            self._setDatasetPixmap(self.last_loaded_piximg)
        self.getPopupWidget().updateDatasetPlotPixmap()
        self.showImage(hover=hover)

    #Set the icon image by
    #either copy the icon from CNN dataset
    #or plot the data with noised added to the math dataset
    def plotData(self):
        tmpfile = "tmp"
        filename = DatasetMeta.dataset_directory+'img/'+tmpfile+'.png'
        DatasetLoader.getDatasetObject().plotData(filename)
        self.loadDatasetImg(tmpfile)
        self.__setLastLoadedDatasetPixmap(self.getDatasetPixmap())
        self.getPopupWidget().updateDatasetPlotPixmap()
        self.showImage(hover=True)

    def addNoiseToData(self, val):
        DatasetLoader.getDatasetObject().varyData(val)
        self.plotData()

    def isDatasetLoaded(self):
        return self.getSelectedDatasetWidget() != None and DatasetLoader.getDatasetObject().isLoadSuccess()

    def isDataLoader(self):
        return True

    def isDatasetIcon(self):
        return False

    def getTrainData(self):
        return DatasetLoader.getDatasetObject().getTrainData()

    def getTestData(self):
        return DatasetLoader.getDatasetObject().getTestData()

    def getTrainingSetRatio(self):
        return DatasetLoader.getDatasetObject().getTrainingSetRatio()

    @staticmethod
    def getDatasetObject():
        return DatasetLoader.dataset_object

    def getPopupWidget(self):
        return self.popup

    def getSelectedDatasetWidget(self):
        return self.selected_dataset_widget

    def setTrainingSetRatio(self, val):
        DatasetLoader.getDatasetObject().setTrainingSetRatio(val)

    @staticmethod
    def setTrainingSignal(state):
        DatasetLoader.inTraining = state

    def __setLastLoadedDatasetPixmap(self, pixmap):
        self.last_loaded_piximg = pixmap

    def __setSelectedDatasetName(self, name):
        self.dataset_name = name

    def __setSelectedDatasetWidget(self, widget):
        self.selected_dataset_widget = widget
