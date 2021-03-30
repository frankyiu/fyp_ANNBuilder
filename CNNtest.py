import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense
import matplotlib.pyplot as plt
from dataset.DatasetObject import DatasetObject
from dataset.CNNDataset import CNNDataset


class DifficultyCalculation():
    epoch = 10
    bs = None
    lr = 0.03

    def __init__(self, dataset_name):
        self.dataset = DatasetObject()
        self.dataset.loadDataset(dataset_name)
        self.gau = True if dataset_name in ['bi_linear', 'multi_three', 'multi_four'] else False
        self.reg = False
        self.loss = 'categorical_crossentropy' if self.dataset.getVariation() > 0 else 'binary_crossentropy'
        self.metric = 'accuracy'
        self.resultlst = []
        pass

    def print_setting(self):
        print("gau", self.gau)
        print("reg", self.reg)
        print("loss", self.loss)
        print("metric", self.metric)

    def createModelSet(self, input_size, output_size):
        print( input_size, output_size)
        model_lst = []
        init = tf.keras.initializers.GlorotUniform()

        for i in range(1):
            inputs = tf.keras.Input(shape=input_size)
            x = inputs

            x = tf.keras.layers.Conv2D(32, (3, 3), activation=tf.nn.relu)(x)
            x = tf.keras.layers.MaxPooling2D((2,2))(x)
            x = tf.keras.layers.Conv2D(64, (3, 3), activation=tf.nn.relu)(x)
            x = tf.keras.layers.MaxPooling2D((2,2))(x)
            x = tf.keras.layers.Conv2D(64, (3, 3), activation=tf.nn.relu)(x)
            x = tf.keras.layers.Flatten()(x)
            x = tf.keras.layers.Dense(64, activation=tf.nn.relu)(x)
            outputs = tf.keras.layers.Dense(output_size)(x)
            model = tf.keras.Model(inputs=inputs, outputs=outputs)
            model_lst.append(model)
        return model_lst

    def calculate(self, verbose):
        for i in [0,1,2,3]:
            if verbose>0:
                print("Noise level:", i)
            acc_lst = []
            n_rounds = 1
            for rounds in range(n_rounds):
                if verbose>0:
                    print("Round", rounds)

                self.dataset.varyData(i)
                self.loss = 'sparse_categorical_crossentropy' if self.dataset.getVariation() > 0 else 'binary_crossentropy'

                X_train = self.dataset.getTrainFeature()
                y_train = self.dataset.getTrainLabel()
                X_test = self.dataset.getTestFeature()
                y_test = self.dataset.getTestLabel()
                y_train = tf.keras.utils.to_categorical(self.dataset.getTrainLabel())#, num_classes=classes)
                y_test = tf.keras.utils.to_categorical(self.dataset.getTestLabel())#, num_classes=classes)
                print(X_train.shape, y_train.shape)
                print(X_test.shape, y_test.shape)
                self.print_setting()
                y_train = y_train[:, (y_train!=0).any(axis=0)]
                y_test = y_test[:, (y_test!=0).any(axis=0)]

                model_lst = self.createModelSet(X_train.shape[1:], y_train.shape[1])
                for model in model_lst:
                    model.compile(loss=tf.keras.losses.CategoricalCrossentropy(from_logits=True),
                                  optimizer=tf.keras.optimizers.Adam(),
                                  metrics=[self.metric])
                    epochs = DifficultyCalculation.epoch
                    history = model.fit(X_train, y_train,
                                        validation_data = (X_test, y_test),
                                        epochs=epochs, verbose=1)
                    _, accuracy = model.evaluate(X_test, y_test, verbose=0)

                    acc_lst.append(round(accuracy*100, 2))
                if verbose>1:
                    print("List of accuracy:", acc_lst[-5:])
            acc_lst = np.array(acc_lst)
            avg = (sum(acc_lst))/len(acc_lst)
            med = np.median(acc_lst)
            if verbose>0:
                print("Average accuracy:", avg)
                print("Median accuracy:", med)
                print("Difficulty:", len(acc_lst[acc_lst >= 80]))
            self.resultlst.append((avg, med))

    def getResultList(self):
        return self.resultlst

for datasetname in ["cnn_cifar10", "cnn_mnist"]:
    obj = DifficultyCalculation(datasetname)
    obj.calculate(verbose=2)
    print(obj.getResultList())
