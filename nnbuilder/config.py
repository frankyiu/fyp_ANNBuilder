from PyQt5.QtGui import QPen, QBrush, QColor
from PyQt5.QtCore import Qt
import math
import os

##################
WINDOW_DEFAULT_WIDTH = 800
WINDOW_DEFAULT_HEIGHT = 600
SCENE_DEFAULT_WIDTH = 800
SCENE_DEFAULT_HEIGHT = 600

##################
PEN_WIDTH = 1.0
FOCUS_OFFSET = 1.5
NNB_PEN = QPen(Qt.black, PEN_WIDTH, Qt.SolidLine)
NNB_BRUSH = QBrush(QColor(255, 255, 255, 0))
NNB_FOCUS_PEN = QPen(Qt.gray, PEN_WIDTH + 2 * FOCUS_OFFSET, Qt.SolidLine)
NNB_FOCUS_BRUSH = QBrush()

# Neuron Settings
NEURON_BODY_COLOR = QColor(255, 255, 255, 128)
NEURON_1D_DEFAULT_NAME = "1D Neuron-{}_{}"
NEURON_1D_BIAS_DEFAULT_NAME = "1D Bias Neuron-{}_{}"
NEURON_1D_STACKED_DEFAULT_NAME = "1D Stacked Neuron-{}_{}"
NEURON_1D_RADIUS = 20
NEURON_1D_DIAMETER = 2 * NEURON_1D_RADIUS
NEURON_1D_DEFAULT_NAME_REGEX = "^1D Neuron-(.*)$"
NEURON_1D_BIAS_DEFAULT_NAME_REGEX = "^1D Bias Neuron-(.*)$"
NEURON_1D_STACKED_DEFAULT_NAME_REGEX = "^1D Stacked Neuron-(.*)$"
NEURON_1D_SYN_LENGTH = 5
NEURON_1D_SYN_OFFSET_X = NEURON_1D_RADIUS - 1
NEURON_1D_SYN_OFFSET_Y = (NEURON_1D_RADIUS ** 2 - NEURON_1D_SYN_OFFSET_X ** 2) ** 0.5
NEURON_1D_SYN_THETA = math.degrees(math.atan(NEURON_1D_SYN_OFFSET_Y / NEURON_1D_SYN_OFFSET_X))

NEURON_2D_DEFAULT_NAME = "2D Neuron-{}_{}"
NEURON_2D_BIAS_DEFAULT_NAME = "2D Bias Neuron-{}_{}"
NEURON_2D_SIZE = 50
NEURON_2D_DEFAULT_NAME_REGEX = "^2D Neuron-(.*)$"
NEURON_2D_BIAS_DEFAULT_NAME_REGEX = "^2D Bias Neuron-(.*)$"

# Connection Settings
LINEAR_1D_CONNECTION_DEFAULT_NAME = "1D Linear Connection-{}-{}"
LINEAR_1D_STACKED_CONNECTION_DEFAULT_NAME = "1D Stacked Lin. Connection-{}-{}"
CONV_2D_CONNECTION_DEFAULT_NAME = "2D Conv. Connection-{}-{}"
LFB_CONNECTION_DEFAULT_NAME = "LBF Connection-{}-{}"
REG_CONNECTION_DEFAULT_NAME = "Reg. Connection-{}-{}"
FLATTEN_2D_CONNECTION_DEFAULT_NAME = "Flatten Connection-{}-{}"
POOLING_2D_CONNECTION_DEFAULT_NAME = "2D Pooling Connection-{}-{}"
DEFAULT_INIT_METHOD = "zero"

# Layer Settings
LAYER_CORNER_RADIUS = 5
LAYER_WIDTH = 5 * NEURON_1D_RADIUS
LAYER_HEIGHT = 300
LAYER_BODY_COLOR = QColor(200, 200, 200, 128)
LAYER_ENLARGE_POINT_RADIUS = 5
LAYER_HEADER_HEIGHT = 20
LAYER_HANDLE_SIZE = +8.0
LAYER_HANDLE_SPACE = -4.0
AFFINE_1D_LAYER_DEFAULT_NAME = "Aff. 1D Layer-{}"
AFFINE_1D_LAYER_DEFAULT_NAME_REGEX = "^Aff. 1D Layer-([\\d]+)$"
STACKED_AFFINE_1D_LAYER_DEFAULT_NAME = "Stacked 1D Layer-{}"
STACKED_AFFINE_1D_LAYER_DEFAULT_NAME_REGEX = "^Stacked 1D Layer-([\\d]+)$"
CONV_2D_LAYER_DEFAULT_NAME = "Conv. 2D Layer-{}"
CONV_2D_LAYER_DEFAULT_NAME_REGEX = "^Conv. 2D Layer-([\\d]+)$"
POOLING_2D_LAYER_DEFAULT_NAME = "Pooling 2D Layer-{}"
POOLING_2D_LAYER_DEFAULT_NAME_REGEX = "^Pooling 2D Layer-([\\d]+)$"
FLATTEN_2D_LAYER_DEFAULT_NAME = "Flatten Layer-{}"
FLATTEN_2D_LAYER_DEFAULT_NAME_REGEX = "^Flatten Layer-([\\d]+)$"
STACKED_AFF_1D_LAYER_SPACE = 3
STACKED_AFF_1D_SKIP_DOT_SIZE = 3
LAYER_MIN_WIDTH = max(NEURON_2D_SIZE, NEURON_1D_DIAMETER) + 10
LAYER_MIN_HEIGHT = LAYER_HEADER_HEIGHT + NEURON_1D_DIAMETER * 4 + STACKED_AFF_1D_LAYER_SPACE * 5 + 10

