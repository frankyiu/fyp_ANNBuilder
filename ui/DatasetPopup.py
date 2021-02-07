import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QPen, QColor, QBrush
from PyQt5.QtCore import QMimeData, Qt, QPoint, QEvent
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.DatasetIcon import *
from ui.DatasetIconCNN import *
from ui.DatasetLoaderImage import *

class DatasetPopup(QWidget):
    #List of prepared datasets
    datasets = ['bi_linear', 'bi_moon', 'bi_circle', 'bi_xor', 'bi_spiral', 'multi_three', 'multi_four', 'multi_circles', 'reg_inform', 'reg_redun', 'cnn_mnist']

    def __init__(self,parent, loader):
        super(QWidget,self).__init__(parent)
        self.loader = loader        #The loader that owns this popup
        self.widget_lst = []        #The list of icons that this popup owns
        self.datasets_info = None
        self.setupUI()
        self.loadDatasetMetadata()

    #accept a dataset name string, show the target dataset meta info with no noise
    #if None is passed, it shows the current selected dataset meta info and current noise
    def showDatasetInfo(self, dataset_name=None):
        noise_statement = ["No Noise", "Low", "Medium", "High"]
        noise_val = 0
        if dataset_name is None:
            noise_val = self.getNoiseValue()
            dataset_name = self.getDataLoader().getDatasetName()

        (dataname, tasktype, difficulty) = self.datasets_info[dataset_name]

        self.DatasetName.setText("Name: {name}".format(name=dataname))
        self.TaskType.setText("Task: {task}".format(task=tasktype))
        self.Difficulty.setText( "Difficulty: {difficulty}".format(difficulty=difficulty[noise_val]))
        self.Split.setEnabled(True)
        self.SplitName.setText("Train Set Split Ratio: {ratio:.0f}%".format(ratio=self.getDataLoader().getTrainingSetRatio()*100))
        self.NoiseName.setText("Noise: {noise}".format(noise=noise_statement[noise_val]))
        if dataset_name is "cnn_mnist":
            vary_statement = ["0, 1", "4, 7, 9", "2, 3, 5, 6, 8", "All"]
            self.NoiseName.setText("Digits: {vary}".format(vary=vary_statement[noise_val]))
            self.Split.setEnabled(False)
            if noise_val==0:
                self.TaskType.setText("Task: {task}".format(task="Binary Classification"))

    def loadDatasetMetadata(self):
        tmp = {}
        import json
        try:
            with open(DatasetIcon.dataset_directory+"DatasetsMetaInfo.json", "r") as f:
                tmp = json.loads(f.read())
        except FileNotFoundError as fnf_error:
            print(fnf_error, "(Failed to Load Datasets Metadata)")
        finally:
            from collections import defaultdict
            self.datasets_info = defaultdict(lambda: ("", "", [0,0,0,0]))
            self.datasets_info.update(tmp)

    def resetNoise(self, noise=0):
        self.Noise.setValue(noise)

    def resetSplit(self, split=8):
        self.Split.setValue(split)

    #This function handles the show/hide of popup widget
    def toggle(self, state=None):
        if state is not None:
            self.setVisible(state)
        elif self.isVisible():
            self.hide()
        else:
            self.show()

    #When user move the cursor from icon to panel, the loader icon keeps the hovering effect
    def enterEvent(self, event):
        self.getDataLoader().showImage(hover=True)

    #When user does not select any data set and leave the panel, change back the loader icon and close popup
    def leaveEvent(self, event):
        self.getDataLoader().changeIconImg(self.getDataLoader(), hover=False)
        self.toggle(False)

    def updateDatasetPlotPixmap(self):
        return self.DatasetSelected.updateReferenceImg(self.getDataLoader().getDatasetPixmap())

    def updateDatasetNoise(self, noise_val):
        self.showDatasetInfo()
        self.getDataLoader().addNoiseToData(noise_val)

    def updateDatasetSplit(self, split_val):
        self.getDataLoader().setTrainingSetRatio(split_val/10.0)
        self.showDatasetInfo()

    def isGaussian(self, dataset):
        return True if dataset in ['bi_linear', 'multi_three', 'multi_four'] else False

    def isRegression(self, dataset):
        return True if dataset in ['reg_inform', 'reg_redun'] else False

    def getDataLoader(self):
        return self.loader

    #an integer from range [1,9]
    def getTrainTestSplitValue(self):
        return self.Split.value()

    #an integer from range [0,3]
    def getNoiseValue(self):
        return self.Noise.value()

    #a wrapper to access the list of dataset icon widgets/ single dataset icon widget
    #query accept integer, dataset name, or None to return the list
    def getDatasetIconWidget(self, query=None):
        if query is None:
            return self.widget_lst
        elif isinstance(query, int):
            return self.widget_lst[idx]
        elif query in DatasetPopup.datasets:
            for obj in  self.widget_lst:
                if query == obj.getDatasetName():
                    return obj
        return None

    def updateDatasetIconList(self, widget):
        self.widget_lst.append(widget)

    def setupUI(self):
        r_topleft = self.getDataLoader().mapTo(self.parent(),  QtCore.QPoint(0, 0))
        self.setGeometry(QtCore.QRect(r_topleft.x()+80, r_topleft.y()+45, 700, 485))
        self.setStyleSheet("background:rgba(27, 31, 38, 200);border-radius: 10px; color:rgba(255,255,255,200);")
        line_style_sheet = "background:rgba(255,255,255,128);"
        hide_stylesheet = "background:rgba(255,255,255,0);"
        i = 0
        self.horizontalLayoutWidget = QtWidgets.QWidget(self)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 700, 485))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_3.setContentsMargins(10, 10, -1, 10)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_3.setVerticalSpacing(4)
        self.DatasetSelect = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.DatasetSelect.setMinimumSize(QtCore.QSize(400, 30))
        self.DatasetSelect.setMaximumSize(QtCore.QSize(400, 30))
        font = QtGui.QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(24)
        self.DatasetSelect.setFont(font)
        self.DatasetSelect.setObjectName("DatasetSelect")
        self.DatasetSelect.setAlignment(Qt.AlignCenter)
        self.gridLayout_3.addWidget(self.DatasetSelect, 0, 0, 1, 1)


        self.gridLayout_2 = QtWidgets.QGridLayout()
        #self.gridLayout_2.setContentsMargins(10, 10, -1, 10)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Dataset01 = DatasetIcon(self.horizontalLayoutWidget, DatasetPopup.datasets[i], self)
        self.updateDatasetIconList(self.Dataset01)
        i += 1
        self.Dataset01.setEnabled(True)
        self.Dataset01.setMinimumSize(QtCore.QSize(100, 100))
        self.Dataset01.setMaximumSize(QtCore.QSize(100, 100))
        self.Dataset01.setObjectName("Dataset01")
        self.gridLayout_2.addWidget(self.Dataset01, 0, 0, 1, 1)
        self.Dataset02 = DatasetIcon(self.horizontalLayoutWidget, DatasetPopup.datasets[i], self)
        self.updateDatasetIconList(self.Dataset02)
        i += 1
        self.Dataset02.setEnabled(True)
        self.Dataset02.setMinimumSize(QtCore.QSize(100, 100))
        self.Dataset02.setMaximumSize(QtCore.QSize(100, 100))
        self.Dataset02.setObjectName("Dataset02")
        self.gridLayout_2.addWidget(self.Dataset02, 0, 1, 1, 1)
        self.Dataset03 = DatasetIcon(self.horizontalLayoutWidget, DatasetPopup.datasets[i], self)
        self.updateDatasetIconList(self.Dataset03)
        i += 1
        self.Dataset03.setEnabled(True)
        self.Dataset03.setMinimumSize(QtCore.QSize(100, 100))
        self.Dataset03.setMaximumSize(QtCore.QSize(100, 100))
        self.Dataset03.setObjectName("Dataset03")
        self.gridLayout_2.addWidget(self.Dataset03, 0, 2, 1, 1)
        self.Dataset04 = DatasetIcon(self.horizontalLayoutWidget, DatasetPopup.datasets[i], self)
        self.updateDatasetIconList(self.Dataset04)
        i += 1
        self.Dataset04.setEnabled(True)
        self.Dataset04.setMinimumSize(QtCore.QSize(100, 100))
        self.Dataset04.setMaximumSize(QtCore.QSize(100, 100))
        self.Dataset04.setObjectName("Dataset04")
        self.gridLayout_2.addWidget(self.Dataset04, 0, 3, 1, 1)
        self.Dataset05 = DatasetIcon(self.horizontalLayoutWidget, DatasetPopup.datasets[i], self)
        self.updateDatasetIconList(self.Dataset05)
        i += 1
        self.Dataset05.setEnabled(True)
        self.Dataset05.setMinimumSize(QtCore.QSize(100, 100))
        self.Dataset05.setMaximumSize(QtCore.QSize(100, 100))
        self.Dataset05.setObjectName("Dataset05")
        self.gridLayout_2.addWidget(self.Dataset05, 1, 0, 1, 1)
        self.Dataset06 = DatasetIcon(self.horizontalLayoutWidget, DatasetPopup.datasets[i], self)
        self.updateDatasetIconList(self.Dataset06)
        i += 1
        self.Dataset06.setEnabled(True)
        self.Dataset06.setMinimumSize(QtCore.QSize(100, 100))
        self.Dataset06.setMaximumSize(QtCore.QSize(100, 100))
        self.Dataset06.setObjectName("Dataset06")
        self.gridLayout_2.addWidget(self.Dataset06, 1, 1, 1, 1)
        self.Dataset07 = DatasetIcon(self.horizontalLayoutWidget, DatasetPopup.datasets[i], self)
        self.updateDatasetIconList(self.Dataset07)
        i += 1
        self.Dataset07.setEnabled(True)
        self.Dataset07.setMinimumSize(QtCore.QSize(100, 100))
        self.Dataset07.setMaximumSize(QtCore.QSize(100, 100))
        self.Dataset07.setObjectName("Dataset07")
        self.gridLayout_2.addWidget(self.Dataset07, 1, 2, 1, 1)
        self.Dataset08 = DatasetIcon(self.horizontalLayoutWidget, DatasetPopup.datasets[i], self)
        self.updateDatasetIconList(self.Dataset08)
        i += 1
        self.Dataset08.setEnabled(True)
        self.Dataset08.setMinimumSize(QtCore.QSize(100, 100))
        self.Dataset08.setMaximumSize(QtCore.QSize(100, 100))
        self.Dataset08.setObjectName("Dataset08")
        self.gridLayout_2.addWidget(self.Dataset08, 1, 3, 1, 1)
        self.Dataset09 = DatasetIconCNN(self.horizontalLayoutWidget, DatasetPopup.datasets[10], self)
        self.updateDatasetIconList(self.Dataset09)
        i += 1
        self.Dataset09.setEnabled(True)
        self.Dataset09.setMinimumSize(QtCore.QSize(100, 100))
        self.Dataset09.setMaximumSize(QtCore.QSize(100, 100))
        self.Dataset09.setObjectName("Dataset09")
        self.gridLayout_2.addWidget(self.Dataset09, 2, 0, 1, 1)

        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_3)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.Dataset11 = DatasetIcon(self.horizontalLayoutWidget, DatasetPopup.datasets[8], self)
        self.updateDatasetIconList(self.Dataset11)
        i += 1
        self.Dataset11.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Dataset11.sizePolicy().hasHeightForWidth())
        self.Dataset11.setSizePolicy(sizePolicy)
        self.Dataset11.setMinimumSize(QtCore.QSize(100, 100))
        self.Dataset11.setMaximumSize(QtCore.QSize(100, 100))
        self.Dataset11.setObjectName("Dataset11")
        self.gridLayout.addWidget(self.Dataset11, 0, 0, 1, 1)
        self.Dataset12 = DatasetIcon(self.horizontalLayoutWidget, DatasetPopup.datasets[9], self)
        self.updateDatasetIconList(self.Dataset12)
        i += 1
        self.Dataset12.setEnabled(True)
        self.Dataset12.setMinimumSize(QtCore.QSize(100, 100))
        self.Dataset12.setMaximumSize(QtCore.QSize(100, 100))
        self.Dataset12.setObjectName("Dataset12")
        self.gridLayout.addWidget(self.Dataset12, 0, 1, 1, 1)
        self.Slot_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Slot_3.setEnabled(False)
        self.Slot_3.setMinimumSize(QtCore.QSize(100, 100))
        self.Slot_3.setMaximumSize(QtCore.QSize(100, 100))
        self.Slot_3.setObjectName("Slot_3")
        self.Slot_3.setStyleSheet(hide_stylesheet)
        self.gridLayout.addWidget(self.Slot_3, 0, 2, 1, 1)
        self.Slot_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Slot_4.setEnabled(False)
        self.Slot_4.setMinimumSize(QtCore.QSize(100, 100))
        self.Slot_4.setMaximumSize(QtCore.QSize(100, 100))
        self.Slot_4.setObjectName("Slot_4")
        self.Slot_4.setStyleSheet(hide_stylesheet)
        self.gridLayout.addWidget(self.Slot_4, 0, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 4, 0, 1, 1)

        self.line_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setLineWidth(100)
        self.line_2.setMidLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.line_2.setStyleSheet(line_style_sheet)
        self.gridLayout_3.addWidget(self.line_2, 1, 0, 1, 1)

        self.line = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.line.setLineWidth(100)
        self.line.setMidLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line.setStyleSheet(line_style_sheet)
        self.gridLayout_3.addWidget(self.line, 3, 0, 1, 1)


        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.DatasetSelected = DatasetLoaderImage(self.horizontalLayoutWidget)
        self.DatasetSelected.setMinimumSize(QtCore.QSize(200, 200))
        self.DatasetSelected.setMaximumSize(QtCore.QSize(200, 200))
        self.DatasetSelected.setObjectName("DatasetSelected")
        self.verticalLayout_4.addWidget(self.DatasetSelected)
        self.DatasetName = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.DatasetName.setMinimumSize(QtCore.QSize(0, 30))
        self.DatasetName.setMaximumSize(QtCore.QSize(200, 30))
        self.DatasetName.setObjectName("DatasetName")
        self.verticalLayout_4.addWidget(self.DatasetName)
        self.TaskType = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.TaskType.setMinimumSize(QtCore.QSize(0, 30))
        self.TaskType.setMaximumSize(QtCore.QSize(300, 30))
        self.TaskType.setObjectName("TaskType")
        self.verticalLayout_4.addWidget(self.TaskType)
        self.Difficulty = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Difficulty.setMinimumSize(QtCore.QSize(0, 30))
        self.Difficulty.setMaximumSize(QtCore.QSize(300, 30))
        self.Difficulty.setObjectName("Difficulty")
        self.verticalLayout_4.addWidget(self.Difficulty)
        self.SplitName = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.SplitName.setMinimumSize(QtCore.QSize(60, 30))
        self.SplitName.setMaximumSize(QtCore.QSize(200, 30))
        self.SplitName.setObjectName("SplitName")
        self.verticalLayout_4.addWidget(self.SplitName)
        self.Split = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.Split.setMinimumSize(QtCore.QSize(200, 20))
        self.Split.setMaximumSize(QtCore.QSize(200, 20))
        self.Split.setMinimum(1)
        self.Split.setMaximum(9)
        self.Split.setSingleStep(1)
        self.Split.setPageStep(1)
        self.Split.setSliderPosition(0)
        self.Split.setTracking(True)
        self.Split.setOrientation(QtCore.Qt.Horizontal)
        self.Split.setInvertedAppearance(False)
        self.Split.setTickPosition(QtWidgets.QSlider.NoTicks)
        self.Split.setTickInterval(0)
        self.Split.setObjectName("Split")
        self.verticalLayout_4.addWidget(self.Split)
        self.NoiseName = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.NoiseName.setMinimumSize(QtCore.QSize(60, 30))
        self.NoiseName.setMaximumSize(QtCore.QSize(200, 30))
        self.NoiseName.setObjectName("NoiseName")
        self.verticalLayout_4.addWidget(self.NoiseName)
        self.Noise = QtWidgets.QSlider(self.horizontalLayoutWidget)
        self.Noise.setMinimumSize(QtCore.QSize(200, 20))
        self.Noise.setMaximumSize(QtCore.QSize(200, 20))
        self.Noise.setMinimum(0)
        self.Noise.setMaximum(3)
        self.Noise.setPageStep(1)
        self.Noise.setOrientation(QtCore.Qt.Horizontal)
        self.Noise.setObjectName("Noise")
        self.verticalLayout_4.addWidget(self.Noise)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        font_info = QtGui.QFont()
        font_info.setFamily(u"Segoe UI")
        font_info.setPointSize(12)
        self.DatasetName.setFont(font_info)
        self.TaskType.setFont(font_info)
        self.Difficulty.setFont(font_info)
        self.SplitName.setFont(font_info)
        self.NoiseName.setFont(font_info)
        info_stylesheet = "QToolTip { color: black; background: white; border: 0px; } QWidget {background:rgba(255,255,255,0);} "
        self.DatasetSelect.setStyleSheet(info_stylesheet)
        self.DatasetSelected.setStyleSheet(info_stylesheet)
        self.DatasetName.setStyleSheet(info_stylesheet)
        self.TaskType.setStyleSheet(info_stylesheet)
        self.Difficulty.setStyleSheet(info_stylesheet)
        self.SplitName.setStyleSheet(info_stylesheet)
        self.Split.setStyleSheet(info_stylesheet)
        self.NoiseName.setStyleSheet(info_stylesheet)
        self.Noise.setStyleSheet(info_stylesheet)
        """
        self.DatasetName.setToolTip("Name of Dataset")
        self.TaskType.setToolTip("Machine Learning Task Type")
        self.Difficulty.setToolTip("Based on Normalised Average Test Accuracy of a Competitive Model")
        self.SplitName.setToolTip("Ratio of Training Set to Testing Set")
        self.NoiseName.setToolTip("Noise added to the data")
        """
        self.DatasetSelected.setText(("DatasetImage"))
        self.DatasetSelect.setText(("Select a Dataset"))
        self.DatasetName.setText(("Name"))
        self.TaskType.setText(("Task"))
        self.Difficulty.setText(("Difficulty"))
        self.SplitName.setText(("Split"))
        self.NoiseName.setText(("Noise"))
        self.Split.setValue(8)
        self.Noise.setValue(0)
        self.Noise.valueChanged[int].connect(self.updateDatasetNoise)
        self.Split.valueChanged[int].connect(self.updateDatasetSplit)
