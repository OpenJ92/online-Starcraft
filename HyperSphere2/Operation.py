from hyperSphere import hyperSphere
from itertools import product

class Operation:
    """
    Parameters
    ___________
    hyperSpheres::itterable(hyperSphere)

    Attributes
    __________
    self.hyperSpheres::itterable(hyperSphere) : set of hyperSpheres upon which child operation will act on.
    self.terms::int : number of term in child operation
    self.RangeDims::itterable(int) : list of range dimension for each hyper sphere
    self.DomainDim::itterable(int) : list of domain dimension for each hyper sphere
    self.IndexDim::itterable(int) : list of max index for each hyper sphere
    self.basis_bounds:itterable(itterable(int)) : set of ranges for each domain list
    self.cartesian_product::itterable : index construction for looping over hyper objects

    Methods
    ________
    self.shift : iterate over hyperSphere objects and augment code s.t. there exists no overlap in domain labels
    self.container : take string vector components from hyperSphere str_func and place into array
    """
    def __init__(self, *hyperSpheres):
        self.hyperSpheres = hyperSpheres
        self.terms = len(self.hyperSpheres)
        self.RangeDims = [hS.dims for hS in self.hyperSpheres]
        self.DomainDims = [hS.dims-1 for hS in self.hyperSpheres]
        self.IndexDims = [dom-1 for dom in self.DomainDims]
        self.basis_bounds = [range(upper) for upper in self.RangeDims]
        self.cartesian_product = product(*self.basis_bounds)

    def shift(self):
        shift_ = [hS.str_func[44:] for hS in self.hyperSpheres]
        for term in range(1, self.terms):
            largest_index = sum(self.IndexDims[:term]) + term 
            for index in reversed(range(self.DomainDims[term])):
                shift_[term] = shift_[term].replace(f"[{index}]", f"[{index + largest_index}]")
        return shift_

    def container(self, shift_):
        return [element.split(',')[:-1] for element in shift_]

