import numpy as np
from functools import reduce
from onlineDB.HyperSphere.hyperSphere import hyperSphere

class Polynomial:
    def __init__(self, coefficents):
        self.coefficents = coefficents
        self.order = len(self.coefficents) -1

    def __call__(self, x):
        f = lambda q: [self.coefficents[element]*(q**element) for element in range(self.order + 1)]
        terms = f(x) 
        return reduce(lambda x, y: x+y, terms)

if __name__ == "__main__":
    hS = hyperSphere(3)
    poly = Polynomial(np.array([1,2,3]))

