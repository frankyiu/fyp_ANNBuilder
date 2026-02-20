import sys
import unittest
import faulthandler
from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

from main import MainWindow
from ui.DatasetPopup import DatasetPopup

app = QtWidgets.QApplication(sys.argv)
faulthandler.enable()

class MainWindowTest(unittest.TestCase):

    def setUp(self):
        self.form = MainWindow()

    def tearDown(self):
        self.form.close()
        DatasetPopup.num_of_datasets = 0
        self.form = None

    #test the default setting
    def test_defaults(self):
        self.assertEqual(self.form.ui.frame_main.width(), 1280)
        self.assertEqual(self.form.ui.frame_main.height(), 720)
        self.assertEqual(self.form.ui.stackedWidget.currentWidget(), self.form.ui.page_home)


    def test_home(self):
        QTest.mouseClick(self.form.ui.btn_gotoTutorial, Qt.LeftButton)
        self.assertEqual(self.form.ui.stackedWidget.currentWidget(), self.form.ui.page_tutorial)

        QTest.mouseClick(self.form.ui.btn_gotoBuilder, Qt.LeftButton)
        self.assertEqual(self.form.ui.stackedWidget.currentWidget(), self.form.ui.page_draw)

        QTest.mouseClick(self.form.ui.btn_gotoBasicCon, Qt.LeftButton)
        self.assertEqual(self.form.ui.stackedWidget.currentWidget(), self.form.ui.page_tutorial)

        QTest.mouseClick(self.form.ui.btn_gotoMLP, Qt.LeftButton)
        self.assertEqual(self.form.ui.stackedWidget.currentWidget(), self.form.ui.page_tutorial)

        QTest.mouseClick(self.form.ui.btn_gotoCNN, Qt.LeftButton)
        self.assertEqual(self.form.ui.stackedWidget.currentWidget(), self.form.ui.page_tutorial)
    def test_menu(self):

        # click home
        QTest.mouseClick(self.form.ui.btn_home, Qt.LeftButton)
        self.assertEqual(self.form.ui.page_home.isVisible(), True)
        self.assertEqual(self.form.ui.page_tutorial.isVisible(), False)
        self.assertEqual(self.form.ui.page_draw.isVisible(), False)

        # click tutorial
        QTest.mouseClick(self.form.ui.btn_tutorial, Qt.LeftButton)
        self.assertEqual(self.form.ui.page_home.isVisible(), False)
        self.assertEqual(self.form.ui.page_tutorial.isVisible(), True)
        self.assertEqual(self.form.ui.page_draw.isVisible(), False)

        # click draw
        QTest.mouseClick(self.form.ui.btn_draw, Qt.LeftButton)
        self.assertEqual(self.form.ui.page_home.isVisible(), False)
        self.assertEqual(self.form.ui.page_tutorial.isVisible(), False)
        self.assertEqual(self.form.ui.page_draw.isVisible(), True)

        # click expand
        QTest.mouseClick(self.form.ui.btn_expand, Qt.LeftButton)
        QTest.qWait(1000)
        self.assertEqual(self.form.ui.frame_left_menu.width(), 150)
        QTest.mouseClick(self.form.ui.btn_expand, Qt.LeftButton)
        QTest.qWait(1000)
        self.assertEqual(self.form.ui.frame_left_menu.width(), 60)

    def test_dataset(self):
        QTest.mouseClick(self.form.ui.btn_draw, Qt.LeftButton)

        #toggle the dataset popup
        QTest.mouseClick(self.form.ui.dataloader, Qt.LeftButton)
        self.assertEqual(self.form.ui.dataloader.getPopupWidget().isVisible(), True)
        for ds_icon in self.form.ui.dataloader.getPopupWidget().getDatasetIconWidget():
            self.assertEqual(ds_icon.isVisible(), True)

        QTest.mouseClick(self.form.ui.dataloader, Qt.LeftButton)
        self.assertEqual(self.form.ui.dataloader.getPopupWidget().isVisible(), False)
        for ds_icon in self.form.ui.dataloader.getPopupWidget().getDatasetIconWidget():
            self.assertEqual(ds_icon.isVisible(), False)

        #click on each dataset icon
        QTest.mouseClick(self.form.ui.dataloader, Qt.LeftButton)
        for ds_icon in self.form.ui.dataloader.getPopupWidget().getDatasetIconWidget():
            QTest.mouseClick(ds_icon, Qt.LeftButton)
            self.assertEqual(self.form.ui.dataloader.isDatasetLoaded(), True)
            self.assertEqual(ds_icon.isSelectedByDataLoader(), True)

    def test_titleBar(self):
        # maximize
        QTest.mouseClick(self.form.ui.btn_maximize_restore, Qt.LeftButton)
        self.assertEqual(self.form.isMaximized(), True)
        # restore
        QTest.mouseClick(self.form.ui.btn_maximize_restore, Qt.LeftButton)
        self.assertEqual(self.form.isMaximized(), False)
        self.assertEqual(self.form.ui.frame_main.width(), 1280)
        self.assertEqual(self.form.ui.frame_main.height(), 720)

        # minimize
        QTest.mouseClick(self.form.ui.btn_minimize, Qt.LeftButton)
        self.assertEqual(self.form.isMinimized(), True)

        # close
        QTest.mouseClick(self.form.ui.btn_close, Qt.LeftButton)
        self.assertEqual(self.form.close(), True)



if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(MainWindowTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
