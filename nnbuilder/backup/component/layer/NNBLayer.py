from NNBBlock import NNBBlock


class NNBLayer(NNBBlock):
    def __init__(self, name, dim=1):
        NNBBlock.__init__(self, name)
        self.layerType = "hidden"  # one of three types : input, hidden, output, by default hidden
        self.dim = dim

        # model parameters
        self.actFunc = "Sigmoid"

