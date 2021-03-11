'''

Reference:
- How to draw QGraphicsLineItem during run time with mouse coordinates:
    https://www.walletfox.com/course/qgraphicsitemruntimedrawing.php
-


'''
import re
from PyQt5.QtGui import QTransform
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsItem, QGraphicsLineItem
import numpy as np
from NNBLayer import NNBLayer
from NNBAffineLayer import NNBAffineLayer
from NNBConvLayer import NNBConvLayer
from NNBNeuron import NNBNeuron
from NNB1DNeuron import NNB1DNeuron
from NNB2DNeuron import NNB2DNeuron
from NNBConnection import NNBConnection
from NNBConvConnection import NNBConvConnection
from NNBSimConnection import NNBSimConnection
from NNBRegConnection import NNBRegConnection
from NNBCostFuncBlock import NNBCostFuncBlock
from NNBRegularizer import NNBRegularizer
from NNBAnimation import NNTrainArrowFlowAnimation
from config import *

class NNBScene(QGraphicsScene):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.sceneMode = SceneMode.SelectMode
        self.env = {} #environment of the builder

        # For connect mode
        self.origPos = None
        self.lineToLink = None
        self.selectionRect = None
        self.hoveredItemOnConnectMode = None
        self.origItemOnConnectMode = None

        # for select mode
        self.itemSelected = []

        # For compiling into a NN model
        #####For now, we force the user to specify the layer type.
        self.inputLayer = None
        self.outputLayer = None
        self.costFuncBlock = None
        self.layers = []

        # For animation
        self.animations = []
        self.inTrainingAnimation = False
        self.currAnimationLayerIdx = 0
        self.ffFlowing = True

    def checkNNModelValid(self):
        if not self.inputLayer:
            print('An input layer is missing.')
            return False
        if not self.outputLayer:
            print('An output layer is missing.')
            return False
        if not self.inputLayer.adjBlocks:
            print('The input layer is isolate.')
            return False
        if not self.outputLayer.adjBlocks:
            print('The output layer is isolate.')
            return False
        if len(self.outputLayer.adjBlocks) == 1:
            if not isinstance(self.outputLayer.adjBlocks[0], NNBCostFuncBlock):
                print('A loss function is missing or it is not connected to an output layer.')
            else:
                print('The output layer is isolate.')
            return False
        if isinstance(self.outputLayer.adjBlocks[0], NNBCostFuncBlock):
            self.costFuncBlock = self.outputLayer.adjBlocks[0]
        elif isinstance(self.outputLayer.adjBlocks[1], NNBCostFuncBlock):
            self.costFuncBlock = self.outputLayer.adjBlocks[1]
        else:
            # should be unreachable
            pass
        # check the connectivity and get the chain of the layers
        self.costFuncBlock = None
        self.layers = [self.inputLayer]
        prev = self.inputLayer
        curr = self.inputLayer.adjBlocks[0]
        while True:
            if isinstance(curr, NNBCostFuncBlock):
                self.costFuncBlock = curr
                break
            elif len(curr.adjBlocks) == 1:
                print('The input layer and the output layer are not connected.')
                return False
            self.layers.append(curr)
            if curr.adjBlocks[0] == prev:
                prev = curr
                curr = curr.adjBlocks[1]
            else:
                prev = curr
                curr = curr.adjBlocks[0]
        # TO-DO check if there are other isolate components
        return True

    def _compileIntoNNModel(self):
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
        '''
        Only available when the train mode is on
        1. There is one input layer and one output layer.
        2. There is one loss function block connected.
        3. No isolate components/models.
        '''
        pass

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
                    elif i == len(self.layers) - 1 and (connection.neuronLeft == self.costFuncBlock or \
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

    def trainModel(self):
        pass

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
                if not isinstance(item, NNBConnection):
                    item.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.sceneMode = mode

    def checkConnectionValid(self, block1, block2):
        '''
        L1 is trying to connect to L2.
        L1 CAN'T be linked to L2 when:
        1. L1 = L2                                        --- (1)
        2. L1 or L2 already has two OTHER adj. layers     --- (2)
        3. L1 or L2 has no neuron.                        --- (3)
        if L1 or L2 is an input or output layer and either of them has already one adj. layer.
        '''

        def checkConnectionValidBB(block1, block2):
            prev = block1
            curr = block1.adjBlocks[0]
            while True:
                if isinstance(curr, NNBCostFuncBlock):
                    break
                if len(curr.adjBlocks) == 1:
                    curr = curr.adjBlocks[0]
                    if curr != block2:
                        break
                    else:
                        return False
                else:
                    if curr.adjBlocks[0] == prev:
                        prev = curr
                        curr = curr.adjBlocks[1]
                    else:
                        prev = curr
                        curr = curr.adjBlocks[0]
                    if curr == block2:
                        return False
            return True

        def checkConnectionValidLB(layer, block):
            # when a layer is trying to connect to a block:
            if len(layer.neurons) == 0:
                print('connection rejected: the layer has no neuron.')
                return False
            if layer.layerType == "input" and len(layer.adjBlocks) == 1 and layer.adjBlocks[0] != block:
                print('connection reject: 3')
                return False
            elif layer.layerType == "output":
                if len(layer.adjBlocks) == 1:
                    if not isinstance(layer.adjBlocks[0], NNBCostFuncBlock) and \
                            (not isinstance(block, NNBCostFuncBlock) and layer.adjBlocks[0] != block):
                        # can only be connected to a loss function block or layer2 in this case
                        print('connection reject: 4')
                        return False
            return True

        def checkConnectionValidCB(cfb, block):
            if not isinstance(block, NNBLayer) or block.layerType != "output":
                print('connection reject: 8')
                return False
            return True

        if block1 == block2:
            print('connection rejected: connection to the same block')
            return False

        if isinstance(block1, NNBLayer):
            if not checkConnectionValidLB(block1, block2):
                return False
        if isinstance(block2, NNBLayer):
            if not checkConnectionValidLB(block2, block1):
                return False
        if isinstance(block1, NNBCostFuncBlock):
            if not checkConnectionValidCB(block1, block2):
                return False
        if isinstance(block2, NNBCostFuncBlock):
            if not checkConnectionValidCB(block2, block1):
                return False

        if len(block1.adjBlocks) == 2 or len(block2.adjBlocks) == 2:
            if block1 not in block2.adjBlocks:
                print('connection reject: 5')
                return False
            else:
                return True
            # return layer2 in layer1.adjBlocks
        if len(block1.adjBlocks) == 1 and len(block2.adjBlocks) != 0:
            if not checkConnectionValidBB(block1, block2):
                print('connection reject: 6')
                return False
            else:
                return True
            # return checkConnectionValidBB(block1, block2)
        if len(block2.adjBlocks) == 1 and len(block1.adjBlocks) != 0:
            if not checkConnectionValidBB(block2, block1):
                print('connection reject: 7')
                return False
            else:
                return True
            # checkConnectionValidBB(block2, block1)
        return True

    def checkConnectivity(self, layer1, layer2):
        connected = False
        if not isinstance(layer1, NNBLayer):
            if not isinstance(layer2, NNBLayer):
                # what?
                pass
            layer1, layer2 = layer2, layer1
        for neuron1 in layer1.neurons:
            for target in neuron1.connections.keys():
                if (isinstance(target, NNBNeuron) and target.layer == layer2) or \
                        (isinstance(target, NNBCostFuncBlock) and target == layer2):
                    connected = True
                    break
            if connected:
                break
        return connected

    def _connect2Neurons(self, neuron1, neuron2):
        # Only check if the connection has already been formed.
        if neuron2 in neuron1.connections:
            return
        if isinstance(neuron1, NNB1DNeuron):
            neuronDefaultNameRegex = NEURON_1D_DEFAULT_NAME_REGEX
            connectionName = LINEAR_CONNECTION_DEFAULT_NAME
            connectionType = NNBSimConnection
        else:  # NNB2DNeuron
            neuronDefaultNameRegex = NEURON_2D_DEFAULT_NAME_REGEX
            connectionName = CONV_CONNECTION_DEFAULT_NAME
            connectionType = NNBConvConnection
        # name the connection
        neuron1Name = neuron1.name
        res = re.findall(neuronDefaultNameRegex, neuron1.name)
        if res:
            neuron1Name = res[0]
        neuron2Name = neuron2.name
        res = re.findall(neuronDefaultNameRegex, neuron2.name)
        if res:
            neuron2Name = res[0]
        connectionName = connectionName.format(neuron1Name, neuron2Name)
        connectedLine = connectionType(connectionName, neuron1, neuron2)
        neuron1.connections[neuron2] = connectedLine
        neuron2.connections[neuron1] = connectedLine
        self.addItem(connectedLine)
        print(connectionName + " is created.")

    def connect2Neurons(self, neuron1, neuron2):
        if not self.checkConnectionValid(neuron1.layer, neuron2.layer):
            return
        self._connect2Neurons(neuron1, neuron2)
        neuron1.layer._connectLayer(neuron2.layer)
        neuron2.layer._connectLayer(neuron1.layer)

    def connect1Neuron1Layer(self, neuron, layer):
        if not self.checkConnectionValid(neuron.layer, layer):
            return
        for layerNeuron in layer.neurons:
            self._connect2Neurons(neuron, layerNeuron)
        neuron.layer._connectLayer(layer)
        layer._connectLayer(neuron.layer)

    def connect2Layers(self, layer1, layer2):
        if not self.checkConnectionValid(layer1, layer2):
            return
        for layer1Neuron in layer1.neurons:
            for layer2Neuron in layer2.neurons:
                self._connect2Neurons(layer1Neuron, layer2Neuron)
        layer1._connectLayer(layer2)
        layer2._connectLayer(layer1)

    def connect1Neuron1CFB(self, neuron, costFuncBlock):
        if not self.checkConnectionValid(neuron.layer, costFuncBlock):
            return
        self._connect2Neurons(neuron, costFuncBlock)
        neuron.layer._connectCFB(costFuncBlock)
        costFuncBlock._connectLayer(neuron.layer)

    def connect1Layer1CFB(self, layer, costFuncBlock):
        if not self.checkConnectionValid(layer, costFuncBlock):
            return
        for layerNeuron in layer.neurons:
            self._connect2Neurons(layerNeuron, costFuncBlock)
        layer._connectCFB(costFuncBlock)
        costFuncBlock._connectLayer(layer)

    def connect1Layer1Reg(self, layer, regularizer):
        #         if not self.checkConnectionValid(layer, costFuncBlock):
        #             return
        connection = NNBRegConnection(layer, regularizer)
        regularizer.connections[layer] = connection
        self.addItem(connection)
        layer._connectReg(regularizer)
        regularizer._connectLayer(layer)

    def keyPressEvent(self, event):
        if event.key() == 16777219:
            # we will first delete all layers, then neurons, then connections, then other components
            itemsToBeCleared = set(self.selectedItems())
            layersToBeRemoved = set()
            neuronsToBeRemoved = set()
            connectionsToBeRemoved = set()
            cfbsToBeRemoved = set()
            for selectedItem in self.selectedItems():
                if isinstance(selectedItem, NNBLayer):
                    layersToBeRemoved.add(selectedItem)
                elif isinstance(selectedItem, NNBNeuron):
                    neuronsToBeRemoved.add(selectedItem)
                elif isinstance(selectedItem, NNBConnection):
                    connectionsToBeRemoved.add(selectedItem)
                elif isinstance(selectedItem, NNBCostFuncBlock):
                    cfbsToBeRemoved.add(selectedItem)
            for layerToBeRemoved in layersToBeRemoved:
                if layerToBeRemoved.layerType == "input":
                    self.inputLayer = None
                elif layerToBeRemoved.layerType == "output":
                    self.outputLayer = None
                for neuron in layerToBeRemoved.neurons:
                    try:
                        neuronsToBeRemoved.remove(neuron)
                    except:
                        itemsToBeCleared.add(neuron)
                    for connection in neuron.connections.values():
                        try:
                            connectionsToBeRemoved.remove(connection)
                        except:
                            itemsToBeCleared.add(connection)
                layerToBeRemoved._remove()

            for neuronToBeRemoved in neuronsToBeRemoved:
                for connection in neuronToBeRemoved.connections.values():
                    try:
                        connectionsToBeRemoved.remove(connection)
                    except:
                        itemsToBeCleared.add(connection)
                neuronToBeRemoved._remove()

            for connectionToBeRemoved in connectionsToBeRemoved:
                connectionToBeRemoved._remove()

            for cfbToBeRemoved in cfbsToBeRemoved:
                cfbToBeRemoved._remove()

            for itemToBeCleared in itemsToBeCleared:
                self.removeItem(itemToBeCleared)
                if itemToBeCleared.form:
                    if itemToBeCleared.isFormOn:
                        itemToBeCleared.form.close()
                    del itemToBeCleared.form
                del itemToBeCleared
            #####
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
        #TO-DO: outside of the scene problem

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
        # elif self.sceneMode == SceneMode.SelectMode and self.origPos:
        #     if not self.selectedItems():
        #         if not self.selectionRect:
        #             self.selectionRect = QGraphicsRectItem()
        #             self.selectionRect.setPen(QPen(QColor(153, 204, 255, 128)))
        #             self.selectionRect.setBrush(QBrush(QColor(153, 204, 255, 128)))
        #             self.selectionRect.setPos(self.origPos)
        #             self.addItem(self.selectionRect)
        #         dx = event.scenePos().x() - self.origPos.x()
        #         dy = event.scenePos().y() - self.origPos.y()
        #         newx, newy = 0, 0
        #         if dx < 0:
        #             newx = newx + dx
        #         if dy < 0:
        #             newy = newy + dy
        #         self.selectionRect.setRect(newx, newy,
        #                                    abs(event.scenePos().x() - self.origPos.x()),
        #                                    abs(event.scenePos().y() - self.origPos.y()))

        super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event):
        if self.sceneMode == SceneMode.ConnectMode:
            self.removeItem(self.lineToLink)
            del self.lineToLink
            self.lineToLink = None
            self.origPos = None
            if self.origItemOnConnectMode and self.hoveredItemOnConnectMode:
                if isinstance(self.origItemOnConnectMode, NNBNeuron):
                    if isinstance(self.hoveredItemOnConnectMode, NNBNeuron):
                        self.connect2Neurons(self.origItemOnConnectMode, self.hoveredItemOnConnectMode)
                    elif isinstance(self.hoveredItemOnConnectMode, NNBLayer):
                        self.connect1Neuron1Layer(self.origItemOnConnectMode, self.hoveredItemOnConnectMode)
                    elif isinstance(self.hoveredItemOnConnectMode, NNBCostFuncBlock):
                        self.connect1Neuron1CFB(self.origItemOnConnectMode, self.hoveredItemOnConnectMode)
                elif isinstance(self.origItemOnConnectMode, NNBLayer):
                    if isinstance(self.hoveredItemOnConnectMode, NNBNeuron):
                        self.connect1Neuron1Layer(self.hoveredItemOnConnectMode, self.origItemOnConnectMode)
                    elif isinstance(self.hoveredItemOnConnectMode, NNBLayer):
                        self.connect2Layers(self.origItemOnConnectMode, self.hoveredItemOnConnectMode)
                    elif isinstance(self.hoveredItemOnConnectMode, NNBCostFuncBlock):
                        self.connect1Layer1CFB(self.origItemOnConnectMode, self.hoveredItemOnConnectMode)
                    elif isinstance(self.hoveredItemOnConnectMode, NNBRegularizer):
                        self.connect1Layer1Reg(self.origItemOnConnectMode, self.hoveredItemOnConnectMode)
                elif isinstance(self.origItemOnConnectMode, NNBCostFuncBlock):
                    if isinstance(self.hoveredItemOnConnectMode, NNBNeuron):
                        self.connect1Neuron1CFB(self.hoveredItemOnConnectMode, self.origItemOnConnectMode)
                    elif isinstance(self.hoveredItemOnConnectMode, NNBLayer):
                        self.connect1Layer1CFB(self.hoveredItemOnConnectMode, self.origItemOnConnectMode)
                    elif isinstance(self.hoveredItemOnConnectMode, NNBRegularizer):
                        self.connect1Layer1Reg(self.origItemOnConnectMode, self.hoveredItemOnConnectMode)
                elif isinstance(self.origItemOnConnectMode, NNBRegularizer):
                    if isinstance(self.hoveredItemOnConnectMode, NNBLayer):
                        self.connect1Layer1Reg(self.hoveredItemOnConnectMode, self.origItemOnConnectMode)
                    elif isinstance(self.hoveredItemOnConnectMode, NNBCostFuncBlock):
                        self.connect1Layer1Reg(self.hoveredItemOnConnectMode, self.origItemOnConnectMode)

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
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        item = self.itemAt(event.scenePos().x(), event.scenePos().y(), QTransform())
        if item:
            selectedItems = self.selectedItems()
            if selectedItems and item != selectedItems[0]:
                selectedItems[0].setSelected(False)
                item.setSelected(True)
                selectedItems[0].update()
                item.update()
            elif not selectedItems:
                item.setSelected(True)
                item.update()

    def dropEvent(self, event):
        iconType = event.mimeData().text()
        if iconType == "affine_layer":
            itemName = self.findNextDefaultName(NNBAffineLayer, AFFINE_LAYER_DEFAULT_NAME)
            layer = NNBAffineLayer(itemName,
                                   event.scenePos().x() - ICON_OFFSET_X,
                                   event.scenePos().y() - ICON_OFFSET_Y)
            self.registerNNBItem(layer)
            self.addItem(layer)
            print(layer.name + " created.")
        elif iconType == "conv_layer":
            itemName = self.findNextDefaultName(NNBConvLayer, CONV_LAYER_DEFAULT_NAME)
            layer = NNBConvLayer(itemName,
                                   event.scenePos().x() - ICON_OFFSET_X,
                                   event.scenePos().y() - ICON_OFFSET_Y)
            self.registerNNBItem(layer)
            self.addItem(layer)
            print(layer.name + " created.")
        elif iconType == "pooling_layer":
            pass
        elif iconType == "flatten_layer":
            pass
        elif iconType == "neuron_1D":
            #TO-DO: CAN Highlight
            item = self.itemAt(event.scenePos().x(), event.scenePos().y(), QTransform())
            if item and isinstance(item, NNBAffineLayer):
                layerName = item.name
                res = re.findall(AFFINE_LAYER_DEFAULT_NAME_REGEX, layerName)
                if res:
                    layerName = res[0]
                neuronName = NEURON_1D_DEFAULT_NAME.format(layerName, "{}")
                neuronName = self.findNextDefaultName(NNB1DNeuron, neuronName)
                neuron = NNB1DNeuron(neuronName,
                                     event.scenePos().x() - ICON_OFFSET_X - item.scenePos().x(),
                                     event.scenePos().y() - ICON_OFFSET_Y - item.scenePos().y())
                item.addNeuron(neuron)
                self.registerNNBItem(neuron)
                print(neuronName + " created.")
            else:
                print("can't create an 1D neuron.")
        elif iconType == "neuron_2D":
            item = self.itemAt(event.scenePos().x(), event.scenePos().y(), QTransform())
            if item and isinstance(item, NNBConvLayer):
                layerName = item.name
                res = re.findall(CONV_LAYER_DEFAULT_NAME_REGEX, layerName)
                if res:
                    layerName = res[0]
                neuronName = NEURON_2D_DEFAULT_NAME.format(layerName, "{}")
                neuronName = self.findNextDefaultName(NNB2DNeuron, neuronName)
                neuron = NNB2DNeuron(neuronName,
                                     event.scenePos().x() - ICON_OFFSET_X - item.scenePos().x(),
                                     event.scenePos().y() - ICON_OFFSET_Y - item.scenePos().y())
                item.addNeuron(neuron)
                self.registerNNBItem(neuron)
                print(neuronName + " created.")
            else:
                print("can't create an 1D neuron.")
        elif iconType == "cost_func_block":
            itemName = self.findNextDefaultName(NNBCostFuncBlock, CFB_DEFAULT_NAME)
            costFuncBlock = NNBCostFuncBlock(itemName,
                                            event.scenePos().x() - ICON_OFFSET_X,
                                            event.scenePos().y() - ICON_OFFSET_Y)
            self.registerNNBItem(costFuncBlock)
            self.addItem(costFuncBlock)
            print(costFuncBlock.name + " created.")
        elif iconType == "regularizer":
            itemName = self.findNextDefaultName(NNBRegularizer, REGULARIZER_DEFAULT_NAME)
            regularizer = NNBRegularizer(itemName,
                                         event.scenePos().x() - ICON_OFFSET_X,
                                         event.scenePos().y() - ICON_OFFSET_Y)
            self.registerNNBItem(regularizer)
            self.addItem(regularizer)
            print(regularizer.name + " created.")

    def registerNNBItem(self, item):
        if type(item) not in self.env:
            self.env[type(item)] = {}
        self.env[type(item)][item] = item.name

    def findNextDefaultName(self, itemType, itemName):
        i = 1
        if itemType not in self.env:
            proposedItemName = itemName.format(i)
        else:
            while True:
                proposedItemName = itemName.format(i)
                if proposedItemName not in self.env[itemType].values():
                    break
                i += 1
        return proposedItemName