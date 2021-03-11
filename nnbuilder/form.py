from PyQt5.QtGui import QIcon, QPalette, QDoubleValidator
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QLineEdit, QPushButton, QComboBox, QHBoxLayout, QVBoxLayout, \
                            QStylePainter, QStyleOptionComboBox, QStyle
from .config import *

class NNBForm(QDialog):
    class NNBComboBox(QComboBox):
        def __init__(self, values, defaultValue, parent=None):
            super().__init__(parent)
            self.values = values
            self.iconSize = 32
            self.setFixedSize(300, 30)
            self.setIconSize(QSize(self.iconSize, self.iconSize))
            for value in self.values:
                icon = QIcon("{}.png".format(value))
                self.addItem(icon, value)

            self.setCurrentIndex(self.values.index(defaultValue))
            self.setEditable(False)
            self.setChoosable(True)
            self.setStyleSheet('''
            QComboBox {
                font: Helvetica, sans-serif; color: gray;
                border-radius: 0px; border-bottom:1px solid black;
                background-color: none;
                padding: 3px 0px 0px 2px;
                selection-color: rgba(128,128,128,0.5);
                selection-background-color: rgba(128,128,128,0.5);
                show-decoration-selected: 0;
            }
            QComboBox:on {
                color: black;
            }
            QComboBox[choosable="false"]::down-arrow {
                image: none;
            }
            QComboBox[choosable="false"]::drop-down {
                width: 0px; 
                border-bottom:1px solid gray;
            }
            '''
                               )

        def setChoosable(self, choosable=True):
            self.setProperty("choosable", choosable)
            self.style().unpolish(self)
            self.style().polish(self)
            self.update()

        def paintEvent(self, event):
            painter = QStylePainter(self)
            painter.setPen(self.palette().color(QPalette.Text))
            opt = QStyleOptionComboBox()
            opt.initFrom(self)
            painter.drawComplexControl(QStyle.CC_ComboBox, opt)
            opt.currentText = self.currentText()
            opt.currentIcon = QIcon()
            painter.drawControl(QStyle.CE_ComboBoxLabel, opt)

        def showPopup(self):
            if self.property("choosable"):
                super().showPopup()

    def __init__(self, block, parent=None):
        super(QDialog, self).__init__(parent)
        self.block = block
        # Prevent Resize and Maximize in QDialog
        self.setFixedSize(500, 200)
        self.setAttribute(Qt.WA_ShowWithoutActivating, True)
        # Background color is white
        self.setStyleSheet("background: white;")

    def createTitleLabel(self, title):
        titleLabel = QLabel()
        titleLabel.setText(title)
        titleLabel.setStyleSheet("font: 20px Helvetica, sans-serif;")
        return titleLabel

    def createFieldLabel(self, labelName):
        label = QLabel()
        label.setFixedSize(150, 30)
        label.setText(labelName)
        label.setStyleSheet("font: bold Helvetica, sans-serif; padding-top: 2px; padding-bottom: 2px")
        return label

    def createLineEdit(self, lineEditDefaultValues, lineEditReadOnly):
        lineEdit = QLineEdit()
        lineEdit.setFixedSize(300, 30)
        lineEdit.setText(lineEditDefaultValues)
        lineEdit.setAttribute(Qt.WA_MacShowFocusRect, 0)  # cancel the default style
        if lineEditReadOnly:
            lineEdit.setReadOnly(True)
            lineEdit.setStyleSheet('''
                font: Helvetica, sans-serif; color: gray;
                border-radius: 0px; 
                border-bottom:1px solid gray;
                background-color: lightgray;
            ''')
        else:
            lineEdit.setValidator(QDoubleValidator(-1, 1, 10))
            lineEdit.setStyleSheet('''
            QLineEdit {
                font: Helvetica, sans-serif; color: gray;
                border-radius: 0px; border-bottom:1px solid gray;
            }
            QLineEdit:hover {
                border-bottom:2px solid black;
            }
            QLineEdit:focus {
                color: black;
                border-bottom:2px solid navy;
                selection-background-color: darkgray;
            }
            QLineEdit:read-only {
                background-color: lightgray
            }
            ''')
        return lineEdit

    def createOkBtn(self):
        okBtn = QPushButton("OK")
        okBtn.setFixedSize(120, 30)
        okBtn.setStyleSheet('''
        QPushButton {
            font: bold Helvetica, sans-serif; border-radius: 5px; background: BlueViolet; color: white;
        }
        QPushButton:hover {
            color: black;
        }
        ''')
        okBtn.clicked.connect(self.confirm)
        return okBtn

    def createCancelBtn(self):
        cancelBtn = QPushButton("CANCEL")
        cancelBtn.setStyleSheet('''
        QPushButton {
            font: cambria; color: gray; border: 0px;
        }
        QPushButton:hover {
            border-radius: 5px; border:1px solid rgba(224, 224, 224); background-color: rgba(224, 224, 224, 0.2);
        }
        '''
                                )
        cancelBtn.setFixedSize(120, 30)
        cancelBtn.clicked.connect(self.cancel)
        return cancelBtn

    def mousePressEvent(self, event):
        focusWidget = QApplication.focusWidget()
        if focusWidget:
            focusWidget.clearFocus()
        super().mousePressEvent(event)

    def confirm(self):
        self.close()

    def cancel(self):
        self.close()

    def close(self):
        self.block.isFormOn = False
        focusWidget = QApplication.focusWidget()
        if focusWidget:
            focusWidget.clearFocus()
        super().close()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Enter or event.key() == Qt.Key_Return:
            return
        super().keyPressEvent(event)

