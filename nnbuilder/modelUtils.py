import tensorflow as tf
from tensorflow.keras import backend as K
from tensorflow.keras import layers, losses, optimizers, regularizers, metrics


class Sparse(layers.Dense):
    def __init__(self, units, WC, bC, **kwargs):
        self.WC = WC
        self.bC = bC
        super().__init__(units, **kwargs)

    def call(self, inputs):
        output = K.dot(inputs, self.kernel * self.WC)
        if self.use_bias:
            output = K.bias_add(output, self.bias * self.bC)
        if self.activation is not None:
            output = self.activation(output)
        return output


class SparseConv2D(layers.Conv2D):
    def __init__(self, units, WC, bC, **kwargs):
        self.WC = WC
        self.bC = bC
        super().__init__(units, **kwargs)

    def call(self, inputs):
        outputs = K.conv2d(
            inputs,
            self.kernel * self.WC,
            strides=self.strides,
            padding=self.padding,
            data_format=self.data_format,
            dilation_rate=self.dilation_rate)

        if self.use_bias:
            outputs = K.bias_add(
                outputs,
                self.bias * self.bC,
                data_format=self.data_format)

        if self.activation is not None:
            return self.activation(outputs)
        return outputs


@tf.keras.utils.register_keras_serializable(package='Custom', name='l3')
class L3(regularizers.Regularizer):
    def __init__(self, l3=0.01):
        self.l3 = l3

    def __call__(self, x):
        return self.l3 * K.mean(K.pow(x, 3))

    def get_config(self):
        return {'l3': float(self.l3)}


@tf.keras.utils.register_keras_serializable(package='Custom', name='lp')
class Lp(regularizers.Regularizer):
    def __init__(self, lp=0.01, p=2):
        self.lp = lp
        self.p = p

    def __call__(self, x):
        return self.lp * K.mean(K.pow(x, self.p))

    def get_config(self):
        return {'lp': float(self.lp), 'p': float(self.p)}


@tf.keras.utils.register_keras_serializable(package='Custom', name='l0_5')
class L0_5(regularizers.Regularizer):
    def __init__(self, l0_5=0.0):
        self.l0_5 = l0_5

    def __call__(self, x):
        return self.l0_5 * K.mean(K.sqrt(x))

    def get_config(self):
        return {'l0_5': float(self.l0_5)}


def sine(x):
    return K.sin(x)


def gaussian(x):
    return K.exp(-K.square(x))


# Ref: https://www.tensorflow.org/api_docs/python/tf/keras/activations
kerasActFuncDict = {
    "linear": layers.Activation('linear'),
    "sigmoid": layers.Activation('sigmoid'),
    "softmax": layers.Activation('softmax'),
    "tanh": layers.Activation('tanh'),
    "softplus": layers.Activation('softplus'),
    "relu": layers.Activation('relu'),
    "elu": layers.Activation('elu'),
    "leaky relu": layers.LeakyReLU,
    "gaussian": layers.Activation(gaussian),
    "sine": layers.Activation(sine),
    None: layers.Activation('linear')
}

# Ref: https://www.tensorflow.org/api_docs/python/tf/keras/losses
kerasLossFuncDict = {
    "MSE": losses.MeanSquaredError(),
    "MAE": losses.MeanAbsoluteError(),
    "CE": losses.SparseCategoricalCrossentropy()
}

# Ref: https://www.tensorflow.org/api_docs/python/tf/keras/metrics
kerasMetricsFuncDict = {
    'AUC': metrics.AUC(),
    'accuracy': metrics.SparseCategoricalAccuracy(),
    'precision': metrics.Precision(),
    'recall': metrics.Recall(),
}


