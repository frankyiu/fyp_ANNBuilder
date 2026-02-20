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
        # self.api.switchMode(SceneMode.TrainMode)
        print(self.getToolName())

    def getToolTipString(self):
        return "Train Network"

    #shows the hovering effect
    def enterEvent(self, event):
        return

    #revert the hovering effect
    def leaveEvent(self, event):
        return

    #When user press the icon, the icon shows a pressing effect
    def mousePressEvent(self, event):
        return

    def mouseReleaseEvent(self, event):
        return

    def setLock(self, islocked):
        if islocked:
            self.parent().setTool(self)
        pass
