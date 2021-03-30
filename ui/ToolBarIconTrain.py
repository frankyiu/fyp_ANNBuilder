from ui.ToolBarIcon import *

class ToolBarIconTrain(ToolBarIcon):
    def isSelect(self):
        return False

    def isConnect(self):
        return False

    def isTrain(self):
        return True

    def getToolName(self):
        return ToolBarIcon.tool_name["train"]

    """
    Switch the mode to Train mode
    """
    def switchMode(self):
        print(self.getToolName())

    def getToolTipString(self):
        return "Train Network"
