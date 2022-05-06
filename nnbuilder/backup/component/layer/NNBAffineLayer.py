from PyQt5.QtWidgets import QGraphicsItem
from NNBResizableLayer import NNBResizableLayer
from NNBForm import NNBAffineLayerForm

class NNBAffineLayer(NNBResizableLayer):
    def __init__(self, name, x, y):
        NNBResizableLayer.__init__(self, name, x, y)

    def createForm(self, window):
        return NNBAffineLayerForm(self, window)

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

    # def paint(self, painter, option, widget = None):
    #     if self.isSelected() or self.hoveredOnConnectMode:
    #         painter.setBrush(NNB_FOCUS_BRUSH)
    #         painter.setPen(NNB_FOCUS_PEN)
    #         painter.drawRoundedRect(self.rect(), LAYER_CORNER_RADIUS, LAYER_CORNER_RADIUS)
    #     painter.setPen(NNB_PEN)
    #     if self.layerType == "hidden":
    #         painter.setBrush(QBrush(QColor(128, 128, 128, 128)))
    #         # painter.setBrush(NNB_BRUSH)
    #     elif self.layerType == "input":
    #         # painter.setPen(QPen(Qt.yellow, PEN_WIDTH + 2 * FOCUS_OFFSET, Qt.SolidLine))
    #         painter.setBrush(QBrush(QColor(255, 229, 204, 128)))
    #     else:  # "output" layertype
    #         painter.setBrush(QBrush(QColor(56, 229, 166, 128)))
    #     painter.drawRoundedRect(self.rect(), LAYER_CORNER_RADIUS, LAYER_CORNER_RADIUS)

    # def setLayerType(self, layerType = "hidden"):
    #     if self.scene().sceneMode != SceneMode.SelectMode:
    #         return
    #     if self.layerType == layerType:
    #         return
    #     # we only allow one input and output layer in the scene.
    #     # when there is two adj. layers, can't set to "input" or "output"
    #     if self.layerType == "output":
    #         for adjBlock in self.adjBlocks:
    #             if isinstance(adjBlock, NNBCostFuncBlock):
    #                 # already connected to a loss function block, can't switch into any other type
    #                 return
    #     if layerType == "input":
    #         if self.scene().inputLayer or len(self.adjBlocks) == 2:
    #             return
    #         self.scene().inputLayer = self
    #     elif layerType == "output":
    #         if self.scene().outputLayer or len(self.adjBlocks) == 2:
    #             return
    #         self.scene().outputLayer = self
    #
    #     # on succeeded in changinging the layer type
    #     if self.layerType == "input":
    #         self.scene().inputLayer = None
    #     elif self.layerType == "output":
    #         self.scene().outputLayer = None
    #     self.layerType = layerType
    #     self.update()

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

def main():
    import sys
    from PyQt5.QtGui import QPainter
    from PyQt5.QtWidgets import QApplication, QGraphicsView, QGraphicsScene
    from config import SCENE_DEFAULT_WIDTH, SCENE_DEFAULT_HEIGHT

    app = QApplication(sys.argv)
    QApplication.setStartDragDistance(1)
    view = QGraphicsView()
    view.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing)
    scene = QGraphicsScene()

    scene.setSceneRect(0, 0, SCENE_DEFAULT_WIDTH, SCENE_DEFAULT_HEIGHT)
    view.setScene(scene)

    layer = NNBAffineLayer("Affine 1D Vec. Layer-1", 12, 20)
    scene.addItem(layer)
    view.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()



