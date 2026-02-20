from NNBComponent import NNBComponent

class NNBNeuron(NNBComponent):
    '''
    Connectable
    Can be
    - 1D (represented as a circle) or
    - 2D (represented as a square and usually called "Feature Map")
    '''
    def __init__(self, name):
        NNBComponent.__init__(self, name)
        self.connections = {}
        self.layer = None
        self.isBias = False

