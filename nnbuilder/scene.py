"""

Reference:
- How to draw QGraphicsLineItem during run time with mouse coordinates:
    https://www.walletfox.com/course/qgraphicsitemruntimedrawing.php
-
http://www.windel.nl/?section=pyqtdiagrameditor

"""
import threading
import re
from PyQt5.QtGui import QTransform
from PyQt5.QtWidgets import QApplication, QGraphicsScene, QGraphicsItem, QGraphicsLineItem, \
    QGraphicsRectItem, QGraphicsEllipseItem
from PyQt5.QtCore import QTimer
import tensorflow as tf

from ml import Training
from .layer import NNB1DAffineLayer, NNB1DStackedAffineLayer, NNB2DConvLayer, \
    NNB2DPoolingLayer, NNB2DFlattenLayer
from .neuron import NNB1DInputNeuron, NNB1DBiasNeuron, NNB1DStackedNeuron, NNB2DInputNeuron, NNB2DBiasNeuron
from .connection import NNB1DLinearConnection, NNB1DStackedLinConnection, \
    NNB2DConvConnection, NNBRegConnection, NNBLFBConnection, \
    NNB2DFlattenConnection, NNB2DPoolingConnection
from .block import NNBLossFuncBlock, NNBRegularizer
from .animation import NNBPathTrainArrowFlowAnimation, NNBCurveTrainArrowFlowAnimation
from .base import _NNBNeuron, _NNB1DNeuron, _NNB2DNeuron,\
    _NNB1DInputNeuron, _NNB1DStackedNeuron, _NNB2DInputNeuron, \
    _NNB1DBiasNeuron, _NNB2DBiasNeuron, \
    _NNBLayer, _NNBTrainableLayer, _NNB1DAffineLayer, _NNB1DStackedLayer, \
    _NNB2DConvLayer, _NNB2DPoolingLayer, _NNB2DFlattenLayer, \
    _NNBConnection, _NNB1DLinearConnection, _NNB1DStackedLinConnection,\
    _NNB2DConvConnection, _NNB2DPoolingConnection, \
    _NNB2DFlattenConnection, _NNBLFBConnection, _NNBRegConnection, \
    _NNBLossFuncBlock, _NNBRegularizer, NNBController
from .modelUtils import *
from .config import *


class NNBMetadata:
    componentLogical2ActualDict = {
        _NNB1DInputNeuron: NNB1DInputNeuron,
        _NNB1DBiasNeuron: NNB1DBiasNeuron,
        _NNB1DStackedNeuron: NNB1DStackedNeuron,
        _NNB2DInputNeuron: NNB2DInputNeuron,
        _NNB2DBiasNeuron: NNB2DBiasNeuron,
        _NNB2DPoolingLayer: NNB2DPoolingLayer,
        _NNB2DFlattenLayer: NNB2DFlattenLayer,
        _NNB1DAffineLayer: NNB1DAffineLayer,
        _NNB1DStackedLayer: NNB1DStackedAffineLayer,
        _NNB2DConvLayer: NNB2DConvLayer,
        _NNB1DLinearConnection: NNB1DLinearConnection,
        _NNB1DStackedLinConnection : NNB1DStackedLinConnection,
        _NNB2DConvConnection: NNB2DConvConnection,
        _NNB2DPoolingConnection: NNB2DPoolingConnection,
        _NNB2DFlattenConnection: NNB2DFlattenConnection,
        _NNBLFBConnection: NNBLFBConnection,
        _NNBRegConnection: NNBRegConnection,
        _NNBLossFuncBlock: NNBLossFuncBlock,
        _NNBRegularizer: NNBRegularizer
    }

    componentDefaultNameDict = {
        NNB1DInputNeuron: NEURON_1D_DEFAULT_NAME,
        NNB1DBiasNeuron: NEURON_1D_BIAS_DEFAULT_NAME,
        NNB1DStackedNeuron: NEURON_1D_STACKED_DEFAULT_NAME,
        NNB2DInputNeuron: NEURON_2D_DEFAULT_NAME,
        NNB2DBiasNeuron: NEURON_2D_BIAS_DEFAULT_NAME,
        NNB1DAffineLayer: AFFINE_1D_LAYER_DEFAULT_NAME,
        NNB1DStackedAffineLayer: STACKED_AFFINE_1D_LAYER_DEFAULT_NAME,
        NNB2DConvLayer: CONV_2D_LAYER_DEFAULT_NAME,
        NNB2DPoolingLayer: POOLING_2D_LAYER_DEFAULT_NAME,
        NNB2DFlattenLayer: FLATTEN_2D_LAYER_DEFAULT_NAME,
        NNBLossFuncBlock: LFB_DEFAULT_NAME,
        NNBRegularizer: REGULARIZER_DEFAULT_NAME,
        NNB1DLinearConnection: LINEAR_1D_CONNECTION_DEFAULT_NAME,
        NNB1DStackedLinConnection: LINEAR_1D_STACKED_CONNECTION_DEFAULT_NAME,
        NNB2DConvConnection: CONV_2D_CONNECTION_DEFAULT_NAME,
        NNBLFBConnection: LFB_CONNECTION_DEFAULT_NAME,
        NNBRegConnection: REG_CONNECTION_DEFAULT_NAME,
        NNB2DFlattenConnection: FLATTEN_2D_CONNECTION_DEFAULT_NAME,
        NNB2DPoolingConnection: POOLING_2D_CONNECTION_DEFAULT_NAME
    }

    componentDefaultNameRegexDict = {
        NNB1DInputNeuron: NEURON_1D_DEFAULT_NAME_REGEX,
        NNB1DBiasNeuron: NEURON_1D_BIAS_DEFAULT_NAME_REGEX,
        NNB1DStackedNeuron: NEURON_1D_STACKED_DEFAULT_NAME_REGEX,
        NNB2DInputNeuron: NEURON_2D_DEFAULT_NAME_REGEX,
        NNB2DBiasNeuron: NEURON_2D_BIAS_DEFAULT_NAME_REGEX,
        NNB1DAffineLayer: AFFINE_1D_LAYER_DEFAULT_NAME_REGEX,
        NNB1DStackedAffineLayer: STACKED_AFFINE_1D_LAYER_DEFAULT_NAME_REGEX,
        NNB2DConvLayer: CONV_2D_LAYER_DEFAULT_NAME_REGEX,
        NNB2DPoolingLayer: POOLING_2D_LAYER_DEFAULT_NAME_REGEX,
        NNB2DFlattenLayer: FLATTEN_2D_LAYER_DEFAULT_NAME_REGEX,
        NNBLossFuncBlock: LFB_DEFAULT_NAME_REGEX,
        NNBRegularizer: REGULARIZER_DEFAULT_NAME_REGEX
    }


