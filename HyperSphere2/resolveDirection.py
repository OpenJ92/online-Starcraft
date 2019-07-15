import numpy as np
from onlineDB.HyperSphere2.hyperSphere import hyperSphere
from onlineDB.HyperSphere2.Polynomial import Polynomial
from sklearn.mixture import GaussianMixture

class resolveDirection:
    """
        Parameters
        ___________
        vector::np.array : target vector
        hyper_sphere::hyperSphere : set of angularly independent vectors in space of self.vector
        sub_space_hyper_sphere : set of angularly independent vectors in domain of self.hyper_sphere
        iterations : maximum number of steps to take in method self.optimize
        o : result of resolveDirection optimization
        
        Attributes
        __________

        Methods
        _________
        self.optimize : carry out the process of resolving direction of target self.vector
        self.sample_domain_sub_domain(domain::(None|np.array),samples::int)::(::np.array, ::np.array)
        self.domain_ball(sub_domain::np.array, radius::float)::np.array
        self.make_domain_range(domain::np.array, domain_ball::np.array)::(::np.array, ::np.array)
        self()::np.array : returns values of self.o
    """
    def __init__(self, vector, iterations = 200):
        self.vector = vector if not isinstance(vector,  Polynomial) else vector.coefficents
        assert np.linalg.norm(self.vector) > 0
        self.hyper_sphere = hyperSphere(len(self.vector))
        self.sub_space_hyper_sphere = hyperSphere(len(self.vector) - 1)
        self.iterations = iterations
        self.o = self.optimize()

    def __call__(self):
        return self.o

    def optimize(self):
        for i in range(self.iterations):
            domain_, sub_domain = self.sample_domain_sub_domain(domain_ if i > 0 else None)
            domain_ball = self.domain_ball(sub_domain, i + 1)
            domain_, range_ = self.make_domain_range(domain_, domain_ball)
            measure__index, domain_ = self.measure_(domain_, range_)
        return domain_ % np.pi*2
        
    def sample_domain_sub_domain(self, domain = None, samples = 100):
        if isinstance(domain, type(None)):
            domain = 2*np.pi*np.random.random_sample(size=(samples, self.hyper_sphere.dims-1))
        sub_domain = 2*np.pi*np.random.random_sample(size=(samples, self.hyper_sphere.dims-2))
        return domain, sub_domain

    def domain_ball(self, sub_domain, radius = .5):
        domain_ball = self.sub_space_hyper_sphere(sub_domain)
        domain_ball = np.apply_along_axis(lambda x: (.5/radius)*np.random.random_sample()*x, 1, domain_ball)
        return domain_ball

    def make_domain_range(self, domain, domain_ball):
        domain_ = np.concatenate([q + domain_ball for q in domain], axis=0)
        range_ = self.hyper_sphere(domain_)
        return domain_, range_

    def measure_(self, domain_, range_, n=20):
        measure__ = np.apply_along_axis(np.linalg.norm, 1, range_ - self.vector)
        measure__index = np.argpartition(measure__, n)
        return measure__index, domain_[measure__index[:n]]

if __name__ == "__main__":
    vector = hyperSphere(7)([np.pi/3, 0, 0, 0, 0, 0])
    poly = Polynomial(vector)
    rD = resolveDirection(poly)
