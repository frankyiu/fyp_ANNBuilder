
from dataset.DatasetMeta import *
from dataset.DatasetObject import *
from ui.DatasetLoader import *
from ml.UpdateDashBoard import *
from ml.Utility import *
from ml.Optimizer import Optimizer
import pyqtgraph as pg
import numpy as np
import time

import sys
import tensorflow as tf
import gc

"""
The model class object should support the following:
- train the model, more refer to doTrainingStep()
- predicts the input, used api: model(X)
- extract the layers and shapes, used api:
-      model.layers[0].input_shape[0][1:], model.layers[-1].output_shape[1:]
"""


"""
The shape of input and expected number of class can be accessed through:
DatasetLoader.getDatasetObject().getFeatureShape()   #shape of input will be (2) or (W,H,C)
DatasetLoader.getDatasetObject().getNumberOfClass()  #number of unique classes label
"""


"""
This class connects other parts from the program:
Dataset, Hyperparameters, Model, and DashBoard
handles the training of the model
"""
class Training():
    timer = pg.QtCore.QTimer()
    def __init__(self):
        #keep a reference to the dataset object, which is a wrapper of the real dataset
        self.dataset = DatasetLoader.getDatasetObject()
        self.epoch_widget = None
        self.__initialize()
        pass

    def __initialize(self, optim=None, loss=None, lr=None, lr_decay=None, batch_size=None):
        self.optim = optim
        self.loss = loss
        self.lr = lr
        self.lr_decay = lr_decay
        self.bs = batch_size
        self.curEpoch = 0
        self.resetTraining()

    """
    This method reset the training state, including
    - remove the references passed to heatmap (the graph is still present)
    - remove the references passed to loss graph (the graph is still present)
    - reset the preprocessed data in previous training
    - remove the model, can be skipped if pause is true
    - reset the timer for multithreading
    - reset the Epoch GUI display
    """
    def resetTraining(self, pause=False):
        UpdateDashBoard.resetHeatmapReference()
        UpdateDashBoard.resetLossGraphReference()
        self.train_losses = []
        self.test_losses = []
        self.processed = None
        Training.timer = pg.QtCore.QTimer()     #create a new timer, clear previously connected singals
        if not pause:
            self.model = None
            self.curEpoch = 0
        self.updateEpochGUI()
        gc.collect()

    def connectEpochWidget(self, widget):
        self.epoch_widget = widget
        self.updateEpochGUI()

    def updateEpochGUI(self):
        if self.epoch_widget is not None:
            self.epoch_widget.setText("Epoch: {}".format(self.curEpoch))

    def setOptimizer(self, optim=None):
        self.optim = optim.text()

    def setLossFunc(self, loss):
        self.loss = loss

    def setLearningRate(self, lr):
        self.lr = lr

    def setLearningRateDecay(self, lr_decay):
        self.lr_decay = lr_decay

    def setBatchSize(self, bs=32):
        self.bs = bs

    def setModel(self, model):
        self.model = model

    def getHyperParameters(self):
        return self.optim, self.loss, self.lr, self.lr_decay, self.bs

    """
    helper function used at the beginning of training, which
    - pass the references of loss history to dashboard
    - update the metric name and visibility in dashboard
            - reset the heatmap state and references in previous training
    """
    def _connectDashboard(self):
        UpdateDashBoard.connectLossGraph(self.train_losses, self.test_losses)
        dataset_name = self.dataset.getDatasetName()
        variation = self.dataset.getVariation()
        UpdateDashBoard.updateMetricNames(dataset_name, variation)

    """
    helper function used at the beginning of training, which
    - get the data from dataset object
    - preprocess the data (one hot encoding for classification)
    """
    def _preprocess(self):
        if self.processed is not None:
            return
        #read dataset
        trainX, trainy = self.dataset.getTrainData()
        testX, testy = self.dataset.getTestData()
        #one hot encoding for classification
        if DatasetMeta.isClassify(self.dataset.getDatasetName()):
            n_classes = int(max(trainy)) + 1
            #self.testy_label is the vector version of test set label (no one hot)
            #make sure the test set label (without one hot) are in order of 0, 1, ...
            self.testy_label = reverse_one_hot(
                                one_hot(testy.copy(), n_classes, mask=self.dataset.isCNNData()))
            trainy = one_hot(trainy, n_classes, mask=self.dataset.isCNNData())
            testy = one_hot(testy, n_classes, mask=self.dataset.isCNNData())
        else:
            trainy = trainy.reshape(-1, 1)
            testy = testy.reshape(-1, 1)
            self.testy_label = testy
        self.processed = (trainX, trainy, testX, testy)

    #HARDCODED for debugging
    def build_demo_model(self):
        input_length = self.dataset.getFeatureShape()   #shape of input will be (2) or (W,H,C)
        output_size = self.dataset.getNumberOfClass()   #number of unique classes label
        init = tf.keras.initializers.GlorotUniform()
        inputs = tf.keras.Input(shape=input_length)
        last_activate = tf.nn.sigmoid if DatasetMeta.isClassify(self.dataset.getDatasetName()) \
                            and not self.dataset.isCNNData() else None
        x = inputs
        if self.dataset.isCNNData():
            x = tf.keras.layers.Conv2D(32, (3, 3), activation=tf.nn.relu)(x)
            x = tf.keras.layers.MaxPooling2D((2,2))(x)
            x = tf.keras.layers.Conv2D(64, (3, 3), activation=tf.nn.relu)(x)
            x = tf.keras.layers.MaxPooling2D((2,2))(x)
            x = tf.keras.layers.Conv2D(64, (3, 3), activation=tf.nn.relu)(x)
            x = tf.keras.layers.Flatten()(x)
            x = tf.keras.layers.Dense(64, activation=tf.nn.relu)(x)
        elif DatasetMeta.isClassify(self.dataset.getDatasetName()):
            x = tf.keras.layers.Dense(7, activation=tf.nn.relu)(x)
            x = tf.keras.layers.Dense(7, activation=tf.nn.relu)(x)
            x = tf.keras.layers.Dense(6, activation=tf.nn.relu)(x)
        outputs = tf.keras.layers.Dense(output_size, activation=last_activate)(x)
        model = tf.keras.Model(inputs=inputs, outputs=outputs)
        self.model = model

    """
    This method get the hyperparameters from GUI/builder
    e.g. optimizer, loss function
    HARDCODED HERE for debugging
    """
    def config_hyperparam(self):
        if DatasetMeta.isRegression(self.dataset.getDatasetName()):
            loss = tf.keras.losses.MeanSquaredError()
        elif self.dataset.getNumberOfClass() == 2:
            loss = tf.keras.losses.BinaryCrossentropy(from_logits=True) #or softmax at last layer
        else:
            loss = tf.keras.losses.CategoricalCrossentropy(from_logits=True) #or softmax at last layer
        self.loss = loss
        self.bs = 10
        #self.optim = tf.keras.optimizers.Adam

    """
    This method toggles the training process
    connected to the Play/Pause button in GUI
    There are different behavior depends on the context
    1. At RESET state, run() will remove any neural network model used previously
    2. At PAUSE state, run() will keep and use the previous network model
    3. At RUN state, run() stop the training and reset the training state
       e.g. loss history, refernces used in drawing the graph, processed data
    """
    def run(self):
        if Training.timer.isActive():
            Training.timer.stop()
            self.resetTraining(True)
            DatasetLoader.setTrainingSignal(False)
        else:
            self.runMultithread()
            DatasetLoader.setTrainingSignal(True)

    """
    This method handles the exit of training and do the clean up
    """
    def reset(self):
        print("Training Done")
        print("==============================")
        print("Average Training time ", np.average(self.t0_lst))
        print("Average Prediction and update heatmap time ", np.average(self.t1_lst))
        print("Average Update loss graph time ", np.average(self.t2_lst))
        print("Average Total time ", np.average(self.t3_lst))
        print("==============================")
        Training.timer.stop()
        self.resetTraining()
        UpdateDashBoard.resetDashboardRendering()
        DatasetLoader.setTrainingSignal(False)

    """
    A method for debugging, simulate the training by
    - randomly update the weight
    - randomly generate losses
    - update the dash board
    to test the fps of loss graph, heatmap and metrics
    """
    def random_walk(self):
        t0 = time.time()    #time log
        new_w = []
        for w in self.model.get_weights():
            new_w.append(w + np.random.normal(scale=0.1, size = w.shape))
        self.model.set_weights(new_w)
        history = {"loss":[np.random.randint(10)], "val_loss":[np.random.randint(100)]}
        self.train_losses.extend(history["loss"])
        self.test_losses.extend(history["val_loss"])
        t1 = time.time()    #time log
        UpdateDashBoard.updateLosses(self.train_losses[-1], self.test_losses[-1])
        UpdateDashBoard.updateLossGraph()
        t2 = time.time()    #time log
        UpdateDashBoard.updatePredictionResult(self.testX, self.testy_label, self.model)
        t3 = time.time()    #time log
        self.t0_lst.append(t1-t0)
        self.t1_lst.append(t2-t1)
        self.t2_lst.append(t3-t2)
        self.t3_lst.append(t3-t0)

    """
    Implement the flow of 1 iteration of training, namely
    - feed forward and back propagate a slice of training data
    - update the loss value and loss graph in GUI
    - evaluate the model using test set data
    - update the evaluation result (metrics, contour/regression line) in GUI
    """
    def doTrainingStep(self):
        """
        depends on real implementation
        """
        #self.random_walk()
        #"""
        self.pred_cnn = None
        rand_slice = np.random.randint(len(self.trainy), size=self.bs)
        trainX, trainy = self.trainX[rand_slice, :], self.trainy[rand_slice, :]
        t0 = time.time()
        with tf.GradientTape() as tape:
            y_pred = self.model(trainX, training=True)
            loss = self.loss(trainy, y_pred)

        trainable_vars = self.model.trainable_variables
        gradients = tape.gradient(loss, trainable_vars)
        self.optimizer.apply_gradients(zip(gradients, trainable_vars))

        t1 = time.time()    #time log
        """
        Compute the loss and update the contour graph
        note that CNN data prediction is done together with the loss compute
            (only a slice of CNN data is used to evaluate to increase interactivity)
        math data prediction is done together with the contour graph
        """
        self.train_losses.append(loss.numpy())
        if self.dataset.isCNNData():
            test_rand_slice = np.random.randint(len(self.testy), size=50)#20*self.dataset.getNumberOfClass())
            self.pred_cnn = self.model(self.testX[test_rand_slice, :]).numpy()
            self.test_losses.append(self.loss(self.testy[test_rand_slice, :], self.pred_cnn).numpy())
            UpdateDashBoard.updatePredictionResult(self.testX, self.testy_label[test_rand_slice], self.model, self.pred_cnn)
        else:
            self.test_losses.append(self.loss(self.testy, self.model(self.testX)).numpy())
            #self.testy_label is the vector version of test set label (not one hot matrix)
            UpdateDashBoard.updatePredictionResult(self.testX, self.testy_label, self.model)

        t2 = time.time()    #time log
        UpdateDashBoard.updateLosses(self.train_losses[-1], self.test_losses[-1])
        UpdateDashBoard.updateLossGraph()
        t3 = time.time()

        self.t0_lst.append(t1-t0)
        self.t1_lst.append(t2-t1)
        self.t2_lst.append(t3-t2)
        self.t3_lst.append(t3-t0)
        #"""
        self.curEpoch += 1      #next slice of data
        self.updateEpochGUI()
        Training.timer.start(1)     #continue

    """
    This method set up the environment before going to the training loop, namely
    - reset previous training and preprocess the data
    - configure the hyperparameters
    - build and compile the model
    - connect to the dashboard (pass the references)
    - start the timer invoke the training loop
    """
    def runMultithread(self):
        self._preprocess()

        (self.trainX, self.trainy, self.testX, self.testy) = self.processed
        """
        Below depends on real implementation
        """
        self.config_hyperparam()

        """
        Support continue training after pausing
        need to check if the dataset matches with the model
        e.g. input shape is not matching, output class is not matching
        If it does not match then throw an error to say model is not compatible
        and reset the training state
        """
        if self.model is None:
            self.build_demo_model()
        else:
            model_input_shape = self.model.layers[0].input_shape[0][1:]
            model_out_shape = self.model.layers[-1].output_shape[1:]
            data_shape = self.testX.shape[1:]
            class_shape = self.testy.shape[1:]
            if model_input_shape != data_shape:
                print("ERROR: Model Input Layer does not match with dataset shape")
                print("Input Layer Shape: {} Dataset Shape: {}".format(model_input_shape, data_shape))
                print("Training Abort")
                self.resetTraining(True)
                return
            elif model_out_shape != class_shape:
                print("ERROR: Model Output layer does not match with dataset class label")
                print("Output Layer Shape: {} Class Label: {}".format(model_out_shape, class_shape))
                print("Training Abort")
                self.resetTraining(True)
                return

        #read the model and configure hyperparameters
        optim, loss, lr, lr_decay, bs = self.getHyperParameters()

        """
        Below depends on real implementation
        """
        self.optimizer = Optimizer(optim, lr, lr_decay).getOptim()
        self.t0_lst = []
        self.t1_lst = []
        self.t2_lst = []
        self.t3_lst = []
        """
        Above depends on real implementation
        """

        #update the dash board
        self._connectDashboard()
        Training.timer.timeout.connect(self.doTrainingStep)
        Training.timer.start(0)

    """
    Return True if it is running, False when it is paused
    Used to signal whether it is training
    """
    @staticmethod
    def isTraining():
        return Training.timer.isActive()

    def forward(self):
        print("Forward")
        pass

    def backward(self):
        print("Backward")
        pass
