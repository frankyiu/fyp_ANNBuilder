"""
+-------------+
| NNB ENGINE |
+------------+

This defines the logical model for the NNBuilder.

"""


class _NNBComponent:
    """
    it has:
    - a name (not necessarily unique and the user can change it)
    - a form (popup dialog which shows information on the component)
    """
    def __init__(self, name):
        self.name = name
        self.form = None

        # states
        self.isFormOn = False
        self.hoveredOnConnectMode = False

    def createForm(self, window):
        pass

    def removeWithoutCheckingConnectivity(self):
        pass

    def remove(self):
        """
        It defines what the component will do when it is going to get removed.
        """
        self.removeWithoutCheckingConnectivity()

    def handleItemChanged(self):
        pass

    def handleMouseDoubleClickEvent(self):
        pass
        # if self.form is None:
        #     self.form = self.createForm(window)
        # if self.isFormOn:
        #     self.form.cancel()
        # self.form.show()
        # self.isFormOn = True


class _NNBBlock(_NNBComponent):
    """
    Connectable
    """
    def __init__(self, name):
        _NNBComponent.__init__(self, name)
        self.connectionsFrom = {}  # stored in the format of {blockFrom : connection}
        self.connectionsTo = {}  #

    def handleItemChanged(self):
        for connection in self.connectionsFrom.values():
            connection.updateConnectionPos()
        for connection in self.connectionsTo.values():
            connection.updateConnectionPos()

    def removeWithoutCheckingConnectivity(self):
        for blockFrom in self.connectionsFrom.keys():
            if self in blockFrom.connectionsTo:
                del blockFrom.connectionsTo[self]
        for blockTo in self.connectionsTo.keys():
            if self in blockTo.connectionsFrom:
                del blockTo.connectionsFrom[self]
        self.connectionsFrom = {}
        self.connectionsTo = {}

    def connectTo(self, blockTo, connection):
        self.connectionsTo[blockTo] = connection
        blockTo.connectionsFrom[self] = connection

    def connectToNeuron(self, neuronTo):
        pass

    def connectToLayer(self, layerTo):
        pass

    def connectToLFB(self, lfbTo):
        pass

    def connectToRegularizer(self, regularizerTo):
        pass


class _NNBNeuron(_NNBBlock):
    """
    Can be
    - 1D (represented as a circle) or
    - 2D (represented as a square and usually called "Feature Map")
    """
    def __init__(self, name, dim, layer=None):
        _NNBBlock.__init__(self, name)
        self.layer = layer

        # model hyper-parameters
        self.dim = dim

    # def removeWithoutCheckingConnectivity(self):
    #     for neuronFrom in self.connectionsFrom.keys():
    #         if self in neuronFrom.connectionsTo:
    #             del neuronFrom.connectionsTo[self]
    #     for neuronTo in self.connectionsTo.keys():
    #         if self in neuronTo.connectionsFrom:
    #             del neuronTo.connectionsFrom[self]
    #     self.connectionsFrom = {}
    #     self.connectionsTo = {}

    def remove(self):
        self.layer.removeNeuron(self)
        self.removeWithoutCheckingConnectivity()
        # special case: when this connection is the only one within two layers, cancel their linking relation
        self.layer.removeAdjLayerIfNoMoreRelation()

    def connectToNeuron(self, neuronTo):
        self.layer.nextLayer = neuronTo.layer
        neuronTo.layer.prevLayer = self.layer

    def connectToLayer(self, layerTo):
        self.layer.nextLayer = layerTo
        layerTo.prevLayer = self.layer

    def connectToLFB(self, lfbTo):
        self.layer.nextLayer = lfbTo
        lfbTo.outputLayer = self.layer


class _NNB1DNeuron(_NNBNeuron):
    def __init__(self, name, layer=None):
        _NNBNeuron.__init__(self, name, 1, layer)


