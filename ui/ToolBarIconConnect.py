from ui.ToolBarIcon import *

class ToolBarIconConnect(ToolBarIcon):
    def isSelect(self):
        return False

    def isConnect(self):
        return True

    def isTrain(self):
        return False

    def getToolName(self):
        return ToolBarIcon.tool_name["connect"]

    """
    Switch the mode to Connect mode
    """
    def switchMode(self):
        self.api.switchMode(SceneMode.ConnectMode)
        print(self.getToolName())

    def getToolTipString(self):
        return "Connect Object"
