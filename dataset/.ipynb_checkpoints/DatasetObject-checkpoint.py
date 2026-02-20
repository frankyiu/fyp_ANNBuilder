import numpy as np
import matplotlib.pyplot as plt

class DatasetObject():
    def __init__(self):
        self.data = None
        self.data_no_noise = None
        self.train_set_ratio = 0.8

    def plotData(self, filename, isClassify=True):        
        from dataset.generator import plot_np
        if self.hasData():
            fig, _ = plot_np(self.data, filename, isClassify)
            plt.close(fig)

    def loadDataset(self, path, dataset_name):
        csv = path + dataset_name + '.csv'
        try:
            self.data = np.genfromtxt(csv, delimiter=',', skip_header=1)
            self.data_no_noise = self.data.copy()
            print('Data set ' + dataset_name +' is loaded')
            return True
        except FileNotFoundError as file_error:
            print(file_error)
            self.data = None
            self.data_no_noise = None
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
            return None

    def hasData(self):
        return self.data is not None

    def getRawData(self):
        return self.data

    #ndarray of shape (N, 2) for classification
    #(N, 1) for regression
    def getFeature(self):
        return self.data[:,:-1] if self.data is not None else None

    #ndarray of shape (N, )
    def getLabel(self):
        return self.data[:,-1] if self.data is not None else None

    def getTrainingSetRatio(self):
        return self.train_set_ratio

    def setTrainingSetRatio(self, val):
        self.train_set_ratio = val
