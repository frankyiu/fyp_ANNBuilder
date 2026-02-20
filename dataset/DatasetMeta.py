import json

def load_dataset_metainfo(path):
    dict_raw = {}
    try:
        with open(path+"DatasetsMetaInfo.json", "r") as f:
            dict_raw = json.loads(f.read())
    except FileNotFoundError as fnf_error:
        print(fnf_error, "(Failed to Load Datasets Metadata)")
    finally:
        from collections import defaultdict
        dict_of_dict = reformat(dict_raw)
    return dict_of_dict

"""
format the dict loaded from json back
to a dict of dict
"""
def reformat(dict):
    #name, task ([]), difficulty [], classify, gaussian, cnn, math, classes ([]), statements ([])
    res_dict = {}
    for k,lst in dict.items():
        res_dict[k] = {}
        res_dict[k]["name"]         = lst[0]
        res_dict[k]["task"]         = lst[1]
        res_dict[k]["difficulty"]   = lst[2]
        res_dict[k]["classify"]     = lst[3]
        res_dict[k]["gaussian"]     = lst[4]
        res_dict[k]["cnn"]          = lst[5]
        res_dict[k]["math"]         = lst[6]
        res_dict[k]["classes"]      = lst[7]
        res_dict[k]["statements"]   = lst[8]
    return res_dict

"""
This class provides the meta information of the datasets
All meta information are stored in a separate json file
All methods are static and return the specific info given the dataset name
"""
class DatasetMeta():
    dataset_directory = 'dataset/'
    dataset_img_directory = dataset_directory + 'img/'
    dataset_data_directory = dataset_directory + 'data/'

    #the order is used in creating the dataset icon
    datasets = ['bi_linear', 'bi_moon', 'bi_circle', 'bi_xor',
                'bi_spiral', 'multi_three', 'multi_four', 'multi_circles',
                'cnn_mnist', 'cnn_cifar10', 'reg_inform', 'reg_redun']
    metadata = load_dataset_metainfo(dataset_directory)

    @staticmethod
    def isDataset(dataset):
        return dataset in DatasetMeta.metadata

    @staticmethod
    def getDatasetIndex(dataset):
        for i, ds in enumerate(DatasetMeta.datasets):
            if ds == dataset:
                return i
        return -1

    @staticmethod
    def isGaussian(dataset):
        return DatasetMeta.metadata[dataset]["gaussian"] if DatasetMeta.isDataset(dataset) else False

    @staticmethod
    def isClassify(dataset):
        return DatasetMeta.metadata[dataset]["classify"] if DatasetMeta.isDataset(dataset) else False

    @staticmethod
    def isRegression(dataset):
        return not DatasetMeta.isClassify(dataset)

    @staticmethod
    def isBinaryMath(dataset):
        return "bi" in DatasetMeta.metadata[dataset]["name"] if DatasetMeta.isDataset(dataset) else False

    @staticmethod
    def isCNN(dataset):
        return DatasetMeta.metadata[dataset]["cnn"] if DatasetMeta.isDataset(dataset) else False

    @staticmethod
    def isMath(dataset):
        return DatasetMeta.metadata[dataset]["math"] if DatasetMeta.isDataset(dataset) else False

    @staticmethod
    def getClasses(dataset, variation=0):
        return DatasetMeta.metadata[dataset]["classes"][variation] if DatasetMeta.isCNN(dataset) else []

    @staticmethod
    def getDatasetName(dataset):
        return DatasetMeta.metadata[dataset]["name"] if DatasetMeta.isDataset(dataset) else ""

    @staticmethod
    def getDatasetTask(dataset, variation=0):
        return DatasetMeta.metadata[dataset]["task"][variation] if DatasetMeta.isCNN(dataset) \
               else DatasetMeta.metadata[dataset]["task"] if DatasetMeta.isDataset(dataset) \
               else ""

    @staticmethod
    def getDatasetDifficulty(dataset, variation=0):
        return DatasetMeta.metadata[dataset]["difficulty"][variation] if DatasetMeta.isDataset(dataset) else 0

    @staticmethod
    def getDatasetMetaInfo(dataset, variation=0):
        return (DatasetMeta.getDatasetName(dataset),
                DatasetMeta.getDatasetTask(dataset, variation),
                DatasetMeta.getDatasetDifficulty(dataset, variation))

    @staticmethod
    def getVaryStatement(dataset, var):
        statements = ["No Noise", "Low", "Medium", "High"]
        f_s = "Noise: {vary}"
        if DatasetMeta.isCNN(dataset):
            f_s = DatasetMeta.metadata[dataset]["statements"][-1]
            statements = DatasetMeta.metadata[dataset]["statements"][:-1]
        return f_s.format(vary=statements[var])
