
import sys


from ui.Ui_n_mainWindow import Ui_MainWindow
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QDrag, QPixmap, QPainter, QCursor, QPen

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #  hide title bar
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()


    sys.exit(app.exec_())
