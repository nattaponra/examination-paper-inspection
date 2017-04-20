# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'format.ui'
#
# Created: Fri Oct 17 12:57:44 2014
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

class Ui_format(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
    def setupUi(self, format):
        format.setObjectName(_fromUtf8("format"))
        format.resize(640, 544)
        font = QtGui.QFont()
        font.setPointSize(10)
        format.setFont(font)
        self.tabWidget = QtGui.QTabWidget(format)
        self.tabWidget.setGeometry(QtCore.QRect(40, 50, 561, 451))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab)
        self.groupBox_6.setGeometry(QtCore.QRect(40, 40, 491, 81))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.label_18 = QtGui.QLabel(self.groupBox_6)
        self.label_18.setGeometry(QtCore.QRect(40, 30, 111, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.comboBox = QtGui.QComboBox(self.groupBox_6)
        self.comboBox.setGeometry(QtCore.QRect(140, 30, 69, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        
        self.groupBox_8 = QtGui.QGroupBox(self.tab)
        self.groupBox_8.setGeometry(QtCore.QRect(40, 140, 491, 121))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.label_21 = QtGui.QLabel(self.groupBox_8)
        self.label_21.setGeometry(QtCore.QRect(20, 30, 211, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.comboBox_2 = QtGui.QComboBox(self.groupBox_8)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 30, 111, 22))
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.label_22 = QtGui.QLabel(self.groupBox_8)
        self.label_22.setGeometry(QtCore.QRect(60, 60, 111, 16))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_8)
        self.comboBox_3.setGeometry(QtCore.QRect(170, 60, 111, 22))
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 501, 61))
        self.groupBox.setCheckable(True)
        self.groupBox.setChecked(True)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.checkBox = QtGui.QCheckBox(self.groupBox)
        self.checkBox.setGeometry(QtCore.QRect(380, 30, 101, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.spinBox = QtGui.QSpinBox(self.groupBox)
        self.spinBox.setGeometry(QtCore.QRect(300, 30, 42, 22))
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(4)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_14 = QtGui.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(220, 30, 91, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 80, 501, 331))
        self.groupBox_2.setCheckable(True)
        self.groupBox_2.setChecked(False)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 30, 471, 81))
        self.groupBox_3.setCheckable(True)
        self.groupBox_3.setChecked(False)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_3 = QtGui.QLabel(self.groupBox_3)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(250, 20, 71, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(180, 20, 61, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 20, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_3)
        self.checkBox_2.setGeometry(QtCore.QRect(20, 50, 101, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.label_17 = QtGui.QLabel(self.groupBox_3)
        self.label_17.setGeometry(QtCore.QRect(340, 20, 91, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.spinBox_4 = QtGui.QSpinBox(self.groupBox_3)
        self.spinBox_4.setGeometry(QtCore.QRect(420, 20, 42, 22))
        self.spinBox_4.setMinimum(1)
        self.spinBox_4.setMaximum(4)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 120, 471, 81))
        self.groupBox_4.setCheckable(True)
        self.groupBox_4.setChecked(False)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(250, 20, 71, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_8 = QtGui.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(180, 20, 61, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_7.setGeometry(QtCore.QRect(60, 20, 113, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.label_15 = QtGui.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(340, 20, 91, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.spinBox_2 = QtGui.QSpinBox(self.groupBox_4)
        self.spinBox_2.setGeometry(QtCore.QRect(420, 20, 42, 22))
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(4)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox_4)
        self.checkBox_3.setGeometry(QtCore.QRect(20, 50, 101, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 210, 471, 81))
        self.groupBox_5.setCheckable(True)
        self.groupBox_5.setChecked(False)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_11 = QtGui.QLabel(self.groupBox_5)
        self.label_11.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_10.setGeometry(QtCore.QRect(250, 20, 71, 20))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.label_12 = QtGui.QLabel(self.groupBox_5)
        self.label_12.setGeometry(QtCore.QRect(180, 20, 61, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_11.setGeometry(QtCore.QRect(60, 20, 113, 20))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.label_16 = QtGui.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(340, 20, 91, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.spinBox_3 = QtGui.QSpinBox(self.groupBox_5)
        self.spinBox_3.setGeometry(QtCore.QRect(420, 20, 42, 22))
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(4)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.checkBox_4 = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox_4.setGeometry(QtCore.QRect(20, 50, 101, 17))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.label_13 = QtGui.QLabel(self.groupBox_2)
        self.label_13.setGeometry(QtCore.QRect(310, 310, 201, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_7.setGeometry(QtCore.QRect(50, 30, 461, 121))
        self.groupBox_7.setCheckable(True)
        self.groupBox_7.setChecked(False)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.label_19 = QtGui.QLabel(self.groupBox_7)
        self.label_19.setGeometry(QtCore.QRect(40, 30, 31, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.lineEdit_12 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_12.setGeometry(QtCore.QRect(80, 30, 291, 20))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.label_20 = QtGui.QLabel(self.groupBox_7)
        self.label_20.setGeometry(QtCore.QRect(80, 60, 111, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.label = QtGui.QLabel(format)
        self.label.setGeometry(QtCore.QRect(40, 20, 101, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.pushButton = QtGui.QPushButton(format)
        self.pushButton.setGeometry(QtCore.QRect(430, 510, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(format)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 510, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(format)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 510, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(format)
       
        QtCore.QMetaObject.connectSlotsByName(format)

    def retranslateUi(self, format):
        format.setWindowTitle(_translate("format", "Format", None))
        self.groupBox_6.setTitle(_translate("format", "การตรวจสอบการฝนคำตอบ", None))
        self.label_18.setText(_translate("format", "ระดับการฝนขั้นต่ำ", None))
        self.comboBox.setItemText(0, _translate("format", "25%", None))
        self.comboBox.setItemText(1, _translate("format", "50%", None))
        self.comboBox.setItemText(2, _translate("format", "75%", None))
        self.comboBox.setItemText(3, _translate("format", "100%", None))
        self.groupBox_8.setTitle(_translate("format", "เงื่อนไขการตรวจ", None))
        self.label_21.setText(_translate("format", "ฝนคำตอบเกินจำนวนคำตอบ  ", None))
        self.comboBox_2.setItemText(0, _translate("format", "คะแนนติดลบ", None))
        self.comboBox_2.setItemText(1, _translate("format", "คะแนนไม่ติดลบ", None))
        self.label_22.setText(_translate("format", "ไม่ทำการฝนคำตอบ", None))
        self.comboBox_3.setItemText(0, _translate("format", "คะแนนติดลบ", None))
        self.comboBox_3.setItemText(1, _translate("format", "คะแนนไม่ติดลบ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("format", "ทั่วไป", None))
        self.groupBox.setTitle(_translate("format", "ทั่วไป", None))
        self.lineEdit.setText(_translate("format", "1", None))
        self.label_2.setText(_translate("format", "คะแนน/ข้อ", None))
        self.checkBox.setText(_translate("format", "ตอบผิดติดลบ", None))
        self.label_14.setText(_translate("format", "จำนวนคำตอบ", None))
        self.groupBox_2.setTitle(_translate("format", "แต่ละข้อคะแนนไม่เท่ากัน", None))
        self.groupBox_3.setTitle(_translate("format", "ช่วงที่1", None))
        self.label_3.setText(_translate("format", "ช่วงข้อ", None))
        self.label_4.setText(_translate("format", "คะแนน/ข้อ", None))
        self.checkBox_2.setText(_translate("format", "ตอบผิดติดลบ", None))
        self.label_17.setText(_translate("format", "จำนวนคำตอบ", None))
        self.groupBox_4.setTitle(_translate("format", "ช่วงที่2", None))
        self.label_7.setText(_translate("format", "ช่วงข้อ", None))
        self.label_8.setText(_translate("format", "คะแนน/ข้อ", None))
        self.label_15.setText(_translate("format", "จำนวนคำตอบ", None))
        self.checkBox_3.setText(_translate("format", "ตอบผิดติดลบ", None))
        self.groupBox_5.setTitle(_translate("format", "ช่วงที่3", None))
        self.label_11.setText(_translate("format", "ช่วงข้อ", None))
        self.label_12.setText(_translate("format", "คะแนน/ข้อ", None))
        self.label_16.setText(_translate("format", "จำนวนคำตอบ", None))
        self.checkBox_4.setText(_translate("format", "ตอบผิดติดลบ", None))
        self.label_13.setText(_translate("format", "ตัวอย่างช่วงข้อ เช่น 1-20,21-100", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("format", "คะแนน/คำตอบ", None))
        self.groupBox_7.setTitle(_translate("format", " คะแนนพรี", None))
        self.label_19.setText(_translate("format", "ข้อ", None))
        self.label_20.setText(_translate("format", "รูปแบบ 1,2,3,4", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("format", "คะแนนฟรี", None))
        self.label.setText(_translate("format", "รูปแบบการตรวจ", None))
        self.pushButton.setText(_translate("format", "ตกลง", None))
        self.pushButton_2.setText(_translate("format", "ปิด", None))
        self.pushButton_3.setText(_translate("format", "ค่าเริ่มต้น", None))
 





        self.tabWidget.setCurrentIndex(0)
        try:
            file = open("setting/format_tab1.txt", "r")
            
            list_setting2=file.readlines()
            
            file.close()
            print list_setting2[0]
            print list_setting2[1]
            print list_setting2[2]
            
            self.comboBox.setCurrentIndex(int(list_setting2[0]))
            self.comboBox_2.setCurrentIndex(int(list_setting2[1]))
            self.comboBox_3.setCurrentIndex(int(list_setting2[2]))
        except:
            self.comboBox.setCurrentIndex(1)
            self.comboBox_2.setCurrentIndex(1)
            self.comboBox_3.setCurrentIndex(1)


        #tab2
        try:
                    file = open("setting/format_tab2.txt", "r")
                    
                    list_setting2=file.readlines()
                    
                    file.close()
                     
               
                    sentence=str(list_setting2[0])

                                        
                    if(sentence.strip()=="No"): 
                       
                        
                        self.groupBox.setChecked(False)
                    else:
                        print "No"
                        self.groupBox.setChecked(True) 

                      
                    self.lineEdit.setText(str(float(list_setting2[1])))  
                    self.spinBox.setProperty("value", int(list_setting2[2]))  
                    ###c
                    sentence=str(list_setting2[3])
                    if(sentence.strip()=="No"): 
                       
                        
                        self.checkBox.setChecked(False)
                    else:
                        print "No"
                        self.checkBox.setChecked(True) 
                                                            
        except:
            pass        
        #tab2_down
        file = open("setting/format_tab2_down.txt", "r")            
        list_setting2=file.readlines()             
        file.close()
        sentence=str(list_setting2[0])
        if(sentence.strip()=="No"):
             self.groupBox_2.setChecked(False) 
        else:
             self.groupBox_2.setChecked(True) 
        
        if(str(list_setting2[2]).strip()=="1Yes"): 
            self.groupBox_3.setChecked(True)
        else:
            self.groupBox_3.setChecked(False)
        self.lineEdit_2.setText(str(list_setting2[3]).strip())
        self.lineEdit_3.setText(str(list_setting2[4]).strip())
        self.spinBox_4.setProperty("value", int(str(list_setting2[5]).strip()))  
        if(str(list_setting2[6]).strip()=="1Yes"): 
             self.checkBox_2.setChecked(True)
        else:
           
             self.checkBox_2.setChecked(False) 
        ##########################################
 
        
        if(str(list_setting2[8]).strip()=="1Yes"): 
            self.groupBox_4.setChecked(True)
        else:
            self.groupBox_4.setChecked(False)
        self.lineEdit_7.setText(str(list_setting2[9]).strip())
        self.lineEdit_6.setText(str(list_setting2[10]).strip())
        self.spinBox_2.setProperty("value", int(str(list_setting2[11]).strip()))  
        if(str(list_setting2[12]).strip()=="1Yes"): 
             self.checkBox_3.setChecked(True)
        else:
           
             self.checkBox_3.setChecked(False) 
        ##########################################
 
        
        if(str(list_setting2[14]).strip()=="1Yes"): 
            self.groupBox_5.setChecked(True)
        else:
            self.groupBox_5.setChecked(False)
        self.lineEdit_11.setText(str(list_setting2[15]).strip())
        self.lineEdit_10.setText(str(list_setting2[16]).strip())
        self.spinBox_3.setProperty("value", int(str(list_setting2[17]).strip()))  
        if(str(list_setting2[18]).strip()=="1Yes"): 
             self.checkBox_4.setChecked(True)
        else:
           
             self.checkBox_4.setChecked(False) 
        ##########################################
        file = open("setting/format_tab3.txt", "r")            
        list_setting=file.readlines()             
        file.close()
        if list_setting[0].strip()=="Yes":
            self.groupBox_7.setChecked(True)
            
            self.lineEdit_12.setText(list_setting[1].strip())
        else:
            self.groupBox_7.setChecked(False)
            self.lineEdit_12.setText(list_setting[1].strip())
           






        self.pushButton_2.clicked.connect(self.exit_)
        self.groupBox.clicked.connect(self.groupBox111)
        self.groupBox_2.clicked.connect(self.groupBox222)
        self.pushButton.clicked.connect(self.ReturnValue)
        self.pushButton_3.clicked.connect(self.SetDefault)
    def exit_(self):
        super(Ui_format, self).accept()
    def groupBox111(self):
        if self.groupBox.isChecked():
                print ("Yes\n")
                self.groupBox_2.setChecked(False)



        else:
                print ("No\n")
                self.groupBox_2.setChecked(True)
        print "test"
    def groupBox222(self):
        if self.groupBox_2.isChecked():
                print ("Yes\n")
                self.groupBox.setChecked(False)



        else:
                print ("No\n")
                self.groupBox.setChecked(True)
        print "test"       
    def ReturnValue(self):
            ########################TAB1###########################
            file = open("setting/format_tab1.txt", "w")
            file.write(str(self.comboBox.currentIndex())+"\n")
            file.write(str(self.comboBox_2.currentIndex())+"\n")
            file.write(str(self.comboBox_3.currentIndex())+"\n")
            print "Persen=",self.comboBox.currentText()
            print self.comboBox_2.currentIndex()
            print self.comboBox_3.currentIndex()
            print "############################"
            print self.spinBox.value()
            ########################TAB2###########################
            file = open("setting/format_tab2.txt", "w")
            if self.groupBox.isChecked():
                file.write("Yes\n")
            else:
                file.write("No\n")
            file.write(str(self.lineEdit.text())+"\n")
            file.write(str(self.spinBox.value())+"\n")
            if self.checkBox.isChecked():
                file.write("Yes\n")
                print "Yes"
            else:
                file.write("No\n")
                print "No"


            if self.checkBox.isChecked():
                print "Yes"
            else: 
                print "No"
            
            file.write( "1 checkBox, 2 num,3 numbercho 4, div\n")
            file.close()
            ##########################TAB2_down#############################
            file = open("setting/format_tab2_down.txt", "w")
            if self.groupBox_2.isChecked(): #แต่ละข้อคะแนนไม่เท่ากัน
                file.write("Yes\n")
            else:
                file.write("No\n")
            ################################################################
            file.write("############################1#############################\n") 
            if self.groupBox_3.isChecked(): #ช่วงที่1
                file.write("1Yes\n")
            else:
                file.write("1No\n")

            file.write(str(self.lineEdit_2.text())+"\n")#ช่วงข้อ
            file.write(str(self.lineEdit_3.text())+"\n")#คะแนน
            file.write(str(self.spinBox_4.value())+"\n")#จำนวนข้อ
            if self.checkBox_2.isChecked():
                file.write("1Yes\n")
            else:
                file.write("1No\n")                
            file.write("############################2#############################\n") 
            ################################################################
            if self.groupBox_4.isChecked(): #ช่วงที่2
                file.write("1Yes\n")
            else:
                file.write("1No\n")

            file.write(str(self.lineEdit_7.text())+"\n")#ช่วงข้อ
            file.write(str(self.lineEdit_6.text())+"\n")#คะแนน
            file.write(str(self.spinBox_2.value())+"\n")#จำนวนข้อ
            if self.checkBox_3.isChecked():
                file.write("1Yes\n")
            else:
                file.write("1No\n")      
            file.write("############################3#############################\n") 
            ################################################################
            if self.groupBox_5.isChecked(): #ช่วงที่3
                file.write("1Yes\n")
            else:
                file.write("1No\n")

            file.write(str(self.lineEdit_11.text())+"\n")#ช่วงข้อ
            file.write(str(self.lineEdit_10.text())+"\n")#คะแนน
            file.write(str(self.spinBox_3.value())+"\n")#จำนวนข้อ
            if self.checkBox_4.isChecked():
                file.write("1Yes\n")
            else:
                file.write("1No\n")                  
            ################################################################
            file.close()
            ########################TAB3###########################
            file = open("setting/format_tab3.txt", "w")
            if self.groupBox_7.isChecked():
                file.write("Yes\n")
            else:
                file.write("No\n")
            file.write(str(self.lineEdit_12.text())+"\n")
     
  
            file.close()
            ###########################################################

            
            super(Ui_format, self).accept()
    def SetDefault(self):
            self.comboBox.setCurrentIndex(1)
            self.comboBox_2.setCurrentIndex(1)
            self.comboBox_3.setCurrentIndex(1)
 

