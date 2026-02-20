
from ui.PopUpGuide import *

class PopUpGuideFactory():

    def __init__(self,  backWidget, callback):
        self.list =[]
        self.callback = callback
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
        if self.index == len(self.list):
            self.skip()
            return
        self.currentguide.close()
        self.currentguide = PopUpGuide(self.list[self.index], self.backWidget, self)

    def append(self, item, offset, text, size=None):
        obj = {
            'item': item,
            'offset': offset,
            'text': text,
            'size': size
        }
        self.list.append(obj)

    def skip(self):
        self.currentguide.close()
        self.currentguide = None
        self.index = 0
        self.isStarted = False
        self.callback()

    def refreshUI(self):
        self.currentguide.refresh()
