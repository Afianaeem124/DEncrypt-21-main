from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from cryptography.fernet import Fernet
from PyQt5.QtGui import QIcon
from PIL import Image
import cryptography
import base64
import mainPage
import sys
import os
import io

class Ui_Dialog(object):
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    def __init__(self, a):

        self.a = a

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(578, 589)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 561, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(110, 290, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(217, 217, 223);\n"
"font: 87 12pt \"Arial Black\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 480, 91, 31))
        self.pushButton_3.setStyleSheet("\n"
"background-color: rgb(217, 217, 223);\n"
"font: 12pt \"Arial\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 350, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(217, 217, 223);\n"
"font: 87 12pt \"Arial Black\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 220, 331, 25))
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(420, 480, 91, 31))
        self.pushButton_4.setStyleSheet("\n"
"background-color: rgb(217, 217, 223);\n"
"font: 12pt \"Arial\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(-4, 3, 561, 541))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/I2TE.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_4.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 290, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(217, 217, 223);\n"
"font: 87 12pt \"Arial Black\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 220, 331, 25))
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(110, 350, 351, 41))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(217, 217, 223);\n"
"font: 87 12pt \"Arial Black\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 480, 91, 31))
        self.pushButton_7.setStyleSheet("\n"
"background-color: rgb(217, 217, 223);\n"
"font: 12pt \"Arial\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(420, 480, 91, 31))
        self.pushButton_8.setStyleSheet("\n"
"background-color: rgb(217, 217, 223);\n"
"font: 9pt \"Arial\";")
        self.pushButton_8.setObjectName("pushButton_8")

        self.message_label = QtWidgets.QLabel(Dialog)
        self.message_label.setGeometry(QtCore.QRect(205, 470, 551, 21))
        self.message_label.setObjectName("message_label")
        self.message_label.setStyleSheet("\n"
"font: 12pt \"Arial\";")

        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(-4, -1, 561, 551))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/I2TD.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.pushButton_5.raise_()
        self.lineEdit_3.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.currentChanged.connect(self.clear_message)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Select the image"))
        self.pushButton_3.setText(_translate("Dialog", "Main Page"))
        self.pushButton_2.setText(_translate("Dialog", "Click here to Encrypt the image"))
        self.pushButton_4.setText(_translate("Dialog", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Encrypt image"))
        self.pushButton_5.setText(_translate("Dialog", "Select the .enc file"))
        self.pushButton_6.setText(_translate("Dialog", "Click here to Decrypt the file"))
        self.pushButton_7.setText(_translate("Dialog", "Main Page"))
        self.pushButton_8.setText(_translate("Dialog", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Solve image"))
        self.message_label.setText("")

        self.pushButton_3.clicked.connect(self.main)
        self.pushButton_7.clicked.connect(self.main)

        self.pushButton_4.clicked.connect(self.exit)
        self.pushButton_8.clicked.connect(self.exit)

        self.pushButton.clicked.connect(self.image)
        self.pushButton_2.clicked.connect(self.en)

        self.pushButton_5.clicked.connect(self.image0)
        self.pushButton_6.clicked.connect(self.rund)


    def rund(self):

        if self.pushButton_6.text() == "Click for solved picture":

            self.dir = QFileDialog.getExistingDirectory(os.getenv("Desktop"))

            self.image = Image.open(io.BytesIO(self.data))
            self.image.save(self.dir+"/output.png")

            self.pushButton_6.setText("Image resolved")

        else:

            self.temp = self.image_file[0].split(".")

            if self.temp[1] != "enc":

                self.pushButton_6.setText("Incorrect file type")
                return

            try:

                self.password = self.lineEdit_3.text()

                backend = default_backend()
                salt = b'\xe2\xaf\xbc:\xdd'

                kdf = PBKDF2HMAC(
                    algorithm=hashes.SHA256(),
                    length=32,
                    salt=salt,
                    iterations=100000,
                    backend=backend
                )

                self.key = base64.urlsafe_b64encode(kdf.derive(self.password.encode()))
                self.f = Fernet(self.key)


                self.file = open(self.image_file[0], "rb")

                self.data = self.f.decrypt(self.file.read())

                self.pushButton_6.setText("Click for solved picture")

                self.file.close()

            except cryptography.fernet.InvalidToken:

                self.file.close()

                self.pushButton_6.setText("Incorrect password")


    def en(self):

        try:

            Image.open(self.image_file[0])

        except:

            self.pushButton_2.setText("Incorrect file type")

            return

        if self.pushButton_2.text() == "Click for the encrypted image":

            self.dir = QFileDialog.getExistingDirectory(os.getenv("Desktop"))

            self.file0 = open(self.image_file[0], "rb")

            self.token = self.f.encrypt(self.file0.read())

            self.file0.close()

            self.dir += "/output.enc"

            self.file = open(self.dir,"wb")

            self.file.write(self.token)

            self.file.close()

            self.pushButton_2.setText("Image is encrypted")

        else:

            self.password = self.lineEdit_2.text()

            if len(self.password) <= 5:

                self.pushButton_2.setText("Password length >= 6")
            
            else:

                backend = default_backend()
                salt = b'\xe2\xaf\xbc:\xdd'

                kdf = PBKDF2HMAC(
                    algorithm=hashes.SHA256(),
                    length=32,
                    salt=salt,
                    iterations=100000,
                    backend=backend
                )

                key = base64.urlsafe_b64encode(kdf.derive(self.password.encode()))

                self.f = Fernet(key)

                self.pushButton_2.setText("Click for the encrypted image")


    def image0(self):

        self.image_file = QFileDialog.getOpenFileName(os.getenv("Desktop"))

        self.temp = self.image_file[0].split(".")

        if self.temp[1] != "enc":

            self.pushButton_6.setText("Incorrect file type")
        else:
            self.message_label.setText("Enc file loaded successfully!")

    def image(self):
        self.image_file = QFileDialog.getOpenFileName(os.getenv("Desktop"))
        
        try:
            Image.open(self.image_file[0])
            self.message_label.setText("Image loaded successfully!") 
        except:
            self.pushButton_2.setText("Incorrect file type")


    def clear_message(self, index):
        if index == 1 or index ==0:  # Index 1 corresponds to the "Solve image" tab
            self.message_label.setText("")

    def main(self):

        self.mainwin=QMainWindow()  
        self.ui=mainPage.Ui_Dialog(self.mainwin) 
        self.ui.setupUi(self.mainwin)  
        self.mainwin.setWindowTitle("    Cryptography Project")
        self.mainwin.setFixedSize(562, 511)
        self.mainwin.move(300,100)
        self.mainwin.show() 
        self.a.hide()

    def exit(self):

        quit()