class NNBTransformer:
    @staticmethod
    # Ref: https://www.tensorflow.org/api_docs/python/tf/keras/regularizers
    def transferToKerasRegularizer(regularizerConfigs):
        regularizer = None
        regType = regularizerConfigs['regType']
        if regType == 'L1':
            C = regularizerConfigs.get('C', 0.01)
            regularizer = regularizers.L1(l1=C)
        elif regType == 'L2':
            C = regularizerConfigs.get('C', 0.01)
            regularizer = regularizers.L2(l2=C)
        elif regType == 'L3':
            C = regularizerConfigs.get('C', 0.01)
            regularizer = L3(l3=C)
        elif regType == 'Lp':
            C = regularizerConfigs.get('C', 0.01)
            p = regularizerConfigs.get('p', 2)
            regularizer = Lp(lp=C, p=p)
        elif regType == 'Elastic Net':
            C1 = regularizerConfigs.get('C1', 0.005)
            C2 = regularizerConfigs.get('C2', 0.005)
            regularizer = regularizers.L1L2(l1=C1, l2=C2)
        return regularizer

    @staticmethod
    def transferToKerasOptimizer(optimizerConfigs):
        optimizer = None
        optimizerType = optimizerConfigs['optimizerType']
        if optimizerType == 'sgd':
            learningRate = optimizerConfigs.get('learningRate', 1e-2)
            optimizer = optimizers.SGD(learning_rate=learningRate)
        elif optimizerType == 'momentum':
            learningRate = optimizerConfigs.get('learningRate', 1e-2)
            momentum = optimizerConfigs.get('momentum', 0.9)
            optimizer = optimizers.SGD(learning_rate=learningRate,
                                       momentum=momentum)
        elif optimizerType == 'rmsprop':
            learningRate = optimizerConfigs.get('learningRate', 1e-3)
            rho = optimizerConfigs.get('decayRate', 0.9)
            momentum = optimizerConfigs.get('momentum', 0.0)
            epsilon = optimizerConfigs.get('epsilon', 1e-7)
            optimizer = optimizers.RMSprop(learning_rate=learningRate,
                                           rho=rho,
                                           momentum=momentum,
                                           epsilon=epsilon)
        elif optimizerType == 'adagrad':
            learningRate = optimizerConfigs.get('learningRate', 1e-3)
            epsilon = optimizerConfigs.get('epsilon', 1e-7)
            optimizer = optimizers.Adagrad(learning_rate=learningRate,
                                           epsilon=epsilon)
        elif optimizerType == 'adadelta':
            learningRate = optimizerConfigs.get('learningRate', 1e-3)
            rho = optimizerConfigs.get('decayRate', 0.95)
            epsilon = optimizerConfigs.get('epsilon', 1e-7)
            optimizer = optimizers.Adadelta(learning_rate=learningRate,
                                            rho=rho,
                                            epsilon=epsilon)
        elif optimizerType == 'adam':
            learningRate = optimizerConfigs.get('learningRate', 1e-3)
            beta1 = optimizerConfigs.get('beta1', 0.9)
            beta2 = optimizerConfigs.get('beta2', 0.999)
            epsilon = optimizerConfigs.get('epsilon', 1e-7)
            optimizer = optimizers.Adadelta(learning_rate=learningRate,
                                            beta_1=beta1,
                                            beta_2=beta2,
                                            epsilon=epsilon)
        return optimizer

    @staticmethod
    def transferToKerasModel(modelConfigs, optimizerConfigs, metricsType):
        inputSize = modelConfigs['inputSize']
        lossFunc = kerasLossFuncDict[modelConfigs['lossFunc']]
        inputLayerX = tf.keras.Input(shape=inputSize)
        prevLayerA = inputLayerX

        for layerConfig in modelConfigs['layers'][:-1]:
            if layerConfig['layerType'] == 'flattenLayer':
                layerA = layers.Flatten()(prevLayerA)
            else:
                actFuncLayer = kerasActFuncDict[layerConfig['actFunc']]
                size = layerConfig['size']
                W = layerConfig['W']
                b = layerConfig['b']
                WC = layerConfig['WC']
                bC = layerConfig['bC']
                regConfigs = layerConfig['regConfigs']
                use_bias = b is not None
                if layerConfig['layerType'] == '1DLayer':
                    if regConfigs:
                        regularizer = NNBTransformer.transferToKerasRegularizer(regConfigs)
                        layer = Sparse(size, WC, bC, use_bias=use_bias, kernel_regularizer=regularizer)
                    else:
                        layer = Sparse(size, WC, bC, use_bias=use_bias)
                else:  # 2DLayer
                    if regConfigs:
                        regularizer = NNBTransformer.transferToKerasRegularizer(regConfigs)
                        layer = SparseConv2D(size, WC, bC, use_bias=use_bias, kernel_regularizer=regularizer)
                    else:
                        layer = SparseConv2D(size, WC, bC, use_bias=use_bias)
                layerZ = layer(prevLayerA)
                layerA = actFuncLayer(layerZ)
                if b is not None:
                    layer.set_weights([W, b])
                else:
                    layer.set_weights([W])
            prevLayerA = layerA

        model = tf.keras.Model(inputs=inputLayerX, outputs=prevLayerA)
        optimizer = NNBTransformer.transferToKerasOptimizer(optimizerConfigs)
        metrics_ = kerasMetricsFuncDict[metricsType]
        model.compile(optimizer=optimizer, loss=lossFunc, metrics=[metrics_])
        return model

    @staticmethod
    def getParamsFromKerasModel(kerasModel):
        layerParams = []
        for layer in kerasModel.layers[1:]:
            if layer.get_weights():
                layerParams.append(layer.get_weights())
        return layerParams, outputs