class _NNB1DInputNeuron(_NNB1DNeuron):
    def __init__(self, name, layer=None):
        _NNB1DNeuron.__init__(self, name, layer)


class _NNB1DBiasNeuron(_NNB1DNeuron):
    def __init__(self, name, layer=None):
        _NNB1DNeuron.__init__(self, name, layer)


class _NNB1DStackedNeuron(_NNB1DNeuron):
    def __init__(self, name, layer=None):
        _NNB1DNeuron.__init__(self, name, layer)


class _NNB2DNeuron(_NNBNeuron):
    def __init__(self, name, layer=None):
        _NNBNeuron.__init__(self, name, 2, layer)


class _NNB2DInputNeuron(_NNB2DNeuron):
    def __init__(self, name, layer=None):
        _NNB2DNeuron.__init__(self, name, layer)


class _NNB2DBiasNeuron(_NNB2DNeuron):
    def __init__(self, name, layer=None):
        _NNB2DNeuron.__init__(self, name, layer)


class _NNBLayer(_NNBBlock):
    def __init__(self, name, dim, inputSize, outputSize):
        _NNBBlock.__init__(self, name)
        self.prevLayer = None
        self.nextLayer = None
        self.neurons = []

        # model hyper-parameters
        self.dim = dim
        self.inputSize = inputSize
        self.outputSize = outputSize

    def getChainOfLayers(self):
        currLayer = self
        layers = [self]
        while True:
            if currLayer.nextLayer:
                if isinstance(currLayer.nextLayer, _NNBLossFuncBlock):
                    break
                currLayer = currLayer.nextLayer
                layers.append(currLayer)
            else:
                break
        return layers

    def addNeuron(self, neuron):
        neuron.layer = self
        self.neurons.append(neuron)
        if self.form:
            self.form.update()

    def removeNeuron(self, neuron):
        self.neurons.remove(neuron)
        if self.form:
            self.form.update()

    def removeWithoutCheckingConnectivity(self):
        super().removeWithoutCheckingConnectivity()
        for neuron in self.neurons:
            neuron.removeWithoutCheckingConnectivity()
        if self.prevLayer:
            self.prevLayer.nextLayer = None
        if self.nextLayer:
            self.nextLayer.prevLayer = None
        self.neurons = []

    def removeAdjLayerIfNoMoreRelation(self):
        if self.prevLayer and not NNBController.checkConnectivityBlockBlock(self, self.prevLayer):
            self.prevLayer.nextLayer = None
            self.prevLayer = None
        if self.nextLayer and not NNBController.checkConnectivityBlockBlock(self, self.nextLayer):
            self.nextLayer.prevLayer = None
            self.nextLayer = None

    def handleItemChanged(self):
        _NNBBlock.handleItemChanged(self)
        for neuron in self.neurons:
            for connection in neuron.connectionsFrom.values():
                connection.updateConnectionPos()
            for connection in neuron.connectionsTo.values():
                connection.updateConnectionPos()

    def connectToNeuron(self, neuronTo):
        self.nextLayer = neuronTo.layer
        neuronTo.layer.prevLayer = self

    def connectToLayer(self, layerTo):
        self.nextLayer = layerTo
        layerTo.prevLayer = self

    def connectToLFB(self, lfbTo):
        self.nextLayer = lfbTo
        lfbTo.outputLayer = self


class _NNBNontrainableLayer(_NNBLayer):
    pass


class _NNBTrainableLayer(_NNBLayer):
    def __init__(self, name, dim, inputSize, outputSize):
        _NNBLayer.__init__(self, name, dim, inputSize, outputSize)
        # self.layerType = "hidden"  # one of three types : input, hidden, output, by default hidden

        # model hyper-parameters
        self.actFunc = "Sigmoid"

    def connectToLBF(self, lfbTo):
        self.nextLayer = lfbTo
        lfbTo.outputLayer = self

    def connectToRegularizer(self, regularizerTo):
        pass


