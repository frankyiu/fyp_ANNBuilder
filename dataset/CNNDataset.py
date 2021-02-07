import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import shutil
import os
class CNNDataset():
    def __init__(self, dataset_name, path=""):
        self.original_data = None
        self.data = None
        self.dataset_name = None
        self.path = None
        self.var = None
        if dataset_name is "cnn_mnist":
            tr, ts = load_mnist_raw(path)
            self.path = path
            self.var = 0
            self.original_data = {"train": normalize_dataset_pixel(tr), "test": normalize_dataset_pixel(ts)}
            self.data = self.original_data
            self.dataset_name = dataset_name

    def showGraph(self, filename):
        if not self.isLoadSuccess():
            print("No Dataset is loaded")
            return
        if self.dataset_name is "cnn_mnist":
            src = self.path + 'img/cnn_mnist_{i}.png'.format(i=self.var)
            dest = filename
            try:
                shutil.copyfile(src, dest)
            except FileNotFoundError as fnf_error:
                print("Image Source File not Found:", src)
                if os.path.exists(dest):
                    os.remove(dest)

    def doVariation(self, var):
        if not self.isLoadSuccess():
            print("No Dataset is loaded")
            return
        if self.dataset_name is "cnn_mnist":
            if var == 0:
                filters = [i for i in range(2,10)]
            elif var == 1:
                filters = [0,1,2,3,5,6,8]
            elif var == 2:
                filters = [0,1,4,7,9]
            else:
                filters = []
            self.var = var
            self.data = {"train": filter_byclass(self.original_data["train"], filters),
                        "test": filter_byclass(self.original_data["test"], filters)}
        return

    def getVariation(self):
        return self.var

    def isLoadSuccess(self):
        return self.data != None

    def getTrainSize(self):
        return len(self.data["train"]["y"])

    def getTestSize(self):
        return len(self.data["test"]["y"])

    def getTrainFeature(self):
        return self.data["train"]["X"]

    def getTrainLabel(self):
        return self.data["train"]["y"]

    def getTestFeature(self):
        return self.data["test"]["X"]

    def getTestLabel(self):
        return self.data["test"]["y"]


def load_mnist_raw(path_to_dataset_folder=""):
    train = {}
    test = {}
    with np.load(path_to_dataset_folder+"cnn_mnist.npz", allow_pickle=True) as f:
        train["X"] = f['x_train']
        train["y"] = f['y_train']
        test["X"] = f['x_test']
        test["y"] = f['y_test']
    return train, test

def filter_byclass(ds_dict, filters = []):
    ds_dict = ds_dict.copy()
    for digit in filters:
        bool_keep = (ds_dict["y"] != digit)
        ds_dict["X"] = ds_dict["X"][bool_keep]
        ds_dict["y"] = ds_dict["y"][bool_keep]
    return ds_dict

def normalize_dataset_pixel(ds_dict):
    ds_dict["X"] = ds_dict["X"].astype('float32') / 255.0
    return ds_dict

if __name__ == '__main__':
    trainX, _ = load_mnist_raw()
    for i in range(10):
        fig, ax = plt.subplots()
        plt.imshow(filter_byclass(trainX, [j for j in range(10) if j != i])["X"][0], cmap=plt.get_cmap('gray'))
        fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
        ax.axis("tight")
        plt.axis('off')
        plt.savefig("mnist-icon/"+str(i)+'.png')
    pass
