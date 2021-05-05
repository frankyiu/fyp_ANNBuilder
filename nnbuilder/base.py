"""
+-------------+
| NNB ENGINE |
+------------+

This defines the logical model for the NNBuilder.

"""


import numpy as np
from .config import *


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

    def removeWithoutCheckingConnectivity(self):
        pass

    def remove(self):
        """
        It defines what the component will do when it is going to get removed.
        """
        self.removeWithoutCheckingConnectivity()

    def handleItemChanged(self):
        pass

    # def createForm(self):
    #     pass

    def handleMouseDoubleClickEvent(self):
        if self.form is None:
            self.form = self.createForm()
        if self.isFormOn:
            self.form.cancel()
        self.form.show()
        self.isFormOn = True


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
    def __init__(self, name, layer=None, weight=None):
        _NNB1DNeuron.__init__(self, name, layer)
        self.weight = weight

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
    def __init__(self, name, layer=None, weight=None):
        _NNB2DNeuron.__init__(self, name, layer)
        self.weight = weight


class _NNBLayer(_NNBBlock):
    def __init__(self, name, dim, inputSize, outputSize):
        _NNBBlock.__init__(self, name)
        self.prevLayer = None
        self.nextLayer = None

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

    def removeWithoutCheckingConnectivity(self):
        super().removeWithoutCheckingConnectivity()
        if self.prevLayer:
            self.prevLayer.nextLayer = None
        if self.nextLayer:
            self.nextLayer.prevLayer = None

    def connectToNeuron(self, neuronTo):
        self.nextLayer = neuronTo.layer
        neuronTo.layer.prevLayer = self

    def connectToLayer(self, layerTo):
        self.nextLayer = layerTo
        layerTo.prevLayer = self

    def connectToLFB(self, lfbTo):
        self.nextLayer = lfbTo
        lfbTo.outputLayer = self

    def weightMat(self):
        pass

    def connectionMat(self):
        pass

    def numOfNeurons(self, includeBias=True):
        pass


class _NNBNontrainableLayer(_NNBLayer):
    pass


class _NNBTrainableLayer(_NNBLayer):
    def __init__(self, name, dim, inputSize, outputSize):
        _NNBLayer.__init__(self, name, dim, inputSize, outputSize)
        self.neurons = []
        self.biasIdx = -1

        # model hyper-parameters
        self.actFunc = "sigmoid"

    def addNeuron(self, neuron):
        neuron.layer = self
        self.neurons.append(neuron)
        if self.form:
            self.form.update()

    def removeNeuron(self, neuron):
        self.neurons.remove(neuron)
        if self.form:
            self.form.update()

    def connectToLBF(self, lfbTo):
        self.nextLayer = lfbTo
        lfbTo.outputLayer = self

    def connectToRegularizer(self, regularizerTo):
        pass

    def removeWithoutCheckingConnectivity(self):
        super().removeWithoutCheckingConnectivity()
        for neuron in self.neurons:
            neuron.removeWithoutCheckingConnectivity()
        self.neurons = []

    def removeAdjLayerIfNoMoreRelation(self):
        if self.prevLayer and not NNBController.checkConnectivityLayerLayer(self, self.prevLayer):
            self.prevLayer.nextLayer = None
            self.prevLayer = None
        if self.nextLayer and not NNBController.checkConnectivityLayerLayer(self, self.nextLayer):
            self.nextLayer.prevLayer = None
            self.nextLayer = None

    def getRegularizer(self):
        regularizer = None
        for component in self.connectionsTo.keys():
            if isinstance(component, _NNBRegularizer):
                regularizer = component
                break
        return regularizer

    def containsBias(self):
        return self.biasIdx != -1

    def updateParams(self, layerParam):
        pass

    def handleItemChanged(self):
        _NNBBlock.handleItemChanged(self)
        for neuron in self.neurons:
            for connection in neuron.connectionsFrom.values():
                connection.updateConnectionPos()
            for connection in neuron.connectionsTo.values():
                connection.updateConnectionPos()


class _NNB2DPoolingLayer(_NNBNontrainableLayer):
    def __init__(self, name):
        _NNBNontrainableLayer.__init__(self, name, 2, (-1, -1), (-1, -1))

        # model hyper-parameters
        self.poolingType = "max"  # can be "mean" or "max"


class _NNB2DFlattenLayer(_NNBNontrainableLayer):
    def __init__(self, name):
        _NNBNontrainableLayer.__init__(self, name, 2, (-1, -1, -1), -1)


