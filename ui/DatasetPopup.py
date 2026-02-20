import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QPen, QColor, QBrush
from PyQt5.QtCore import QMimeData, Qt, QPoint, QEvent
from PyQt5 import QtCore, QtGui, QtWidgets
from ui.DatasetIcon import *
from ui.DatasetLoaderImage import *
from dataset.DatasetMeta import *

"""
The pop up shown when dataloader is clicked
It shows the DatasetIcons for user to select
On the right, shows the meta info of the selected/hovering dataset
A graph is shown on the top to visualize the data
"""
class DatasetPopup(QWidget):
    #List of prepared datasets
    datasets = DatasetMeta.datasets
    num_of_datasets = 0

    def __init__(self,parent, loader):
        super(QWidget,self).__init__(parent)
        self.loader = loader        #The loader that owns this popup
        self.widget_lst = []        #The list of icons that this popup owns
        self.setupUI()


    """
    This methods updates the meta info panel in the pop up
    it accepts the dataset name as argument and get the meta info
        from DatasetMeta class
    if no argument is specified, it shows the meta info of the
        currently selected dataset
    The meta info panel will update whenever a dataset is loaded, or
        hovering a dataset Icon, or the noise/split ratio is updated
    For hovering, the original version of dataset will be displayed for math,
        and binary classification task for cnn dataset
    """
    def showDatasetInfo(self, dataset_name=None):
        noise_val = 0
        if dataset_name is None:
            noise_val = self.getNoiseValue()
            dataset_name = self.getDataLoader().getDatasetName()

        (dataname, tasktype, difficulty) = DatasetMeta.getDatasetMetaInfo(dataset_name, noise_val)
        split_statement = "Train Set Split Ratio: {ratio:.0f}%".format(
                          ratio=self.getDataLoader().getTrainingSetRatio()*100)
        noise_statement = DatasetMeta.getVaryStatement(dataset_name, noise_val)
        split_enabled = False if DatasetMeta.isCNN(dataset_name) else True
        self.__setDatasetMetaInfo(dataname, tasktype, difficulty, split_statement, noise_statement, split_enabled)

    def __setDatasetMetaInfo(self, name, task, difficulty, split_str, noise_str, split_enabled):
        self.DatasetName.setText("Name: {name}".format(name=name))
        self.TaskType.setText("Task: {task}".format(task=task))
        self.Difficulty.setText( "Difficulty: {difficulty}".format(difficulty=difficulty))
        self.SplitName.setText(split_str)
        self.NoiseName.setText(noise_str)
        self.Split.setEnabled(split_enabled)

    #invoked when a dataset is loaded or a dataset setting is loaded
    def resetNoise(self, noise=0):
        self.Noise.setValue(noise)

    #invoked when a dataset setting is loaded
    def resetSplit(self, split=8):
        self.Split.setValue(split)

    #handles the show/hide of popup widget
    #ignore when it is in training state
    def toggle(self, state=None):
        if state is not None:
            self.setVisible(state)
        elif self.isVisible():
            self.hide()
        else:
            self.show()

    #maintain the hovering effect of the dataloader when user is still focusing on the popup
    def enterEvent(self, event):
        self.getDataLoader().showImage(hover=True)

    #When user does not select any data set and leave the panel, change back the loader icon and close popup
    def leaveEvent(self, event):
        self.getDataLoader().changeIconImg(self.getDataLoader(), hover=False)
        self.toggle(False)

    #handles the update of graph on top right corner
    def updateDatasetPlotPixmap(self):
        return self.DatasetSelected.updateReferenceImg(self.getDataLoader().getDatasetPixmap())

    #connected to the slider
    def updateDatasetNoise(self, noise_val):
        self.getDataLoader().addNoiseToData(noise_val)
        self.showDatasetInfo()

    #connected to the slider
    def updateDatasetSplit(self, split_val):
        self.getDataLoader().setTrainingSetRatio(split_val/10.0)
        self.showDatasetInfo()

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
            for obj in self.widget_lst:
                if query == obj.getDatasetName():
                    return obj
        return None

    def __createDatasetIcon(self, parent_of_icon_widget):
        name = DatasetPopup.datasets[DatasetPopup.num_of_datasets]
        widget = DatasetIcon(parent_of_icon_widget, name, self)
        widget.setEnabled(True)
        widget.setMinimumSize(QtCore.QSize(100, 100))
        widget.setMaximumSize(QtCore.QSize(100, 100))
        widget.setObjectName("Dataset" + name)
        self.widget_lst.append(widget)
        DatasetPopup.num_of_datasets += 1
        return widget

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
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName("gridLayout_2")

        dw0 = self.__createDatasetIcon(self.horizontalLayoutWidget)
        self.gridLayout_2.addWidget(dw0, 0, 0, 1, 1)
        dw1 = self.__createDatasetIcon(self.horizontalLayoutWidget)
        self.gridLayout_2.addWidget(dw1, 0, 1, 1, 1)
        dw2 = self.__createDatasetIcon(self.horizontalLayoutWidget)
        self.gridLayout_2.addWidget(dw2, 0, 2, 1, 1)
        dw3 = self.__createDatasetIcon(self.horizontalLayoutWidget)
        self.gridLayout_2.addWidget(dw3, 0, 3, 1, 1)
        dw4 = self.__createDatasetIcon(self.horizontalLayoutWidget)
        self.gridLayout_2.addWidget(dw4, 1, 0, 1, 1)
        dw5 = self.__createDatasetIcon(self.horizontalLayoutWidget)
        self.gridLayout_2.addWidget(dw5, 1, 1, 1, 1)
        dw6 = self.__createDatasetIcon(self.horizontalLayoutWidget)
        self.gridLayout_2.addWidget(dw6, 1, 2, 1, 1)
        dw7 = self.__createDatasetIcon(self.horizontalLayoutWidget)
        self.gridLayout_2.addWidget(dw7, 1, 3, 1, 1)
        dw8 = self.__createDatasetIcon(self.horizontalLayoutWidget)
        self.gridLayout_2.addWidget(dw8, 2, 0, 1, 1)
        dw9 = self.__createDatasetIcon(self.horizontalLayoutWidget)
        self.gridLayout_2.addWidget(dw9, 2, 1, 1, 1)

        self.gridLayout_3.addLayout(self.gridLayout_2, 2, 0, 1, 1)
        self.horizontalLayout_6.addLayout(self.gridLayout_3)

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")

        dw10 = self.__createDatasetIcon(self.horizontalLayoutWidget)
        """
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(dw10.sizePolicy().hasHeightForWidth())
        dw10.setSizePolicy(sizePolicy)
        """
        self.gridLayout.addWidget(dw10, 0, 0, 1, 1)
        dw11 = self.__createDatasetIcon(self.horizontalLayoutWidget)
        self.gridLayout.addWidget(dw11, 0, 1, 1, 1)

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
        slider_stylesheet = "QToolTip { color: black; background: white; border: 0px; } \
                             QWidget {background:rgba(255,255,255,0);} \
                             QSlider::groove:horizontal {background-color: rgb(98, 98, 98); height: 20px;  } \
                             QSlider::handle:horizontal {background-color: rgb(141, 141, 166); \
                             height: 30px;width: 20px;border: 2px solid white;} \
                             QSlider::handle:!enabled {background-color: rgb(25, 25, 25);} \
                             QSlider::handle:hover {background-color: rgb(208, 208, 254);} \
                             QSlider::handle:pressed {background-color: rgb(96, 96, 120); border: 2px solid rgb(200,200,200);}"
        self.DatasetSelect.setStyleSheet(info_stylesheet)
        self.DatasetSelected.setStyleSheet(info_stylesheet)
        self.DatasetName.setStyleSheet(info_stylesheet)
        self.TaskType.setStyleSheet(info_stylesheet)
        self.Difficulty.setStyleSheet(info_stylesheet)
        self.SplitName.setStyleSheet(info_stylesheet)
        self.Split.setStyleSheet(slider_stylesheet)
        self.NoiseName.setStyleSheet(info_stylesheet)
        self.Noise.setStyleSheet(slider_stylesheet)
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
