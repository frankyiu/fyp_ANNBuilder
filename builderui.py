from PyQt5.QtWidgets import QStyleOption, QStyle, QButtonGroup

from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

from ui.Message import Message
from ui.PopUpGuideFactory import *
from ui.DatasetLoader import *
from ui.ToolBarWidget import *
from ui.ResultDashBoard import *
from nnbuilder.config import *
from nnbuilder.scene import NNBScene


class BuilderUI():

    def __init__(self, ui):
        self.ui = ui
        self.modelPara ={
            "Learning_rate": 0.01,
            "Decay_rate": 0.9,
            "Optimization": "Full-Batch",
        }
        self.popUpGuide = PopUpGuideFactory(self.ui.page_draw)
        self.setupData()
        self.setupControl()
        self.setupBuilder()
        self.setupGuide()
        self.setupViewer()
        self.setupMessage()
        self.firstTimeGuide = True

    def setupData(self):
        self.ui.dataloader = DatasetLoader(self.ui.frame_dataloader, self.ui.page_draw, QtCore.QRect(34, 15, 120, 120))


    def setupBuilder(self):

        self.scene = NNBScene()
        self.scene.setSceneRect(0,0,self.ui.graphicsView.width(), self.ui.graphicsView.height())
        self.ui.graphicsView.setMouseTracking(True)
        self.ui.graphicsView.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing)
        self.ui.graphicsView.setScene(self.scene)
        self.ui.widget_toolbar = ToolBarWidget(self.scene, parent=self.ui.frame_2)
        self.ui.horizontalLayout_7.addWidget(self.ui.widget_toolbar)

    def setupControl(self):

        def trainOnclickedEvent(checked):
            icon = QIcon()
            if checked:
                icon.addFile(u":/basic/icons/basic/001-play-button.png", QSize(), QIcon.Normal, QIcon.Off)
            else:
                icon.addFile(u":/basic/icons/basic/011-pause.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.btn_train.setIcon(icon)

        def empty():
            return

        def optimiBtnsOnclickEvent(btn):
            self.modelPara["Optimization"] = btn.text()
            print(self.modelPara)

        def decayRateChanged(i):
            self.modelPara["Decay_rate"] = i

        def learningRateChanged(i):
            self.modelPara["Learning_rate"] = i

        self.optimiBtns = QButtonGroup()
        self.optimiBtns.addButton(self.ui.radio_fullbatch)
        self.optimiBtns.addButton(self.ui.radio_minibatch)
        self.optimiBtns.addButton(self.ui.radio_adaDelta)
        self.optimiBtns.addButton(self.ui.radio_adaGrad)
        self.optimiBtns.addButton(self.ui.radio_adam)
        self.optimiBtns.addButton(self.ui.radio_momentum)
        self.optimiBtns.addButton(self.ui.radio_rmsProp)
        self.optimiBtns.addButton(self.ui.radio_sgd)

        self.optimiBtns.buttonClicked.connect(optimiBtnsOnclickEvent)
        self.ui.spin_decayRate.valueChanged.connect(decayRateChanged)
        self.ui.spin_learningRate.valueChanged.connect(learningRateChanged)

        self.ui.btn_train.toggled.connect(trainOnclickedEvent)
        self.ui.btn_backprop.toggled.connect(empty)
        self.ui.btn_feedfor.toggled.connect(empty)
        self.ui.btn_restart.toggled.connect(empty)

        return

    def setupGuide(self):
        self.popUpGuide.append(self.ui.frame_dataset, QPoint(150, 0),
                               'This is the Data Panel\nYou can choose our prepared dataset here before building your own model')
        self.popUpGuide.append(self.ui.frame_component, QPoint(150, 0),
                               'This is the Component Panel\nYou can drag and drop the components to the building panel to build your own model')
        self.popUpGuide.append(self.ui.graphicsView, QPoint(-200, 0),
                               'This is the Building Panel\nYou can modify the model by moving and connecting the components, details of the components can be setted by right click')
        self.popUpGuide.append(self.ui.btn_message, QPoint(-250, 0),
                               'A warning message will be prompted for any errors in constructing the model')
        self.popUpGuide.append(self.ui.widget_toolbar, QPoint(-250, 0),
                               'You can change the mode in building by clicking these icons')
        self.popUpGuide.append(self.ui.frame_optimi, QPoint(-200, -120),
                               'This is the Optimization Panel\nBe sure to set the optimization, learning rate, decay rate here before training the model')
        self.popUpGuide.append(self.ui.frame_control, QPoint(-280, -50),
                               'This is the Control Panel\nYou can click the Play button to train the model, perform Feedforward or Backpropagation in once by clicking the buttons beside.')
        self.popUpGuide.append(self.ui.draw_right, QPoint(-280, 0),
                               'This is the Viewer Panel\nYou can inspect the trained model metrics here by toggled this button')
        self.popUpGuide.append(self.ui.btn_guide, QPoint(-250, 0),
                               'If you want to check this tour again, you can click this question button.\nEnjoy building!')

        self.ui.btn_guide.clicked.connect(self.guideOnclickEvent)
        return

    def setupMessage(self):
        size = QPoint(391, 61)
        self.ui.message = Message(self.ui.graphicsView, size, 'helloWorld', self.ui.page_draw)
        self.ui.btn_message.toggled.connect(self.ui.message.toggleEvent)
        return

    def setupViewer(self):
        size = QPoint(170, 500)
        self.ui.inspector = ScrollableResultDashBoard(self.ui.page_draw)
        self.ui.inspector.hide()
        def testEvent(checked):
            pos = self.ui.btn_inspector.mapTo(self.ui.page_draw, QPoint(0, 0))
            self.ui.inspector.setGeometry(pos.x() - size.x(), pos.y(), size.x(), size.y())
            self.ui.inspector.setStyleSheet('background-color: rgb(0,0,0)')
            if checked:
                self.ui.inspector.show()
            else:
                self.ui.inspector.hide()

        self.ui.btn_inspector.toggled.connect(testEvent)
        # self.ui.btn_inspector.setStyleSheet('background-color: rgb(0,0,0);')
        # self.ui.btn_inspector.paintEvent = self.paintEvent
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
            self.ui.draw_right.setMinimumWidth(self.ui.btn_viewer.width() + 10)
            icon.addFile(u":/basic/icons/basic/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.btn_viewer.setIcon(icon)

    def update(self):
        return

    def resizeEvent(self, event):
        if self.popUpGuide.isStarted:
            self.popUpGuide.refreshUI()
        self.ui.message.refreshUi()