class _NNB1DAffineLayer(_NNBTrainableLayer):
    def __init__(self, name):
        _NNBTrainableLayer.__init__(self, name, 1, -1, -1)

    def numOfNeurons(self, includeBias=True):
        if includeBias:
            numNeurons = len(self.neurons)
        else:
            numNeurons = len(self.neurons) - (1 if self.biasIdx != -1 else 0)
        return numNeurons

    def addNeuron(self, neuron):
        super().addNeuron(neuron)
        if isinstance(neuron, _NNB1DBiasNeuron):
            self.biasIdx = len(self.neurons) - 1

    def removeNeuron(self, neuron):
        super().removeNeuron(neuron)
        if isinstance(neuron, _NNB1DBiasNeuron):
            self.biasIdx = -1

    def getConnectivity(self):
        if isinstance(self.nextLayer, _NNBLossFuncBlock):
            WC = np.zeros((self.numOfNeurons(), 1))
            bC = None
            for i, neuronFrom in enumerate(self.neurons):
                if self.nextLayer in neuronFrom.connectionsTo:
                    WC[i, :] = 1
        else:
            bC = None
            if isinstance(self.nextLayer, _NNBLossFuncBlock):
                WC = np.zeros((self.numOfNeurons(), 1))
                for i, neuronFrom in enumerate(self.neurons):
                    if self.nextLayer in neuronFrom.connectionsTo:
                        WC[i, 0] = 1.0
            else:
                WC = np.zeros((self.numOfNeurons() - (1 if self.containsBias() else 0),
                              self.nextLayer.numOfNeurons() - (1 if self.nextLayer.containsBias() else 0)))
                bC = None
                ii = 0
                nNeurons = self.nextLayer.numOfNeurons() - (1 if self.nextLayer.containsBias() else 0)
                if isinstance(self.nextLayer, _NNB1DStackedLayer):
                    for i, neuronFrom in enumerate(self.neurons):
                        if i == self.biasIdx:
                            bC = np.ones((nNeurons,))
                        else:
                            WC = np.ones((nNeurons,))
                            ii += 1
                else:
                    for i, neuronFrom in enumerate(self.neurons):
                        if i == self.biasIdx:
                            bC = np.zeros((nNeurons,))
                            jj = 0
                            for j, neuronTo in enumerate(self.nextLayer.neurons):
                                if j == self.nextLayer.biasIdx:
                                    continue
                                if neuronTo in neuronFrom.connectionsTo:
                                    bC[jj] = 1
                                jj += 1
                        else:
                            jj = 0
                            for j, neuronTo in enumerate(self.nextLayer.neurons):
                                if j == self.nextLayer.biasIdx:
                                    continue
                                if neuronTo in neuronFrom.connectionsTo:
                                    WC[ii, jj] = 1
                                jj += 1
                            ii += 1
        return WC, bC

    def getParams(self):
        if isinstance(self.nextLayer, _NNBLossFuncBlock):
            W = None
            b = None
        else:
            W = np.zeros((self.numOfNeurons() - (1 if self.containsBias() else 0),
                          self.nextLayer.numOfNeurons() - (1 if self.nextLayer.containsBias() else 0)))
            b = None
            ii = 0
            if isinstance(self.nextLayer, _NNB1DStackedLayer):
                for i, neuronFrom in enumerate(self.neurons):
                    if i == self.biasIdx:
                        b = neuronFrom.connectionsTo[self.nextLayer.neurons[0]].weight[i, :]
                    else:
                        W[ii, :] = neuronFrom.connectionsTo[self.nextLayer.neurons[0]].weight[i, :]
                        ii += 1
            else:
                for i, neuronFrom in enumerate(self.neurons):
                    if i == self.biasIdx:
                        b = np.zeros((self.nextLayer.numOfNeurons() - (1 if self.nextLayer.containsBias() else 0), ))
                        jj = 0
                        for j, neuronTo in enumerate(self.nextLayer.neurons):
                            if j == self.nextLayer.biasIdx:
                                continue
                            if neuronTo in neuronFrom.connectionsTo:
                                b[jj] = neuronFrom.connectionsTo[neuronTo].weight
                            jj += 1
                    else:
                        jj = 0
                        for j, neuronTo in enumerate(self.nextLayer.neurons):
                            if j == self.nextLayer.biasIdx:
                                continue
                            if neuronTo in neuronFrom.connectionsTo:
                                W[ii, jj] = neuronFrom.connectionsTo[neuronTo].weight
                            jj += 1
                        ii += 1
        return W, b

    def updateParams(self, layerParam):
        if isinstance(self.nextLayer, _NNBLossFuncBlock):
            return
        W_ = layerParam[0]
        b_ = None
        if len(layerParam) == 2:
            b_ = layerParam[1]
        ii = 0
        if isinstance(self.nextLayer, _NNB1DStackedLayer):
            for i, neuronFrom in enumerate(self.neurons):
                if i == self.biasIdx:
                    neuronFrom.connectionsTo[self.nextLayer.neurons[0]].weight[i, :] = b_
                else:
                    neuronFrom.connectionsTo[self.nextLayer.neurons[0]].weight[i, :] = W_[ii, :]
                    ii += 1
        else:
            for i, neuronFrom in enumerate(self.neurons):
                if i == self.biasIdx:
                    jj = 0
                    for j, neuronTo in enumerate(self.nextLayer.neurons):
                        if j == self.nextLayer.biasIdx:
                            continue
                        if neuronTo in neuronFrom.connectionsTo:
                            neuronFrom.connectionsTo[neuronTo].weight = b_[jj]
                        jj += 1
                else:
                    jj = 0
                    for j, neuronTo in enumerate(self.nextLayer.neurons):
                        if j == self.nextLayer.biasIdx:
                            continue
                        if neuronTo in neuronFrom.connectionsTo:
                            neuronFrom.connectionsTo[neuronTo].weight = W_[ii, jj]
                        jj += 1
                    ii += 1


