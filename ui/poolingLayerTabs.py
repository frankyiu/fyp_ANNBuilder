import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class PoolingLayerTabs(QTabWidget):
    def __init__(self, parent = None):
        super(PoolingLayerTabs, self).__init__(parent)

        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()

        self.addTab(self.tab1, 'Pooling layer')
        self.addTab(self.tab2, 'Max-pooling')
        self.addTab(self.tab3, 'Average-pooling')

        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        layout.addWidget(QLabel('A pooling layer is usually placed after a convolutional layer to refine its ouput feature maps.'))      
        layout.addWidget(QLabel('By doing so:\n1. feature maps with smaller sizes are obtained and they would relief the burden of computation in later stages\n2. the information contained in the input feature maps is mostly retained and abstracted'))        
        layout.addWidget(QLabel('Max-pooling and average-pooling are the two most common pooling schemes used to process feature maps obtained from convolution.'))        

        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel('Max-pooling is the scheme of generating a refined matrix from an input feature map by taking the maximum of the values in each application of a kernel with a certain size as a cell of the refined matrix over the course of sweeping through the input feature map from the top-left corner to the bottom-right corner.'))        
        
        layout.addWidget(QLabel('Here is a 4x4 input feature map:'))        
        
        setup_graph = QLabel()
        setup_graph.setPixmap(QPixmap('./png/PoolingLayer/MaxPooling/setup.png'))
        layout.addWidget(setup_graph)
        
        layout.addWidget(QLabel('Let see the demostration of max-pooling on the feature map above with a 2x2 kernel and a stride of 2:'))        

        maxPooling_gif = QLabel()
        maxPooling_movie = QMovie('./gifs/PoolingLayer/MaxPooling/maxPooling.gif')
        maxPooling_gif.setMovie(maxPooling_movie)
        maxPooling_movie.start()
        layout.addWidget(maxPooling_gif)
        
        self.tab2.setLayout(layout)
        
    def tab3UI(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel('Average-pooling is the scheme of generating a refined matrix from an input feature map by taking the average of the values in each application of a kernel with a certain size as a cell of the refined matrix over the course of sweeping through the input feature map from the top-left corner to the bottom-right corner.'))        
        
        layout.addWidget(QLabel('Here is a 4x4 input feature map:'))        

        setup_graph = QLabel()
        setup_graph.setPixmap(QPixmap('./png/PoolingLayer/AveragePooling/setup.png'))
        layout.addWidget(setup_graph)
        
        layout.addWidget(QLabel('Let see the demostration of average-pooling on the feature map above with a 2x2 kernel and a stride of 2:'))        
        
        maxPooling_gif = QLabel()
        maxPooling_movie = QMovie('./gifs/PoolingLayer/AveragePooling/avgPooling.gif')
        maxPooling_gif.setMovie(maxPooling_movie)
        maxPooling_movie.start()
        layout.addWidget(maxPooling_gif)
        
        qna_layout = QHBoxLayout()
        
        qna_layout.addWidget(QLabel('What is X?'))
        
        le = QLineEdit()
        le.setObjectName('ans')
        qna_layout.addWidget(le)
        
        pb = QPushButton('Submit')
        pb.setObjectName('submit_btn')
        pb.clicked.connect(self.check_ans)
        qna_layout.addWidget(pb)
        
        qna_layout_widget = QWidget()
        qna_layout_widget.setLayout(qna_layout)
        
        layout.addWidget(qna_layout_widget)
        
        output_lb = QLabel()
        output_lb.setObjectName('output_lb')
        
        layout.addWidget(output_lb)
        
        self.tab3.setLayout(layout)
        
    def check_ans(self):
        if self.tab3.findChild(QLineEdit, 'ans').text() == '7':
            self.tab3.findChild(QLabel, 'output_lb').setText('True!')
        else:
            self.tab3.findChild(QLabel, 'output_lb').setText('False, please try again!')
