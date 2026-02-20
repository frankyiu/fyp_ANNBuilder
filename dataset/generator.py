import matplotlib.pyplot as plt
import numpy as np

rand_state = 2021


def plot_np(data, filename=None, isClassify=True, fig=None, ax=None, dot_size=60):
    plt.rcParams['savefig.facecolor'] = '#3d3d3d'

    colors = {0:'blue', 1:'darkorange', 2:'green', 3:'red'}
    if fig is None or ax is None:
        fig, ax = plt.subplots()
    else:
        fig.patch.set_facecolor('#3d3d3d')

    if isClassify:
        for key,color in colors.items():
            class_data = data[data[:,-1]==key]
            ax.scatter(x=class_data[:,0], y=class_data[:,1], color=color, edgecolors='white', s=dot_size)
    else:
        ax.scatter(x=data[:,0], y=data[:,1], color='blue', edgecolors='white', s=dot_size)

    ax.axis('off')
    plt.axis('off')
    if filename is not None:
        plt.savefig(filename)
    return fig, ax


def plot(df, filename, isClassify=True):
    data = df.to_numpy()
    fig, _ = plot_np(data, 'img/'+filename, isClassify)
    plt.close(fig)
    pass

#name, task [], difficulty, classify, gaussian, cnn, math, classes [], statements []

#linear classifier, linearly separable
def binary_1():
    name = 'bi_linear'
    n_sample = 400
    X,y = make_blobs(n_samples=n_sample,centers=2, center_box=(-4,4), n_features=2,random_state=rand_state)
    df = pd.DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
    plot(df, name+'.png')
    df.to_csv(name+".csv", index=False)
    return {name:("Gaussian", "Binary Classification", [61,71,81,91], True, True, False, True, None, None)}

#non-linear classifier, 3rd degree polynomial
def binary_2():
    name = 'bi_moon'
    n_sample = 400
    noise = 0.04
    X,y = make_moons(n_samples=n_sample,noise=noise,random_state=rand_state)
    df = pd.DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
    plot(df, name+'.png')
    df.to_csv(name+".csv", index=False)
    return {name:("Moon", "Binary Classification", [62,72,82,92], True, False, False, True, None, None)}

#non-linear classifier, quadratic in 2 unknown
def binary_3():
    name = 'bi_circle'
    n_sample = 400
    noise = 0.04
    ratio = 0.5
    X,y = make_circles(n_samples=n_sample,noise=noise, factor=ratio,random_state=rand_state)
    df = pd.DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
    plot(df, name+'.png')
    df.to_csv(name+".csv", index=False)
    return {name:("Circle", "Binary Classification", [63,73,83,93], True, False, False, True, None, None)}

#non-linear classifier, xor function
def binary_4():
    name = 'bi_xor'
    n_sample = 400
    randgen = np.random.RandomState(rand_state)
    X = np.zeros((n_sample, 2))
    sector = int(n_sample/4)
    shift = 2
    for i in range(4):
        X[i::4, :] = randgen.randn(sector, 2) + np.array([shift if i%2 else -shift, shift if i <2 else -shift])

    y = np.array(np.logical_xor(X[:, 0] > 0, X[:, 1] > 0),dtype=int)
    def normalize(data):
        return 2 * (data - data.min())/(data.max()-data.min()) - 1
    df = pd.DataFrame(dict(x=normalize(X[:,0]), y=normalize(X[:,1]), label=y))
    plot(df, name+'.png')
    df.to_csv(name+".csv", index=False)
    return {name:("Exclusive OR", "Binary Classification", [64,74,84,94], True, False, False, True, None, None)}

#non-linear classifier, spiral
def binary_5():
    name = 'bi_spiral'
    n_sample = 400
    n_period = 4
    randgen = np.random.RandomState(rand_state)
    theta = np.sqrt(randgen.rand(n_sample))*n_period*np.pi
    r_a = 3*theta
    x_a = np.array([np.cos(theta)*r_a, np.sin(theta)*r_a]).T  #+ randgen.randn(n_sample,2)

    r_b = -3*theta
    x_b = np.array([np.cos(theta)*r_b, np.sin(theta)*r_b]).T  #+ randgen.randn(n_sample,2)

    factor = n_period*np.pi
    res_a = np.append(x_a/factor, np.zeros((n_sample,1)), axis=1)
    res_b = np.append(x_b/factor, np.ones((n_sample,1)), axis=1)
    res = np.append(res_a, res_b, axis=0)
    randgen.shuffle(res)

    X = res[:,:-1]
    y = res[:,-1]

    df = pd.DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
    plot(df, name+'.png')
    df.to_csv(name+".csv", index=False)
    return {name:("Spiral", "Binary Classification", [65,75,85,95], True, False, False, True, None, None)}

#linear classifier, 3 class
def multi_1():
    name = 'multi_three'
    n_sample = 600
    X,y = make_blobs(n_samples=n_sample,centers=3, center_box=(-4,4), n_features=2,random_state=rand_state)
    df = pd.DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
    plot(df, name+'.png')
    df.to_csv(name+".csv", index=False)
    return {name:("Gaussian", "Multiclass Classification", [66,76,86,96], True, True, False, True, None, None)}

