import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class OptimizersTabs(QTabWidget):
    def __init__(self, parent = None):
        super(OptimizersTabs, self).__init__(parent)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()       
        self.tab6 = QWidget()
        self.tab7 = QWidget()

        self.addTab(self.tab1, 'Introduction')
        self.addTab(self.tab2, 'Batch Gradient Descent - BGD')
        self.addTab(self.tab3, 'Pros and Cons of BGD')
        self.addTab(self.tab4, 'Stochastic Gradient Descent - SGD')
        self.addTab(self.tab5, 'Pros and Cons of SGD')
        self.addTab(self.tab6, 'Mini-batch Gradient Descent - MBGD')
        self.addTab(self.tab7, 'Other Advanced Optimizers')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()
        self.tab4UI()
        self.tab5UI()
        self.tab6UI()
        self.tab7UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('An optimizer is an optimization scheme used to minimize the loss function.'))
        layout.addWidget(QLabel('There are many optimizers available, which behave differently.'))
        layout.addWidget(QLabel('The three most common and basic ones are going to be examined in detail in the following tabs.'))
        
        self.tab1.setLayout(layout)

    def tab2UI(self):               # https://towardsdatascience.com/batch-mini-batch-stochastic-gradient-descent-7a62ecba642a
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('The workflow of batch gradient descent:\n1. feed all the training examples into the neural network under training one-by-one\n2. obtain the mean gradient of all the training examples\n3. update the weights accordingly\n4. repeat 1 to 3 till the training is terminated'))
        
        layout.addWidget(QLabel('How loss varies in BGD:'))

        bgd_gif = QLabel()
        bgd_movie = QMovie('./gifs/Optimizers/BatchGradientDescent/bgd.gif')
        bgd_gif.setMovie(bgd_movie)
        bgd_movie.start()
        layout.addWidget(bgd_gif)

        self.tab2.setLayout(layout)
        
    def tab3UI(self):               # https://towardsdatascience.com/batch-mini-batch-stochastic-gradient-descent-7a62ecba642a
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Pros of BGD:\nAs illustrated, the training does not take much detour and converges to the optimum almost in a straight line manner.\nIt means the algorithm is relatively tolerant to noise.'))
        layout.addWidget(QLabel('Cons of BGD:\n1. It takes up a significant amount of computer memory if the size of the training set is considerable.\n2. Each iteration of weight update could be extremely slow.'))
        layout.addWidget(QLabel('Verdict: Batch gradient descent is only suitable for small datasets.'))

        self.tab3.setLayout(layout)

    def tab4UI(self):               # https://towardsdatascience.com/batch-mini-batch-stochastic-gradient-descent-7a62ecba642a
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('The workflow of stochastic gradient descent:\n1. feed one example of the training set into the neural network under training at a time\n2. calculate the gradient\n3. do the weight update accordingly\n4. repeat 1 to 3 for each trainng example\n5. after a pass of the entire training set, namely a epoch, start a new epoch by repeating 1 to 4 till the training is terminated'))
           
        layout.addWidget(QLabel('How loss varies in SGD:'))

        sgd_gif = QLabel()
        sgd_movie = QMovie('./gifs/Optimizers/StochasticGradientDescent/sgd.gif')
        sgd_gif.setMovie(sgd_movie)
        sgd_movie.start()
        layout.addWidget(sgd_gif)   
                
        self.tab4.setLayout(layout)
        
    def tab5UI(self):               # https://towardsdatascience.com/batch-mini-batch-stochastic-gradient-descent-7a62ecba642a
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Pros of SGD:\n1. It takes up a little  amount of computer memory.\n2. The time needed per each weight update is shorter.'))
        layout.addWidget(QLabel('Cons of SGD:\nAs illustrated, the training takes much detour, as it converges to the optimum in a sawtooth manner.\nIt means the algorithm is relatively sensitive to noise.'))
        layout.addWidget(QLabel('Verdict: Stochastic gradient descent works fine with large datasets.'))
        
        self.tab5.setLayout(layout)

    def tab6UI(self):               # https://towardsdatascience.com/batch-mini-batch-stochastic-gradient-descent-7a62ecba642a
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Mini-batch gradient descent is a compromise between batch gradient descent and stochastic gradient descent.'))
        layout.addWidget(QLabel('The workflow of mini-batch gradient descent:\n1. divide the training set into mini-batches as per the batch size given\n2. feed all the examples of a mini-batch into the neural network under training one-by-one\n3. obtain the average gradient of the mini-batch\n4. do the weight update accordingly\n5. repeat 2 to 4 for each mini-batch\n6. after each mini-batch is visited, repeat 1 to 5 till the training is terminated'))
        
        layout.addWidget(QLabel('How loss varies in MBGD:'))

        mbgd_gif = QLabel()
        mbgd_movie = QMovie('./gifs/Optimizers/MiniBatchGradientDescent/mbgd.gif')
        mbgd_gif.setMovie(mbgd_movie)
        mbgd_movie.start()
        layout.addWidget(mbgd_gif)   
        
        layout.addWidget(QLabel('As illustrated, the training takes less detour than stochastic gradient descent and need less computer memory than batch gradient descent to operate.'))
        layout.addWidget(QLabel('Mini-batch gradient descent hence is the most popular optimizers among the three in reality.'))

        self.tab6.setLayout(layout)
    
    def tab7UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('Many optimizers other than the three introduced can also be used in neural network training.'))
        layout.addWidget(QLabel('For examples,\n1. Momentum\n2. Adam\n3. Adagrad\n4. Adadelta\n5. RMSProp'))
        layout.addWidget(QLabel('The working principles and the implementations of these optimizers can be found online easily and many of them are in fact derived from the optimizers just introduced in detail.'))
        
        self.tab7.setLayout(layout)
            
