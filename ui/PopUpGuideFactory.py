
from ui.PopUpGuide import *

class PopUpGuideFactory():

    def __init__(self,  backWidget,  itemlist=[], offsetlist= [], textlist=[]):
        self.itemlist = itemlist
        self.textlist = textlist
        self.offsetlist = offsetlist
        self.index = 0
        self.isStarted = False
        self.backWidget = backWidget
        
    def start(self):
        #generateFirstItem
        if(self.isStarted == True):
            return
        self.index = 0
        self.currentguide = PopUpGuide(self.offsetlist[0], self.textlist[0],  self.itemlist[0], self.backWidget, self)
        self.isStarted = True
        
    def next(self):
        self.index += 1
        self.currentguide.close()
        if self.index == len(self.itemlist):
            self.isStarted = False
            return
        self.currentguide = PopUpGuide(self.offsetlist[self.index], self.textlist[self.index], self.itemlist[self.index], self.backWidget, self)

    def append(self,  item, offset, text):
        self.itemlist.append(item)
        self.offsetlist.append(offset)
        self.textlist.append(text)

    def skip(self):
        self.currentguide.close()
        self.index = 0
        self.isStarted = False

    def refreshUI(self):
        self.currentguide.refresh()
