import itertools
import functools
import numpy as np
from itertools import product, zip_longest
from functools import reduce
from Operation import Operation
from Loop import Loop
from hyperSphere import hyperSphere

class Add(Operation):
    """
    Inheritance
    ___________
    see Operation.py

    Parameters
    ___________
    hyperSpheres::iterable(hyperSphere)

    Attributes
    __________
    self.dims::int : dimenstion of the space needed to evaluate Multiply
    self.str_func::str : resulting code from construction

    Methods
    __________
    self.make_add : generator function -> code to produce str_func
    self.container_vector(container) : construct add vector from container

    self(x::np.array)::np.array
    self(x::Loop)::np.ndarray
    self(hyperSphere)::np.ndarray
    """
    def __init__(self, *hyperSpheres):
        super(Add, self).__init__(*hyperSpheres)
        self.str_func = self.make_add()
        exec(self.str_func)
        self.evaluate_function = locals()['hyper_sphere']
        self.dims = sum(self.DomainDims)
    
    def __call__(self, theta):
        if isinstance(theta, Loop):
            assert self.dims == theta().shape[1]
            return np.apply_along_axis(self, 1, theta())
        elif isinstance(theta, hyperSphere):
            assert self.dims == theta.dims
            sample = theta.sample(500)
            return np.apply_along_axis(self, 1, sample)
        else:
            return np.array(self.evaluate_function(theta))
    
    def sample(self, sample_size):
        sample_domain = np.random.random_sample(size = (self.dims, sample_size))
        return np.apply_along_axis(self, 0, sample_domain).T

    def make_add(self):
        shift_ = self.shift()
        container_ = self.container(shift_)
        container_vector_ = self.container_vector(container_)

        function_head = "def hyper_sphere(theta):"
        function_body = f"""{container_vector_}"""[1:-1].replace("'", "").replace("\n", ",").replace(" +", "")
        function_complete = f"""{function_head}
            return {function_body}"""

        return function_complete

    def container_vector(self, container_):
        container_ = [reversed(element) for element in container_]
        container_vector_ = np.empty(shape = max(self.RangeDims), dtype = "O")
        for index, elements in enumerate(zip_longest(*container_, fillvalue = '')):
            expression = reduce(lambda x,y: f"{x}+{y}", elements)
            container_vector_[index] = expression
        return container_vector_
