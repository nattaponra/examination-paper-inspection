# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login1.ui'
#
# Created: Sun Jan 25 01:46:54 2015
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Login(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(515, 387)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 320, 141, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(200, 250, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(200, 290, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 250, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 290, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 515, 180))
        self.pixmap = QtGui.QPixmap("test1.png")
        self.label_3.setPixmap(self.pixmap)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(200, 200, 121, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton.clicked.connect(self.handleLogin)
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "โปรแกรมตรวจข้อสอบโดยการประมวลผลภาพ", None))
        self.pushButton.setText(_translate("Dialog", "LOGIN", None))
        self.label.setText(_translate("Dialog", "Username", None))
        self.label_2.setText(_translate("Dialog", "Password", None))
        self.label_4.setText(_translate("Dialog", "Plase Login Program", None))
    def handleLogin(self):
        import hashlib
        U=hashlib.md5()
        P=hashlib.md5()
        file = open("setting/username.txt", "r")
        Password =file.readlines()
        file.close()
        U1=str(self.lineEdit.text())
        P1=str(self.lineEdit_2.text())
        U.update(U1)
        P.update(P1)
        if (U.hexdigest()== Password[0].strip() and
            P.hexdigest()== Password[1].strip()):
            self.accept()
        else:
            QtGui.QMessageBox.warning(
               self, 'Error', 'Bad user or password')

        
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    if Login().exec_() == QtGui.QDialog.Accepted:
                    import os
                    os.system("main.py arg")
                     
                    sys.exit()
    sys.exit(app.exec_())

