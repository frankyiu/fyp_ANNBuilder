import numpy as np

"""
customized one hot encoding
      arr:  np array of size (N, )
n_classes:  number of columns exist in the sparse matrix
     mask:  remove zero columns or not, used by CNN dataset
"""
def one_hot(arr, n_classes, mask=True):
    res = np.eye(n_classes)[arr.astype(int)]
    if mask:
        masks = (res==0).all(0)
        res = res[:, ~masks]
    return res

def reverse_one_hot(arr):
    return np.argmax(arr, axis=1).reshape(-1).astype(int)

"""
a method to split the dataset into several parts
    arr:  np array
  n_arr:  number of sub array to be divided from arr
"""
def split_evenly(arr, n_arr):
    n = int(len(arr)/n_arr)
    return [arr[i:i+n] for i in range(0, len(arr), n)]
