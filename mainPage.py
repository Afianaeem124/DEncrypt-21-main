from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import sys
import main
import os

class Ui_Dialog(object):
    os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    def __init__(self, a):

        self.a = a
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(562, 511)
        Dialog.setStyleSheet("")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(6, 3, 551, 501))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("images/Main1.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 410, 141, 51))
        self.pushButton.setStyleSheet("background-color: rgb(244, 221, 252);\n"
"border-color: rgb(2, 2, 2);\n"
"font: 12pt \"Arial\";")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Click here to start!"))
        self.pushButton.clicked.connect(self.main)

    def main(self):

        self.mainwin=QMainWindow()  
        self.ui=main.Ui_Dialog(self.mainwin) 
        self.ui.setupUi(self.mainwin)  
        self.mainwin.setWindowTitle("    Cryptography Project")
        self.mainwin.setFixedSize(666, 450)
        self.mainwin.move(300,100)
        self.mainwin.show() 
        self.a.hide()

def init():

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog(Dialog)
    ui.setupUi(Dialog)
    Dialog.setWindowTitle("    Cryptography Project")
    Dialog.setFixedSize(562, 511)
    Dialog.move(300,100)
    Dialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":

    init()