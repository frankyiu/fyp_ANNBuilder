#
#
# class NNBMetadata:
#     componentDefaultNameDict = {
#         _NNB1DInputNeuron: NEURON_1D_DEFAULT_NAME,
#         _NNB1DBiasNeuron: NEURON_1D_BIAS_DEFAULT_NAME,
#         _NNB2DInputNeuron: NEURON_2D_DEFAULT_NAME,
#         _NNB2DBiasNeuron: NEURON_2D_BIAS_DEFAULT_NAME,
#         _NNB1DAffineLayer: AFFINE_1D_LAYER_DEFAULT_NAME,
#         _NNB2DConvLayer: CONV_2D_LAYER_DEFAULT_NAME,
#         _NNB2DPoolingLayer: POOLING_2D_LAYER_DEFAULT_NAME,
#         _NNB2DFlattenLayer: FLATTEN_2D_LAYER_DEFAULT_NAME,
#         _NNBLossFuncBlock: LFB_DEFAULT_NAME,
#         _NNBRegularizer: REGULARIZER_DEFAULT_NAME,
#         _NNB1DLinearConnection: LINEAR_1D_CONNECTION_DEFAULT_NAME,
#         _NNB2DConvConnection: CONV_2D_CONNECTION_DEFAULT_NAME,
#         _NNB2DPoolingConnection: POOLING_2D_CONNECTION_DEFAULT_NAME,
#         _NNB2DFlattenConnection: FLATTEN_2D_CONNECTION_DEFAULT_NAME,
#         _NNBLFBConnection: LFB_CONNECTION_DEFAULT_NAME,
#         _NNBRegConnection: REG_CONNECTION_DEFAULT_NAME
#     }
#
#     componentDefaultNameRegexDict = {
#         _NNB1DInputNeuron: NEURON_1D_DEFAULT_NAME_REGEX,
#         _NNB1DBiasNeuron: NEURON_1D_BIAS_DEFAULT_NAME_REGEX,
#         _NNB2DNeuron: NEURON_2D_DEFAULT_NAME_REGEX,
#         _NNB2DBiasNeuron: NEURON_2D_BIAS_DEFAULT_NAME_REGEX,
#         _NNB1DAffineLayer: AFFINE_1D_LAYER_DEFAULT_NAME_REGEX,
#         _NNB2DConvLayer: CONV_2D_LAYER_DEFAULT_NAME_REGEX,
#         _NNB2DPoolingLayer: POOLING_2D_LAYER_DEFAULT_NAME_REGEX,
#         _NNB2DFlattenLayer: FLATTEN_2D_LAYER_DEFAULT_NAME_REGEX,
#         _NNBLossFuncBlock: LFB_DEFAULT_NAME_REGEX,
#         _NNBRegularizer: REGULARIZER_DEFAULT_NAME_REGEX,
#     }
#
# class NNBEnv:
#     def __init__(self):
#         self.env = {}  # environment of the builder
#
#     def registerComponent(self, component):
#         # this register the component into the environment
#         if type(component) not in self.env:
#             self.env[type(component)] = {}
#         self.env[type(component)][component] = component.name
#
#     def findNextDefaultName(self, componentType, componentDefaultName = None):
#         if componentDefaultName is None:
#             componentDefaultName = NNBMetadata.componentDefaultNameDict[componentType]
#         if componentType not in self.env:
#             proposedDefaultName = componentDefaultName.format(1)
#         else:
#             i = 1
#             while True:
#                 proposedDefaultName = componentDefaultName.format(i)
#                 if proposedDefaultName not in self.env[componentType].values():
#                     break
#                 i += 1
#         return proposedDefaultName
#
#     def addComponent(self, component):
#         self.registerComponent(component)  # register the component to the environment
#         print(component + " is created.")
#
#     def createNeuron(self, x, y, neuronType, layer):
#         layerName = layer.name
#         res = re.findall(NNBMetadata.componentDefaultNameRegexDict[type(layer)], layerName)
#         if res:
#             layerName = res[0]
#         neuronName = NNBMetadata.componentDefaultNameDict[neuronType].format(layerName, "{}")
#         neuronName = self.findNextDefaultName(neuronType, neuronName)
#         neuron = neuronType(neuronName, x, y)
#         layer.addNeuron(neuron)
#         self.addComponent(neuron)
#
#     def createLayer(self, x, y, layerType):
#         layerName = self.findNextDefaultName(layerType)
#         layer = layerType(layerName, x, y)
#         self.addComponent(layer)
#
#     def createLossFuncBlock(self, x, y):
#         itemName = self.findNextDefaultName(NNBLossFuncBlock)
#         lossFuncBlock = NNBLossFuncBlock(itemName, x, y)
#         self.addComponent(lossFuncBlock)
#
#     def createRegularizer(self, x, y):
#         itemName = self.findNextDefaultName(NNBRegularizer)
#         regularizer = NNBRegularizer(itemName, x, y)
#         self.addComponent(regularizer)
#
#     def createConnectionLine(self, blockFrom, blockTo, connectionType, connectToFunc):
#         # name the connection
#         blockFromName = blockFrom.name
#         res = re.findall(blockFrom.defaultNameRegex, blockFromName)
#         if res:
#             blockFromName = res[0]
#         blockToName = blockTo.name
#         res = re.findall(blockTo.defaultNameRegex, blockToName)
#         if res:
#             blockToName = res[0]
#         connectionName = NNBMetadata.componentDefaultNameDict[connectionType].format(blockFromName, blockToName)
#         connectToFunc()
#         connection = connectionType(connectionName, blockFrom, blockTo)
#         self.addComponent(connection)
#
#