class _NNB1DStackedLayer(_NNBTrainableLayer):
    def __init__(self, name, numNeurons=-1, hasBias=True):
        _NNBTrainableLayer.__init__(self, name, 1, -1, -1)
        self.numNeurons = numNeurons
        self.hasBias = hasBias

    def numOfNeurons(self, includeBias=True):
        if includeBias:
            numNeurons = self.numNeurons
        else:
            numNeurons = self.numNeurons - (1 if self.biasIdx != -1 else 0)
        return numNeurons

    def containsBias(self):
        return self.hasBias

    def changeNumNeurons(self, numNeurons):
        pass

    # determine the number of neurons when the previous layer is a flatten layer
    def deduceNumOfNeurons(self):
        self.numNeurons = self.prevLayer.prevLayer.outputSize

    def getConnectivity(self):
        bC = None
        if isinstance(self.nextLayer, _NNBLossFuncBlock):
            WC = None
        else:
            nNeurons = self.numOfNeurons() - (1 if self.containsBias() else 0)
            nNeuronsNext = self.nextLayer.numOfNeurons() - (1 if self.nextLayer.containsBias() else 0)
            if isinstance(self.nextLayer, _NNB1DStackedLayer):
                WC = np.ones((nNeurons, nNeuronsNext))
                if self.containsBias():
                    bC = np.ones((nNeuronsNext, ))
            else:
                WC = np.zeros((nNeurons, nNeuronsNext))
                if self.containsBias():
                    bC = np.zeros((nNeuronsNext,))
                jj = 0
                neuronFrom = self.neurons[0]
                for j, neuronTo in enumerate(self.nextLayer.neurons):
                    if j == self.nextLayer.biasIdx:
                        continue
                    if neuronTo in neuronFrom.connectionsTo:
                        WC[:, jj] = np.ones_like(WC[:, jj])
                        if self.containsBias():
                            bC[jj] = 1
                        jj += 1
        return WC, bC

    def getParams(self):
        b = None
        if isinstance(self.nextLayer, _NNBLossFuncBlock):
            W = None
        else:
            if isinstance(self.nextLayer, _NNB1DStackedLayer):
                if self.containsBias():
                    W = self.neurons[0].connectionsTo[self.nextLayer.neurons[0]].weight[:-1, :]
                    b = W[-1, :]
                else:
                    W = self.neurons[0].connectionsTo[self.nextLayer.neurons[0]].weight
            else:
                nNeurons = self.numOfNeurons() - (1 if self.containsBias() else 0)
                nNeuronsNext = self.nextLayer.numOfNeurons() - (1 if self.nextLayer.containsBias() else 0)
                W = np.zeros((nNeurons, nNeuronsNext))
                if self.containsBias():
                    b = np.zeros((nNeuronsNext,))
                jj = 0
                neuronFrom = self.neurons[0]
                for j, neuronTo in enumerate(self.nextLayer.neurons):
                    if j == self.nextLayer.biasIdx:
                        continue
                    if neuronTo in neuronFrom.connectionsTo:
                        if self.containsBias():
                            W[:, jj] = neuronFrom.connectionsTo[neuronTo].weight[:-1]
                            b[jj] = neuronFrom.connectionsTo[neuronTo].weight[-1]
                        else:
                            W[:, jj] = neuronFrom.connectionsTo[neuronTo].weight
                        jj += 1
        return W, b

    def updateParams(self, layerParam):
        if isinstance(self.nextLayer, _NNBLossFuncBlock):
            return
        W_ = layerParam[0]
        b_ = None
        if len(layerParam) == 2:
            b_ = layerParam[1]
        if isinstance(self.nextLayer, _NNB1DStackedLayer):
            if self.containsBias():
                self.neurons[0].connectionsTo[self.nextLayer.neurons[0]].weight[:-1, :] = W_
                self.neurons[0].connectionsTo[self.nextLayer.neurons[0]].weight[-1, :] = b_
            else:
                self.neurons[0].connectionsTo[self.nextLayer.neurons[0]] = W_
        else:
            jj = 0
            neuronFrom = self.neurons[0]
            for j, neuronTo in enumerate(self.nextLayer.neurons):
                if j == self.nextLayer.biasIdx:
                    continue
                if self.containsBias():
                    neuronFrom.connectionsTo[neuronTo].weight[:-1] = W_[:, jj]
                    neuronFrom.connectionsTo[neuronTo].weight[-1] = b_[jj]
                else:
                    neuronFrom.connectionsTo[neuronTo].weight = W_[:, jj]
                    jj += 1


