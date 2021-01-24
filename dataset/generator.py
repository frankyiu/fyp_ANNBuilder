import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import *

rand_state = 2021

def plot(df, filename):
    plt.rcParams['axes.facecolor'] = '#e9ebeb'
    plt.rcParams['savefig.facecolor'] = '#3d3d3d'
    color = {0:'blue', 1:'darkorange', 2:'green', 3:'red'}
    _, ax = plt.subplots()
    for key, group in df.groupby('label'):
        group.plot(ax=ax, kind='scatter', x='x', y='y', color=color[key], edgecolors='white', s=30)

    plt.savefig('img/'+filename)
    pass

#linear classifier, linearly separable
def binary_1():
    name = 'bi_linear'
    n_sample = 400
    X,y = make_blobs(n_samples=n_sample,centers=2, center_box=(-4,4), n_features=2,random_state=rand_state)
    df = pd.DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
    plot(df, name+'.png')
    df.to_csv(name+".csv", index=False)
    pass

#non-linear classifier, 3rd degree polynomial
def binary_2():
    name = 'bi_moon'
    n_sample = 400
    noise = 0.04
    X,y = make_moons(n_samples=n_sample,noise=noise,random_state=rand_state)
    df = pd.DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
    plot(df, name+'.png')
    df.to_csv(name+".csv", index=False)
    pass

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
    pass

#non-linear classifier, xor function
def binary_4():
    name = 'bi_xor'
    n_sample = 400
    randgen = np.random.RandomState(rand_state)
    X = randgen.randn(n_sample, 2)
    y = np.array(np.logical_xor(X[:, 0] > 0, X[:, 1] > 0),dtype=int)
    df = pd.DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
    plot(df, name+'.png')
    df.to_csv(name+".csv", index=False)
    pass

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
    pass

#linear classifier, 3 class
def multi_1():
    name = 'multi_three'
    n_sample = 600
    X,y = make_blobs(n_samples=n_sample,centers=3, center_box=(-4,4), n_features=2,random_state=rand_state)
    df = pd.DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
    plot(df, name+'.png')
    df.to_csv(name+".csv", index=False)
    pass

#linear classifier, 4 class
def multi_2():
    name = 'multi_four'
    n_sample = 600
    X,y = make_classification(n_samples=n_sample, n_classes=4, n_clusters_per_class=1, n_features=2, \
                              flip_y=0, n_redundant=0, n_informative=2, class_sep=2.0, random_state=rand_state)
    df = pd.DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
    plot(df, name+'.png')
    df.to_csv(name+".csv", index=False)
    pass

#non-linear classifier, 4 class circle
def multi_3():
    name = 'multi_circles'
    n_sample = 800
    X,y = make_gaussian_quantiles(n_samples=n_sample,n_features=2, n_classes=4, random_state=rand_state)
    df = pd.DataFrame(dict(x=X[:,0], y=X[:,1], label=y))
    plot(df, name+'.png')
    df.to_csv(name+".csv", index=False)
    pass


binary_1()

binary_2()

binary_3()

binary_4()

binary_5()

multi_1()

multi_2()

multi_3()
pass
