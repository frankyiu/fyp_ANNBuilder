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
        
        style = """
        QWidget{
            background-color: rgb(40, 44, 52);
        }
        QLabel{
            font-size: 16pt;
        }
        QPushButton{
            border: 2px solid black;
            background-color: #F9F7ED;
            color: black;
            border-radius : 12px;
            padding: 2px 4px 2px 4px;
            font-size: 16pt;
        }
        QPushButton::hover
        {
            background-color : #24a0ed;
            color: white;
        }
        QLineEdit::hover
        {
            background-color : white;
        }
        """
        self.setStyleSheet(style)
        
        self.tab1UI()
        self.tab2UI()
        self.tab3UI()

    def tab1UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('A pooling layer is usually placed after a convolutional layer to refine its ouput feature maps.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('By doing so:\n1. feature maps with smaller sizes are obtained and this would relief the burden of computation in later stages\n2. most of the information carried by the input feature maps is retained and abstracted')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        label3 = QLabel('Max-pooling and average-pooling are the two most common pooling schemes used to process feature maps obtained from convolution.')
        label3.setWordWrap(True)
        layout.addWidget(label3)
        
        self.tab1.setLayout(layout)

    def tab2UI(self):
        layout = QVBoxLayout()
            
        label1 = QLabel('Max-pooling is the scheme of generating a refined matrix from an input feature map, by taking the maximum of the values in each application of a filter/kernel on the input feature map as one of the cells of the output refined matrix. The filter/kernel applied generally sweeps across the input feature map from the top-left corner to the bottom-right corner.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('Here is a 4x4 input feature map:')
        label2.setWordWrap(True)
        layout.addWidget(label2)
                
        setup_graph = QLabel()
        setup_graph.setAlignment(Qt.AlignCenter)
        setup_graph.setPixmap(QPixmap('./png/PoolingLayer/MaxPooling/setup.png'))
        layout.addWidget(setup_graph)
        
        label3 = QLabel('Let see the demostration of max-pooling on the feature map above with a 2x2 kernel and a stride of 2:')
        label3.setWordWrap(True)
        layout.addWidget(label3)
        
        maxPooling_gif = QLabel()
        maxPooling_gif.setAlignment(Qt.AlignCenter)
        maxPooling_movie = QMovie('./gifs/PoolingLayer/MaxPooling/maxPooling.gif')
        maxPooling_gif.setMovie(maxPooling_movie)
        maxPooling_movie.start()
        layout.addWidget(maxPooling_gif)
        
        self.tab2.setLayout(layout)
        
    def tab3UI(self):
        layout = QVBoxLayout()
        
        label1 = QLabel('Average-pooling is the scheme of generating a refined matrix from an input feature map, by taking the average of the values in each application of a filter/kernel on the input feature map as one of the cells of the output refined matrix. The filter/kernel applied generally sweeps across the input feature map from the top-left corner to the bottom-right corner.')
        label1.setWordWrap(True)
        layout.addWidget(label1)
        
        label2 = QLabel('Here is a 4x4 input feature map:')
        label2.setWordWrap(True)
        layout.addWidget(label2)
        
        setup_graph = QLabel()
        setup_graph.setAlignment(Qt.AlignCenter)
        setup_graph.setPixmap(QPixmap('./png/PoolingLayer/AveragePooling/setup.png'))
        layout.addWidget(setup_graph)
        
        label3 = QLabel('Let see the demostration of average-pooling on the feature map above with a 2x2 kernel and a stride of 2:')
        label3.setWordWrap(True)
        layout.addWidget(label3)
                
        maxPooling_gif = QLabel()
        maxPooling_gif.setAlignment(Qt.AlignCenter)
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
        output_lb.setAlignment(Qt.AlignCenter)
        output_lb.setObjectName('output_lb')
        
        layout.addWidget(output_lb)
        
        self.tab3.setLayout(layout)
        
    def check_ans(self):
        if self.tab3.findChild(QLineEdit, 'ans').text() == '7':
            self.tab3.findChild(QLabel, 'output_lb').setText('True! You now have a basic understanding of how pooling works!')
        else:
            self.tab3.findChild(QLabel, 'output_lb').setText('False, please try again!')