class NNBScene(QGraphicsScene):
    timer = QTimer()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sceneMode = SceneMode.SelectMode
        self.env = {}  # environment of the builder

        # For connect mode
        self.origPos = None
        self.lineToLink = None
        self.hoveredItemOnConnectMode = None
        self.origItemOnConnectMode = None

        # for select mode
        self.selectionRect = None
        self.itemSelected = []

        # For compiling into a NN model
        self.inputLayer = None
        self.outputLayer = None
        self.lossFuncBlock = None
        self.layers = []
        self.initMethod = DEFAULT_INIT_METHOD  # can be changed

        # For animation
        self.animations = []
        self.inTrainingAnimation = False
        self.currAnimationLayerIdx = 0
        self.ffFlowing = True

        self.ffonce = False

    def switchMode(self, mode):
        if self.sceneMode == SceneMode.TrainMode and mode != SceneMode.SelectMode:
            return
        if self.sceneMode == SceneMode.ConnectMode and mode == SceneMode.DragDrogMode:
            return
        if mode == SceneMode.ConnectMode:
            for item in self.items():
                self.views()[0].setCursor(Qt.CrossCursor)
                item.setFlag(QGraphicsItem.ItemIsMovable, False)
                item.setFlag(QGraphicsItem.ItemIsSelectable, False)
        elif mode == SceneMode.TrainMode:
            for item in self.items():
                self.views()[0].setCursor(Qt.WhatsThisCursor)
                item.setFlag(QGraphicsItem.ItemIsMovable, False)
                item.setFlag(QGraphicsItem.ItemIsSelectable, True)
        else:
            for item in self.items():
                self.views()[0].setCursor(Qt.ArrowCursor)
                item.setFlag(QGraphicsItem.ItemIsSelectable, True)
                if not isinstance(item, _NNBConnection) and not isinstance(item, _NNB1DStackedNeuron):
                    item.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.sceneMode = mode

    # ------------------------------------------------- #
    #     dealing with the creation of components       #
    # ------------------------------------------------- #

    def registerComponent(self, component):
        # this register the component into the environment
        if type(component) not in self.env:
            self.env[type(component)] = {}
        self.env[type(component)][component] = component.name

    def findNextDefaultName(self, componentType, componentDefaultName=None):
        if componentDefaultName is None:
            componentDefaultName = NNBMetadata.componentDefaultNameDict[componentType]
        if componentType not in self.env:
            proposedDefaultName = componentDefaultName.format(1)
        else:
            i = 1
            while True:
                proposedDefaultName = componentDefaultName.format(i)
                if proposedDefaultName not in self.env[componentType].values():
                    break
                i += 1
        return proposedDefaultName

    def addComponent(self, component):
        self.registerComponent(component)  # register the component to the environment
        if not isinstance(component, _NNBNeuron):  # since we called setParentItem, no need to add it to scene again
            self.addItem(component)  # add the component to the scene

    def createNeuron(self, x, y, neuronType, layer):
        layerName = layer.name
        res = re.findall(NNBMetadata.componentDefaultNameRegexDict[type(layer)], layerName)
        if res:
            layerName = res[0]
        neuronName = NNBMetadata.componentDefaultNameDict[neuronType].format(layerName, "{}")
        neuronName = self.findNextDefaultName(neuronType, neuronName)
        neuron = neuronType(neuronName, x, y)
        layer.addNeuron(neuron)
        neuron.setParentItem(layer)
        self.addComponent(neuron)

    def createLayer(self, x, y, layerType):
        layerName = self.findNextDefaultName(layerType)
        layer = layerType(layerName, x, y)
        self.addComponent(layer)
        if layerType == NNB1DStackedAffineLayer:
            self.createNeuron(x, y, NNB1DStackedNeuron, layer)

    def createLossFuncBlock(self, x, y):
        lfbName = self.findNextDefaultName(NNBLossFuncBlock)
        lossFuncBlock = NNBLossFuncBlock(lfbName, x, y)
        self.addComponent(lossFuncBlock)

    def createRegularizer(self, x, y):
        regularizerName = self.findNextDefaultName(NNBRegularizer)
        regularizer = NNBRegularizer(regularizerName, x, y)
        self.addComponent(regularizer)

    def createConnection(self, blockFrom, blockTo, blockFromName, blockToName, connectionType):
        connectionName = NNBMetadata.componentDefaultNameDict[connectionType].format(blockFromName, blockToName)
        connection = connectionType(connectionName, blockFrom, blockTo)
        self.addComponent(connection)
        blockFrom.connectTo(blockTo, connection)
        connection.updateConnectionPos()

    # -------------------------------------------------#
    #     dealing with the cleaning up components      #
    # -------------------------------------------------#

    def removeAllComponents(self):
        for components in self.env.values():
            for component in components.keys():
                if component.form:
                    if component.isFormOn:
                        component.form.close()
                    del component.form
                self.removeItem(component)
                del component
        self.env = {}

    def removeSelectedComponents(self):
        if not self.selectedItems():
            return
        # we will first delete all layers, then neurons, then connections, then other blocks
        componentsToBeRemovedFromBuilder = set(self.selectedItems())
        layersToBeRemoved = set()
        neuronsToBeRemoved = set()
        connectionsToBeRemoved = set()
        lfbsToBeRemoved = set()
        regularizersToBeRemoved = set()
        for selectedItem in self.selectedItems():
            if isinstance(selectedItem, _NNBLayer):
                layersToBeRemoved.add(selectedItem)
            elif isinstance(selectedItem, _NNBNeuron):
                neuronsToBeRemoved.add(selectedItem)
            elif isinstance(selectedItem, _NNBConnection):
                connectionsToBeRemoved.add(selectedItem)
            elif isinstance(selectedItem, _NNBLossFuncBlock):
                lfbsToBeRemoved.add(selectedItem)
            elif isinstance(selectedItem, _NNBRegularizer):
                regularizersToBeRemoved.add(selectedItem)
        for layerToBeRemoved in layersToBeRemoved:
            for connection in layerToBeRemoved.connectionsTo.values():  # regularizer or loss function block
                try:
                    connectionsToBeRemoved.remove(connection)
                except KeyError:
                    componentsToBeRemovedFromBuilder.add(connection)
            for connection in layerToBeRemoved.connectionsFrom.values():  # for flatten layer only
                try:
                    connectionsToBeRemoved.remove(connection)
                except KeyError:
                    componentsToBeRemovedFromBuilder.add(connection)
            if isinstance(layerToBeRemoved, _NNBTrainableLayer):
                for neuron in layerToBeRemoved.neurons:
                    try:
                        neuronsToBeRemoved.remove(neuron)
                    except KeyError:
                        componentsToBeRemovedFromBuilder.add(neuron)
                    neuron.setParentItem(None)
                    for connection in neuron.connectionsFrom.values():
                        try:
                            connectionsToBeRemoved.remove(connection)
                        except KeyError:
                            componentsToBeRemovedFromBuilder.add(connection)
                    for connection in neuron.connectionsTo.values():
                        try:
                            connectionsToBeRemoved.remove(connection)
                        except KeyError:
                            componentsToBeRemovedFromBuilder.add(connection)
            layerToBeRemoved.remove()

        for neuronToBeRemoved in neuronsToBeRemoved:
            for connection in neuronToBeRemoved.connectionsFrom.values():
                try:
                    connectionsToBeRemoved.remove(connection)
                except KeyError:
                    componentsToBeRemovedFromBuilder.add(connection)
            for connection in neuronToBeRemoved.connectionsTo.values():
                try:
                    connectionsToBeRemoved.remove(connection)
                except KeyError:
                    componentsToBeRemovedFromBuilder.add(connection)
            neuronToBeRemoved.remove()

        for connectionToBeRemoved in connectionsToBeRemoved:
            connectionToBeRemoved.remove()

        for lfbToBeRemoved in lfbsToBeRemoved:
            for connection in lfbToBeRemoved.connectionsFrom.values():  # an output layer or a regularizer
                try:
                    connectionsToBeRemoved.remove(connection)
                except KeyError:
                    componentsToBeRemovedFromBuilder.add(connection)
            lfbToBeRemoved.remove()

        for regularizerToBeRemoved in regularizersToBeRemoved:
            for connection in regularizerToBeRemoved.connectionsFrom.values():  # a trainable layer
                try:
                    connectionsToBeRemoved.remove(connection)
                except ValueError:
                    componentsToBeRemovedFromBuilder.add(connection)
            for connection in regularizerToBeRemoved.connectionsTo.values():  # a loss function block
                try:
                    connectionsToBeRemoved.remove(connection)
                except ValueError:
                    componentsToBeRemovedFromBuilder.add(connection)
            regularizerToBeRemoved.remove()

        # remove all of the components involved from the scene
        for componentToBeRemovedFromBuilder in componentsToBeRemovedFromBuilder:
            if componentToBeRemovedFromBuilder.form:
                if componentToBeRemovedFromBuilder.isFormOn:
                    componentToBeRemovedFromBuilder.form.close()
                del componentToBeRemovedFromBuilder.form
            self.removeItem(componentToBeRemovedFromBuilder)  # remove it from the scene
            typeComponent = type(componentToBeRemovedFromBuilder)
            if typeComponent in self.env:
                if componentToBeRemovedFromBuilder in self.env[typeComponent]:
                    del self.env[typeComponent][componentToBeRemovedFromBuilder]  # remove it from the environment
            del componentToBeRemovedFromBuilder  # delete the object

        self.update()

    # ------------------------------------------------- #
    #        dealing with the connecting blocks         #
    # ------------------------------------------------- #

    # Given two blocks, if they are to be connect, which type of connection should be adopted?
    @staticmethod
    def determineConnectionType(blockFrom, blockTo):
        if isinstance(blockFrom, _NNB1DAffineLayer) or isinstance(blockFrom, _NNB1DNeuron):
            if isinstance(blockTo, _NNB1DAffineLayer) or isinstance(blockTo, _NNB1DNeuron):
                return NNB1DLinearConnection
            elif isinstance(blockTo, _NNB1DStackedLayer) or isinstance(blockTo, _NNB1DStackedNeuron):
                return NNB1DStackedLinConnection
            elif isinstance(blockTo, _NNBLossFuncBlock):
                return NNBLFBConnection
        elif isinstance(blockFrom, _NNB1DStackedLayer) or isinstance(blockFrom, _NNB1DStackedNeuron):
            if isinstance(blockTo, _NNB1DAffineLayer) or isinstance(blockTo, _NNB1DNeuron):
                return NNB1DStackedLinConnection
            elif isinstance(blockTo, _NNB1DStackedLayer) or isinstance(blockTo, _NNB1DStackedNeuron):
                return NNB1DStackedLinConnection
        elif isinstance(blockFrom, _NNB2DConvLayer) or isinstance(blockFrom, _NNB2DNeuron):
            if isinstance(blockTo, _NNB2DConvLayer) or isinstance(blockTo, _NNB2DNeuron):
                return NNB2DConvConnection
            elif isinstance(blockTo, _NNB2DPoolingLayer):
                return NNB2DPoolingConnection
            elif isinstance(blockTo, _NNB2DFlattenLayer):
                return NNB2DFlattenConnection
        elif isinstance(blockFrom, _NNB2DFlattenLayer):
            if isinstance(blockTo, _NNB1DStackedLayer) or isinstance(blockTo, _NNB1DStackedNeuron):
                return NNB2DFlattenConnection
        elif isinstance(blockFrom, _NNBTrainableLayer):
            if isinstance(blockTo, _NNBRegularizer):
                return _NNBRegConnection
        elif isinstance(blockFrom, _NNBLossFuncBlock):
            if isinstance(blockTo, _NNBRegularizer):
                return _NNBRegConnection
        return None

    @staticmethod
    def extractBlockName(block):
        blockName = block.name
        res = re.findall(NNBMetadata.componentDefaultNameRegexDict[type(block)], blockName)
        if res:
            blockName = res[0]
        return blockName

    def connectNeuronToNeuron(self, neuronFrom, neuronTo):
        if neuronTo in neuronFrom.connectionsTo:
            return
        neuronFrom.connectToNeuron(neuronTo)
        neuronFromName = self.extractBlockName(neuronFrom)
        neuronToName = self.extractBlockName(neuronTo)
        connectionType = NNBScene.determineConnectionType(neuronFrom, neuronTo)
        self.createConnection(neuronFrom, neuronTo, neuronFromName, neuronToName, connectionType)

    def connectNeuronToLayer(self, neuronFrom, layerTo):
        neuronFrom.connectToLayer(layerTo)
        neuronFromName = self.extractBlockName(neuronFrom)
        connectionType = NNBScene.determineConnectionType(neuronFrom, layerTo)
        for neuronTo in layerTo.neurons:
            if isinstance(neuronTo, _NNB1DBiasNeuron) or neuronTo in neuronFrom.connectionsTo:
                continue
            neuronToName = self.extractBlockName(neuronTo)
            self.createConnection(neuronFrom, neuronTo, neuronFromName, neuronToName, connectionType)

    def connectLayerToNeuron(self, layerFrom, neuronTo):
        layerFrom.connectToNeuron(neuronTo)
        neuronToName = self.extractBlockName(neuronTo)
        connectionType = NNBScene.determineConnectionType(layerFrom, neuronTo)
        if isinstance(layerFrom, _NNB2DFlattenLayer):
            if isinstance(neuronTo, _NNB1DBiasNeuron) or neuronTo in layerFrom.connectionsTo:
                return
            layerFromName = self.extractBlockName(layerFrom)
            self.createConnection(layerFrom, neuronTo, layerFromName, neuronToName, connectionType)
            layerFrom.connectToNeuron(neuronTo)
        else:
            for neuronFrom in layerFrom.neurons:
                if isinstance(neuronTo, _NNB1DBiasNeuron) or neuronTo in neuronFrom.connectionsTo:
                    continue
                neuronFromName = self.extractBlockName(neuronFrom)
                self.createConnection(neuronFrom, neuronTo, neuronFromName, neuronToName, connectionType)

    def connectLayerToLayer(self, layerFrom, layerTo):
        layerFrom.connectToLayer(layerTo)
        connectionType = NNBScene.determineConnectionType(layerFrom, layerTo)
        if connectionType == NNB2DFlattenConnection:
            if isinstance(layerFrom, NNB2DConvLayer):
                layerToName = self.extractBlockName(layerTo)
                for neuronFrom in layerFrom.neurons:
                    if layerTo in neuronFrom.connectionsTo:
                        continue
                    neuronFromName = self.extractBlockName(neuronFrom)
                    self.createConnection(neuronFrom, layerTo, neuronFromName, layerToName, NNB2DFlattenConnection)
            elif isinstance(layerFrom, NNB2DFlattenLayer):
                layerFromName = self.extractBlockName(layerFrom)
                for neuronTo in layerTo.neurons:
                    if isinstance(neuronTo, _NNB1DBiasNeuron) or layerFrom in neuronTo.connectionsFrom:
                        continue
                    neuronToName = self.extractBlockName(neuronTo)
                    self.createConnection(layerFrom, neuronTo, layerFromName, neuronToName, NNB2DFlattenConnection)
            return
        for neuronFrom in layerFrom.neurons:
            neuronFromName = self.extractBlockName(neuronFrom)
            for neuronTo in layerTo.neurons:
                if isinstance(neuronTo, _NNB1DBiasNeuron) or isinstance(neuronTo, _NNB2DBiasNeuron) or \
                        neuronTo in neuronFrom.connectionsTo:
                    continue
                neuronToName = self.extractBlockName(neuronTo)
                self.createConnection(neuronFrom, neuronTo, neuronFromName, neuronToName, connectionType)

    def connectRegToLFB(self, regularizerFrom, lfbTo):
        if lfbTo in regularizerFrom.connectionsTo:
            return
        connectionType = NNBRegConnection
        regularizerFromName = self.extractBlockName(regularizerFrom)
        lfbToName = self.extractBlockName(lfbTo)
        self.createConnection(regularizerFrom, lfbTo, regularizerFromName, lfbToName, connectionType)
        regularizerFrom.connectToLFB(lfbTo)

    def connectLayerToReg(self, layerFrom, regTo):
        if regTo in layerFrom.connectionsTo:
            return
        connectionType = NNBRegConnection
        layerFromName = self.extractBlockName(layerFrom)
        regToName = self.extractBlockName(regTo)
        self.createConnection(layerFrom, regTo, layerFromName, regToName, connectionType)
        layerFrom.connectToRegularizer(regTo)

    def connectNeuronToLFB(self, neuronFrom, lfbTo):
        if lfbTo in neuronFrom.connectionsTo:
            return
        connectionType = NNBLFBConnection
        neuronFromName = self.extractBlockName(neuronFrom)
        lfbToName = self.extractBlockName(lfbTo)
        self.createConnection(neuronFrom, lfbTo, neuronFromName, lfbToName, connectionType)
        neuronFrom.connectToLFB(lfbTo)

    def connectLayerToLFB(self, layerFrom, lfbTo):
        connectionType = NNBLFBConnection
        lfbToName = self.extractBlockName(lfbTo)
        for neuronFrom in layerFrom.neurons:
            if lfbTo in neuronFrom.connectionsTo:
                continue
            neuronFromName = self.extractBlockName(neuronFrom)
            self.createConnection(neuronFrom, lfbTo, neuronFromName, lfbToName, connectionType)
        layerFrom.connectToLFB(lfbTo)

    def connectionHandler(self):
        blockFrom = self.origItemOnConnectMode
        blockTo = self.hoveredItemOnConnectMode
        if not NNBController.checkConnectableBlockBlock(blockFrom, blockTo):
            return
        connectionFunc = None
        if isinstance(blockFrom, _NNBNeuron):
            if isinstance(blockTo, _NNBNeuron):
                connectionFunc = self.connectNeuronToNeuron
            elif isinstance(blockTo, _NNBLayer):
                connectionFunc = self.connectNeuronToLayer
            elif isinstance(blockTo, _NNBLossFuncBlock):
                connectionFunc = self.connectNeuronToLFB
        elif isinstance(blockFrom, _NNBLayer):
            if isinstance(blockTo, _NNBNeuron):
                connectionFunc = self.connectLayerToNeuron
            elif isinstance(blockTo, _NNBLayer):
                connectionFunc = self.connectLayerToLayer
            elif isinstance(blockTo, _NNBLossFuncBlock):
                connectionFunc = self.connectLayerToLFB
            elif isinstance(blockTo, _NNBRegularizer):
                connectionFunc = self.connectLayerToReg
        elif isinstance(blockFrom, _NNBRegularizer):
            if isinstance(blockTo, _NNBLossFuncBlock):
                connectionFunc = self.connectRegToLFB
        if connectionFunc:
            connectionFunc(blockFrom, blockTo)

    # ------------------------------------------------- #
    #              dealing with animation               #
    # ------------------------------------------------- #

    def makeTrainingAnimation(self):
        if self.inTrainingAnimation:
            return

        self.animations = [[], []]
        for i, layer in enumerate(self.layers):
            firstAnimation = True
            self.animations[0].append([])
            self.animations[1].append([])
            for j, neuron in enumerate(layer.neurons):
                self.animations[0][i].append([])
                self.animations[1][i].append([])
                for connection in neuron.connectionsTo.values():
                    allowAnimation = False
                    if i == 0:
                        allowAnimation = True
                    elif i == len(self.layers) - 1 and (connection.blockFrom == self.lossFuncBlock or
                                                        connection.blockTo == self.lossFuncBlock):
                        allowAnimation = True
                    elif connection.blockFrom.layer != self.layers[i - 1] and \
                            connection.blockTo.layer != self.layers[i - 1]:
                        allowAnimation = True
                    if allowAnimation:
                        fAnimation = NNBPathTrainArrowFlowAnimation(connection)
                        bAnimation = NNBPathTrainArrowFlowAnimation(connection, forward=False)
                        if firstAnimation:
                            fAnimation.finishedConnect()
                            bAnimation.finishedConnect()
                            firstAnimation = False
                        self.animations[0][i][j].append(bAnimation)
                        self.animations[1][i][j].append(fAnimation)

            for regularizer, regConnection in layer.connectionsTo.items():
                if i != len(self.layers) - 1:
                    fAnimation = NNBCurveTrainArrowFlowAnimation(regConnection)
                    bAnimation = NNBCurveTrainArrowFlowAnimation(regConnection, forward=False)
                    self.animations[0][i].append([])
                    self.animations[1][i].append([])
                    self.animations[0][i][-1].append(bAnimation)
                    self.animations[1][i][-1].append(fAnimation)

        if len(self.layers) > 1:
            for regularizer, regConnection in self.lossFuncBlock.connectionsFrom.items():
                if isinstance(regConnection, NNBRegConnection):
                    fAnimation = NNBCurveTrainArrowFlowAnimation(regConnection)
                    bAnimation = NNBCurveTrainArrowFlowAnimation(regConnection, forward=False)
                    self.animations[0][-1].append([])
                    self.animations[1][-1].append([])
                    self.animations[0][-1][-1].append(bAnimation)
                    self.animations[1][-1][-1].append(fAnimation)

        self.inTrainingAnimation = True
        self.ffFlowing = True
        self.currAnimationLayerIdx = 0
        NNBScene.timer = QTimer()
        NNBScene.timer.timeout.connect(self.startOneLayerFlowAnimation)
        NNBScene.timer.start(1)
        #self.startOneLayerFlowAnimation()

    # TO-DO Animation
    def finishOneLayerFlowAnimation(self):
        NNBScene.timer.stop()
        # stop animation
        for layerAnimations in self.animations[self.ffFlowing][self.currAnimationLayerIdx]:
            for animation in layerAnimations:
                animation.vanish()

        if self.ffFlowing:
            if self.currAnimationLayerIdx == len(self.layers) - 1:
                # if done
                self.ffFlowing = False
            else:
                # TO-DO: update neuron's value
                self.currAnimationLayerIdx = self.currAnimationLayerIdx + 1
        else:
            if self.currAnimationLayerIdx == 0:
                self.ffFlowing = True
                self.updateParams()
                if self.ffonce == True:
                    return self.trainModeAct()
            else:
                if isinstance(self.layers[self.currAnimationLayerIdx-1], _NNBTrainableLayer):
                    self.layers[self.currAnimationLayerIdx - 1].updateParams(
                        self.layerNewParams[self.currAnimationLayerIdx - 1])
                self.currAnimationLayerIdx = self.currAnimationLayerIdx - 1
        NNBScene.timer.start(1)
        #self.startOneLayerFlowAnimation()

    def startOneLayerFlowAnimation(self):
        for layerAnimations in self.animations[self.ffFlowing][self.currAnimationLayerIdx]:
            for animation in layerAnimations:
                animation.start()
        for neuron in self.layers[self.currAnimationLayerIdx].neurons:
            for connection in neuron.connectionsTo.values():
                connection.onWeightChangedOnTrainMode()
        NNBScene.timer.stop()

    def stopAnimations(self):
        NNBScene.timer.stop()
        for layerAnimations in self.animations[self.ffFlowing][self.currAnimationLayerIdx]:
            for animation in layerAnimations:
                animation.vanish()
                animation.stop()

        for i in range(len(self.layers)):
            for layerAnimations in self.animations[self.ffFlowing][i]:
                for animation in layerAnimations:
                    animation.destroy()
            for layerAnimations in self.animations[not self.ffFlowing][i]:
                for animation in layerAnimations:
                    animation.destroy()

    def trainUntilStop(self, shouldStop):
        if shouldStop:
            pass

    # ------------------------------------------------- #
    #          dealing with model conversion            #
    # ------------------------------------------------- #

    def checkNNModelValid(self, dataset=None):
        # for 1D data, it should be a scalar; for 2D data, it should be in the triple of (C, H, W)
        QApplication.activeWindow().builder.train._preprocess()
        datasetInputDim = QApplication.activeWindow().builder.train.testX.shape[1:]
        datasetOutputDim = QApplication.activeWindow().builder.train.testy.shape[1:]
        if len(datasetInputDim) == 1:
            datasetInputDim = datasetInputDim[0]
        if len(datasetOutputDim) == 1:
            datasetOutputDim = datasetOutputDim[0]
        warningMessage = None
        layersInBuilder = []
        self.layers = None
        self.inputLayer = None
        self.outputLayer = None
        for component in self.items():
            if isinstance(component, _NNBLayer):
                layersInBuilder.append(component)
                if component.prevLayer is None:
                    if component.nextLayer is None:
                        warningMessage = 'model error: there is at least one isolate layer in the builder.'
                        return warningMessage
                    if self.inputLayer:
                        warningMessage = 'model error: there are at least two input layers in the builder.'
                        return warningMessage
                    else:
                        if not isinstance(component, _NNBTrainableLayer):
                            warningMessage = 'model error: the input layer should be a trainable layer.'
                            return warningMessage
                        if component.containsBias():
                            warningMessage = 'model error: the input layer shouldn\'t contain a bias.'
                            return warningMessage
                        self.inputLayer = component
                elif component.nextLayer is None:
                    warningMessage = 'model error: the output layer should be connected to a loss function block.'
                    return warningMessage

                elif isinstance(component.nextLayer, NNBLossFuncBlock):
                    if self.outputLayer:
                        warningMessage = 'model error: there are at least two output layers in the builder.'
                        return warningMessage
                    else:
                        self.outputLayer = component

        if self.outputLayer is None:
            warningMessage = 'model error: there should be at least two layers in the model.'
            return warningMessage

        if isinstance(self.inputLayer, _NNB1DStackedLayer) and self.inputLayer.numNeurons == -1:
            self.inputLayer.changeNumNeurons(datasetInputDim)
        elif isinstance(self.inputLayer, _NNB2DConvLayer):
            if type(datasetInputDim) == int:
                warningMessage = 'model error: the dimension of the input layer does not match that of the dataset.'
                return warningMessage
            if datasetInputDim[0] != self.inputLayer.numOfNeurons():
                warningMessage = 'model error: the channel number of the input layer ' \
                                 'does not match that of the dataset.'
                return warningMessage
            self.inputLayer.inputSize = datasetInputDim[1:]
        elif self.inputLayer.numOfNeurons() != datasetInputDim:
            warningMessage = 'model error: the dimension of the input layer does not match that of the dataset.'
            return warningMessage
        # Problem: if the input layer is a 1DStackedLayer and the validation fails here,
        if isinstance(self.outputLayer, _NNB1DStackedLayer) and self.outputLayer.numNeurons == -1:
            self.outputLayer.changeNumNeurons(datasetOutputDim)
        elif self.outputLayer.numOfNeurons() != datasetOutputDim:
            warningMessage = 'model error: the dimension of the output layer does not match that of the dataset.'
            return warningMessage
        self.layers = self.inputLayer.getChainOfLayers()
        if len(self.layers) != len(layersInBuilder):
            warningMessage = 'model error: there are at least one isolate layer in the builder.'
            return warningMessage

        # confirm all the size of all layers have been deduced
        for layer in layersInBuilder[1:-1]:
            if isinstance(layer, _NNB1DStackedLayer):
                if layer.prevLayer and layer.numNeurons == -1:
                    warningMessage = 'model error: the number of neurons in \"{}\" must ' \
                                     'be specified.'.format(layer.name)
                    return warningMessage
            elif isinstance(layer, _NNB2DConvLayer):
                layer.deduceOutputSize()
            elif isinstance(layer, _NNB2DFlattenLayer):
                layer.nextLayer.deduceNumOfNeurons()

        # initialize all the layers if necessary
        # for layer in layersInBuilder:

        self.lossFuncBlock = self.layers[-1].nextLayer
        if self.lossFuncBlock is None:
            warningMessage = 'model error: there is no loss function block.'
            return warningMessage
        return warningMessage

    def compileIntoNNModel(self):
        # can ONLY be called when there is a model
        LFB = self.lossFuncBlock
        modelConfigs = {}
        layersConfigs = []
        modelConfigs["layers"] = layersConfigs
        lastIdx = len(self.layers) - 1
        for i, layer in enumerate(self.layers):
            if isinstance(layer, _NNBTrainableLayer):
                layerConfigs = {}
                if isinstance(layer, _NNB1DAffineLayer) or isinstance(layer, _NNB1DStackedLayer):
                    layerConfigs['layerType'] = "1DLayer"
                    if i != lastIdx:
                        layerConfigs['size'] = layer.nextLayer.numOfNeurons() - \
                                               (1 if layer.nextLayer.containsBias() else 0)
                    else:
                        layerConfigs['size'] = 0
                elif isinstance(layer, _NNB2DConvLayer):
                    layerConfigs['layerType'] = "2DLayer"
                    layerConfigs['convParams'] = layer.getConvParams()
                    if not isinstance(layer.nextLayer, _NNB2DFlattenLayer):
                        layerConfigs['size'] = layer.nextLayer.numOfNeurons() - \
                                               (1 if layer.nextLayer.containsBias() else 0)
                layerConfigs['WC'], layerConfigs['bC'] = layer.getConnectivity()
                layerConfigs['W'], layerConfigs['b'] = layer.getParams()
                layerConfigs['regConfigs'] = None
                layerConfigs['actFunc'] = layer.actFunc
                if i != lastIdx:
                    regularizer = layer.getRegularizer()
                    if regularizer:
                        layerConfigs['regConfigs'] = regularizer.getConfigs()

                layersConfigs.append(layerConfigs)
            else:
                if isinstance(layer, _NNB2DFlattenLayer):
                    layersConfigs.append({'layerType': 'flattenLayer'})

        modelConfigs['lossFunc'] = LFB.lossFunc
        modelConfigs['inputSize'] = self.layers[0].numOfNeurons()
        self.modelConfigs = modelConfigs

    def trainModel(self):
        self.actModel = NNBTransformer.transferToKerasModel(self.modelConfigs, fooOptimizerConfigs, 'accuracy')

    def updateParams(self):
        self.layerNewParams = NNBTransformer.getParamsFromKerasModel(self.actModel)

    # ------------------------------------------------- #
    #                 Event handlers                    #
    # ------------------------------------------------- #

    def reset(self):
        # clear all selectionRect
        if self.selectionRect:
            # find items selected
            itemsSelected = self.collidingItems(self.selectionRect)
            for itemSelected in itemsSelected:
                itemSelected.setSelected(True)
                itemSelected.update()
            self.removeItem(self.selectionRect)
            del self.selectionRect
            self.selectionRect = None
        self.origPos = None
        # reset the handlers of the selected layer

    def trainModeAct(self):
        if self.sceneMode == SceneMode.TrainMode:
            self.switchMode(SceneMode.SelectMode)
            self.stopAnimations()
            self.inTrainingAnimation = False
            if self.ffonce:
                self.ffonce = False
        else:
            message = self.checkNNModelValid()
            if message:
                QApplication.activeWindow().builder.setupMessage(message=message)
                QApplication.activeWindow().ui.message.toggleEvent(True)
                self.ffonce = False
                return False
            self.switchMode(SceneMode.TrainMode)
            self.compileIntoNNModel()
            self.makeTrainingAnimation()
            self.trainModel()
            if QApplication.activeWindow().builder.train.hasReset:
                self.reinitializeKerasModelWeights()
            self.updateParams()
            QApplication.activeWindow().builder.train.setModel(self.actModel)
        return True

    def reinitializeKerasModelWeights(self):
        weight = self.actModel.get_weights()
        new_weight = [tf.initializers.GlorotUniform()
                        (shape=w.shape, dtype=tf.float32) for w in weight]
        self.actModel.set_weights(new_weight)
        self.updateParams()

    def keyPressEvent(self, event):
        if event.key() == 16777219 or event.key() == Qt.Key_Delete:
            self.removeSelectedComponents()

    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            if self.sceneMode == SceneMode.ConnectMode:
                self.switchMode(SceneMode.SelectMode)
            else:
                self.switchMode(SceneMode.ConnectMode)
            super().mousePressEvent(event)
            return

        if self.sceneMode == SceneMode.ConnectMode:
            item = self.itemAt(event.scenePos().x(), event.scenePos().y(), QTransform())
            if item:
                item.hoveredOnConnectMode = True
                item.update()
                self.origItemOnConnectMode = item

            self.origPos = event.scenePos()
        elif self.sceneMode == SceneMode.SelectMode:
            self.origPos = event.scenePos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        item = self.itemAt(event.scenePos().x(), event.scenePos().y(), QTransform())
        if self.sceneMode == SceneMode.SelectMode:
            if item and not self.selectionRect:
                self.views()[0].setCursor(Qt.OpenHandCursor)
            else:
                self.views()[0].setCursor(Qt.ArrowCursor)
        elif self.sceneMode == SceneMode.TrainMode:
            if item:
                self.views()[0].setCursor(Qt.OpenHandCursor)
            else:
                self.views()[0].setCursor(Qt.WhatsThisCursor)
        # TO-DO: outside of the scene problem

        if self.sceneMode == SceneMode.ConnectMode and self.origPos:
            # item = self.itemAt(event.scenePos().x(), event.scenePos().y(), QTransform())
            if item and not isinstance(item, QGraphicsLineItem):
                if not self.origItemOnConnectMode or self.origItemOnConnectMode != item:
                    if self.hoveredItemOnConnectMode:
                        self.hoveredItemOnConnectMode.hoveredOnConnectMode = False
                        self.hoveredItemOnConnectMode.update()
                    item.hoveredOnConnectMode = True
                    item.update()
                    self.hoveredItemOnConnectMode = item
                elif self.origItemOnConnectMode == item and self.hoveredItemOnConnectMode:
                    self.hoveredItemOnConnectMode.hoveredOnConnectMode = False
                    self.hoveredItemOnConnectMode.update()
            elif not item and self.hoveredItemOnConnectMode:
                self.hoveredItemOnConnectMode.hoveredOnConnectMode = False
                self.hoveredItemOnConnectMode.update()
                self.hoveredItemOnConnectMode = None

            if not self.lineToLink:
                self.lineToLink = QGraphicsLineItem()
                self.lineToLink.setPos(self.origPos)
                self.addItem(self.lineToLink)
            self.lineToLink.setLine(0, 0,
                                    event.scenePos().x() - self.origPos.x(),
                                    event.scenePos().y() - self.origPos.y())
        elif self.sceneMode == SceneMode.SelectMode and self.origPos:
            if not self.selectedItems():
                if not self.selectionRect:
                    self.selectionRect = QGraphicsRectItem()
                    self.selectionRect.setPen(QPen(QColor(153, 204, 255, 128)))
                    self.selectionRect.setBrush(QBrush(QColor(153, 204, 255, 128)))
                    self.selectionRect.setPos(self.origPos)
                    self.addItem(self.selectionRect)
                dx = event.scenePos().x() - self.origPos.x()
                dy = event.scenePos().y() - self.origPos.y()
                newX, newY = 0, 0
                if dx < 0:
                    newX = newX + dx
                if dy < 0:
                    newY = newY + dy
                self.selectionRect.setRect(newX, newY,
                                           abs(event.scenePos().x() - self.origPos.x()),
                                           abs(event.scenePos().y() - self.origPos.y()))

        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.sceneMode == SceneMode.ConnectMode:
            if self.lineToLink:
                self.removeItem(self.lineToLink)
                del self.lineToLink
                self.lineToLink = None
                self.origPos = None

            if self.origItemOnConnectMode and self.hoveredItemOnConnectMode:
                self.connectionHandler()

            if self.origItemOnConnectMode:
                self.origItemOnConnectMode.hoveredOnConnectMode = False
                self.origItemOnConnectMode.update()
                self.origItemOnConnectMode = None
            if self.hoveredItemOnConnectMode:
                self.hoveredItemOnConnectMode.hoveredOnConnectMode = False
                self.hoveredItemOnConnectMode.update()
                self.hoveredItemOnConnectMode = None
        elif self.sceneMode == SceneMode.SelectMode:
            self.reset()
        super().mouseReleaseEvent(event)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText() and self.sceneMode == SceneMode.SelectMode:
            event.accept()
            # switch into drag-drop mode
            self.reset()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        item = self.itemAt(event.scenePos().x(), event.scenePos().y(), QTransform())
        selectedItems = self.selectedItems()
        if item:
            if selectedItems and item != selectedItems[0]:
                selectedItem = selectedItems[0]
                selectedItem.setSelected(False)
                selectedItem.update()
                item.setSelected(True)
                item.update()
            elif not selectedItems:
                item.setSelected(True)
                item.update()
        elif selectedItems:
            selectedItem = selectedItems[0]
            selectedItem.setSelected(False)
            selectedItem.update()

    def dropEvent(self, event):
        iconType = event.mimeData().text()
        x = event.scenePos().x() - ICON_OFFSET_X
        y = event.scenePos().y() - ICON_OFFSET_Y
        message = None
        if iconType == "affine_layer":
            self.createLayer(x, y, NNB1DAffineLayer)
        elif iconType == "stacked_affine_layer":
            self.createLayer(x, y, NNB1DStackedAffineLayer)
        elif iconType == "conv_layer":
            self.createLayer(x, y, NNB2DConvLayer)
        elif iconType == "pooling_layer":
            self.createLayer(x, y, NNB2DPoolingLayer)
        elif iconType == "flatten_layer":
            self.createLayer(x, y, NNB2DFlattenLayer)
        elif iconType == "neuron_1D":
            # TO-DO: CAN Highlight
            layer = self.itemAt(event.scenePos().x(), event.scenePos().y(), QTransform())
            if layer:
                if isinstance(layer, NNB1DAffineLayer):
                    self.createNeuron(x - layer.scenePos().x(),
                                      y - layer.scenePos().y(),
                                      NNB1DInputNeuron,
                                      layer)
                elif isinstance(layer, NNB2DConvLayer):
                    message = "creation failure: can't create an 1D neuron in a 2D layer."
                else:
                    message = "creation failure: can't create an 1D neuron in the layer."
            else:
                message = "creation failure: can't create an 1D neuron."
        elif iconType == "neuron_bias_1D":
            # TO-DO: CAN Highlight
            layer = self.itemAt(event.scenePos().x(), event.scenePos().y(), QTransform())
            if layer:
                if isinstance(layer, NNB1DAffineLayer):
                    if layer.containsBias():
                        message = "creation failure: the layer already has a bias!"
                    elif isinstance(layer.nextLayer, _NNBLossFuncBlock):
                        message = "creation failure: can't create a bias in a layer supposed to be an output layer"
                    else:
                        self.createNeuron(x - layer.scenePos().x(),
                                          y - layer.scenePos().y(),
                                          NNB1DBiasNeuron,
                                          layer)
                elif isinstance(layer, NNB2DConvLayer):
                    message = "creation failure: can't create an 1D bias in a 2D layer."
                else:
                    message = "creation failure: can't create an 1D bias in the layer."
            else:
                message = "creation failure: can't create a 1D bias."
        elif iconType == "neuron_2D":
            layer = self.itemAt(event.scenePos().x(), event.scenePos().y(), QTransform())
            if layer:
                if isinstance(layer, NNB2DConvLayer):
                    self.createNeuron(x - layer.scenePos().x(),
                                      y - layer.scenePos().y(),
                                      NNB2DInputNeuron,
                                      layer)
                elif isinstance(layer, NNB1DAffineLayer):
                    message = "creation failure: can't create an 2D neuron in a 1D layer."
                else:
                    message = "creation failure: can't create an 2D neuron in the layer."
            else:
                message = "creation failure: can't create an 2D neuron."
        elif iconType == "neuron_bias_2D":
            layer = self.itemAt(event.scenePos().x(), event.scenePos().y(), QTransform())
            if layer:
                if isinstance(layer, NNB2DConvLayer):
                    if layer.containsBias():
                        message = "creation failure: the layer already has a bias!"
                    else:
                        self.createNeuron(x - layer.scenePos().x(),
                                          y - layer.scenePos().y(),
                                          NNB2DBiasNeuron,
                                          layer)
                elif isinstance(layer, NNB1DAffineLayer):
                    message = "creation failure: can't create an 2D bias in a 1D layer."
                else:
                    message = "creation failure: can't create an 2D bias in the layer."
            else:
                message = "creation failure: can't create an 2D neuron."
        elif iconType == "loss_func_block":
            self.createLossFuncBlock(x, y)
        elif iconType == "regularizer":
            self.createRegularizer(x, y)

        if message:
            QApplication.activeWindow().builder.setupMessage(message=message)
            QApplication.activeWindow().ui.message.toggleEvent(True)

        # upon finish and creation (if possible)
        self.sceneMode = SceneMode.SelectMode
        selectedItems = self.selectedItems()
        if selectedItems:
            selectedItem = selectedItems[0]
            selectedItem.setSelected(False)
            selectedItem.update()