class _NNB2DPoolingLayer(_NNBNontrainableLayer):
    def __init__(self, name):
        _NNBNontrainableLayer.__init__(self, name, 2, (-1, -1), (-1, -1))

        # model hyper-parameters
        self.poolingType = "max"  # can be "mean" or "max"


class _NNB2DFlattenLayer(_NNBNontrainableLayer):
    def __init__(self, name):
        _NNBNontrainableLayer.__init__(self, name, 2, (-1, -1), -1)


class _NNB1DAffineLayer(_NNBTrainableLayer):
    def __init__(self, name):
        _NNBTrainableLayer.__init__(self, name, 1, -1, -1)


class _NNB1DStackedLayer(_NNBTrainableLayer):
    def __init__(self, name):
        _NNBTrainableLayer.__init__(self, name, 1, -1, -1)


class _NNB2DConvLayer(_NNBTrainableLayer):
    def __init__(self, name, kernelSize=(3, 3), padding=(0, 0)):
        _NNBTrainableLayer.__init__(self, name, 2, (-1, -1), (-1, -1))

        # model parameters
        self.kernelSize = kernelSize
        self.padding = padding


class _NNBConnection(_NNBComponent):
    def __init__(self, name, blockFrom, blockTo):
        _NNBComponent.__init__(self, name)
        self.blockFrom = blockFrom
        self.blockTo = blockTo

    def updateConnectionPos(self):
        # To be overridden
        pass

    def onWeightChangedOnTrainMode(self):
        # TO-DO
        if self.form:
            self.form.update()

    def removeWithoutCheckingConnectivity(self):
        if self.blockFrom in self.blockTo.connectionsFrom:
            del self.blockTo.connectionsFrom[self.blockFrom]
        if self.blockTo in self.blockFrom.connectionsTo:
            del self.blockFrom.connectionsTo[self.blockTo]


class _NNBNonTrainableConnection(_NNBConnection):
    pass


class _NNBTrainableConnection(_NNBConnection):
    """
    blockFrom and blockTo must be of NNBLayer type
    """
    def __init__(self, name, blockFrom, blockTo, weight):
        _NNBConnection.__init__(self, name, blockFrom, blockTo)

        # model parameters
        self.weight = weight

    def remove(self):
        self.removeWithoutCheckingConnectivity()
        # special case: when this connection is the only one within two layers, cancel their linking relation
        if not NNBController.checkConnectivityBlockBlock(self.blockFrom.layer, self.blockTo.layer):
            self.blockFrom.layer.nextLayer = None
            self.blockTo.layer.prevLayer = None


class _NNB1DLinearConnection(_NNBTrainableConnection):
    def __init__(self, name, blockFrom, blockTo):
        _NNBTrainableConnection.__init__(self, name, blockFrom, blockTo, 0.0)


class _NNB1DStackedLinConnection(_NNBTrainableConnection):
    def __init__(self, name, blockFrom, blockTo):
        _NNBTrainableConnection.__init__(self, name, blockFrom, blockTo, 0.0)


class _NNB2DConvConnection(_NNBTrainableConnection):
    # lazy evaluation is applied for the weight
    def __init__(self, name, blockFrom, blockTo):
        _NNBTrainableConnection.__init__(self, name, blockFrom, blockTo, None)


class _NNB2DPoolingConnection(_NNBNonTrainableConnection):
    def __init__(self, name, blockFrom, blockTo):
        _NNBNonTrainableConnection.__init__(self, name, blockFrom, blockTo)


class _NNB2DFlattenConnection(_NNBNonTrainableConnection):
    def __init__(self, name, blockFrom, blockTo):
        _NNBNonTrainableConnection.__init__(self, name, blockFrom, blockTo)


