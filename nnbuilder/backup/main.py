import sys
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsView
from NNBScene import NNBScene
from config import *
from NNBIcon import NNB1DNeuronIcon, NNB2DNeuronIcon, NNBAffineLayerIcon, NNBConvLayerIcon, NNBCostFuncBlock, \
    NNBRegularizerIcon


# app = QApplication(sys.argv)
# QApplication.setStartDragDistance(1)
# window = QMainWindow()
# window.setGeometry(100, 100, 800, 600)
#
# view = QGraphicsView()
# view.setMouseTracking(True)
# view.setRenderHints(QPainter.Antialiasing | QPainter.HighQualityAntialiasing)
# scene = NNBScene()
# scene.setSceneRect(0, 0, 800, 600)
# view.setScene(scene)
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
neuron2DIcon = NNB2DNeuronIcon(45, 20)
affineLayerIcon = NNBAffineLayerIcon(10, 60)
convLayerIcon = NNBConvLayerIcon(40, 60)
CFBIcon = NNBCostFuncBlock(10, 150)
regularizerIcon = NNBRegularizerIcon(10, 210)


scene.addItem(neuron1DIcon)
scene.addItem(neuron2DIcon)
scene.addItem(affineLayerIcon)
scene.addItem(convLayerIcon)
scene.addItem(CFBIcon)
scene.addItem(regularizerIcon)
view.show()
sys.exit(app.exec_())