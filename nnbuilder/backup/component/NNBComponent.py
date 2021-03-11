
class NNBComponent:
    '''
    it has:
    - a name (not necessarily unique and the user can change it)
    - a form (popup dialog which shows information on the component)
    '''
    def __init__(self, name):
        self.name = name
        self.form = None

        # states
        self.isFormOn = False
        self.hoveredOnConnectMode = False

    def handleMouseDoubleClickEvent(self):
        pass
        # if self.form is None:
        #     self.form = self.createForm(window)
        # if self.isFormOn:
        #     self.form.cancel()
        # self.form.show()
        # self.isFormOn = True

    def createForm(self, window):
        pass