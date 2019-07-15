import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
from hyperSphere import hyperSphere
from Multiply import Multiply
from Add import Add
from Loop import Loop
from resolveDirection import resolveDirection

def test_unit(hypS, sample_size):
    sample = np.pi*2*np.random.random_sample((sample_size, hypS.dims-1))
    A = np.apply_along_axis(hypS, 1, sample)
    B = np.apply_along_axis(np.linalg.norm, 1, A)
    return B

def test_angle(hypS, sample_size):
    pass

def plot_Loop(*loop):
        fig = plt.figure()
        ax = plt.axes(projection='3d')
        A = np.concatenate([_() for _ in loop], 0)
        ax.scatter3D(*[A[:,i] for i in range(A.shape[1])])
        plt.show()

if __name__ == "__main__":
    hS = hyperSphere(2)
    hS1 = hyperSphere(3)
    n = 2
    m = Multiply(hS, *[hS1 for i in range(n)])
    m_ = Multiply(hS, hS)
    m__ = Multiply(7)
    a = Add(hS, *[hS1 for i in range(n)])
    
    sample = np.ones(3)

    loops = [Loop(sample) for _ in range(4)]
    hyper_spheres = [hyperSphere(2), hyperSphere(3), hyperSphere(3)]

    
