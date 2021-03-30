from ui.ToolBarIcon import *

class ToolBarIconSelect(ToolBarIcon):
    def isSelect(self):
        return True

    def isConnect(self):
        return False

    def isTrain(self):
        return False

    def getToolName(self):
        return ToolBarIcon.tool_name["select"]

    """
    Switch the mode to Select mode
    """
    def switchMode(self):
        print(self.getToolName())

    def getToolTipString(self):
        return "Select Object"
