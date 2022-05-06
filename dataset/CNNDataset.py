import shutil
import os
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import pickle
from dataset.DatasetMeta import *

"""
A wrapper class to CNN data
"""
class CNNDataset():
    path_to_data = DatasetMeta.dataset_data_directory
    path_to_img = DatasetMeta.dataset_img_directory

    def __init__(self, dataset_name):
        tr, ts = self.__loadDataset(dataset_name)
        if tr and ts:
            self.__initialize(tr, ts, dataset_name)
        else:
            self.__initialize()

    def __initialize(self, tr=None, ts=None, dataset_name=None):
        self.dataset_name = dataset_name
        self.raw_data = {"train": normalize_dataset_pixel(tr),
                         "test": normalize_dataset_pixel(ts)} \
                         if tr and ts else None
        self.sampled_data = self.raw_data
        self.variation = 0

    def __loadDataset(self, dataset_name):
        fun_ptr = None
        tr, ts = None, None
        if CNNDataset.isMNIST(dataset_name):
            fun_ptr = load_mnist_raw
        elif CNNDataset.isCIFAR10(dataset_name):
            fun_ptr = load_cifar10_raw
        if fun_ptr is not None:
            try:
                tr, ts = fun_ptr(CNNDataset.path_to_data)
            except:
                tr, ts = None, None
        return tr, ts

    def showGraph(self, filename):
        if not self.isLoadSuccess():
            print("No Dataset is loaded. Cannot plot graph")
            return
        src = self.__getVariationImagePath()
        copy_image(src, filename)

    def __getVariationImagePath(self):
        return CNNDataset.path_to_img + '{cnn_dataset}_{i}.png'.format(
               i=self.variation, cnn_dataset=self.dataset_name)

    def doVariation(self, var):
        if not self.isLoadSuccess():
            print("No Dataset is loaded. Cannot do variation")
            return
        filters = self.__getSubtractedClasses(var)
        self.variation = var
        self.sampled_data = {"train": filter_byclass(self.raw_data["train"], filters),
                             "test": filter_byclass(self.raw_data["test"], filters)}

    def __getSubtractedClasses(self, var):
        filters = list(set(DatasetMeta.getClasses(self.dataset_name, -1)) - set(DatasetMeta.getClasses(self.dataset_name, var)))
        return filters

    @staticmethod
    def isMNIST(str_name):
        return str_name == "cnn_mnist"

    @staticmethod
    def isCIFAR10(str_name):
        return str_name == "cnn_cifar10"

    def isMath(self):
        return False

    def isCNN(self):
        return True

    def getVariation(self):
        return self.variation

    def isLoadSuccess(self):
        return self.sampled_data != None

    def getTrainSize(self):
        return len(self.sampled_data["train"]["y"])

    def getTestSize(self):
        return len(self.sampled_data["test"]["y"])

    #return in shape (N, width, height, channel)
    def getTrainFeature(self):
        return self.sampled_data["train"]["X"]

    #return in shape (N, )
    def getTrainLabel(self):
        return self.sampled_data["train"]["y"]

    #return in shape (N, width, height, channel)
    def getTestFeature(self):
        return self.sampled_data["test"]["X"]

    #return in shape (N, )
    def getTestLabel(self):
        return self.sampled_data["test"]["y"]


def copy_image(src, dest):
    try:
        shutil.copyfile(src, dest)
    except FileNotFoundError as fnf_error:
        print("Image Source File not Found:", src)
        if os.path.exists(dest):
            os.remove(dest)

def load_mnist_raw(path_to_dataset_folder=""):
    train = {}
    test = {}
    with np.load(path_to_dataset_folder+"cnn_mnist.npz", allow_pickle=True) as f:
        train["X"] = f['x_train'].reshape(-1, 28, 28, 1)
        train["y"] = f['y_train']
        test["X"] = f['x_test'].reshape(-1, 28, 28, 1)
        test["y"] = f['y_test']
    return train, test

def load_cifar10_raw(path_to_dataset_folder=""):
    train = {"X":np.zeros((50000, 32, 32, 3)), "y":np.zeros(50000,)}
    test = {"X":np.zeros((10000, 32, 32, 3)), "y":np.zeros(10000,)}
    for i in range(1, 6):
        with open(path_to_dataset_folder+"cifar10/data_batch_"+str(i), "rb") as f:
            dict = pickle.load(f, encoding="bytes")
            decoded = {k.decode("utf8"):v for k,v in dict.items()}
            X = decoded['data'].reshape(-1,3,32,32).transpose(0, 2, 3, 1)
            y = decoded['labels']
            train["X"][(i-1)*10000:i*10000, :, :, :] = X
            train["y"][(i-1)*10000:i*10000] = y

    with open(path_to_dataset_folder+"cifar10/test_batch", "rb") as f:
        dict = pickle.load(f, encoding="bytes")
        decoded = {k.decode("utf8"):v for k,v in dict.items()}
        X = decoded['data'].reshape(-1,3,32,32).transpose(0, 2, 3, 1)
        y = decoded['labels']
        test["X"] = X
        test["y"] = np.array(y)
    return train, test

"""
Vectorized version to filter the data by class
"""
def filter_byclass(ds_dict, filters=None):
    ds_dict = ds_dict.copy()
    if filters is None:
        filters = []
    bool_keep = np.isin(ds_dict["y"], filters, invert=True)
    ds_dict["X"] = ds_dict["X"][bool_keep]
    ds_dict["y"] = ds_dict["y"][bool_keep]
    print(len(ds_dict["X"]), len(ds_dict["y"]))
    return ds_dict

def normalize_dataset_pixel(ds_dict):
    ds_dict["X"] = ds_dict["X"].astype('float32') / 255.0
    return ds_dict

if __name__ == '__main__':
    def plot_icon(folder_name, trainX):
        for i in range(10):
            fig, ax = plt.subplots()
            plt.imshow(filter_byclass(trainX,[j for j in range(10) if j != i])["X"][0].astype('uint8'), cmap=plt.get_cmap('gray'))
            fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
            ax.axis("tight")
            plt.axis('off')
            plt.savefig(folder_name+str(i)+'.png')
    train, _ = load_mnist_raw()
    plot_icon("mnist-icon/", train)
    train, _ = load_cifar10_raw()
    plot_icon("cifar10-icon/", train)
