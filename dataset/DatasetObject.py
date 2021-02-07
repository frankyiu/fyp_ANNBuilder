import numpy as np
import matplotlib.pyplot as plt
from dataset.CNNDataset import *

class DatasetObject():
    def __init__(self):
        self.data = None
        self.data_no_noise = None
        self.train_set_ratio = 0.8
        self.isCNN = False

    def plotData(self, filename, isClassify=True):
        if self.isCNNData():
            self.data.showGraph(filename)
        else:
            from dataset.generator import plot_np
            if self.hasData():
                fig, _ = plot_np(self.data, filename, isClassify)
                plt.close(fig)
            else:
                print("No Dataset is loaded")

    def loadDataset(self, path, dataset_name):
        csv = path + dataset_name + '.csv'
        isCNN = True if 'cnn' in dataset_name else False
        if isCNN:
            try:
                self.data = CNNDataset(dataset_name, path)
                print('Dataset ' + dataset_name +' is loaded')
                self.isCNN = isCNN
                return True
            except:
                print("Dataset " + dataset_name + " not Found")
                self.data = None
                self.data_no_noise = None
                self.isCNN = False
                return False
        else:
            try:
                self.data = np.genfromtxt(csv, delimiter=',', skip_header=1)
                self.data_no_noise = self.data.copy()
                self.isCNN = isCNN
                print('Dataset ' + dataset_name +' is loaded')
                return True
            except:
                print("Dataset Source not Found:", csv)
                self.data = None
                self.data_no_noise = None
                self.isCNN = False
                return False

    def addNoiseToData(self, val, is_gaussian, is_regression):
        if self.hasData():
            mean = 0
            multiplier = 7 if is_gaussian else 1
            sd = 0.1 * val * multiplier
            self.data = self.data_no_noise.copy()
            if is_regression:
                self.data += np.random.normal(mean,sd, self.data.shape)
                isClassify = False
            else:
                self.data[:,:-1] += np.random.normal(mean,sd, self.data[:,:-1].shape)
                isClassify = True
            return isClassify
        else:
            print("No Dataset is loaded")

    def doVariation(self, val):
        self.data.doVariation(val)

    def getVariation(self):
        return self.data.getVariation() if self.isCNNData() else None

    """
    Member functions below are for the ML Process
    """

    def isCNNData(self):
        return self.isCNN

    def hasData(self):
        return self.data is not None

    def getRawData(self):
        return self.data if not self.isCNNData() else None

    def getFeatureShape(self):
        return self.getTestFeature().shape[1:] if self.data is not None else None

    def getLabelShape(self):
        return self.getTestLabel().shape[1:] if self.data is not None else None

    def getTrainSize(self):
        return self.data.getTrainSize() if self.isCNNData() \
                else int(len(self.data)*self.getTrainingSetRatio()) if self.data is not None else None

    def getTestSize(self):
        return self.data.getTestSize() if self.isCNNData() \
                else (len(self.data)-int(len(self.data)*self.getTrainingSetRatio())) if self.data is not None else None

    def getTrainData(self):
        return self.getTrainFeature(), self.getTrainLabel()

    def getTestData(self):
        return self.getTestFeature(), self.getTestLabel()

    def getTrainFeature(self):
        return self.data.getTrainFeature() if self.isCNNData() \
                else self.data[:self.getTrainSize(),:-1] if self.data is not None else None

    def getTrainLabel(self):
        return self.data.getTrainLabel() if self.isCNNData() \
                else self.data[:self.getTrainSize(),-1] if self.data is not None else None

    def getTestFeature(self):
        return self.data.getTestFeature() if self.isCNNData() \
                else self.data[self.getTrainSize():,:-1] if self.data is not None else None

    def getTestLabel(self):
        return self.data.getTestLabel() if self.isCNNData() \
                else self.data[self.getTrainSize():,-1] if self.data is not None else None

    def getTrainingSetRatio(self):
        return float(self.data.getTrainSize()/(self.data.getTrainSize()+self.data.getTestSize())) \
                if self.isCNNData() else self.train_set_ratio

    def setTrainingSetRatio(self, val):
        self.train_set_ratio = val
