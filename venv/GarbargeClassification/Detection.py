from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from PIL.ImageQt import ImageQt
import pickle
import os
import sys
import numpy as np
import operator
from PIL import Image
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model
from keras.preprocessing import image
from keras.preprocessing import image as image_utils
import tensorflow as tf
from DBconn import DBConnection


class Ui_Detect(object):
    def alertmsg(self, title, Message):
        self.warn = QtWidgets.QMessageBox()
        self.warn.setIcon(QtWidgets.QMessageBox.Information)
        self.warn.setWindowTitle(title)
        self.warn.setText(Message)
        self.warn.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.warn.exec_()
    def select_file(self):
        try:
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select File", "*.jpg", "*.png")
            # print(fileName)
            self.lineEdit.setText(fileName)
            img = QPixmap(fileName)
            self.label_2.setPixmap(img)

        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print(tb.tb_lineno)

    def detection_img(self):
        try:
            testimage = self.lineEdit.text()
            if testimage == "null" or testimage == "":
                self.alertmsg("failed", "Please Select the Image")
            else:


                model_path = 'cnn_model.h5'
                model = load_model(model_path)
                class_labels = ["cardboard", "glass", "metal", "paper",
                                "plastic", "trash"]
                test_image = []
                test_image = image.load_img(testimage, target_size=(128, 128))
                test_image = image.img_to_array(test_image)
                test_image = np.expand_dims(test_image, axis=0)
                test_image /= 255
                result = model.predict(test_image)
                decoded_predictions = dict(zip(class_labels, result[0]))
                decoded_predictions = sorted(decoded_predictions.items(), key=operator.itemgetter(1), reverse=True)
                # print(decoded_predictions[0][0])
                print(str(decoded_predictions[0][0]))
                self.result.setText(decoded_predictions[0][0])
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[1]
            print("LINE NO: ", tb.tb_lineno)

    def percent(self):
        try:
            val = self.result.text()
            if val == "" or val == "null":
                self.alertmsg("error", "Please select the image first")
            else:
                mydb = DBConnection.getConnection()
                cursor = mydb.cursor()
                query = "SELECT percentage FROM decompose WHERE garbagetype = '" + val + "' "
                print(query)
                # val = str(dis)
                cursor.execute(query)
                print(cursor)
                result_ = cursor.fetchone()[0]
                print(result_)
                mydb.commit()
                cursor.close()

                # print(result_)
                self.percentage.setText(result_)
        except Exception as e:
            print("Error=" + e.args[0])
            tb = sys.exc_info()[2]
            print("LINE NO: ", tb.tb_lineno)
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(850, 500)
        Dialog.setStyleSheet("QDialog{background-image: url(../GarbargeClassification/uiimg/user.jpg);}")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(490, -20, 431, 111))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("\n"
"color: rgb(0, 85, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 341, 321))
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setLineWidth(2)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(410, 130, 351, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(760, 130, 85, 31))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(660, 180, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet("background-color: rgb(68, 221, 229);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(440, 260, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.result = QtWidgets.QLabel(Dialog)
        self.result.setGeometry(QtCore.QRect(520, 240, 251, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.result.setFont(font)
        self.result.setStyleSheet("color: rgb(255, 0, 0);")
        self.result.setText("")
        self.result.setAlignment(QtCore.Qt.AlignCenter)
        self.result.setObjectName("result")
        self.percentage = QtWidgets.QLabel(Dialog)
        self.percentage.setGeometry(QtCore.QRect(620, 350, 131, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.percentage.setFont(font)
        self.percentage.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(121, 121, 121, 122), stop:1 rgba(121, 121, 121, 122));")
        self.percentage.setText("")
        self.percentage.setAlignment(QtCore.Qt.AlignCenter)
        self.percentage.setObjectName("percentage")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(420, 360, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(520, 450, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("background-color: rgb(186, 200, 197);")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.pushButton.clicked.connect(self.select_file)
        self.pushButton_2.clicked.connect(self.detection_img)
        self.pushButton_3.clicked.connect(self.percent)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "C L A S S I F I C A T I O N"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Select Image Here"))
        self.pushButton.setText(_translate("Dialog", "Choose"))
        self.pushButton_2.setText(_translate("Dialog", "Detect"))
        self.label_3.setText(_translate("Dialog", "Result"))
        self.label_4.setText(_translate("Dialog", "Decomposition\n"
"Percentage"))
        self.pushButton_3.setText(_translate("Dialog", "Get Decomposition Percentage"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Detect()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