class _NNB2DConvLayer(_NNBTrainableLayer):
    def __init__(self, name, kernelSize=(3, 3), padding=0, stride=1):
        _NNBTrainableLayer.__init__(self, name, 2, (-1, -1), (-1, -1))

        # model parameters
        self.kernelSize = kernelSize
        self.padding = padding
        self.stride = stride

    def deduceOutputSize(self):
        # only available when the input size is confirmed
        if isinstance(self.nextLayer, _NNB2DFlattenLayer):
            self.outputSize = self.inputSize[0] * self.inputSize[1] * self.numOfNeurons()
        else:
            self.outputSize = ((self.inputSize[0] + self.padding - self.kernelSize[0]) / (self.stride + 1),
                               (self.inputSize[1] + self.padding - self.kernelSize[1]) / (self.stride + 1))
            self.nextLayer.inputSize = self.outputSize

        # TO-DO: deal with negative size

    def getConnectivity(self):
        WC = np.zeros((self.numOfNeurons() - (1 if self.containsBias() else 0),
                       self.nextLayer.numOfNeurons() - (1 if self.nextLayer.containsBias() else 0)))
        bC = None
        ii = 0
        nNeurons = self.nextLayer.numOfNeurons() - (1 if self.nextLayer.containsBias() else 0)
        for i, neuronFrom in enumerate(self.neurons):
            if i == self.biasIdx:
                bC = np.zeros((nNeurons,))
                jj = 0
                for j, neuronTo in enumerate(self.nextLayer.neurons):
                    if j == self.nextLayer.biasIdx:
                        continue
                    if neuronTo in neuronFrom.connectionsTo:
                        bC[jj] = 1
                    jj += 1
            else:
                jj = 0
                for j, neuronTo in enumerate(self.nextLayer.neurons):
                    if j == self.nextLayer.biasIdx:
                        continue
                    if neuronTo in neuronFrom.connectionsTo:
                        WC[ii, jj] = 1
                    jj += 1
                ii += 1
        return WC, bC

    def getParams(self):
        # in the form of (K, K, N, C)
        W = np.zeros((*self.kernelSize,
                      self.numOfNeurons() - (1 if self.containsBias() else 0),
                      self.nextLayer.numOfNeurons() - (1 if self.nextLayer.containsBias() else 0)
                      ))
        b = None
        ii = 0
        for i, neuronFrom in enumerate(self.neurons):
            if i == self.biasIdx:
                b = np.zeros((*self.kernelSize,
                              self.nextLayer.numOfNeurons() - (1 if self.nextLayer.containsBias() else 0)
                              ))
                jj = 0
                for j, neuronTo in enumerate(self.nextLayer.neurons):
                    if j == self.nextLayer.biasIdx:
                        continue
                    if neuronTo in neuronFrom.connectionsTo:
                        b[:, :, jj] = neuronFrom.connectionsTo[neuronTo].weight
                    jj += 1
            else:
                jj = 0
                for j, neuronTo in enumerate(self.nextLayer.neurons):
                    if j == self.nextLayer.biasIdx:
                        continue
                    if neuronTo in neuronFrom.connectionsTo:
                        W[:, :, ii, jj] = neuronFrom.connectionsTo[neuronTo].weight
                    jj += 1
                ii += 1
        return W, b

    def updateParams(self, layerParam):
        # in the form of (K, K, N, C)
        W_ = layerParam[0]
        b_ = None
        if len(layerParam) == 2:
            b_ = layerParam[1]
        ii = 0
        for i, neuronFrom in enumerate(self.neurons):
            if i == self.biasIdx:
                jj = 0
                for j, neuronTo in enumerate(self.nextLayer.neurons):
                    if j == self.nextLayer.biasIdx:
                        continue
                    if neuronTo in neuronFrom.connectionsTo:
                        neuronFrom.connectionsTo[neuronTo].weight = b_[:, :, jj]
                    jj += 1
            else:
                jj = 0
                for j, neuronTo in enumerate(self.nextLayer.neurons):
                    if j == self.nextLayer.biasIdx:
                        continue
                    if neuronTo in neuronFrom.connectionsTo:
                        neuronFrom.connectionsTo[neuronTo].weight = W_[:, :, ii, jj]
                    jj += 1
                ii += 1

    def getConvParams(self):
        return {
            "filter_size": self.kernelSize,
            "pad": self.padding,
            "stride": self.stride
        }

    def addNeuron(self, neuron):
        super().addNeuron(neuron)
        if isinstance(neuron, _NNB2DBiasNeuron):
            self.biasIdx = len(self.neurons) - 1

    def removeNeuron(self, neuron):
        super().removeNeuron(neuron)
        if isinstance(neuron, _NNB2DBiasNeuron):
            self.biasIdx = -1


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
    def __init__(self, name, blockFrom, blockTo):
        _NNBConnection.__init__(self, name, blockFrom, blockTo)

        # model parameters
        self.weight = 0.0
        self.initializeWeight()

    def remove(self):
        self.removeWithoutCheckingConnectivity()
        # special case: when this connection is the only one within two layers, cancel their linking relation
        if not NNBController.checkConnectivityLayerLayer(self.blockFrom.layer, self.blockTo.layer):
            self.blockFrom.layer.nextLayer = None
            self.blockTo.layer.prevLayer = None

    def initializeWeight(self, initMethod="zero"):
        self.weight = np.random.normal()

    def setWeight(self, weight):
        self.weight = weight


