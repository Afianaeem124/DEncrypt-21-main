from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QIcon
import sys
import Text2ImageEnc
import Image2TextEnc
import os
import mainPage

class Ui_Dialog(object):
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    def __init__(self, a):

        self.a = a

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(666, 449)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 671, 451))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/BGMain2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(140, 80, 101, 31))
        self.pushButton.setStyleSheet("background-color: rgb(244, 221, 77);\n"
"border-color: rgb(3, 3, 3);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(455, 330, 101, 31))
        self.pushButton_2.setStyleSheet("background-color: rgb(199, 199, 201);\n"
"border-color: rgb(7, 7, 7);")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Click Here"))
        self.pushButton_2.setText(_translate("Dialog", "Click Here"))
        self.pushButton.clicked.connect(self.clickb)
        self.pushButton_2.clicked.connect(self.clicka)


    def clicka(self):

        self.mainwin=QMainWindow()  
        self.ui=Image2TextEnc.Ui_Dialog(self.mainwin) 
        self.ui.setupUi(self.mainwin)  
        self.mainwin.setWindowTitle("       Image to Text Encryption and Decryption")
        self.mainwin.setFixedSize(579, 571)
        self.mainwin.move(300,100)
        self.mainwin.show() 
        self.a.hide()

    def clickb(self):

        self.mainwin=QMainWindow()  
        self.ui=Text2ImageEnc.Ui_Dialog(self.mainwin) 
        self.ui.setupUi(self.mainwin)  
        self.mainwin.setWindowTitle("      Text to Image Encryption and Decryption")
        self.mainwin.setFixedSize(579, 571)
        self.mainwin.move(300,100)
        self.mainwin.show() 
        self.a.hide()

    def main(self):

        self.mainwin=QMainWindow()  
        self.ui=mainPage.Ui_Dialog(self.mainwin) 
        self.ui.setupUi(self.mainwin)  
        self.mainwin.setWindowTitle("    Cryptography Project")
        self.mainwin.setFixedSize(562, 511)
        self.mainwin.move(300,100)
        self.mainwin.show() 
        self.a.hide()
