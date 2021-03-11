from NNBComponent import NNBComponent

class NNBConnection(NNBComponent):
    '''


    '''
    def __init__(self, name, component1, component2):
        NNBComponent.__init__(self, name)
        self.component1 = component1
        self.component2 = component2

    def updateConnectionPos(self):
        #To be overriden
        pass

