import sys
import faulthandler
import unittest

from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt

from main import MainWindow
from nnbuilder.config import *

app = QtWidgets.QApplication(sys.argv)
faulthandler.enable()


class BuilderUITest(unittest.TestCase):


    def setUp(self):
        self.form = MainWindow()
        self.builder = self.form.builder
        QTest.mouseClick(self.form.ui.btn_draw, Qt.LeftButton)

    def tearDown(self):
        self.form.close()
        self.form = None

    def test_defaults(self):
        self.assertEqual(self.form.ui.radio_fullbatch.isChecked(), True)
        self.assertEqual(self.form.ui.spin_learningRate.value(), 0.01)
        self.assertEqual(self.form.ui.spin_decayRate.value(), 0.9)
        QTest.mouseClick(self.builder.popUpGuide.currentguide.guide.btn_skip, Qt.LeftButton)

    def test_control(self):
        return

    def test_toolbarsbutton(self):
        #toolbarbutton
        QTest.mouseClick(self.form.ui.widget_toolbar.toolbar[0],Qt.LeftButton)
        self.assertEqual(self.builder.scene.sceneMode, SceneMode.SelectMode)
        QTest.mouseClick(self.form.ui.widget_toolbar.toolbar[1],Qt.LeftButton)
        self.assertEqual(self.builder.scene.sceneMode, SceneMode.ConnectMode)
        QTest.mouseClick(self.form.ui.widget_toolbar.toolbar[2],Qt.LeftButton)
        self.assertEqual(self.builder.scene.sceneMode, SceneMode.TrainMode)


    def test_guidePopUp(self):
        #case first popup
        self.assertEqual(self.builder.popUpGuide.isStarted, True)
        self.assertEqual(self.builder.popUpGuide.currentguide.shadow.isVisible(), True)
        self.assertEqual(self.builder.popUpGuide.currentguide.guide.isVisible(), True)
        #skip to exit
        QTest.mouseClick(self.builder.popUpGuide.currentguide.guide.btn_skip, Qt.LeftButton)
        self.assertEqual(self.builder.popUpGuide.currentguide, None)
        #case no retrigger popUp
        QTest.mouseClick(self.form.ui.btn_home, Qt.LeftButton)
        QTest.mouseClick(self.form.ui.btn_draw, Qt.LeftButton)
        self.assertEqual(self.builder.popUpGuide.isStarted, False)
        self.assertEqual(self.builder.popUpGuide.currentguide, None)
        #test click button
        QTest.mouseClick(self.form.ui.btn_guide, Qt.LeftButton)
        self.assertEqual(self.builder.popUpGuide.isStarted, True)
        self.assertEqual(self.builder.popUpGuide.currentguide.shadow.isVisible(), True)
        self.assertEqual(self.builder.popUpGuide.currentguide.guide.isVisible(), True)

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(BuilderUITest)
    unittest.TextTestRunner(verbosity=2).run(suite)


