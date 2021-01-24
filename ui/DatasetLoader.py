import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QPen, QColor, QBrush
from PyQt5.QtCore import QMimeData, Qt, QPoint
from ui.SelectDatasetPopup import *
from ui.DatasetIcon import *

#This is the widget attched to the main canvas
#when click on this widget, it pop up another widget to select data set
#get the data (ndarray, (N, 2) for features, (N, ) for label) using obj.getFeature(), and obj.getLabel()
#return None if data set is not found
class DatasetLoader(DatasetIcon):
    def __init__(self,parent, popUpParent, loaderQRect):
        super().__init__(parent, 'bi_linear')
        self.setGeometry(loaderQRect)
        self.setAcceptDrops(False)
        self.setText("")
        self.qrect = loaderQRect    #position data of this loader object
        self.data = None            #store the real data
        self.loadDataSet(self)      #load the real data
        self.show()
        self.popup = SelectDatasetPopup(popUpParent,self) #create the popup and hide it
        self.popup.toggle(False)

    #override the DatasetIcon
    #When user press the dataloader icon, it shows the pressing effect
    def mousePressEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        if event.button() == Qt.LeftButton:
            self.showImage(press=True)

    #override the DatasetIcon
    #When user release the button, it show/hide the popup panel
    #followed by the release effect
    def mouseReleaseEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)
        self.popup.toggle()
        self.showImage(hover=True)

    #load the image and csv file to the program
    #accept a DatasetIcon object
    def loadDataSet(self, selected):
        self.dataset_name = selected.dataset_name     #set the selected dataset
        self.dataset_piximg = selected.dataset_piximg #use the pixmap of the DatasetIcon object
        self.last_loaded_piximg = self.dataset_piximg #keep a copy every time it load a pixmap
        self.showImage()

        csv = DatasetIcon.dataset_directory + self.dataset_name + '.csv'
        try:
            self.data = np.genfromtxt(csv, delimiter=',', skip_header=1)
            print('Data set ' + self.dataset_name +' is loaded')
        except FileNotFoundError as file_error:
            print(file_error)
            self.data = None

    #ndarray of shape (N, 2)
    def getFeature(self):
        return self.data[:,:-1] if self.data is not None else None

    #ndarray of shape (N, )
    def getLabel(self):
        return self.data[:,-1] if self.data is not None else None
