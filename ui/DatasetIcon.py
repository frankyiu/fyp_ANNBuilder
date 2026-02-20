import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QPen, QColor, QBrush
from PyQt5.QtCore import QMimeData, Qt, QPoint, QFile
from ui.QLabelEffect import QLabelEffect
from dataset.DatasetMeta import *

"""
The class for the icons used in popup widget, inherit QLabelEffect to Reuse the drawing Code
"""
class DatasetIcon(QLabelEffect):
    def __init__(self,parent, dataset, popup=None):
        super().__init__(parent)
        self.dataset_name = dataset     #string name of the dataset, used for loading the image and data
        self.dataset_piximg = None      #Pixmap of the dataset icon
        self.popup = popup              #the popup widget which owns this icon
        self.icon_loaded = False
        self.setScaledContents(True)
        self.setStyleSheet("background:transparent;")
        self.loadDatasetImg()
        self.show()

    """
    When user press the icon, the icon shows a pressing effect
    overrided by the DatasetLoader
    """
    def mousePressEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        if event.button() == Qt.LeftButton:
            self.showImage(press=True)

    """
    When user release the button, it select and load the dataset.
    overrided by the DatasetLoader
    """
    def mouseReleaseEvent(self, event):
        self.showImage(hover=True)
        self.getPopupWidget().getDataLoader().loadDataset(self)

    """
    When user hover the icon, it changes the icon of dataloader temporarily
    """
    def enterEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)
        self.showImage(hover=True)
        if self.isDatasetIcon():
            self.getPopupWidget().getDataLoader().changeIconImg(self, hover=True)
            self.getPopupWidget().showDatasetInfo(self.getDatasetName())
            if not self.isIconLoaded(): #try reloading the image
                self.loadDatasetImg()

    """
    When user leave the icon after hovering, it change back the icon of dataloader
    """
    def leaveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        if self.isDataLoader():
            self.showImage(hover=False)
        else:
            self.showImage(press=self.isSelectedByDataLoader())        #show the press effect if this dataset is selected
            self.getPopupWidget().getDataLoader().changeIconImg( \
                    self.getPopupWidget().getDataLoader(), hover=True) #show the image of last selected dataset
            self.getPopupWidget().showDatasetInfo()                    #show the info of last selected dataset

    """
    handles the hovering and pressing effect of the icon
    """
    def showImage(self, hover=False, press=False):
        super().showImage(hover, press)

    #load the image file using the dataset name from the system
    def loadDatasetImg(self, filename=None):
        filename = self.getDatasetName() if filename is None else filename
        path = DatasetMeta.dataset_img_directory+filename+('.png' if not self.isCNNIcon() else '_0.png')
        self.__setIconPixmap(path)
        self.setQPixmapDrawn(self.getDatasetPixmap())
        self.setRoundedRadius(50)
        self.showImage()

    def __setIconPixmap(self, path):
        if QFile.exists(path):
            self._setDatasetPixmap(QPixmap(path))
            self.icon_loaded = True
        else:
            print("Image Source File not Found:", path)
            self._setDatasetPixmap(DatasetIcon.getDefaultPixmap())
            self.icon_loaded = False

    """
    Whether this refers to a CNN dataset or not
    """
    def isCNNIcon(self):
        return DatasetMeta.isCNN(self.dataset_name) if self.isDatasetIcon() else False

    def isDataLoader(self):
        return False

    def isDatasetIcon(self):
        return True

    def isIconLoaded(self):
        return self.icon_loaded

    def isSelectedByDataLoader(self):
        return self == self.getPopupWidget().getDataLoader().getSelectedDatasetWidget()

    def getPopupWidget(self):
        return self.popup

    def getDatasetName(self):
        return self.dataset_name

    def getDatasetPixmap(self):
        return self.dataset_piximg

    def _setDatasetPixmap(self, pixmap):
        self.dataset_piximg = pixmap
        self.setQPixmapDrawn(self.dataset_piximg)

    @staticmethod
    def getDefaultPixmap():
        return QLabelEffect.getDefaultPixmap()