class _NNBLFBConnection(_NNBConnection):
    """
    blockFrom: a loss function block
    blockTo: a trainable output layer
    """
    def __init__(self, name, blockFrom, blockTo):
        _NNBConnection.__init__(self, name, blockFrom, blockTo)

    def remove(self):
        self.removeWithoutCheckingConnectivity()
        # special case: when this connection is the only one within two layers, cancel their linking relation
        if not NNBController.checkConnectivityBlockBlock(self.blockTo, self.blockFrom):
            self.blockTo.nextLayer = None


class _NNBRegConnection(_NNBConnection):
    """
    blockFrom: a trainable layer or a loss function block
    blockTo: a regularizer
    """
    def __init__(self, name, blockFrom, blockTo):
        _NNBConnection.__init__(self, name, blockFrom, blockTo)


class _NNBLossFuncBlock(_NNBBlock):
    def __init__(self, name):
        _NNBBlock.__init__(self, name)
        self.outputLayer = None

        # model hyper-parameter
        self.costFunc = "MSE"  # MAE, MSE, CE

    def removeWithoutCheckingConnectivity(self):
        for neuron in self.connectionsFrom.values():
            if self in neuron.connectionsTo:
                del neuron.connectionsTo[self]
        self.connectionsFrom = {}
        if self.outputLayer:
            self.outputLayer.nextLayer = None


class _NNBRegularizer(_NNBBlock):
    def __init__(self, name):
        _NNBBlock.__init__(self, name)
        # can be connected to a layer or a loss function block

        # model hyper-parameters
        self.regularization = "L2"  # L1, L2, L0.5, L3, Lp, Elastic Net
        self.C = 1.0

    def removeWithoutCheckingConnectivity(self):
        for lfbTo in self.connectionsTo.keys():
            if self in lfbTo.connectionsFrom:
                del lfbTo.connectionsFrom[self]

    def connectToLFB(self, lfbTo):
        pass


