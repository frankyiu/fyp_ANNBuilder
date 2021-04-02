
from ui.PopUpGuide import *

class PopUpGuideFactory():

    def __init__(self,  backWidget):
        self.list =[]
        self.index = 0
        self.isStarted = False
        self.backWidget = backWidget

    def start(self):
        #generateFirstItem
        if(self.isStarted == True):
            return
        self.index = 0
        self.currentguide = PopUpGuide(self.list[0], self.backWidget, self)
        self.isStarted = True
        
    def next(self):
        self.index += 1
        self.currentguide.close()
        self.currentguide = None
        if self.index == len(self.list):
            self.isStarted = False
            return
        self.currentguide = PopUpGuide(self.list[self.index], self.backWidget, self)

    def append(self, item, offset, text):
        obj = {
            'item': item,
            'offset': offset,
            'text': text
        }
        self.list.append(obj)

    def skip(self):
        self.currentguide.close()
        self.currentguide = None
        self.index = 0
        self.isStarted = False

    def refreshUI(self):
        self.currentguide.refresh()
