
from PyQt5.QtWidgets import QApplication, QFrame, QWidget, QLabel
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor
from PyQt5.QtCore import QMimeData, Qt,  QRect
from ui.DraggableLabel import *


class DroppableFrame(QFrame):
        
        frameList =[]
    
        def __init__(self, parent):
            super().__init__(parent)
            self.setAcceptDrops(True)
            self.labelList =[]
            DroppableFrame.frameList.append(self)
            
            
        def dragEnterEvent(self,  event):
            event.acceptProposedAction();
        
        def dropEvent(self,  event):            
            #if label
            olabel = event.source()
            label = DraggableLabel(self)
            label.setGeometry(QRect(event.pos().x(), event.pos().y(), 40, 40))
            label.setStyleSheet(olabel.styleSheet())
            label.setText(olabel.text())
            label.deletable = True
            label.show()
            
            if (olabel.deletable == True):
                olabel.parent().labelList.remove(olabel)
                olabel.hide()
                olabel.clear()
                
            self.labelList.append(label)
            self.connectFrame(label)
            
        def connectFrame(self,  label):
                for f,  i in zip(DroppableFrame.frameList,  range(len(DroppableFrame.frameList))):
                    if(f == self):
                        #connectBefore
                        if (i>0):
                            label.connectLeft(DroppableFrame.frameList[i-1].labelList) 
                        #connectAfters
                        if (i< len(DroppableFrame.frameList)-1):
                            label.connectRight(DroppableFrame.frameList[i+1].labelList)

            
