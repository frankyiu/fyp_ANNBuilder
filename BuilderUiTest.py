import sys, time, threading
import faulthandler
import unittest

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QApplication
from pymouse import PyMouse

from main import MainWindow
from nnbuilder.config import *
from ui.DatasetPopup import DatasetPopup
import numpy as np

app = QtWidgets.QApplication(sys.argv)
faulthandler.enable()


# credit: https://stackoverflow.com/questions/24144482/how-to-test-drag-and-drop-behavior-in-pyqt
def mouseDrag(source, dest, rate=10000):
    mouse = PyMouse()
    mouse.press(*source)

    # smooth move from source to dest
    npoints = int(np.sqrt((dest[0] - source[0]) ** 2 + (dest[1] - source[1]) ** 2) / (rate / 1000))
    for i in range(npoints):
        x = int(source[0] + ((dest[0] - source[0]) / npoints) * i)
        y = int(source[1] + ((dest[1] - source[1]) / npoints) * i)
        mouse.move(x, y)
        time.sleep(0.001)

    mouse.release(*dest)


def center(widget):
    midpoint = QtCore.QPoint(widget.width() / 2, widget.height() / 2)
    return widget.mapToGlobal(midpoint)


class BuilderUITest(unittest.TestCase):

    def setUp(self):
        self.form = MainWindow()
        self.form.show()
        self.builder = self.form.builder
        self.form.ui.stackedWidget.setCurrentWidget(self.form.ui.page_draw)

    def tearDown(self):
        self.form.close()
        DatasetPopup.num_of_datasets = 0
        self.form = None

    def test_defaults(self):
        self.assertEqual(self.form.ui.radio_adam.isChecked(), True)
        self.assertEqual(self.form.ui.spin_batchSize.value(), 32)
        self.assertEqual(self.form.ui.spin_batchSize.minimum(), 1)
        self.assertEqual(self.form.ui.spin_batchSize.maximum(), 1000)

        self.assertEqual(self.form.ui.spin_learningRate.value(), 0.001)
        self.assertEqual(self.form.ui.spin_learningRate.minimum(), 0.000010)
        self.assertEqual(self.form.ui.spin_learningRate.maximum(), 100)

        self.assertEqual(self.form.ui.spin_decayRate.value(), 0.0001)
        self.assertEqual(self.form.ui.spin_decayRate.minimum(), 0)
        self.assertEqual(self.form.ui.spin_decayRate.maximum(), 1)

    ## no built-in function for simulate drag and Drop
    #TODO assert component
    def test_dragAndDrop(self):
        self.form.show()
        QTest.qWait(1000)

        neuron_obj = [self.form.ui.neuron_1D, self.form.ui.neuron_2D, self.form.ui.neuron_bias_1D,
                    self.form.ui.neuron_bias_2D]

        layer_obj = [self.form.ui.affine_layer, self.form.ui.stacked_affine_layer,
                    self.form.ui.conv_layer, self.form.ui.pooling_layer,self.form.ui.flatten_layer]

        other_obj = [self.form.ui.regularizer, self.form.ui.loss_func_block]

        full_obj = neuron_obj+layer_obj+other_obj
        drop_obj = self.form.ui.graphicsView

        for obj in full_obj:
            # scroll to end
            if obj == self.form.ui.pooling_layer:
                self.form.ui.scrollArea.verticalScrollBar().setValue(
                    self.form.ui.scrollArea.verticalScrollBar().maximum())
            # grab the center of the widgets
            fromPos = center(obj)
            toPos = center(drop_obj)
            dragThread = threading.Thread(target=mouseDrag, args=((fromPos.x(), fromPos.y()), (toPos.x(), toPos.y())))
            dragThread.start()
            # cannot join, use non-blocking wait
            while dragThread.is_alive():
                QTest.qWait(1000)

    def test_message(self):
        #test popUp
        self.form.ui.message.setMessage('A')
        self.assertEqual(self.form.ui.message.isVisible(), True)
        self.assertEqual(self.form.ui.message.textbrowser.toPlainText(), 'A')


    def test_control(self):
        return

    def test_toolbarsbutton(self):
        # toolbarbutton
        QTest.mouseClick(self.form.ui.widget_toolbar.toolbar_dict['select'], Qt.LeftButton)
        self.assertEqual(self.builder.scene.sceneMode, SceneMode.SelectMode)
        QTest.mouseClick(self.form.ui.widget_toolbar.toolbar_dict['connect'], Qt.LeftButton)
        self.assertEqual(self.builder.scene.sceneMode, SceneMode.ConnectMode)
        QTest.mouseClick(self.form.ui.widget_toolbar.toolbar_dict['train'], Qt.LeftButton)
        self.assertEqual(self.builder.scene.sceneMode, SceneMode.TrainMode)

    def test_guidePopUp(self):
        # case first popup
        QTest.mouseClick(self.form.ui.btn_draw, Qt.LeftButton)
        self.assertEqual(self.builder.popUpGuide.isStarted, True)
        self.assertEqual(self.builder.popUpGuide.currentguide.shadow.isVisible(), True)
        self.assertEqual(self.builder.popUpGuide.currentguide.guide.isVisible(), True)
        ##save current guide for next test
        previousGuide = self.builder.popUpGuide.currentguide
        # next to vist
        QTest.mouseClick(self.builder.popUpGuide.currentguide.guide.btn_next, Qt.LeftButton)
        self.assertNotEqual(previousGuide, self.builder.popUpGuide.currentguide)
        self.assertEqual(self.builder.popUpGuide.currentguide.shadow.isVisible(), True)
        self.assertEqual(self.builder.popUpGuide.currentguide.guide.isVisible(), True)
        # skip to exit
        QTest.mouseClick(self.builder.popUpGuide.currentguide.guide.btn_skip, Qt.LeftButton)
        self.assertEqual(self.builder.popUpGuide.currentguide, None)
        # case no retrigger popUp
        QTest.mouseClick(self.form.ui.btn_home, Qt.LeftButton)
        QTest.mouseClick(self.form.ui.btn_draw, Qt.LeftButton)
        self.assertEqual(self.builder.popUpGuide.isStarted, False)
        self.assertEqual(self.builder.popUpGuide.currentguide, None)
        # test click button
        QTest.mouseClick(self.form.ui.btn_guide, Qt.LeftButton)
        self.assertEqual(self.builder.popUpGuide.isStarted, True)
        self.assertEqual(self.builder.popUpGuide.currentguide.shadow.isVisible(), True)
        self.assertEqual(self.builder.popUpGuide.currentguide.guide.isVisible(), True)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(BuilderUITest)
    unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(app.exec_())
