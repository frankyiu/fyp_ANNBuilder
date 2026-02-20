from PyQt5.QtWidgets import QStyleOption, QStyle, QButtonGroup

from PyQt5.QtCore import QSize, QRectF
from PyQt5.QtGui import QIcon

from ui.Message import Message
from ui.PopUpGuideFactory import *
from ui.DatasetLoader import *
from ui.ToolBarWidget import *
from ui.ResultDashBoard import *
from nnbuilder.config import *
from nnbuilder.scene import NNBScene
from ml.Training import *


class BuilderUI():

    def __init__(self, ui):
        self.ui = ui
        self.popUpGuide = PopUpGuideFactory(self.ui.page_draw, self.popCloseEvent)
        self.setupData()
        self.train = Training()
        self.setupControl()
        self.setupBuilder()
        self.setupMessagePanel()
        self.setupGuide()
        self.firstTimeGuide = True

    def setupData(self):
        #load dataset
        self.ui.dataloader = DatasetLoader(self.ui.frame_dataloader, self.ui.page_draw, QtCore.QRect(34, 15, 120, 120))


    def setupBuilder(self):
        #set up scene
        self.scene = NNBScene()
        self.ui.graphicsView.setMouseTracking(True)
        self.ui.graphicsView.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing)
        self.ui.graphicsView.setScene(self.scene)
        #set up toolbar
        self.ui.widget_toolbar = ToolBarWidget(self.scene, parent=self.ui.frame_2)
        self.ui.horizontalLayout_7.addWidget(self.ui.widget_toolbar)

    def setupControl(self):

        def trainRun():
            if self.scene.trainModeAct():
                trainUIEvent(self.scene.sceneMode == SceneMode.TrainMode)
                self.train.run(runOnce=False)
                self.ui.widget_toolbar.setLock(self.scene.sceneMode == SceneMode.TrainMode)

        def StepOnce():
            if self.scene.ffonce:
                return
            self.scene.ffonce = True
            if self.scene.trainModeAct():
                self.train.run(runOnce=True)


        #train button ui effect
        def trainUIEvent(isTrainMode):
            icon = QIcon()
            if not isTrainMode:
                icon.addFile(u":/basic/icons/basic/001-play-button.png", QSize(), QIcon.Normal, QIcon.Off)
            else:
                icon.addFile(u":/basic/icons/basic/011-pause.png", QSize(), QIcon.Normal, QIcon.Off)
            self.ui.btn_train.setIcon(icon)

        def restart():
            self.train.reset()
            self.scene.reinitializeKerasModelWeights()
            if self.scene.sceneMode != SceneMode.TrainMode:
                return
            if self.scene.trainModeAct():
                trainUIEvent(False)
            self.ui.widget_toolbar.setLock(self.scene.sceneMode == SceneMode.TrainMode)

        #
        self.optimiBtns = QButtonGroup()
        self.optimiBtns.addButton(self.ui.radio_adaDelta)
        self.optimiBtns.addButton(self.ui.radio_adaGrad)
        self.optimiBtns.addButton(self.ui.radio_adam)
        self.optimiBtns.addButton(self.ui.radio_momentum)
        self.optimiBtns.addButton(self.ui.radio_rmsProp)
        self.optimiBtns.addButton(self.ui.radio_sgd)


        # self.ui.btn_train.toggled.connect(trainUIEvent)

        self.ui.spin_learningRate.valueChanged.connect(self.train.setLearningRate)
        self.ui.spin_decayRate.valueChanged.connect(self.train.setLearningRateDecay)
        self.optimiBtns.buttonClicked.connect(self.train.setOptimizer)

        self.ui.radio_adam.click()
        self.ui.spin_learningRate.setValue(0.001)
        self.ui.spin_decayRate.setValue(1e-4)

        self.train.connectEpochWidget(self.ui.label_13)

        self.ui.btn_train.clicked.connect(trainRun)
        self.ui.btn_restart.clicked.connect(restart)
        self.ui.btn_feedfor.clicked.connect(StepOnce)
        # self.ui.btn_backprop.clicked.connect(self.train.backward)
        #convert the radio button states to a meaningful value (String, depends on real implementation)
        #self.optimzer.valueChanged.connect(lambda: train.setOptimizer(self.radioButton))
        self.ui.spin_batchSize.valueChanged.connect(self.train.setBatchSize)    #please add back a batch size spin box just like the learning rate
        self.train.setBatchSize(32)
        return

    def setupGuide(self):
        #insert Tour Content
        self.popUpGuide.append(self.ui.frame_dataset, QPoint(150, 0),
                               'This is the Data Panel\nYou can choose some prepared dataset for different tasks, select the ratio of train/test and set the noise here.')
        self.popUpGuide.append(self.ui.frame_component, QPoint(150, 0),
                               'This is the Component Panel\nYou can drag and drop the components to the building panel to build your own model.')
        self.popUpGuide.append(self.ui.graphicsView, QPoint(-200, 0),
                               'This is the Building Panel\nYou can modify the model by moving and connecting the components, double click the components to show the detail setting dialog.')
        self.popUpGuide.append(self.ui.widget_toolbar, QPoint(-250, 0),
                               'During the building process, you can switch to select mode, connect mode and train mode in this toolbar.')
        self.popUpGuide.append(self.ui.message, QPoint(-250, -100),
                               'A warning message will be prompted for any errors in constructing the model.')
        self.popUpGuide.append(self.ui.frame_optimi, QPoint(-200, -120),
                               'This is the Optimization Panel\nBe sure to choose the optimizer, learning rate, decay rate and batch size here before training the model.')
        self.popUpGuide.append(self.ui.frame_control, QPoint(-280, -50),
                               'This is the Control Panel\nYou can click the Play button to start or suspend the training, restart or step forward the training.')
        self.popUpGuide.append(self.ui.widget_dashboard, QPoint(-280, 0),
                               'This is the Result dashboard\nYou can inspect the real-time model metrics here.')
        self.popUpGuide.append(self.ui.btn_guide, QPoint(-250, 0),
                               'If you want to check this tour again, you can click this button.\nEnjoy building!')

        self.ui.btn_guide.clicked.connect(self.guideOnclickEvent)
        return

    def setupMessagePanel(self, message='This is a sample warnning message'):
        size = QPoint(391, 61)
        self.ui.message = Message(self.ui.graphicsView, size, message, self.ui.page_draw)
        self.ui.btn_message.disconnect()
        self.ui.btn_message.toggled.connect(self.ui.message.toggleEvent)
        return

    def setupMessage(self, message='This is a sample warnning message'):
        self.ui.message.setMessage(message)
        self.ui.message.hide()
        return


    def menuclicked(self):
        if self.firstTimeGuide:
            self.guideOnclickEvent()

    def guideOnclickEvent(self):
        self.popUpGuide.start()
        self.ui.message.refreshUi()
        self.ui.message.show()
        self.firstTimeGuide = False
        return

    def popCloseEvent(self):
        self.ui.message.hide()


    def resizeEvent(self, event):
        bound = self.scene.itemsBoundingRect()
        if bound.isNull():
            self.scene.setSceneRect(0,0,self.ui.graphicsView.width()-20, self.ui.graphicsView.height()-20)
        else:
            bound.setWidth(bound.width()-20)
            bound.setHeight(bound.height()-20)
            self.scene.setSceneRect(bound)
        if self.popUpGuide.isStarted:
            self.popUpGuide.refreshUI()
        self.ui.message.refreshUi()

