import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QPen, QColor, QBrush
from PyQt5.QtCore import QMimeData, Qt, QPoint, QFile

#This is the class for the icons used in popup widget
class DatasetIcon(QLabel):

    dataset_directory = 'dataset/'

    def __init__(self,parent, dataset, popup=None):
        super(QLabel,self).__init__(parent)
        self.dataset_name = dataset     #string name of the dataset, used for loading the image and csv
        self.dataset_piximg = None      #Pixmap of the dataset icon
        self.popup = popup              #the popup widget which owns this icon
        self.icon_loaded = False
        self.setScaledContents(True)
        self.setStyleSheet("background:transparent;")
        self.loadDatasetImg()
        self.show()

    #When user press the icon, the icon shows a pressing effect
    #overrided by the DatasetLoader
    def mousePressEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        if event.button() == Qt.LeftButton:
            self.showImage(press=True)

    #When user release the button, it select and load the dataset.
    #after that, close the popup panel
    #overrided by the DatasetLoader
    def mouseReleaseEvent(self, event):
        self.showImage(hover=True)
        self.getPopupWidget().getDataLoader().loadDataset(self)

    #When user hover the icon, it changes the icon of dataloader temporarily
    def enterEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)
        self.showImage(hover=True)
        if self.isDatasetIcon():
            self.getPopupWidget().getDataLoader().changeIconImg(self, hover=True)
            self.getPopupWidget().showDatasetInfo(self.getDatasetName())
            if not self.isIconLoaded():
                self.loadDatasetImg()


    #When user leave the icon after hovering, it change back the icon of dataloader
    def leaveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        if not self.isDataLoader():
            if not self.isSelectedByDataLoader():
                self.showImage(hover=False)
                self.getPopupWidget().getDataLoader().changeIconImg(self.getPopupWidget().getDataLoader(), hover=True)
                self.getPopupWidget().showDatasetInfo()
            else:
                self.showImage(press=True)
                self.getPopupWidget().getDataLoader().changeIconImg(self.getPopupWidget().getDataLoader(), hover=True)
                self.getPopupWidget().showDatasetInfo()
        else:
            self.showImage(hover=False)


    #This function handles the hovering and pressing effect of the icon
    def showImage(self, hover=False, press=False):
        tmp = QPixmap(self.getDatasetPixmap().size())
        tmp.fill(Qt.transparent)
        painter = QPainter(tmp)
        painter.setBrush(QBrush(self.getDatasetPixmap()))
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)
        radius = 50
        painter.drawRoundedRect(self.getDatasetPixmap().rect(), radius, radius)
        if hover:
            painter.setBrush(QColor(255,255,255,128))
            painter.drawRoundedRect(self.getDatasetPixmap().rect(), radius, radius)
        elif press:
            painter.setBrush(QColor(0,0,0,128))
            painter.drawRoundedRect(self.getDatasetPixmap().rect(), radius, radius)
        self.setPixmap(tmp)
        painter.end()

    #load the image file using the dataset name from the system
    def loadDatasetImg(self, filename=None):
        if filename is None:
            filename = self.getDatasetName()
        path = DatasetIcon.dataset_directory+'img/'+filename+('.png' if not self.isCNNIcon() else '_0.png')
        if QFile.exists(path):
            self.setDatasetPixmap(QPixmap(path))
            self.icon_loaded = True
        else:
            print("Image Source File not Found:", path)
            self.setDatasetPixmap(QPixmap(600,600))
            self.icon_loaded = False
        if self.isDataLoader():
            self.setLastLoadedDatasetPixmap(self.getDatasetPixmap())
        self.showImage()

    def isCNNIcon(self):
        return False

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

    def setDatasetPixmap(self, pixmap):
        self.dataset_piximg = pixmap
