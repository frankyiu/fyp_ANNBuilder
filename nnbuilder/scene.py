"""

Reference:
- How to draw QGraphicsLineItem during run time with mouse coordinates:
    https://www.walletfox.com/course/qgraphicsitemruntimedrawing.php
-
http://www.windel.nl/?section=pyqtdiagrameditor

"""
import re
from PyQt5.QtGui import QTransform
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsItem, QGraphicsLineItem, QGraphicsRectItem, QGraphicsEllipseItem
import numpy as np

from .layer import NNB1DAffineLayer, NNB1DStackedAffineLayer, NNB2DConvLayer, \
    NNB2DPoolingLayer, NNB2DFlattenLayer
from .neuron import NNB1DInputNeuron, NNB1DBiasNeuron, NNB1DStackedNeuron, NNB2DInputNeuron, NNB2DBiasNeuron
from .connection import NNB1DLinearConnection, NNB1DStackedLinConnection, \
    NNB2DConvConnection, NNBRegConnection, NNBLFBConnection, \
    NNB2DFlattenConnection, NNB2DPoolingConnection
from .block import NNBLossFuncBlock, NNBRegularizer
from .animation import NNTrainArrowFlowAnimation
from .base import _NNBNeuron, _NNB1DNeuron, _NNB2DNeuron,\
    _NNB1DInputNeuron, _NNB1DStackedNeuron, _NNB2DInputNeuron, \
    _NNB1DBiasNeuron, _NNB2DBiasNeuron, \
    _NNBLayer, _NNBTrainableLayer, _NNB1DAffineLayer, _NNB1DStackedLayer, \
    _NNB2DConvLayer, _NNB2DPoolingLayer, _NNB2DFlattenLayer, \
    _NNBConnection, _NNB1DLinearConnection, _NNB1DStackedLinConnection,\
    _NNB2DConvConnection, _NNB2DPoolingConnection, \
    _NNB2DFlattenConnection, _NNBLFBConnection, _NNBRegConnection, \
    _NNBLossFuncBlock, _NNBRegularizer, NNBController

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
        # For now, we force the user to specify the layer type.
        self.inputLayer = None
        self.outputLayer = None
        self.costFuncBlock = None
        self.layers = []

        # For animation
        self.animations = []
        self.inTrainingAnimation = False
        self.currAnimationLayerIdx = 0
        self.ffFlowing = True

    def switchMode(self, mode):
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
        print(component.name + " is created." + " " + str(component))

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
            # if isinstance(layerToBeRemoved, _NNBTrainableLayer):
            #     if layerToBeRemoved.layerType == "input":
            #         self.inputLayer = None
            #     elif layerToBeRemoved.layerType == "output":
            #         self.outputLayer = None
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
                except ValueError:
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
    # -------------------------------------------------#
    # dealing with the saving and loading the builder #
    # -------------------------------------------------#

    def saveEnv(self):  # return a json object
        # TO-DO
        pass

    def loadEnv(self, json):
        # TO-DO
        pass

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
            if neuronTo in neuronFrom.connectionsTo:
                continue
            neuronToName = self.extractBlockName(neuronTo)
            self.createConnection(neuronFrom, neuronTo, neuronFromName, neuronToName, connectionType)

    def connectLayerToNeuron(self, layerFrom, neuronTo):
        layerFrom.connectToNeuron(neuronTo)
        neuronToName = self.extractBlockName(neuronTo)
        connectionType = NNBScene.determineConnectionType(layerFrom, neuronTo)
        if isinstance(layerFrom, _NNB2DFlattenLayer):
            if neuronTo in layerFrom.connectionsTo:
                return
            layerFromName = self.extractBlockName(layerFrom)
            self.createConnection(layerFrom, neuronTo, layerFromName, neuronToName, connectionType)
            layerFrom.connectToNeuron(neuronTo)
        else:
            for neuronFrom in layerFrom.neurons:
                if neuronTo in neuronFrom.connectionsTo:
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
                    if layerFrom in neuronTo.connectionsFrom:
                        continue
                    neuronToName = self.extractBlockName(neuronTo)
                    self.createConnection(layerFrom, neuronTo, layerFromName, neuronToName, NNB2DFlattenConnection)
            return
        for neuronFrom in layerFrom.neurons:
            neuronFromName = self.extractBlockName(neuronFrom)
            for neuronTo in layerTo.neurons:
                if neuronTo in neuronFrom.connectionsTo:
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
        else:
            print("what's going on?")

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
                for connection in neuron.connections.values():
                    allowAnimation = False
                    if i == 0:
                        allowAnimation = True
                    elif i == len(self.layers) - 1 and (connection.neuronLeft == self.costFuncBlock or
                                                        connection.neuronRight == self.costFuncBlock):
                        allowAnimation = True
                    elif connection.neuronLeft.layer != self.layers[i - 1] and \
                            connection.neuronRight.layer != self.layers[i - 1]:
                        allowAnimation = True
                    if allowAnimation:
                        forward = (connection.neuronLeft == neuron)
                        fAnimation = NNTrainArrowFlowAnimation(connection, forward=forward)
                        bAnimation = NNTrainArrowFlowAnimation(connection, forward=not forward)
                        if firstAnimation:
                            fAnimation.fAnimation.finished.connect(fAnimation.onAnimationFinished)
                            bAnimation.fAnimation.finished.connect(bAnimation.onAnimationFinished)
                            firstAnimation = False
                        self.animations[0][i][j].append(bAnimation)
                        self.animations[1][i][j].append(fAnimation)
        self.inTrainingAnimation = True
        self.ffFlowing = True
        self.currAnimationLayerIdx = 0
        self.startOneLayerFlowAnimation()
        # ...
        # connection details
        # num of neuron details...
        # return layers #for now

    # TO-DO Animation
    def finishOneLayerFlowAnimation(self):
        # stop animation
        for layerAnimations in self.animations[self.ffFlowing][self.currAnimationLayerIdx]:
            for animation in layerAnimations:
                animation.vanish()

        if self.ffFlowing:
            if self.currAnimationLayerIdx == len(self.layers) - 1:
                self.ffFlowing = False
            else:
                self.currAnimationLayerIdx = self.currAnimationLayerIdx + 1
        else:
            if self.currAnimationLayerIdx == 0:
                self.ffFlowing = True
            else:
                self.currAnimationLayerIdx = self.currAnimationLayerIdx - 1

        self.startOneLayerFlowAnimation()

    def startOneLayerFlowAnimation(self):
        for layerAnimations in self.animations[self.ffFlowing][self.currAnimationLayerIdx]:
            for animation in layerAnimations:
                animation.start()
        for neuron in self.layers[self.currAnimationLayerIdx].neurons:
            for connection in neuron.connections.values():
                connection.weight += 0.1
                connection.onWeightChangedOnTrainMode()

    # ------------------------------------------------- #
    #          dealing with model conversion            #
    # ------------------------------------------------- #

    def compileIntoNNModel(self):
        # CURR
        # CAN only be called when there is a model
        nLayers = len(self.layers)
        CFB = self.costFuncBlock.costFunc
        modelConfig = {}
        lastIdx = len(self.layers) - 1
        for i, layer in enumerate(self.layers):
            if i == lastIdx:
                modelConfig[lastIdx] = {}
                modelConfig[lastIdx]['numNeuron'] = len(self.layers[-1].neurons)
                modelConfig[lastIdx]['connectMat'] = np.zeros((len(layer.neurons), 1))
                modelConfig[i]['weightMat'] = None
                modelConfig[i]['actFunc'] = None
                for j, neuronLeft in enumerate(self.layers[-1].neurons):
                    if CFB in neuronLeft.connections:
                        modelConfig[lastIdx]['connectMat'][j, 0] = 1.0
            else:
                modelConfig[i] = {}
                modelConfig[i]['numNeuron'] = len(layer.neurons)
                modelConfig[i]['connectMat'] = np.zeros((len(layer.neurons), len(self.layers[i + 1].neurons)))
                modelConfig[i]['weightMat'] = np.zeros((len(layer.neurons), len(self.layers[i + 1].neurons)))
                modelConfig[i]['actFunc'] = layer.actFunc
                # has bias?
                for j, neuronLeft in enumerate(layer.neurons):
                    for k, neuronRight in enumerate(self.layers[i + 1].neurons):
                        if neuronRight in neuronLeft.connections:
                            modelConfig[i]['connectMat'][j, k] = 1.0
                            modelConfig[i]['weightMat'][j, k] = neuronLeft.connections[neuronRight].weight

        print('+--------------------------------------+')
        print("number of layers: {}".format(nLayers))
        print("cost function: {}".format(CFB))
        for i, layerConfig in modelConfig.items():
            print("#L{}:".format(i + 1))
            print("number of neurons: {}".format(modelConfig[i]['numNeuron']))
            print("connection matrix: {}".format(modelConfig[i]['connectMat']))
            print("weight matrix: {}".format(modelConfig[i]['weightMat']))
            print("activation function: {}".format(modelConfig[i]['actFunc']))
        print('+--------------------------------------+')

    def toModel(self, numNeurons, weightMats, actFuncs, connectMats):
        """
        Only available when the train mode is on
        1. There is one input layer and one output layer.
        2. There is one loss function block connected.
        3. No isolate components/models.
        """
        pass

    def trainModel(self):
        pass

    # ------------------------------------------------- #
    #                 Event handlers                    #
    # ------------------------------------------------- #

    def keyPressEvent(self, event):
        if event.key() == 16777219:
            self.removeSelectedComponents()
        elif event.key() == Qt.Key_Space:
            if self.sceneMode == SceneMode.TrainMode:
                self.switchMode(SceneMode.SelectMode)
            else:
                if not self.checkNNModelValid():
                    return
                self.switchMode(SceneMode.TrainMode)
                self._compileIntoNNModel()
                self.makeTrainingAnimation()

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
        super().mouseReleaseEvent(event)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText() and self.sceneMode == SceneMode.SelectMode:
            event.accept()
            # switch into drag-drop mode
            self.sceneMode = SceneMode.DragDrogMode
            self.selectionRect = None
            self.origPos = None
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
            if layer and isinstance(layer, NNB1DAffineLayer):
                self.createNeuron(x - layer.scenePos().x(),
                                  y - layer.scenePos().y(),
                                  NNB1DInputNeuron,
                                  layer)
            else:
                print("can't create an 1D neuron.")
        elif iconType == "neuron_bias_1D":
            # TO-DO: CAN Highlight
            layer = self.itemAt(event.scenePos().x(), event.scenePos().y(), QTransform())
            if layer and isinstance(layer, NNB1DAffineLayer):
                self.createNeuron(x - layer.scenePos().x(),
                                  y - layer.scenePos().y(),
                                  NNB1DBiasNeuron,
                                  layer)
            else:
                print("can't create an 1D bias neuron.")
        elif iconType == "neuron_2D":
            layer = self.itemAt(event.scenePos().x(), event.scenePos().y(), QTransform())
            if layer and isinstance(layer, NNB2DConvLayer):
                self.createNeuron(x - layer.scenePos().x(),
                                  y - layer.scenePos().y(),
                                  NNB2DInputNeuron,
                                  layer)
            else:
                print("can't create an 2D neuron.")
        elif iconType == "neuron_bias_2D":
            layer = self.itemAt(event.scenePos().x(), event.scenePos().y(), QTransform())
            if layer and isinstance(layer, NNB2DConvLayer):
                self.createNeuron(x - layer.scenePos().x(),
                                  y - layer.scenePos().y(),
                                  NNB2DBiasNeuron,
                                  layer)
            else:
                print("can't create an 2D neuron.")
        elif iconType == "loss_func_block":
            self.createLossFuncBlock(x, y)
        elif iconType == "regularizer":
            self.createRegularizer(x, y)

        # upon finish and creation (if possible)
        self.sceneMode = SceneMode.SelectMode
        selectedItems = self.selectedItems()
        if selectedItems:
            selectedItem = selectedItems[0]
            selectedItem.setSelected(False)
            selectedItem.update()