class _NNB1DLinearConnection(_NNBTrainableConnection):
    def __init__(self, name, blockFrom, blockTo):
        _NNBTrainableConnection.__init__(self, name, blockFrom, blockTo)


class _NNB1DStackedLinConnection(_NNBTrainableConnection):
    def __init__(self, name, blockFrom, blockTo):
        _NNBTrainableConnection.__init__(self, name, blockFrom, blockTo)

    def initializeWeight(self, initializeMethod="zero"):
        numNeuronsFrom = self.blockFrom.layer.numOfNeurons() if isinstance(self.blockFrom, _NNB1DStackedNeuron) else 1
        numNeuronsTo = self.blockTo.layer.numOfNeurons() if isinstance(self.blockFrom, _NNB1DStackedNeuron) else 1

        if numNeuronsFrom == -1 or numNeuronsTo == -1:
            self.weight = None
            return

        # TO-DO
        if initializeMethod == "zero":
            self.weight = np.zeros((numNeuronsFrom, numNeuronsTo))
        elif initializeMethod == "normal":
            self.weight = np.random.normal((numNeuronsFrom, numNeuronsTo))


class _NNB2DConvConnection(_NNBTrainableConnection):
    # lazy evaluation is applied for the weight
    def __init__(self, name, blockFrom, blockTo):
        _NNBTrainableConnection.__init__(self, name, blockFrom, blockTo)
        self.initializeWeight()

    # TO-DO
    def initializeWeight(self, initializeMethod=DEFAULT_INIT_METHOD):
        if initializeMethod == "zero":
            self.weight = np.zeros(self.blockFrom.layer.kernelSize)
        elif initializeMethod == "normal":
            self.weight = np.random.normal(self.blockFrom.layer.kernelSize)


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
        if not NNBController.checkConnectivityNeuronLFB(self.blockFrom, self.blockTo):
            self.blockFrom.nextLayer = None


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
        self.lossFunc = "MSE"  # MAE, MSE, CE

    def removeWithoutCheckingConnectivity(self):
        for neuron in self.connectionsFrom.keys():
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
        self.regType = "L2"  # L1, L2, L0.5, L3, Lp, Elastic Net
        self.C = 1.0
        self.p = 2  # used in Lp
        self.C2 = 0.0  # used in Elastic Net

    def removeWithoutCheckingConnectivity(self):
        for lfbTo in self.connectionsTo.keys():
            if self in lfbTo.connectionsFrom:
                del lfbTo.connectionsFrom[self]

    def connectToLFB(self, lfbTo):
        pass

    def getConfigs(self):
        if self.regType == "Elastic Net":
            return {
                "regType": self.regType,
                "C1": self.C,
                "C2": self.C2
            }
        elif self.regType == "Lp":
            return {
                "regType": self.regType,
                "C": self.C,
                "p": self.p
            }
        else:
            return {
                "regType": self.regType,
                "C": self.C,
            }


