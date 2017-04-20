# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogKey.ui'
#
# Created: Fri Oct 17 12:56:46 2014
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

class Ui_Dialog_SetKey(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(879, 400)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 20, 231, 101))
        self.groupBox.setCheckable(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(90, 30, 131, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
 
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 140, 231, 231))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 191, 41))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 80, 191, 41))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 132, 191, 41))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 182, 191, 41))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.groupBox_7 = QtGui.QGroupBox(Dialog)
        self.groupBox_7.setGeometry(QtCore.QRect(270, 20, 381, 351))
        self.groupBox_7.setCheckable(True)
        self.groupBox_7.setChecked(False)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 20, 341, 71))
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setChecked(False)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_3)
        self.comboBox_2.setGeometry(QtCore.QRect(90, 20, 201, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_3)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 100, 341, 71))
        self.groupBox_4.setCheckable(True)
        self.groupBox_4.setChecked(False)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_3 = QtGui.QLabel(self.groupBox_4)
        self.label_3.setGeometry(QtCore.QRect(30, 30, 61, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_3.setGeometry(QtCore.QRect(90, 30, 211, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 180, 341, 71))
        self.groupBox_5.setCheckable(True)
        self.groupBox_5.setChecked(False)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.comboBox_4 = QtGui.QComboBox(self.groupBox_5)
        self.comboBox_4.setGeometry(QtCore.QRect(90, 30, 211, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.label_4 = QtGui.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(30, 30, 61, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox_7)
        self.groupBox_6.setGeometry(QtCore.QRect(20, 260, 341, 71))
        self.groupBox_6.setCheckable(True)
        self.groupBox_6.setChecked(False)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.comboBox_5 = QtGui.QComboBox(self.groupBox_6)
        self.comboBox_5.setGeometry(QtCore.QRect(90, 30, 211, 22))
        self.comboBox_5.setObjectName(_fromUtf8("comboBox_5"))
        self.label_5 = QtGui.QLabel(self.groupBox_6)
        self.label_5.setGeometry(QtCore.QRect(30, 30, 61, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.groupBox_8 = QtGui.QGroupBox(Dialog)
        self.groupBox_8.setGeometry(QtCore.QRect(660, 20, 201, 351))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.scrollArea = QtGui.QScrollArea(self.groupBox_8)
        self.scrollArea.setGeometry(QtCore.QRect(10, 20, 181, 291))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 179, 289))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.listWidget = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 181, 291))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_5 = QtGui.QPushButton(self.groupBox_8)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 320, 75, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_8)
        self.pushButton_6.setGeometry(QtCore.QRect(110, 320, 75, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Select Key", None))
        self.groupBox.setTitle(_translate("Dialog", "ใช้เฉลยชุดเดียว", None))
        self.label.setText(_translate("Dialog", "เลือกเฉลย:", None))
        self.comboBox.setItemText(0, _translate("Dialog", "New Item", None))
        self.comboBox.setItemText(1, _translate("Dialog", "New Item", None))
        self.comboBox.setItemText(2, _translate("Dialog", "New Item", None))
        self.comboBox.setItemText(3, _translate("Dialog", "New Item", None))
        self.groupBox_2.setTitle(_translate("Dialog", "เพิ่มเฉลยใหม่", None))
        self.pushButton.setText(_translate("Dialog", "เพิ่มจากไฟล์ภาพ", None))
        self.pushButton_2.setText(_translate("Dialog", "เพิ่มจากโปรแกรม", None))
        self.pushButton_3.setText(_translate("Dialog", "บันทึก", None))
        self.pushButton_4.setText(_translate("Dialog", "ยกเลิก", None))
        self.groupBox_7.setTitle(_translate("Dialog", "เลือกเฉลยอัตโนมัติ", None))
        self.groupBox_3.setTitle(_translate("Dialog", "ชุดที่ 1", None))
        self.label_2.setText(_translate("Dialog", "เลือกเฉลย:", None))
        self.groupBox_4.setTitle(_translate("Dialog", "ชุดที่ 2", None))
        self.label_3.setText(_translate("Dialog", "เลือกเฉลย:", None))
        self.groupBox_5.setTitle(_translate("Dialog", "ชุดที่ 3", None))
        self.label_4.setText(_translate("Dialog", "เลือกเฉลย:", None))
        self.groupBox_6.setTitle(_translate("Dialog", "ชุดที่ 4", None))
        self.label_5.setText(_translate("Dialog", "เลือกเฉลย:", None))
        self.groupBox_8.setTitle(_translate("Dialog", "จัดการ", None))
        self.pushButton_5.setText(_translate("Dialog", "ลบเฉลย", None))
        self.pushButton_6.setText(_translate("Dialog", "แก้ไข", None))



        self.pushButton_5.setEnabled(False) 
        self.pushButton_6.setEnabled(False) 
        self.pushButton_5.clicked.connect(self.DeleteKey)
        self.pushButton_6.clicked.connect(self.EditKey)

        self.AddListKey()
        self.UpdateCombo()

        self.groupBox.setChecked(False)
        self.groupBox_7.setChecked(False)
        self.groupBox.clicked.connect(self.groupSigleKey)
        self.groupBox_7.clicked.connect(self.groupMultiKey)
        self.listWidget.currentItemChanged.connect(self.ClickList)



        self.pushButton_4.clicked.connect(self.cancel)
        self.pushButton_3.clicked.connect(self.SelectKey)
        self.pushButton_2.clicked.connect(self.AddKeyFormCheckBox)
        self.pushButton.clicked.connect(self.AddKeyFormImg)


        file = open("setting/SelectKey.txt", "r")
        list_setting=file.readlines()
        file.close()
        if list_setting[0].strip()=="single":
            self.groupBox.setChecked(True)
            self.groupBox_7.setChecked(False)
            self.comboBox.setCurrentIndex(int(list_setting[2].strip()))
        else:
            self.groupBox.setChecked(False)
            self.groupBox_7.setChecked(True)
            self.comboBox_2.setCurrentIndex(int(list_setting[5].strip()))
            self.comboBox_3.setCurrentIndex(int(list_setting[6].strip()))
            self.comboBox_4.setCurrentIndex(int(list_setting[7].strip()))
            self.comboBox_5.setCurrentIndex(int(list_setting[8].strip()))
            if list_setting[9].strip()=="Yes":
                 self.groupBox_3.setChecked(True)
            else:
                 self.groupBox_3.setChecked(False)
            if list_setting[10].strip()=="Yes":
                 self.groupBox_4.setChecked(True)
            else:
                 self.groupBox_4.setChecked(False)
            if list_setting[11].strip()=="Yes":
                 self.groupBox_5.setChecked(True)
            else:
                 self.groupBox_5.setChecked(False)
            if list_setting[12].strip()=="Yes":
                 self.groupBox_6.setChecked(True)
            else:
                 self.groupBox_6.setChecked(False)





    def EditKey(self):
        print "EditKey"


    def DeleteKey(self):
        List_key=self.ReadDirAnswer()
        index=self.listWidget.currentRow()
        #print self.listWidget.currentRow()
        #print    self.listWidget.currentItem()
        print List_key
        os.remove("key\{:>}".format(str(List_key[index])))    
        self.UpdateList()

    def ClickList(self):
        self.pushButton_5.setEnabled(True) 
        self.pushButton_6.setEnabled(True) 

    def AddListKey(self):
        List_Key=self.ReadDirAnswer()
        if len(List_Key)>0:
            self.pushButton_5.setEnabled(True) 
            self.pushButton_6.setEnabled(True)
        for i in range(len(List_Key)):
                item = QtGui.QListWidgetItem()
                self.listWidget.addItem(item)                                                                                                                                                                        
                item = self.listWidget.item(i)                                                                                                                                              
                item.setText(_translate("Dialog", ("No: "+str(i+1)+" "+str(List_Key[i])), None)) 


    def UpdateList(self):
                List_Key=self.ReadDirAnswer()

                self.listWidget.clear()
                index=self.listWidget.currentRow()
                
                for i in range(len(List_Key)):
                    item = QtGui.QListWidgetItem()
                    self.listWidget.addItem(item)                                                                                                                                                                        
                    item = self.listWidget.item(i)                                                                                                                                              
                    item.setText(_translate("Dialog", ("No: "+str(i+1)+" "+str(List_Key[i])), None)) 

                if self.listWidget.count()==0:
                        self.pushButton_5.setEnabled(False) 
                        self.pushButton_6.setEnabled(False)

    def UpdateCombo(self):
        List_key=self.ReadDirAnswer()
        for i in range(len(List_key)):
            self.comboBox.addItem(_fromUtf8(""))
            self.comboBox.setItemText(i, _translate("Dialog", str(List_key[i]), None))

            self.comboBox_3.addItem(_fromUtf8(""))
            self.comboBox_3.setItemText(i, _translate("Dialog", str(List_key[i]), None))  

            self.comboBox_4.addItem(_fromUtf8(""))
            self.comboBox_4.setItemText(i, _translate("Dialog", str(List_key[i]), None))          

            self.comboBox_5.addItem(_fromUtf8(""))
            self.comboBox_5.setItemText(i, _translate("Dialog", str(List_key[i]), None))

            self.comboBox_2.addItem(_fromUtf8(""))
            self.comboBox_2.setItemText(i, _translate("Dialog", str(List_key[i]), None))
    def cancel(self):
        super(Ui_Dialog_SetKey, self).accept()

    def SelectKey(self):
        print "Save"
        file = open("setting/SelectKey.txt", "w")
        
        if self.groupBox.isChecked():
            file.write("single\n")

            file.write(str(self.comboBox.currentText())+"\n")
            file.write(str(self.comboBox.currentIndex())+"\n")
            file.close()
        if self.groupBox_7.isChecked():
            file.write("multiple\n")
            if self.groupBox_3.isChecked():
                file.write(str(self.comboBox_2.currentText())+"\n")
            else:
                file.write("\n")
            if self.groupBox_4.isChecked():
                file.write(str(self.comboBox_3.currentText())+"\n")
            else:
                file.write("\n")
            if self.groupBox_5.isChecked():
                file.write(str(self.comboBox_4.currentText())+"\n")
            else:
                file.write("\n")
            if self.groupBox_6.isChecked():
                file.write(str(self.comboBox_5.currentText())+"\n")
            else:
                file.write("\n")
            file.write(str(self.comboBox_2.currentIndex())+"\n")
            file.write(str(self.comboBox_3.currentIndex())+"\n")
            file.write(str(self.comboBox_4.currentIndex())+"\n")
            file.write(str(self.comboBox_5.currentIndex())+"\n")
            if self.groupBox_3.isChecked():
                file.write("Yes\n")
            else:
                file.write("No\n")
            if self.groupBox_4.isChecked():
                file.write("Yes\n")
            else:
                file.write("No\n")
            if self.groupBox_5.isChecked():
                file.write("Yes\n")
            else:
                file.write("No\n")
            if self.groupBox_6.isChecked():
                file.write("Yes\n")
            else:
                file.write("No\n")
        

 
            file.close()

        super(Ui_Dialog_SetKey, self).accept()
    def groupMultiKey(self):
        if self.groupBox_7.isChecked():
            self.groupBox.setChecked(False)
        else:
            self.groupBox.setChecked(True)

    def groupSigleKey(self):
        if self.groupBox.isChecked():
            self.groupBox_7.setChecked(False)
        else:
            self.groupBox_7.setChecked(True)

        print "yes"
    def AddKeyFormCheckBox(self):
        print "AddKeyFormCheckBox"



        import DialogAddKeyFormCheck

        self.ui=DialogAddKeyFormCheck.DialogAddKeyFormCheck()
        self.ui.setModal(True)
        self.ui.show()
        super(Ui_Dialog_SetKey, self).accept()
    def AddKeyFormImg(self):
        print "AddKeyFormImg"

        import DialogAddKeyFormImg

        self.ui=DialogAddKeyFormImg.Ui_DialogAddKeyFormImg()
        self.ui.setModal(True)
        self.ui.show()
        super(Ui_Dialog_SetKey, self).accept()

    def ReadDirAnswer(self):
        items = os.listdir("key")
        newlist = []
        List_pp=[]
        for names in items:
             if names.endswith(".txt"):
                     newlist.append(names)
                     #print newlist
        for i in range(len(newlist)):
               print newlist[i]
        return newlist