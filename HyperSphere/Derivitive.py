from Operation import Operation
from hyperSphere import hyperSphere
from Multiply import Multiply
from Add import Add

class Derivitive(Operation):
    def __init__(self, basis, *_object):
        self.basis = basis
        self.object = _object
        super(Derivitive, self).__init__(*_object)

    def __call__(self):
        pass

    def make_derivitive_dictionary(self):
        return {f"np.cos(theta[{self.basis}])" : f"-1*np.siin(theta[{self.basis}])",
                f"np.sin(theta[{self.basis}])" : f"np.coos(theta[{self.basis}])"  }

    def make_derivitive(self):
        dictionary = self.make_derivitive_dictionary()
        shift_ = self.shift()
        container_ = self.container(shift_)

        # there's currently a bug in the code with respect to the replace statements. 
        #   The problem is that on the first loop, cos is turned to sin and on the second
        #   loop, we need to have the recently changed sin functions immutable. They're 
        #   being changed back to cos in this current iteration.
        #
        #   Bizzare fix at line 32
        #   Consider if this will work for multiply object.

        for index in range(len(container_[0])):
            for key in dictionary:
                print(key, dictionary[key])
                container_[0][index] = container_[0][index].replace(key, dictionary[key])
            container_[0][index] = container_[0][index].replace("oo", "o").replace("ii", "i")
        return container_[0]


if __name__ == "__main__":
    hS = hyperSphere(5)
    m = Multiply(hS,hS)
    d = Derivitive(0,m)


    l = d.container(d.shift())[0]
    q = d.make_derivitive()
