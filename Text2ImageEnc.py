from cryptosteganography import CryptoSteganography
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QIcon
from PIL import Image
import mainPage
import sys
import os

class Ui_Dialog(object):
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    def __init__(self, a):

        self.a = a

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(579, 571)
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 561, 551))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(110, 360, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(255, 162, 116);\n"
"font: 87 12pt \"Arial Black\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 470, 91, 31))
        self.pushButton_3.setStyleSheet("background-color: rgb(248, 155, 165);\n"
"font: 10pt \"Arial\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(110, 410, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 162, 116);\n"
"font: 87 12pt \"Arial Black\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 200, 311, 21))
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 470, 91, 31))
        self.pushButton_4.setStyleSheet("background-color: rgb(248, 155, 165);\n"
"font: 10pt \"Arial\";")
        self.pushButton_4.setObjectName("pushButton_4")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(130, 310, 311, 21))
        self.lineEdit.setFrame(False)
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(0, -10, 551, 531))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("images/T2IE.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_6.raise_()
        self.pushButton.raise_()
        self.pushButton_3.raise_()
        self.pushButton_2.raise_()
        self.lineEdit_2.raise_()
        self.pushButton_4.raise_()
        self.lineEdit.raise_()
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setGeometry(QtCore.QRect(110, 260, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 162, 116);\n"
"font: 87 12pt \"Arial Black\";")
        self.pushButton_5.setObjectName("pushButton_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 210, 321, 25))
        self.lineEdit_3.setFrame(False)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setGeometry(QtCore.QRect(110, 310, 351, 31))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(10)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setStyleSheet("background-color: rgb(255, 162, 116);\n"
"font: 87 12pt \"Arial Black\";")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setGeometry(QtCore.QRect(50, 470, 91, 31))
        self.pushButton_7.setStyleSheet("background-color: rgb(248, 155, 165);\n"
"font: 10pt \"Arial\";")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(430, 470, 91, 31))
        self.pushButton_8.setStyleSheet("background-color: rgb(248, 155, 165);\n"
"font: 10pt \"Arial\";")
        self.pushButton_8.setObjectName("pushButton_8")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setGeometry(QtCore.QRect(120, 370, 331, 61))
        self.textBrowser.setStyleSheet("border-color: rgb(255, 255, 255);")
        self.textBrowser.setLineWidth(0)
        self.textBrowser.setObjectName("textBrowser")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(-4, 3, 561, 521))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/T2ID.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label.raise_()

        self.message_label = QtWidgets.QLabel(Dialog)
        self.message_label.setGeometry(QtCore.QRect(205, 490, 551, 21))
        self.message_label.setObjectName("message_label")
        self.message_label.setStyleSheet("\n"
"font: 12pt \"Arial\";")
        
        self.pushButton_5.raise_()
        self.lineEdit_3.raise_()
        self.pushButton_6.raise_()
        self.pushButton_7.raise_()
        self.pushButton_8.raise_()
        self.textBrowser.raise_()
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
        self.pushButton_2.setText(_translate("Dialog", "Click here to Encrypt"))
        self.pushButton_4.setText(_translate("Dialog", "Exit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Embed text"))
        self.pushButton_5.setText(_translate("Dialog", "Select the image"))
        self.pushButton_6.setText(_translate("Dialog", "Click here to Decrypt"))
        self.pushButton_7.setText(_translate("Dialog", "Main Page"))
        self.pushButton_8.setText(_translate("Dialog", "Exit"))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.1pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans\'; font-size:10pt;\">Encrypted will appear here once decrypted.</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Extract text"))
        self.message_label.setText("")

        self.pushButton_3.clicked.connect(self.main)
        self.pushButton_7.clicked.connect(self.main)

        self.pushButton_4.clicked.connect(self.exit)
        self.pushButton_8.clicked.connect(self.exit)

        self.pushButton.clicked.connect(self.image)
        self.pushButton_2.clicked.connect(self.image_run)

        self.pushButton_5.clicked.connect(self.image)
        self.pushButton_6.clicked.connect(self.run_st)


    def run_st(self):

        try:

            Image.open(self.image_file[0])

        except:

            self.pushButton_2.setText("Incorrect file type")

            return

        self.password = self.lineEdit_3.text()

        self.crypto_steganography = CryptoSteganography(self.password)

        self.secret = self.crypto_steganography.retrieve(self.image_file[0])

        if self.secret==None:

            self.pushButton_6.setText("Incorrect password")

        else:

            self.textBrowser.setText("Solved text : "+self.secret)
            self.pushButton_6.setText("Decrypted")


    def image_run(self):

        try:

            Image.open(self.image_file[0])

        except:

            self.pushButton_2.setText("Incorrect file type")
            return

        if self.pushButton_2.text() == "Click for hidden text and image":

            self.dir = QFileDialog.getExistingDirectory(os.getenv("Desktop"))

            self.crypto_steganography.hide(self.image_file[0], str(self.dir)+"/output.png", self.text)

            self.pushButton_2.setText("Text has been embedded in the image")

        elif self.pushButton_2.text() != "Click here to save the embedded image" and self.pushButton_2.text() != "Select the image":

            self.text = self.lineEdit.text()

            self.password = self.lineEdit_2.text()

            if len(self.text)==0:

                self.pushButton_2.setText("Enter the text to be embedded")

            elif len(self.password) <= 5:

                self.pushButton_2.setText("Password length >= 6")

            else:

                self.crypto_steganography = CryptoSteganography(self.password)


                self.pushButton_2.setText("Click for hidden text and image")


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