class NNBController:

    @classmethod
    def checkConnectableBlockBlock(cls, blockFrom, blockTo):
        if isinstance(blockFrom, _NNBLayer):
            return cls.checkConnectableLayerBlock(blockFrom, blockTo)
        elif isinstance(blockFrom, _NNBNeuron):
            return cls.checkConnectableLayerBlock(blockFrom.layer, blockTo)
        elif isinstance(blockFrom, _NNBLossFuncBlock):
            print("connection rejected: you can't start linking from a loss function block.")
        elif isinstance(blockFrom, _NNBRegularizer):
            if isinstance(blockTo, _NNBTrainableLayer):
                print("connection rejected: wrong direction.")
            elif isinstance(blockTo, _NNBLossFuncBlock):
                return True
            else:
                print("connection rejected:.")
            return False
        return False  # should be unreachable

    @classmethod
    def checkConnectableLayerBlock(cls, layerFrom, blockTo):
        if isinstance(blockTo, _NNBLayer):
            return cls.checkConnectableLayerLayer(layerFrom, blockTo)
        elif isinstance(blockTo, _NNBNeuron):
            return cls.checkConnectableLayerLayer(layerFrom, blockTo.layer)
        elif isinstance(blockTo, _NNBLossFuncBlock):
            return cls.checkConnectableBlockLFB(layerFrom, blockTo)
        elif isinstance(blockTo, _NNBRegularizer):
            return cls.checkConnectableBlockRegularizer(layerFrom, blockTo)
        return False  # should be unreachable

    @classmethod
    def checkConnectableLayerLayer(cls, layerFrom, layerTo):
        if layerFrom == layerTo:
            return False
        if layerFrom.nextLayer and layerFrom.nextLayer != layerTo:
            print("connection rejected: the starting layer has already been connected to another layer.")
            return False
        if layerTo.prevLayer and layerTo.prevLayer != layerFrom:
            print("connection rejected: the ending layer has already been connected to another layer.")
            return False
        if layerFrom.dim != layerTo.dim and not \
                (isinstance(layerFrom, _NNB2DFlattenLayer) and isinstance(layerTo, _NNB1DStackedLayer)):
            print("connection rejected: dimensions don't match.")
            return False
        lastLayerTo = layerTo.getChainOfLayers()[-1]
        if lastLayerTo == layerFrom:
            print("connection rejected: a loop will be formed.")
            return False

        if isinstance(layerFrom, _NNBTrainableLayer) and isinstance(layerTo, _NNBTrainableLayer):
            if len(layerFrom.neurons) == 0 or len(layerTo.neurons) == 0:
                print("connection rejected: one of the layer doesn't have a neuron.")
                return False
            # if layerTo.layerType == "input":
            #     print("connection rejected: an input layer can't be connected to.")
            #     return False
            # elif layerFrom.layerType == "output":
            #     print("connection rejected: an output layer can't connect to another layer.")
            #     return False
        return True

    @classmethod
    def checkConnectableBlockLFB(cls, blockFrom, lfbTo):
        if isinstance(blockFrom, _NNBTrainableLayer):
            # if blockFrom.layerType != "output":
            #     print("connection rejected: only an output layer can connect to a loss function block.")
            #     return False
            if blockFrom.dim != 1:
                print("connection rejected: only a 1D layer can be reduced to a scalar loss value.")
                return False
            if blockFrom.nextLayer and blockFrom.nextLayer != lfbTo:
                print("connection rejected: the loss function block has already been connected to the other layer.")
                return False
            return True
        elif isinstance(blockFrom, _NNBNeuron):
            return cls.checkConnectableBlockLFB(blockFrom.layer, lfbTo)
        else:
            print("connection rejected: only a layer or a neuron can connect to a loss function block")
        return False

    @classmethod
    def checkConnectableBlockRegularizer(cls, blockFrom, regularizerTo):
        if isinstance(blockFrom, _NNBLayer):
            if not isinstance(blockFrom, _NNBTrainableLayer):
                print("connection rejected: only a trainable layer can connect to a regularizer.")
                return False
        elif isinstance(blockFrom, _NNBNeuron):
            return cls.checkConnectableBlockRegularizer(blockFrom.layer, regularizerTo)
        elif isinstance(blockFrom, _NNBLossFuncBlock):
            print("connection rejected: wrong direction when linking a regularizer to loss function block")
        else:
            print("connection rejected: only a layer or a neuron can connect to a regularizer")
        return True

    @classmethod
    def checkConnectivityBlockBlock(cls, blockFrom, blockTo):
        # blockFrom can only be: layer,
        # blockTo can be: layer, loss function block
        connected = False
        for neuronFrom in blockFrom.neurons:
            for neuronTo in neuronFrom.connectionsTo.keys():
                if neuronTo.layer == blockTo:
                    connected = True
                    break
                if connected:
                    break
        return connected

    @classmethod
    def VerifyNNModel(cls, inputLayer, outputLayer):
        if not inputLayer:
            print('An input layer is missing.')
            return False
        if not outputLayer:
            print('An output layer is missing.')
            return False
        if not inputLayer.nextLayer:
            print('The input layer is isolate.')
            return False
        if not outputLayer.prevLayer:
            print('The output layer is isolate.')
            return False
        if not isinstance(outputLayer.nextLayer, _NNBLossFuncBlock):
            print('A loss function is missing or it is not connected to an output layer.')
            return False
        # what if there are more than one LFB?
        lostFuncBlock = outputLayer.nextLayer

        # check the connectivity and get the chain of the layers
        layers = inputLayer.getChainOfLayers()
        if layers[-1] != lostFuncBlock:
            print("the input layer and output layer are not connected.")

        # TO-DO check if there are other isolate components
        return True

    @classmethod
    def compileIntoNNModel(cls, layers):
        pass

    @classmethod
    def toModel(cls, numNeurons, weightMats, actFuncs, connectMats):
        """
        Only available when the train mode is on
        1. There is one input layer and one output layer.
        2. There is one loss function block connected.
        3. No isolate components/models.
        """
        pass
