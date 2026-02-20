from tensorflow.keras.optimizers import Adadelta, Adagrad, SGD, RMSprop, Adam

"""
A wrapper class to convert string to optimzer
"""
class Optimizer():
    def __init__(self, optim, lr, decay):
        self.optim = optim
        self.lr = lr
        self.lr_decay = decay

    def getOptim(self):
        str = self.optim
        fun_ptr = None
        if str == u"AdaDelta":
            fun_ptr = Adadelta
        elif str == u"AdaGrad":
            fun_ptr =  Adagrad
        elif str == u"Adam":
            fun_ptr =  Adam
        elif str == u"Full-Batch":
            pass
        elif str == u"Mini-Batch":
            pass
        elif str == u"Momentum":
            pass
        elif str == u"RMSProp":
            fun_ptr =  RMSprop
        elif str == u"SGD":
            fun_ptr =  SGD

        return fun_ptr(learning_rate=self.lr, decay=self.lr_decay)
