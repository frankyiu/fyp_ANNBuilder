import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QPen, QColor, QBrush
from PyQt5.QtCore import QMimeData, Qt, QPoint

#This is the class for the icons used in popup widget
class DatasetIcon(QLabel):
    
    dataset_directory = 'dataset/'
    
    def __init__(self,parent, dataset, loader=None):
        super(QLabel,self).__init__(parent)
        self.dataset_name = dataset     #string name of the dataset, used for loading the image and csv
        self.dataset_piximg = None      #Pixmap of the dataset icon
        self.loader = loader            #the dataloader
        self.setScaledContents(True)
        self.setStyleSheet("background:transparent;")
        self.loadDataSetImg()
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
        if self.loader is not None:
            self.loader.loadDataSet(self)
            self.loader.popup.toggle(False)

    #When user hover the icon, it changes the icon of dataloader temporarily
    def enterEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)
        self.showImage(hover=True)
        if self.loader is not None:
            self.loader.setDataSetImg(self)
            self.loader.showImage(hover=True)

    #When user leave the icon after hovering, it change back the icon of dataloader
    def leaveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        self.showImage(hover=False)
        if self.loader is not None:
            self.loader.setDataSetImg(self.loader)
            self.loader.showImage(hover=True)

    #This function handles the hovering and pressing effect of the icon
    def showImage(self, hover=False, press=False):
        tmp = QPixmap(self.dataset_piximg.size())
        tmp.fill(Qt.transparent)
        painter = QPainter(tmp)
        painter.setBrush(QBrush(self.dataset_piximg))
        painter.setPen(Qt.NoPen)
        painter.setRenderHint(QPainter.Antialiasing)
        radius = 50
        painter.drawRoundedRect(self.dataset_piximg.rect(), radius, radius)
        if hover:
            painter.setBrush(QColor(255,255,255,128))
            painter.drawRoundedRect(self.dataset_piximg.rect(), radius, radius)
            pass
        elif press:
            painter.setBrush(QColor(0,0,0,64))
            painter.drawRoundedRect(self.dataset_piximg.rect(), radius, radius)
            pass
        self.setPixmap(tmp)
        painter.end()

    #load the image file using the dataset name from the system
    def loadDataSetImg(self):
        self.dataset_piximg = QPixmap(DatasetIcon.dataset_directory+'img/'+self.dataset_name+'.png')
        self.last_loaded_piximg = self.dataset_piximg
        self.showImage()

    #Set the icon image using the icon image in datasetIcon object
    def setDataSetImg(self, datasetIcon):
        if self != datasetIcon:
            self.dataset_piximg = datasetIcon.dataset_piximg
        else:
            self.dataset_piximg = self.last_loaded_piximg
        self.showImage()