# Cost Function Block
LFB_WIDTH = 50
LFB_HEIGHT = 50
LFB_BODY_COLOR = QColor(157, 165, 239, 128)
LFB_DEFAULT_NAME = "loss_func_block-{}"
LFB_DEFAULT_NAME_REGEX = "^loss_func_block-([\\d]+)$"

# Regularizer
REGULARIZER_WIDTH = 50
REGULARIZER_HEIGHT = 50
REGULARIZER_BODY_COLOR = QColor(178, 102, 255, 128)
REGULARIZER_DEFAULT_NAME = "regularizer-{}"
REGULARIZER_DEFAULT_NAME_REGEX = "^regularizer-([\\d]+)$"

# Animation Settings
ANIMATION_ARROWHEAD_LENGTH = 12
ANIMATION_ARROWHEAD_FACTOR = 0.2
ANIMATION_DURATION = 100

# COLOR
WHITE_TRANSPARENT = QColor(255, 255, 255, 0)
WHITE_HALF_TRANSPARENT = QColor(255, 255, 255, 128)

#
DIR = os.path.dirname(__file__)
RES_ACT_FUNC_PATH = DIR + '/res/act_func/'
RES_LOSS_FUNC_PATH = DIR + '/res/loss_func/'
RES_REG_FUNC_PATH = DIR + '/res/reg_func/'
ACTIVATION_FUNC_LIST = ["linear", "sigmoid", "softmax", "tanh", "relu", "elu",
                        "leaky relu", "softmax", "gaussian", "sine"]
LOSS_FUNC_LIST = ["MAE", "MSE", "CE"]
REGULARIZATION_LIST = ["L1", "L2", "L3", "L0.5", "Lp", "Elastic Net"]


class SceneMode:
    SelectMode = 1
    DragDrogMode = 2
    ConnectMode = 3
    TrainMode = 4


# TO BE DEL
ICON_OFFSET_X = 10
ICON_OFFSET_Y = 15
NEURON_1D_ICON_SIZE = NEURON_1D_RADIUS * 1.5
NEURON_2D_ICON_SIZE = NEURON_2D_SIZE // 2
AFFINE_LAYER_ICON_WIDTH = LAYER_WIDTH // 4
AFFINE_LAYER_ICON_HEIGHT = LAYER_HEIGHT // 4
CONV_LAYER_ICON_WIDTH = LAYER_WIDTH // 4
CONV_LAYER_ICON_HEIGHT = LAYER_HEIGHT // 4
REGULARIZER_ICON_WIDTH = REGULARIZER_WIDTH // 1.5
REGULARIZER_ICON_HEIGHT = REGULARIZER_HEIGHT // 1.5
LFB_ICON_WIDTH = LFB_WIDTH // 1.6
LFB_ICON_HEIGHT = LFB_HEIGHT // 1.6
TEST_DATA_DIM = (3, 2)

fooOptimizerConfigs = {
    'optimizerType': 'sgd',
    'learning_rate': 0.01,
    'momentum': 0.9,
    'decaryRate': 0.99,
}

def getData():
    import numpy as np

    def softmax(x):
        exp = np.exp(x - np.max(x, axis=1, keepdims=True))
        return exp / np.sum(exp, axis=1, keepdims=True)

    nData = 1000
    nTrainData = int(0.9 * nData)
    x = np.random.rand(nData, 2)
    W1 = [[1.1, 0.2, 1.2], [1.4, 1.2, 3.1]]
    b1 = [3.2, 3.4, 2.3]
    z1 = x @ W1 + b1
    ySoft = softmax(z1)
    y = np.argmax(ySoft, 1)
    X_train = x[:nTrainData]
    y_train = y[:nTrainData]
    X_val = x[nTrainData:]
    y_val = y[nTrainData:]
    return X_train, y_train, X_val, y_val


fooXTrain, fooYTrain, fooXVal, fooYVal = getData()
fooBatchSize = 100
