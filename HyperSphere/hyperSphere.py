import numpy as np

class hyperSphere:
    """
        Parameters
        ____________
        dims::int : Expected range dimension of the constructed hyper sphere
        offset::np.array : Global point upon which we generate our hyper sphere

        Attributes
        ___________
        self.domain_dims::np.array : the dimension of the space needed to evaluate hyper sphere
        self.str_func::str : resulting code from construction
        self.hyper_sphere::function : resulting callable function generated by mhs
        
        Methods
        __________
        self.sample(sample_size::int)::np.array : evaluate self at a random sample
        self(x::np.array|hyperSphere|Bezier)::np.array : evaluate self over a particular domain
    """
    def __init__(self, dims, offset = None):
        self.dims = dims
        self.domain_dims = self.dims - 1
        self.str_func = self.mhs(dims)
        exec(self.str_func)
        self.hyper_sphere = locals()['hyper_sphere']
        self.offset = np.zeros(self.dims) if not offset else offset

    def __call__(self, theta):
        if isinstance(theta, type(self)):
            assert self.domain_dims == theta.dims
            sample = theta.sample(500)
            return np.apply_along_axis(self, 1, sample) + self.offset
        elif isinstance(theta, np.ndarray) and len(theta.shape) == 2:
            return np.apply_along_axis(self.hyper_sphere, 1, theta)
        else:
            return np.array(self.hyper_sphere(theta))
    
    def sample(self, sample_size):
        sample_domain = np.random.random_sample(size = (self.dims-1, sample_size)).T
        return self(sample_domain)

    def mhs(self, dims):
        function_head = f'def hyper_sphere(theta):'
        function_body = ''
        for j in range(0, dims-1):
            function_body += f"np.cos(theta[{j}])*"
        function_body += '1,'
        for i in range(0, dims-1):
            for j in range(i, dims-1):
                if i == j:
                    function_body += f"np.sin(theta[{j}])"
                else:
                    function_body += f"*np.cos(theta[{j}])"
            function_body += '*1,'
        complete_function = f"""{function_head}
            return {function_body}"""
        return complete_function

if __name__ == "__main__":
    hS = hyperSphere(2)
    hS_ = hyperSphere(300)
