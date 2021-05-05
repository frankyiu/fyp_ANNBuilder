import sys
import unittest
import faulthandler
from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

from main import MainWindow

app = QtWidgets.QApplication(sys.argv)
faulthandler.enable()

class DatasetTest(unittest.TestCase):

    def setUp(self):
        self.form = MainWindow()


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



if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(DatasetTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
