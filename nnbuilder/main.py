import sys
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView
from scene import NNBScene
from icon import NNB1DNeuronIcon, NNB2DNeuronIcon, NNBAffineLayerIcon, NNBConvLayerIcon, NNBLostFuncBlock, \
    NNBRegularizerIcon, NNBPoolingLayerIcon, NNBFlattenLayerIcon, \
    NNB1DBiasNeuronIcon, NNB2DBiasNeuronIcon, NNBStacked1DAffLayerIcon

# nLayers = 6
# for i in range(nLayers):
#     layer = NNBLayer(10 + (2 * NEURON_RADIUS + LAYER_WIDTH) * i,
#                      2, LAYER_WIDTH, LAYER_HEIGHT)
#     neuron1 = NNBNeuron(12 + (2 * NEURON_RADIUS + LAYER_WIDTH) * i,
#                         2 + 2 * NEURON_RADIUS, 2 * NEURON_RADIUS, 2 * NEURON_RADIUS)
#     neuron2 = NNBNeuron(12 + (2 * NEURON_RADIUS + LAYER_WIDTH) * i,
#                         2 + 4 * NEURON_RADIUS, 2 * NEURON_RADIUS, 2 * NEURON_RADIUS)
#     neuron3 = NNBNeuron(12 + (2 * NEURON_RADIUS + LAYER_WIDTH) * i,
#                         2 + 6 * NEURON_RADIUS, 2 * NEURON_RADIUS, 2 * NEURON_RADIUS)
#     neuron3.isBias = True
#     layer.addNeuron(neuron1)
#     layer.addNeuron(neuron2)
#     layer.addNeuron(neuron3)
#     scene.addItem(layer)
#     if i == 0:
#         layer.setLayerType("input")
#     elif i == nLayers - 1:
#         layer.setLayerType("output")
#
# loss = NNBCostFuncBlock(300, 300, CFB_WIDTH, CFB_HEIGHT)
# regularizer = NNBRegularizer(350, 200, CFB_WIDTH, CFB_HEIGHT)
# scene.addItem(loss)
# scene.addItem(regularizer)
# window.setCentralWidget(view)
# window.setAttribute(Qt.WA_TranslucentBackground)
# window.show()
# sys.exit(app.exec_())
app = QApplication(sys.argv)
QApplication.setStartDragDistance(1)
window = QMainWindow()
window.setGeometry(100, 100, 800, 600)

view = QGraphicsView()
view.setMouseTracking(True)
view.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing)
scene = NNBScene()
scene.setSceneRect(0, 0, 800, 600)
view.setScene(scene)
neuron1DIcon = NNB1DNeuronIcon(10, 20)
neuron1DBiasIcon = NNB1DBiasNeuronIcon(45, 20)

neuron2DIcon = NNB2DNeuronIcon(10, 60)
neuron2DBiasIcon = NNB2DBiasNeuronIcon(45, 60)

affineLayerIcon = NNBAffineLayerIcon(10, 90)
stackedAffineLayerIcon = NNBStacked1DAffLayerIcon(40, 90)
convLayerIcon = NNBConvLayerIcon(10, 170)

poolingLayerIcon = NNBPoolingLayerIcon(10, 250)
flattenLayerIcon = NNBFlattenLayerIcon(40, 250)

CFBIcon = NNBLostFuncBlock(10, 330)
regularizerIcon = NNBRegularizerIcon(50, 330)


scene.addItem(neuron1DIcon)
scene.addItem(neuron1DBiasIcon)
scene.addItem(neuron2DIcon)
scene.addItem(neuron2DBiasIcon)
scene.addItem(affineLayerIcon)
scene.addItem(stackedAffineLayerIcon)
scene.addItem(convLayerIcon)
scene.addItem(poolingLayerIcon)
scene.addItem(flattenLayerIcon)
scene.addItem(CFBIcon)
scene.addItem(regularizerIcon)

view.show()
sys.exit(app.exec_())
