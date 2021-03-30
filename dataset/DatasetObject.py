from dataset.CNNDataset import *
from dataset.MathDataset import *
#from CNNDataset import *
from dataset.DatasetMeta import *

"""
A wrapper class to the dataset
Important method attached with comments
"""
class DatasetObject():
    def __init__(self):
        self.dataset = None
        self.train_set_ratio = 0.8

    def plotData(self, filename):
        if self.dataset:
            self.dataset.showGraph(filename)

    def loadDataset(self, dataset_name):
        isCNN = DatasetMeta.isCNN(dataset_name)
        dataset_ptr = None
        if isCNN:
            dataset_ptr = CNNDataset
        else:
            dataset_ptr = MathDataset
        try:
            self.dataset = dataset_ptr(dataset_name)
            print('Dataset ' + dataset_name +' is loaded')
            self.varyData(0)    #selection for CNN data, do nothing to Math data
            return True
        except:
            self.dataset = None
            print("Dataset " + dataset_name + " not Found")
            return False

    def varyData(self, val):
        if self.isMathData():
            self.dataset.addNoiseToData(val)
        elif self.isCNNData():
            self.dataset.doVariation(val)

    """
    Functions below for the ML Process
    """
    def isLoadSuccess(self):
        return self.dataset.isLoadSuccess() if self.dataset else False

    def isMathData(self):
        return self.dataset.isMath() if self.dataset else False

    def isCNNData(self):
        return self.dataset.isCNN() if self.dataset else False

    def getVariation(self):
        return self.dataset.getVariation() if self.dataset.isCNN() else 0

    def getDatasetName(self):
        return self.dataset.dataset_name if self.dataset is not None else ""

    def getFeatureShape(self):
        return self.getTestFeature().shape[1:] if self.dataset is not None else None

    def getLabelShape(self):
        return self.getTestLabel().shape[1:] if self.dataset is not None else None

    def getNumberOfClass(self):
        return len(np.unique(self.getTrainLabel())) \
                if DatasetMeta.isClassify(self.dataset.dataset_name) else 1

    def getTrainSize(self):
        return self.dataset.getTrainSize() if self.isCNNData() \
               else self.dataset.getTrainSize(self.getTrainingSetRatio()) \
               if self.isMathData() else None

    def getTestSize(self):
        return self.dataset.getTestSize() if self.isCNNData() \
               else self.dataset.getTestSize(self.getTrainingSetRatio()) \
               if self.isMathData() else None

    """
    Get the train set data
    """
    def getTrainData(self):
        return self.getTrainFeature(), self.getTrainLabel()

    """
    Get the test set data
    """
    def getTestData(self):
        return self.getTestFeature(), self.getTestLabel()

    def getTrainFeature(self):
        return self.dataset.getTrainFeature().astype(np.float32) if self.isCNNData() \
               else self.dataset.getTrainFeature(self.getTrainingSetRatio()).astype(np.float32) \
               if self.isMathData() else None

    def getTrainLabel(self):
        return self.dataset.getTrainLabel() if self.isCNNData() \
               else self.dataset.getTrainLabel(self.getTrainingSetRatio()) \
               if self.isMathData() else None

    def getTestFeature(self):
        return self.dataset.getTestFeature().astype(np.float32) if self.isCNNData() \
               else self.dataset.getTestFeature(self.getTrainingSetRatio()).astype(np.float32) \
               if self.isMathData() else None

    def getTestLabel(self):
        return self.dataset.getTestLabel() if self.isCNNData() \
               else self.dataset.getTestLabel(self.getTrainingSetRatio()) \
               if self.isMathData() else None

    def getTrainingSetRatio(self):
        return float(self.dataset.getTrainSize()/(self.dataset.getTrainSize()+self.dataset.getTestSize())) \
               if self.isCNNData() else self.train_set_ratio

    def setTrainingSetRatio(self, val):
        self.train_set_ratio = val