#linear classifier, 4 class
def multi_2():
    name = 'multi_four'
    n_sample = 600
    X,y = make_classification(n_samples=n_sample, n_classes=4, n_clusters_per_class=1, n_features=2, \
                              flip_y=0, n_redundant=0, n_informative=2, class_sep=2.0, random_state=rand_state)
    df = pd.DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
    plot(df, name+'.png')
    df.to_csv(name+".csv", index=False)
    return {name:("Gaussian", "Multiclass Classification", [67,77,87,97], True, True, False, True, None, None)}

#non-linear classifier, 4 class circle
def multi_3():
    name = 'multi_circles'
    n_sample = 400
    noise = 0.04
    ratio = 0.5
    ratio2 = 0.75
    X1, y1 = make_circles(n_samples=n_sample,noise=noise, factor=ratio,random_state=rand_state)
    X1, y1 = X1, 1 - y1
    X2, y2 = make_circles(n_samples=n_sample,noise=noise, factor=ratio2,random_state=rand_state+1)
    X2, y2 = 2 * X2, 3 - y2
    def interleave(a, b, n):
        a, b = a.reshape(-1, n), b.reshape(-1, n)
        res = np.empty((a.shape[0]*2, a.shape[1]))
        res[::2, :] = a
        res[1::2, :] = b
        return res
    X = interleave(X1, X2, 2)
    y = interleave(y1, y2, 1).reshape(-1)
    #def normalize(data):
    #    return 4 * (data - data.min())/(data.max()-data.min()) - 2
    #df = pd.DataFrame(dict(x=normalize(X[:,0]), y=normalize(X[:,1]), label=y))
    df = pd.DataFrame(dict(x=(X[:,0]), y=(X[:,1]), label=y))
    plot(df, name+'.png')
    df.to_csv(name+".csv", index=False)
    return {name:("Circle", "Multiclass Classification", [68,78,88,98], True, False, False, True, None, None)}

def regression_1():
    name = 'reg_inform'
    n_sample = 200
    X, y = make_regression(n_samples=n_sample,n_features=1, n_informative=1, noise=30, random_state=rand_state)
    def normalize(data):
        return 2 * (data-data.min())/(data.max()-data.min()) - 1
    df = pd.DataFrame(dict(x=normalize(X[:, 0]), y=normalize(y)))
    plot(df, name+'.png', isClassify=False)
    df.to_csv(name+".csv", index=False)
    return {name:("Informative Feature", "Linear Regression", [69,79,89,99], False, False, False, True, None, None)}

def regression_2():
    name = 'reg_redun'
    n_sample = 200
    X, y = make_regression(n_samples=n_sample,n_features=1, n_informative=0, noise=1, random_state=rand_state)
    def normalize(data):
        return 2 * (data-data.min())/(data.max()-data.min()) - 1
    df = pd.DataFrame(dict(x=normalize(X[:, 0]), y=normalize(y)))
    plot(df, name+'.png', isClassify=False)
    df.to_csv(name+".csv", index=False)
    return {name:("Redundant Feature", "Linear Regression", [69.1,79.1,89.1,99.1], False, False, False, True, None, None)}

#name, task [], difficulty, classify, gaussian, cnn, math, classes [], statements []
def cnn_1():
    name = 'cnn_mnist'
    return {name:("MNIST Digit",
                  ["Binary Classification","Multiclass Classification",
                   "Multiclass Classification","Multiclass Classification"],
                  [69.1,79.1,89.1,99.1], True, False, True, False,
                  [[0,1], [4,7,9], [2,3,5,6,8], [0,1,2,3,4,5,6,7,8,9]],
                  ["0, 1", "4, 7, 9", "2, 3, 5, 6, 8", "All", "Digits: {vary}"])}

def cnn_2():
    name = 'cnn_cifar10'
    return {name:("cifar-10",
                  ["Binary Classification", "Multiclass Classification",
                   "Multiclass Classification", "Multiclass Classification"],
                  [69.1,79.1,89.1,99.1], True, False, True, False,
                  [[3,5], [0,1,8,9], [2,3,4,5,6,7], [0,1,2,3,4,5,6,7,8,9]],
                  ["Cat vs Dog", "Vehicles", "Animals", "All", "Classes: {vary}"])}

if __name__ == "__main__":
    import json
    import pandas as pd
    from sklearn.datasets import *
    binary_4()
    """
    with open("DatasetsMetaInfo.json", "w") as f:
        metadict = {}
        metadict.update(binary_1())
        metadict.update(binary_2())
        metadict.update(binary_3())
        metadict.update(binary_4())
        metadict.update(binary_5())
        metadict.update(multi_1())
        metadict.update(multi_2())
        metadict.update(multi_3())
        metadict.update(cnn_1())
        metadict.update(cnn_2())
        metadict.update(regression_1())
        metadict.update(regression_2())
        f.write(json.dumps(metadict))
    """