class NNBController:
    # rule of connections, ...
    @classmethod
    def checkConnectableBlockBlock(cls, blockFrom, blockTo):
        if isinstance(blockFrom, _NNBLayer):
            return cls.checkConnectableLayerBlock(blockFrom, blockTo)
        elif isinstance(blockFrom, _NNBNeuron):
            val = cls.checkConnectableLayerBlock(blockFrom.layer, blockTo)
            if not val:
                return False
            if isinstance(blockTo, _NNB1DBiasNeuron) or isinstance(blockTo, _NNB2DBiasNeuron):
                print("connection rejected: you can't connect to a bias.")
                return False
            return True
        elif isinstance(blockFrom, _NNBLossFuncBlock):
            print("connection rejected: you can't start linking from a loss function block.")
            return False
        elif isinstance(blockFrom, _NNBRegularizer):
            if isinstance(blockTo, _NNBTrainableLayer):
                print("connection rejected: wrong direction.")
                return False
            elif isinstance(blockTo, _NNBLossFuncBlock):
                return True
            else:
                print("connection rejected: you can't connect a regularizer to {}".format(blockTo.name))
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
            if layerFrom.numOfNeurons() == 0:
                print("connection rejected: \"{}\" doesn't have any neuron or bias.".format(layerFrom.name))
            elif layerFrom.numOfNeurons(includeBias=False) == 0:
                if layerFrom.containsBias():
                    print("connection rejected: \"{}\" doesn't have any neuron.".format(layerTo.name))
                    return False
                else:
                    print("connection rejected: \"{}\" only has a bias.".format(layerTo.name))
                return False
        return True

    @classmethod
    def checkConnectableBlockLFB(cls, blockFrom, lfbTo):
        if isinstance(blockFrom, _NNBTrainableLayer):
            if blockFrom.dim != 1:
                print("connection rejected: only a 1D layer can be reduced to a scalar loss value.")
                return False
            if blockFrom.nextLayer and blockFrom.nextLayer != lfbTo:
                print("connection rejected: the loss function block has already been connected to the other layer.")
                return False
            if blockFrom.containsBias():
                print("connection rejected: you can't connect a layer with a bias to the loss function block.")
                return False
            return True
        elif isinstance(blockFrom, _NNBNeuron):
            return cls.checkConnectableBlockLFB(blockFrom.layer, lfbTo)
        else:
            print("connection rejected: only a 1D layer or a neuron can connect to a loss function block")
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
            return False
        else:
            print("connection rejected: only a layer or a neuron can connect to a regularizer")
            return False
        return True

    @classmethod
    def checkConnectivityLayerLayer(cls, layerFrom, layerTo):
        connected = False
        for neuronFrom in layerFrom.neurons:
            for neuronTo in neuronFrom.connectionsTo.keys():
                if neuronTo.layer == layerTo:
                    connected = True
                    break
                if connected:
                    break
        return connected

    @classmethod
    def checkConnectivityNeuronLFB(cls, neuronFrom, LBFTo):
        connected = False
        for neuronFrom in neuronFrom.layer.neurons:
            for blockTo in neuronFrom.connectionsTo.keys():
                if blockTo == LBFTo:
                    connected = True
                    break
                if connected:
                    break
        return connected
