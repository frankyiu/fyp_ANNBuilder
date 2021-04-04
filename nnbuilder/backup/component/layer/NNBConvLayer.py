from PyQt5.QtWidgets import QGraphicsItem
from NNBResizableLayer import NNBResizableLayer


class NNBConvLayer(NNBResizableLayer):
    def __init__(self, name, x, y):
        NNBResizableLayer.__init__(self, name, x, y)
        self.featureMapWidth = -1
        self.featureMapHeight = -1
        self.kernelWidth = 3
        self.kernelHeight = 3

    # def createForm(self, window):
    #     return NNBConvLayerForm(self, window)

    def addNeuron(self, neuron):
        neuron.layer = self
        neuron.setParentItem(self)
        self.neurons.append(neuron)
        if self.form:
            self.form.update()

    def _removeNeuron(self, neuron):
        self.neurons.remove(neuron)
        if self.form:
            self.form.update()

    def _connectLayer(self, layer):
        if layer not in self.adjBlocks:
            self.adjBlocks.append(layer)

    def _connectCFB(self, costFuncBlock):
        if costFuncBlock not in self.adjBlocks:
            self.adjBlocks.append(costFuncBlock)

    def _connectReg(self, reg):
        if reg not in self.regs:
            self.regs.append(reg)

    def _remove(self):
        for neuron in self.neurons:
            neuron._removeWithoutCheckConnectivity()
        for adjBlock in self.adjBlocks:
            adjBlock.adjBlocks.remove(self)
        self.neurons = []

    def itemChange(self, change, value):
        if change == QGraphicsItem.ItemPositionChange:
            for neuron in self.neurons:
                for connection in neuron.connections.values():
                    connection.updateConnectionPos()
            for reg in self.regs:
                for connection in reg.connections.values():
                    connection.updateConnectionPos()
        return super().itemChange(change, value)