class NNB1DLinearConnectionForm(NNBForm):
    def __init__(self, connection, parent=None):
        super().__init__(connection, parent)
        self.prevWeight = connection.weight
        layout = QVBoxLayout()
        weightHLayout = QHBoxLayout()
        self.weightLineEdit = self.createLineEdit(str(self.prevWeight), False)
        weightHLayout.addWidget(self.createFieldLabel("Weight"))
        weightHLayout.addWidget(self.weightLineEdit)

        dWeightHLayout = QHBoxLayout()
        self.dWeightLineEdit = self.createLineEdit("NULL", True)
        dWeightHLayout.addWidget(self.createFieldLabel("dW"))
        dWeightHLayout.addWidget(self.dWeightLineEdit)

        btnHLayout = QHBoxLayout()
        btnHLayout.addStretch()
        btnHLayout.addWidget(self.createCancelBtn())
        btnHLayout.addWidget(self.createOkBtn())

        layout.addWidget(self.createTitleLabel("Connection"))
        layout.addStretch()
        layout.addLayout(weightHLayout)
        layout.addLayout(dWeightHLayout)
        layout.addLayout(btnHLayout)
        self.setLayout(layout)

    def cancel(self):
        currWeight = float(self.weightLineEdit.text())
        if self.prevWeight != currWeight:
            self.weightLineEdit = self.createLineEdit(str(self.prevWeight), False)
            self.block.weight = currWeight
        super().close()

    def confirm(self):
        currWeight = float(self.weightLineEdit.text())
        if self.prevWeight != currWeight:
            ##
            self.block.weight = currWeight
        super().close()

    def update(self):
        self.prevWeight = self.block.weight
        self.weightLineEdit.setText(str(self.block.weight))
        super().update()

class NNB1DNeuronForm(NNBForm):
    def __init__(self, neuron, parent=None):
        super().__init__(neuron, parent)
        if neuron.layer.layerType == "input":
            labelName = "Input Value"
        elif neuron.layer.layerType == "output":
            labelName = "Output Value"
        else:
            labelName = "Activation Value"

        layout = QVBoxLayout()
        actHLayout = QHBoxLayout()
        self.actLineEdit = self.createLineEdit("NULL", True)
        actHLayout.addWidget(self.createFieldLabel(labelName))
        actHLayout.addWidget(self.actLineEdit)

        deltaHLayout = QHBoxLayout()
        self.deltaLineEdit = self.createLineEdit("NULL", True)
        deltaHLayout.addWidget(self.createFieldLabel("Delta"))
        deltaHLayout.addWidget(self.deltaLineEdit)

        daHLayout = QHBoxLayout()
        self.daLineEdit = self.createLineEdit("NULL", True)
        daHLayout.addWidget(self.createFieldLabel("da"))
        daHLayout.addWidget(self.daLineEdit)

        btnHLayout = QHBoxLayout()
        btnHLayout.addStretch()
        btnHLayout.addWidget(self.createOkBtn())

        titleName = "Neuron"
        if neuron.isBias:
            titleName = "Bias " + titleName

        layout.addWidget(self.createTitleLabel(titleName))
        layout.addStretch()
        layout.addLayout(actHLayout)
        layout.addLayout(deltaHLayout)
        layout.addLayout(daHLayout)
        layout.addLayout(btnHLayout)
        self.setLayout(layout)

