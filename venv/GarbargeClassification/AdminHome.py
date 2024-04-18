

from PyQt5 import QtCore, QtGui, QtWidgets
from Training import CNN_BULDMODEL
from Accuracy import calculate_cnn_accuracy


class Ui_Adminhome(object):
    def buildmodel(self):
        CNN_BULDMODEL()
    def accuracy(self):
        calculate_cnn_accuracy()

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(850, 500)
        Dialog.setStyleSheet("QDialog{background-image: url(../GarbargeClassification/uiimg/adminhome.jpg);}")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(300, 310, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(194, 202, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 390, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(194, 202, 255);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(330, 150, 281, 81))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.buildmodel)
        self.pushButton_2.clicked.connect(self.accuracy)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Build Model"))
        self.pushButton_2.setText(_translate("Dialog", "Performance"))
        self.label.setText(_translate("Dialog", "A D M I N"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Adminhome()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
