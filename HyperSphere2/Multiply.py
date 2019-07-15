import itertools
import functools
import numpy as np
from itertools import product
from functools import reduce
from Operation import Operation
from Loop import Loop
from hyperSphere import hyperSphere

class Multiply(Operation):
    """
        Inheritance
        ___________
        see Operation.py

       Parameters
        ___________
        hyperSpheres::iterable(hyperSphere)

        Attributes
        ___________
        self.dims::int : dimenstion of the space needed to evaluate Multiply
        self.str_func::str : resulting code from construction

        Methods
        __________
        self.make_product : generator function -> code to produce str_func
        self.container_hyper_rectangle(conatiner) : take hyperSphere elements and pair in hyper rectangle
        self.conatiner_vector(x::hyper_rectangle) : construct product vector from rectangle
        self.sample(x::int)::np.array : evaluate self at a random sample

        self(x::np.array)::np.array
        self(x::Loop)::np.ndarray
        self(x::hyperSphere)::np.ndarray
    """
    def __init__(self, *hyperSpheres):
        hyperSpheres = tuple(self.mhSfi(hyperSpheres[0])) if isinstance(hyperSpheres[0], int) else hyperSpheres
        super(Multiply, self).__init__(*hyperSpheres)
        self.str_func = self.make_product()
        exec(self.str_func)
        self.evaluate_function = locals()['hyper_sphere']
        self.dims = sum(self.DomainDims) + 1

    def __call__(self, theta):
        if isinstance(theta, Loop):
            assert self.dims == theta().shape[1]
            return np.apply_along_axis(self, 1, theta())
        elif isinstance(theta, hyperSphere):
            assert self.dims == theta.dims
            sample = theta.sample(500)
            return np.apply_along_axis(self, 1, sample)
        else:
            return np.apply_along_axis(self.evaluate_function, 1, theta) 

    def sample(self, sample_size):
        sample_domain = np.random.random_sample(size = (self.dims, sample_size))
        return np.apply_along_axis(self, 0, sample_domain).T

    def make_product(self):
        shift_ = self.shift()
        container_ = self.container(shift_)
        container_hyper_rectangle_ = self.container_hyper_rectangle(container_)
        container_vector_ = self.container_vector(container_hyper_rectangle_)
        function_head = "def hyper_sphere(theta):"
        function_body = f"""{container_vector_}"""[1:-1].replace("'", "").replace("\n", ",")
        function_complete = f"""{function_head}
            return {function_body}"""
        return function_complete

    def container_hyper_rectangle(self, container_):
        hyper_rectangle = np.empty(shape = (self.RangeDims), dtype = "O")
        cartesian_product = product(*self.basis_bounds)
        for index in cartesian_product:
            for sub_index, vector in zip(index, container_):
                if hyper_rectangle[index] == None:
                    hyper_rectangle[index] = f"{vector[sub_index]}"
                else:
                    hyper_rectangle[index] += f"*{vector[sub_index]}"
        
        return hyper_rectangle

    def container_vector(self, container_hyper_rectangle_):
        vector_shape = reduce(lambda x,y: x+y,self.DomainDims) + 1
        container_vector = np.empty(shape = (vector_shape), dtype = "O")
        cartesian_product = product(*self.basis_bounds)
        for index in cartesian_product:
            A = reduce(lambda x,y: x+y, index)
            print(A, index)
            if container_vector[A] == None:
                container_vector[A] = f"{container_hyper_rectangle_[index]}"
            else:
                container_vector[A] += f"+{container_hyper_rectangle_[index]}"
        return container_vector

    def mhSfi(self, int_):
        int_-=1
        linear_form = [] if int_ % 2 != 1 else [hyperSphere(2)]
        quadradic_forms = [hyperSphere(3) for _ in range(int_ // 2)]
        return linear_form + quadradic_forms

if __name__ == "__main__":
    n = 2 
    linear = hyperSphere(2)
    quadratic = [hyperSphere(3) for _ in range(n)]
    m = Multiply(linear, *quadratic)