class NNB1DAffineLayerForm(NNBForm):
    def __init__(self, layer, parent=None):
        super().__init__(layer, parent)
        self.prevActFunc = layer.actFunc
        # input layer
        layout = QVBoxLayout()
        actHLayout = QHBoxLayout()
        self.actFuncComboBox = NNBForm.NNBComboBox(ACTIVATION_FUNC_LIST, self.prevActFunc, self)
        actHLayout.addWidget(self.createFieldLabel("Activation Function"))
        actHLayout.addWidget(self.actFuncComboBox)

        nNeuronHLayout = QHBoxLayout()
        self.nNeuronLineEdit = self.createLineEdit(str(len(layer.neurons)), True)
        nNeuronHLayout.addWidget(self.createFieldLabel("Number of neurons"))
        nNeuronHLayout.addWidget(self.nNeuronLineEdit)

        hasBiasHLayout = QHBoxLayout()
        hasBiasText = "NO"
        for neuron in layer.neurons:
            if neuron.isBias:
                hasBiasText = "YES"
        self.hasBiasLineEdit = self.createLineEdit(hasBiasText, True)
        hasBiasHLayout.addWidget(self.createFieldLabel("Has a bias"))
        hasBiasHLayout.addWidget(self.hasBiasLineEdit)

        btnHLayout = QHBoxLayout()
        btnHLayout.addStretch()
        btnHLayout.addWidget(self.createCancelBtn())
        btnHLayout.addWidget(self.createOkBtn())

        layerType = "Hidden Layer"
        if layer.layerType == "input":
            layerType = "Input Layer"
        elif layer.layerType == "output":
            layerType = "Output Layer"

        layout.addWidget(self.createTitleLabel(layerType))
        layout.addStretch()
        layout.addLayout(actHLayout)
        layout.addLayout(nNeuronHLayout)
        layout.addLayout(hasBiasHLayout)
        layout.addLayout(btnHLayout)
        self.setLayout(layout)

    def cancel(self):
        currActFunc = self.actFuncComboBox.currentText()
        if self.prevActFunc != currActFunc:
            self.actFuncComboBox.setCurrentIndex(self.actFuncComboBox.values.index(self.prevActFunc))
        self.block.isFormOn = False
        super().cancel()

    def confirm(self):
        currActFunc = self.actFuncComboBox.currentText()
        if self.prevActFunc != currActFunc:
            self.block.actFunc = currActFunc
            self.prevActFunc = currActFunc
        super().confirm()

    def update(self):
        # num of neurons and has bias
        self.nNeuronLineEdit.setText(str(len(self.block.neurons)))
        super().update()

class NNBLFBForm(NNBForm):
    def __init__(self, costFuncBlock, parent=None):
        super().__init__(costFuncBlock, parent)
        self.prevCostFunc = costFuncBlock.costFunc

        layout = QVBoxLayout()
        costFuncHLayout = QHBoxLayout()
        # TO-DO: set a global constant
        self.costFuncComboBox = NNBForm.NNBComboBox(LOSS_FUNC_LIST, self.prevCostFunc, self)
        costFuncHLayout.addWidget(self.createFieldLabel("Activation Function"))
        costFuncHLayout.addWidget(self.costFuncComboBox)

        lossValueHLayout = QHBoxLayout()
        self.lossValueLineEdit = self.createLineEdit("NULL", True)
        lossValueHLayout.addWidget(self.createFieldLabel("Loss Value J"))
        lossValueHLayout.addWidget(self.lossValueLineEdit)

        dJHLayout = QHBoxLayout()
        self.dJLineEdit = self.createLineEdit("NULL", True)
        dJHLayout.addWidget(self.createFieldLabel("dJ"))
        dJHLayout.addWidget(self.dJLineEdit)

        btnHLayout = QHBoxLayout()
        btnHLayout.addStretch()
        btnHLayout.addWidget(self.createCancelBtn())
        btnHLayout.addWidget(self.createOkBtn())

        layout.addWidget(self.createTitleLabel("Loss Function Block"))
        layout.addStretch()
        layout.addLayout(costFuncHLayout)
        layout.addLayout(lossValueHLayout)
        layout.addLayout(dJHLayout)
        layout.addLayout(btnHLayout)
        self.setLayout(layout)

    def cancel(self):
        currCostFunc = self.costFuncComboBox.currentText()
        if self.prevCostFunc != currCostFunc:
            self.costFuncComboBox.setCurrentIndex(self.costFuncComboBox.values.index(self.prevCostFunc))
        self.block.isFormOn = False
        super().cancel()

    def confirm(self):
        currCostFunc = self.costFuncComboBox.currentText()
        if self.prevCostFunc != currCostFunc:
            self.block.costFunc = currCostFunc
            self.prevCostFunc = currCostFunc
        super().confirm()

class NNBRegularizerForm(NNBForm):
    def __init__(self, regularizer, parent=None):
        super().__init__(regularizer, parent)
        self.prevReg = regularizer.regularization

        layout = QVBoxLayout()
        regHLayout = QHBoxLayout()
        self.regComboBox = NNBForm.NNBComboBox(REGULARIZATION_LIST, self.prevReg, self)
        regHLayout.addWidget(self.createFieldLabel("Regularization"))
        regHLayout.addWidget(self.regComboBox)

        lambdaHLayout = QHBoxLayout()
        self.lambdaLineEdit = self.createLineEdit("1.0", False)
        lambdaHLayout.addWidget(self.createFieldLabel("lambda"))
        lambdaHLayout.addWidget(self.lambdaLineEdit)

        regValueHLayout = QHBoxLayout()
        self.regValueLineEdit = self.createLineEdit("NULL", True)
        regValueHLayout.addWidget(self.createFieldLabel("Regularization Value"))
        regValueHLayout.addWidget(self.regValueLineEdit)

        btnHLayout = QHBoxLayout()
        btnHLayout.addStretch()
        btnHLayout.addWidget(self.createCancelBtn())
        btnHLayout.addWidget(self.createOkBtn())

        layout.addWidget(self.createTitleLabel("Regularizer"))
        layout.addStretch()
        layout.addLayout(regHLayout)
        layout.addLayout(lambdaHLayout)
        layout.addLayout(regValueHLayout)
        layout.addLayout(btnHLayout)
        self.setLayout(layout)

