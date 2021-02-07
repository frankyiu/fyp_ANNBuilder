from ui.PopUpGuideFactory import *
from ui.DatasetLoader import *
from ui.ToolBarWidget import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

class Builder():
    def __init__(self, ui):
        self.ui = ui
        self.dataText ={}
        self.popUpGuide = PopUpGuideFactory(self.ui.page_draw)
        self.setupData()
        self.setupControl()
        self.setupGuide()
        self.setupViewer()
        self.firstTimeGuide = True
        
    def setupData(self):
        self.ui.dataloader = DatasetLoader(self.ui.frame_dataloader, self.ui.page_draw, QtCore.QRect(34, 15, 120, 120))
        self.dataText = {'ratio': self.ui.label_ratio.text(), 'noise': self.ui.label_noise.text(), 'batch': self.ui.label_batch.text()}
        self.ui.label_ratio.setText(f'{self.dataText["ratio"]}{self.ui.slider_ratio.value()}:{self.ui.slider_ratio.maximum()-self.ui.slider_ratio.value()}')
        self.ui.label_noise.setText(self.dataText['noise']+str(self.ui.slider_noise.value()))
        self.ui.label_batch.setText(self.dataText['batch']+str(self.ui.slider_batch.value()))
        self.ui.slider_ratio.valueChanged.connect(lambda value: self.ui.label_ratio.setText(f'{self.dataText["ratio"]}{value}:{self.ui.slider_ratio.maximum()-value}'))
        self.ui.slider_noise.valueChanged.connect(lambda value: self.ui.label_noise.setText(self.dataText['noise']+str(value)))
        self.ui.slider_batch.valueChanged.connect(lambda value: self.ui.label_batch.setText(self.dataText['batch']+str(value)))
        self.ui.frame_datapara.hide()

    def setupControl(self):
        return


    def setupGuide(self):
        self.popUpGuide.append(self.ui.frame_dataset, QPoint(150, 0), 'This is the Data Panel\nYou can setup the Dataset and Parameter here')
        self.popUpGuide.append(self.ui.frame_component, QPoint(150, 0), 'This is the Component Panel\nYou can drag and drop the components to the building panel to build your own model')
        self.popUpGuide.append(self.ui.graphicsView, QPoint(-200, 0), 'This is the Building Panel\nYou can modify the model by moving the components, be sure to create a valid model before training the model')
        self.popUpGuide.append(self.ui.draw_right, QPoint(-280,0), 'This is the Viewer Panel\nYou can inspect the variable weighting and metrics here.\nYou can click the arrow button to hide it')
        self.popUpGuide.append(self.ui.frame_control, QPoint(-280, -50), 'This is the Control Panel\nClick the Play button to train the model')
        self.popUpGuide.append(self.ui.btn_guide, QPoint(-250, 0), 'If you want to check this tour again, you can click this question button.\nEnjoy your building!')
        self.ui.btn_guide.clicked.connect(self.guideOnclickEvent)
        return

    def setupViewer(self):
        self.ui.btn_viewer.clicked.connect(self.viewerOnclickEvent)
        return

    def menuclicked(self):
        if self.firstTimeGuide:
            self.guideOnclickEvent()

    def guideOnclickEvent(self):
        self.popUpGuide.start()
        self.firstTimeGuide = False
        return

    def viewerOnclickEvent(self):
        icon = QIcon()
        if self.ui.tab_viewer.isHidden():
            self.ui.tab_viewer.show()
            self.ui.draw_right.setMinimumWidth(200)
            icon.addFile(u":/basic/icons/basic/next-1.png", QSize(), QIcon.Normal, QIcon.Off)
        else:
            self.ui.tab_viewer.hide()
            self.ui.draw_right.setMinimumWidth(self.ui.btn_viewer.width()+10)
            icon.addFile(u":/basic/icons/basic/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_viewer.setIcon(icon)

    def resizeEvent(self,event):
        if self.popUpGuide.isStarted:
            self.popUpGuide.refreshUI()
