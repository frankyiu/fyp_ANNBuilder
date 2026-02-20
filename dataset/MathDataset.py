import numpy as np
import matplotlib.pyplot as plt
from dataset.generator import plot_np
from dataset.DatasetMeta import *

"""
A wrapper class to Math data
"""
class MathDataset():
    NOISE_MEAN = 0
    NOISE_SD = {"Gaussian": 0.7, "Default": 0.1}
    path_to_data = DatasetMeta.dataset_data_directory

    def __init__(self, dataset_name):
        data = self.__loadDataset(dataset_name)
        if data is not None:
            self.__initialize(data, dataset_name)
        else:
            self.__initialize()

    def __initialize(self, data=None, dataset_name=None):
        self.dataset_name = dataset_name
        self.data = data
        self.clean_data = self.data.copy() if self.data is not None else None
        self.is_classify = DatasetMeta.isClassify(dataset_name)
        self.noise_sd = MathDataset.NOISE_SD["Default"] if not DatasetMeta.isGaussian(dataset_name) \
                        else MathDataset.NOISE_SD["Gaussian"]

    def __loadDataset(self, dataset_name):
        csv = MathDataset.path_to_data + dataset_name + '.csv'
        try:
            data = np.genfromtxt(csv, delimiter=',', skip_header=1)
        except:
            data = None
        return data

    def showGraph(self, filename):
        if not self.isLoadSuccess():
            print("No Dataset is loaded. Cannot plot graph")
            return
        fig, _ = plot_np(self.data, filename, self.is_classify)
        plt.close(fig)

    def addNoiseToData(self, val):
        if not self.isLoadSuccess():
            print("No Dataset is loaded. Cannot do variation")
            return
        mean = MathDataset.NOISE_MEAN
        sd = self.noise_sd * val
        self.data = self.clean_data.copy()
        if self.is_classify:
            self.data[:,:-1] += np.random.normal(mean, sd, self.data[:,:-1].shape)
        else:
            self.data += np.random.normal(mean, sd, self.data.shape)

    def isMath(self):
        return True

    def isCNN(self):
        return False

    def isLoadSuccess(self):
        return self.data is not None

    def getSize(self):
        return len(self.data)

    def getFeature(self):
        return self.data[:,:-1]

    def getLabel(self):
        return self.data[:, -1]

    def getTrainSize(self, split):
        return int(len(self.data)*split)

    def getTestSize(self, split):
        return len(self.data)-int(len(self.data)*split)

    #return in shape (N, F)
    def getTrainFeature(self, split):
        return self.data[:int(len(self.data)*split), :-1]

    #return in shape (N, )
    def getTrainLabel(self, split):
        return self.data[:int(len(self.data)*split), -1]

    #return in shape (N, F)
    def getTestFeature(self, split):
        return self.data[int(len(self.data)*split):, :-1]

    #return in shape (N, )
    def getTestLabel(self, split):
        return self.data[int(len(self.data)*split):, -1]
