# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EditID.ui'
#
# Created: Sun Dec 21 14:07:23 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import sys
import os
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

class Edit_ID(QtGui.QDialog):
    Dir=""
    File=""
    path=""
    def __init__(self,Dir,File):
        QtGui.QDialog.__init__(self)
        self.setupUi(self,Dir,File)
        
    def setupUi(self, Dialog,Dir,File):
        self.Dir=Dir
        self.File=File
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 195)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(40, 20, 331, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(70, 30, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setDragEnabled(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 70, 211, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(210, 150, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(300, 150, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Edit Student ID", None))
        self.groupBox.setTitle(_translate("Dialog", "Edit Student ID", None))
        self.label.setText(_translate("Dialog", "Old ID:", None))
        self.label_2.setText(_translate("Dialog", "New ID:", None))
        self.pushButton.setText(_translate("Dialog", "Finish", None))
        self.pushButton_2.setText(_translate("Dialog", "Close", None))
        
        self.pushButton.clicked.connect(self.Edit)

        file = open(self.Dir+self.File, "r")
        list_Code=file.readlines() 
        file.close
        self.lineEdit.setText(list_Code[1].strip())
        print list_Code[0].strip()
        self.path=list_Code[0].strip()
    def Edit(self):



  


        if str(self.lineEdit_2.text()).strip()!="":
            file = open(self.Dir+self.File, "r+") 
            file.write(self.path+"\n")
            file.write(str(self.lineEdit_2.text()).strip()+"\n")
            file.close()
            os.rename(self.Dir+self.File, self.Dir+str(self.lineEdit_2.text()).strip()+".txt")
            super(Edit_ID, self).accept()
        else:
            pass



        




