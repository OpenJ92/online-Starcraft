import numpy as np
from hyperSphere import hyperSphere
from Bezier import bezierCurve
from controlPoints import controlPointsUniformRandomEnclosingPrism

class Loop:
    """
    Parameters
    __________
    domain_in::np.array : initial location in domain space to generate loop
    domain_out::np.array : domain_out % np.pi*2 == domain_in must be satisfied
    dim::int : dimensions of the resulting Loop
    control_points::controlPoints|np.array : control point set to generate Bezier Curve
    bezier::Bezier : family of functions parameterized on self.control_points
    hyper_sphere::hyperSphere : hyper surface to map bezier to
    offset::np.array : vector by which we carry a global translation on loop

    Attributes
    ___________

    Methods
    ___________
    self() : evaluate loop over generated domain.
    """
    def __init__(self, domain_in,
            control_points=controlPointsUniformRandomEnclosingPrism,
            samples = 200,
            offset = None):
        self.domain_in = domain_in
        self.domain_out = self.domain_in + np.pi*2
        self.dims = len(self.domain_in) + 1
        self.control_points = control_points(self.domain_in, self.domain_out)(5)
        self.bezier = bezierCurve(self.domain_in, self.domain_out, self.control_points).sample(samples)
        self.hyper_sphere = hyperSphere(len(domain_in) + 1)
        self.offset = np.zeros(self.bezier.shape[1] + 1) if not offset else offset 

    def __call__(self):
        return np.apply_along_axis(self.hyper_sphere, 1, self.bezier) + self.offset

if __name__ == "__main__":
    sample = np.ones(4)
    adjust = np.ones_like(sample)*np.pi*2

    loops = [Loop(sample) for _ in range(9)]
    hyper_spheres = [hyperSphere(2), hyperSphere(3), hyperSphere(3)]
