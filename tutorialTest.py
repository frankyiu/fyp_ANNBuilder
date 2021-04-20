import sys
import unittest
from PyQt5 import QtWidgets
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QMovie
from ui.Ui_tutorialsWindow import Ui_tutorialsWindow
import main

class TutorialTest(unittest.TestCase):
    
    #@classmethod
    #def setUpClass(cls):
    #    app = QtWidgets.QApplication(sys.argv)
    #    window = main.MainWindow()
    #    Ui_tutorialsWindow = Ui_tutorialsWindow(window)
    #    Ui_tutorialsWindow.show()
    #    sys.exit(app.exec_())
        
    #@classmethod 
    # def tearDownClass(cls):
    #     pass
        
    #def setUp(self):
    #    pass
        
    #def tearDown(self):
    #   pass
    
    #def test_Perceptron_Demonstration_setup(self):
    #    perceptron_demonstration_setup = Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'Perceptron_Demonstration').movie().fileName()
    #    self.assertEqual(perceptron_demonstration_setup, './gifs/Perceptron/Demonstration/initialFrame.png')
    
    # Test Case 1
    def test_Perceptron_Demonstration_Case1(self):
        Perceptron_Demonstration_PushButton1 = Ui_tutorialsWindow.findChild(QtWidgets.QPushButton, 'Perceptron_Demonstration_PushButton1')
        QTest.mouseClick(Perceptron_Demonstration_PushButton1,  Qt.LeftButton)
        Perceptron_Demonstration_Case1 = Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'Perceptron_Demonstration').movie().fileName()
        self.assertEqual(Perceptron_Demonstration_Case1, './gifs/Perceptron/Demonstration/case1.gif')
        
    # Test Case 2
    def test_Perceptron_Demonstration_Case2(self):
        Perceptron_Demonstration_PushButton2 = Ui_tutorialsWindow.findChild(QtWidgets.QPushButton, 'Perceptron_Demonstration_PushButton2')
        QTest.mouseClick(Perceptron_Demonstration_PushButton2,  Qt.LeftButton)
        Perceptron_Demonstration_Case2 = Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'Perceptron_Demonstration').movie().fileName()
        self.assertEqual(Perceptron_Demonstration_Case2, './gifs/Perceptron/Demonstration/case2.gif')
        
    # Test Case 3
    def test_Perceptron_Demonstration_Case3(self):
        Perceptron_Demonstration_PushButton3 = Ui_tutorialsWindow.findChild(QtWidgets.QPushButton, 'Perceptron_Demonstration_PushButton3')
        QTest.mouseClick(Perceptron_Demonstration_PushButton3,  Qt.LeftButton)
        Perceptron_Demonstration_Case3 = Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'Perceptron_Demonstration').movie().fileName()
        self.assertEqual(Perceptron_Demonstration_Case3, './gifs/Perceptron/Demonstration/case3.gif')

    # Test Case 4
    def test_Perceptron_Demonstration_Case4(self):
        Perceptron_Demonstration_PushButton4 = Ui_tutorialsWindow.findChild(QtWidgets.QPushButton, 'Perceptron_Demonstration_PushButton4')
        QTest.mouseClick(Perceptron_Demonstration_PushButton4,  Qt.LeftButton)
        Perceptron_Demonstration_Case4 = Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'Perceptron_Demonstration').movie().fileName()
        self.assertEqual(Perceptron_Demonstration_Case4, './gifs/Perceptron/Demonstration/case4.gif')
        
        
    # Test Case 5
    def test_Perceptron_Exercise_correct_input(self):
        
        Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine1').clear()
        Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine2').clear()
        Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine3').clear()
        Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine4').clear()
        Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'perceptronExerciseResult').setText('')
        
        Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine1').setText('1')
        Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine2').setText('1')
        Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine3').setText('1')
        Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine4').setText('0')
        
        submit = Ui_tutorialsWindow.findChild(QtWidgets.QPushButton, 'perceptronExerciseSubmitButton')
        QTest.mouseClick(submit,  Qt.LeftButton)
        result = Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'perceptronExerciseResult').text()

        self.assertEqual(result, 'True!\nIn fact, this perceptron is implemented to hanlde the "OR" logic.')
    
    
    # Test Case 6
    def test_Perceptron_Exercise_incorrect_input(self):
        
        test_values = [-1, 0, 1, 2]
        
        Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine1').setText('0')
        
        for i in test_values:
            for j in test_values:
                for k in test_values:
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine2').clear()
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine3').clear()
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine4').clear()
                    Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'perceptronExerciseResult').setText('')
                    
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine2').setText(str(i))
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine3').setText(str(j))
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine4').setText(str(k))
                    
                    submit = Ui_tutorialsWindow.findChild(QtWidgets.QPushButton, 'perceptronExerciseSubmitButton')
                    QTest.mouseClick(submit,  Qt.LeftButton)
                    result = Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'perceptronExerciseResult').text()

                    self.assertEqual(result, 'False! Please try again!')
                  
        Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine2').setText('0')

        for i in test_values:
            for j in test_values:
                for k in test_values:
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine1').clear()
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine3').clear()
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine4').clear()
                    Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'perceptronExerciseResult').setText('')
                    
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine1').setText(str(i))
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine3').setText(str(j))
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine4').setText(str(k))
                    
                    submit = Ui_tutorialsWindow.findChild(QtWidgets.QPushButton, 'perceptronExerciseSubmitButton')
                    QTest.mouseClick(submit,  Qt.LeftButton)
                    result = Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'perceptronExerciseResult').text()

                    self.assertEqual(result, 'False! Please try again!')
                    
        Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine3').setText('0')

        for i in test_values:
            for j in test_values:
                for k in test_values:
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine1').clear()
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine2').clear()
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine4').clear()
                    Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'perceptronExerciseResult').setText('')
                    
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine1').setText(str(i))
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine2').setText(str(j))
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine4').setText(str(k))
                    
                    submit = Ui_tutorialsWindow.findChild(QtWidgets.QPushButton, 'perceptronExerciseSubmitButton')
                    QTest.mouseClick(submit,  Qt.LeftButton)
                    result = Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'perceptronExerciseResult').text()

                    self.assertEqual(result, 'False! Please try again!')
                    
        Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine4').setText('1')

        for i in test_values:
            for j in test_values:
                for k in test_values:
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine1').clear()
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine2').clear()
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine3').clear()
                    Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'perceptronExerciseResult').setText('')
                    
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine1').setText(str(i))
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine2').setText(str(j))
                    Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'perceptronExerciseLine3').setText(str(k))
                    
                    submit = Ui_tutorialsWindow.findChild(QtWidgets.QPushButton, 'perceptronExerciseSubmitButton')
                    QTest.mouseClick(submit,  Qt.LeftButton)
                    result = Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'perceptronExerciseResult').text()

                    self.assertEqual(result, 'False! Please try again!')
                    
                    
                    
    # Test Case 7                    
    def test_FeedforwardAndBackpropagation_Exercise_correct_input(self):
        
        Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'feedForwardAndBackpropagationLine1').clear()
        Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'feedForwardAndBackpropagationLine2').clear()
        Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'feedForwardAndBackpropagationResult').setText('')
        
        x_correct_values = [-0.4, -0.40]           #   x = -0.4 and x = -0.40 are both taken as correct
        y_correct_values = [-0.6, -0.60]           #   y = -0.6 and y = -0.60 are both taken as correct
        
        for x in x_correct_values:
            for y in y_correct_values:
                Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'feedForwardAndBackpropagationLine1').setText(str(x))
                Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'feedForwardAndBackpropagationLine2').setText(str(y))
        
                submit = Ui_tutorialsWindow.findChild(QtWidgets.QPushButton, 'feedForwardAndBackpropagationSubmitButton')
                QTest.mouseClick(submit,  Qt.LeftButton)
                result = Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'feedForwardAndBackpropagationResult').text()
                
                self.assertEqual(result, 'True!\nYou now have at least a basic understanding of backpropagation!')
           
    # Test Case 8
    def test_FeedforwardAndBackpropagation_Exercise_incorrect_input(self):
        
        Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'feedForwardAndBackpropagationLine1').clear()
        Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'feedForwardAndBackpropagationLine2').clear()
        Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'feedForwardAndBackpropagationResult').setText('')
        
        x_incorrect_values = [-0.5, -0.41, -0.39, -0.3, 0.4]          
        y_incorrect_values = [-0.7, -0.61, -0.59, -0.5, 0.6]          
        
        for x in x_incorrect_values:
            for y in y_incorrect_values:
                Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'feedForwardAndBackpropagationLine1').setText(str(x))
                Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'feedForwardAndBackpropagationLine2').setText(str(y))
        
                submit = Ui_tutorialsWindow.findChild(QtWidgets.QPushButton, 'feedForwardAndBackpropagationSubmitButton')
                QTest.mouseClick(submit,  Qt.LeftButton)
                result = Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'feedForwardAndBackpropagationResult').text()
            
                self.assertEqual(result, 'False! Please try again!')
            
    # Test Case 9
    def test_AveragePooling_Exercise_correct_input(self):
        
        Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'averagePoolingExerciseResult').setText('')
        
        Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'averagePoolingExerciseAnswer').setText('7')
        
        submit = Ui_tutorialsWindow.findChild(QtWidgets.QPushButton, 'averagePoolingExcerciseSubmitButton')
        QTest.mouseClick(submit,  Qt.LeftButton)
        result = Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'averagePoolingExerciseResult').text()
        
        self.assertEqual(result, 'True! You now have a basic understanding of how pooling works!')
        
    # Test Case 10
    def test_AveragePooling_Exercise_incorrect_input(self):
        
        Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'averagePoolingExerciseResult').setText('')
        
        incorrect_answers = [-8, -7, -6, 6, 8]
        for x in incorrect_answers:
            Ui_tutorialsWindow.findChild(QtWidgets.QLineEdit, 'averagePoolingExerciseAnswer').setText(str(x))
            submit = Ui_tutorialsWindow.findChild(QtWidgets.QPushButton, 'averagePoolingExcerciseSubmitButton')
            QTest.mouseClick(submit,  Qt.LeftButton)
            result = Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'averagePoolingExerciseResult').text()
            self.assertEqual(result, 'False, please try again!')

    # Test Case 11            
    def test_Convolutional_Layer_Stride_Case1(self):
        Convolutional_Layer_Stride_PushButton1 = Ui_tutorialsWindow.findChild(QtWidgets.QPushButton, 'Convolutional_Layer_Stride_PushButton1')
        QTest.mouseClick(Convolutional_Layer_Stride_PushButton1,  Qt.LeftButton)
        Convolutional_Layer_Stride_Case1 = Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'Convolutional_Layer_Stride_QLabel').movie().fileName()
        self.assertEqual(Convolutional_Layer_Stride_Case1, './gifs/ConvolutionalLayer/Stride/stride1.gif')
 
    # Test Case 12 
    def test_Convolutional_Layer_Stride_Case2(self):
        Convolutional_Layer_Stride_PushButton2 = Ui_tutorialsWindow.findChild(QtWidgets.QPushButton, 'Convolutional_Layer_Stride_PushButton2')
        QTest.mouseClick(Convolutional_Layer_Stride_PushButton2,  Qt.LeftButton)
        Convolutional_Layer_Stride_Case2 = Ui_tutorialsWindow.findChild(QtWidgets.QLabel, 'Convolutional_Layer_Stride_QLabel').movie().fileName()
        self.assertEqual(Convolutional_Layer_Stride_Case2, './gifs/ConvolutionalLayer/Stride/stride2.gif')
                
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = main.MainWindow()
    Ui_tutorialsWindow = Ui_tutorialsWindow(window)
    #Ui_tutorialsWindow.show()
    unittest.main()
    #sys.exit(app.exec_())
