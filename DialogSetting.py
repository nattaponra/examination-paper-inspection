# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogSetting.ui'
#
# Created: Fri Oct 17 12:57:18 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import os
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

class Ui_Dialog_Setting(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(550, 258)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../test/icon/Categories-preferences-system-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 220, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 220, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 220, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 511, 181))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 20, 451, 91))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_2)
        self.comboBox_2.setGeometry(QtCore.QRect(20, 50, 141, 21))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 51, 29))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 451, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(390, 40, 41, 21))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 141, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 40, 361, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(20, 90, 121, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        #self.comboBox.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Setting", None))
        self.pushButton_2.setText(_translate("Dialog", "เสร็จ", None))
        self.pushButton_3.setText(_translate("Dialog", "ปิด", None))
        self.pushButton_4.setText(_translate("Dialog", "ตั้งค่าเริ่มต้น", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Input", None))
        self.comboBox_2.setItemText(0, _translate("Dialog", ".PNG", None))
        self.comboBox_2.setItemText(1, _translate("Dialog", ".JPEG", None))
        self.comboBox_2.setItemText(2, _translate("Dialog", ".BMP", None))
        self.label_3.setText(_translate("Dialog", "File Type ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Input", None))
        self.groupBox.setTitle(_translate("Dialog", "Output", None))
        self.pushButton.setText(_translate("Dialog", "....", None))
        self.label.setText(_translate("Dialog", "เลือกไดเรกทอรี่บันทึก ผลลัพธ์", None))
        self.label_2.setText(_translate("Dialog", "ประเภทไฟล์ผลลัพธ์", None))
        self.comboBox.setItemText(0, _translate("Dialog", ".CSV", None))
        #self.comboBox.setItemText(1, _translate("Dialog", ".Xl", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Output", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", "Genaral", None))
        





        
        try:
            file = open("setting/setting.txt", "r")
            #print file.readlines()
            list_setting=file.readlines()
            #print list_setting[1]
            file.close()
             
            self.lineEdit.setText(str(list_setting[2]))
            self.comboBox_2.setCurrentIndex(int(list_setting[0]))
            self.comboBox.setCurrentIndex(int(list_setting[1]))
        except:
            self.comboBox_2.setCurrentIndex(0)
            self.comboBox.setCurrentIndex(0)
        #print   self.comboBox_2.currentText()
        self.pushButton_2.clicked.connect(self.ReturnValue) # 
        self.pushButton.clicked.connect(self.Directory_out)
        self.pushButton_4.clicked.connect(self.set_default)
        #self.connect(self.comboBox_2, QtCore.SIGNAL('activated(QString)'), self.type_file)
    def Directory_out(self):
        directory = QtGui.QFileDialog.getExistingDirectory(self)
        self.lineEdit.setText(directory)

    def set_default(self):
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox.setCurrentIndex(0)
        self.lineEdit.setText("C:\CPE_INSPECTOR")
    def ReturnValue(self):
             print  "Type Picture:",self.comboBox_2.currentText() 
             print "Directory:",self.lineEdit.text()
             print "Type Output:",self.comboBox.currentText()
              
             file = open("setting/setting.txt", "w")
             file.write(str(self.comboBox_2.currentIndex())+"\n")
             file.write(str(self.comboBox.currentIndex())+"\n")
             file.write(str(self.lineEdit.text()).strip()+"\n")
             file.write(str(self.comboBox_2.currentText())+"\n")
             file.close()
             super(Ui_Dialog_Setting, self).accept()

    def type_file(self,type):
            print type
            self.label_3.setText(type)
 


