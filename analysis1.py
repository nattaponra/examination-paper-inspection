# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analysis.ui'
#
# Created: Wed Dec 03 00:48:36 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import sys,os
import difficulty
import distracter
import Cart_diff
import Chart_distinguish1
import Chart_distinguish2
import Chart_distinguish3
import Chart_distinguish4
import distinguish
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

class Ui_Dialog(QtGui.QDialog):
    sta1=0
    sta2=0
    sta3=0
    sta4=0
    LI=[]
    Dir=""
    State=False
    Statediff=False
    Distracter_state=False
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(997, 597)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 981, 541))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_6.setGeometry(QtCore.QRect(30, 40, 451, 461))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.listWidget = QtGui.QListWidget(self.groupBox_6)
        self.listWidget.setGeometry(QtCore.QRect(210, 30, 231, 411))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_6)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 20, 191, 221))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.label_13 = QtGui.QLabel(self.groupBox_8)
        self.label_13.setGeometry(QtCore.QRect(20, 190, 71, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_8.setGeometry(QtCore.QRect(90, 190, 61, 20))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 100, 61, 20))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 130, 61, 20))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_14 = QtGui.QLabel(self.groupBox_8)
        self.label_14.setGeometry(QtCore.QRect(60, 40, 21, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_11 = QtGui.QLabel(self.groupBox_8)
        self.label_11.setGeometry(QtCore.QRect(20, 130, 71, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 70, 61, 20))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_12 = QtGui.QLabel(self.groupBox_8)
        self.label_12.setGeometry(QtCore.QRect(20, 160, 71, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_10 = QtGui.QLabel(self.groupBox_8)
        self.label_10.setGeometry(QtCore.QRect(30, 100, 61, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_9 = QtGui.QLabel(self.groupBox_8)
        self.label_9.setGeometry(QtCore.QRect(10, 70, 81, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_7.setGeometry(QtCore.QRect(90, 160, 61, 20))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 40, 91, 20))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.groupBox_9 = QtGui.QGroupBox(self.groupBox_6)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 250, 191, 201))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.label_16 = QtGui.QLabel(self.groupBox_9)
        self.label_16.setGeometry(QtCore.QRect(60, 20, 21, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.groupBox_9)
        self.label_17.setGeometry(QtCore.QRect(30, 50, 46, 13))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.groupBox_9)
        self.label_18.setGeometry(QtCore.QRect(30, 80, 46, 13))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.groupBox_9)
        self.label_19.setGeometry(QtCore.QRect(30, 110, 46, 13))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.groupBox_9)
        self.label_20.setGeometry(QtCore.QRect(50, 140, 21, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.groupBox_9)
        self.label_21.setGeometry(QtCore.QRect(30, 170, 41, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_9.setGeometry(QtCore.QRect(80, 20, 71, 20))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_10.setGeometry(QtCore.QRect(80, 50, 101, 20))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_11.setGeometry(QtCore.QRect(80, 80, 71, 20))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_12 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_12.setGeometry(QtCore.QRect(80, 110, 71, 20))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.lineEdit_13 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_13.setGeometry(QtCore.QRect(80, 140, 71, 20))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.lineEdit_14 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_14.setGeometry(QtCore.QRect(80, 170, 71, 20))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_7.setGeometry(QtCore.QRect(500, 40, 451, 401))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.label_15 = QtGui.QLabel(self.groupBox_7)
        self.label_15.setGeometry(QtCore.QRect(20, 70, 421, 301))
        self.label_15.setText(_fromUtf8(""))
        self.label_15.setPixmap(QtGui.QPixmap(_fromUtf8("sssschart/foo1.png")))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(490, 60, 451, 441))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 421, 301))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("chart/foo.png")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(30, 60, 451, 441))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
       
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 380, 171, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 40, 31, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 40, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(180, 380, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.comboBox = QtGui.QComboBox(self.tab)
        self.comboBox.setGeometry(QtCore.QRect(80, 20, 69, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 20, 241, 481))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
 
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 46, 13))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(270, 20, 351, 481))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.comboBox_3 = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_3.setGeometry(QtCore.QRect(40, 20, 121, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        
        self.groupBox_5 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(630, 20, 331, 311))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_8 = QtGui.QLabel(self.groupBox_5)
        self.label_8.setGeometry(QtCore.QRect(10, 30, 311, 261))
        self.label_8.setText(_fromUtf8(""))
        
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_25 = QtGui.QLabel(self.groupBox_5)
        self.label_25.setGeometry(QtCore.QRect(10, 30, 311, 261))
        self.label_25.setText(_fromUtf8(""))
        self.label_25.setPixmap(QtGui.QPixmap(_fromUtf8("../icon/sdftled.JPG")))
        self.label_25.setScaledContents(True)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox_10 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_10.setGeometry(QtCore.QRect(20, 10, 951, 471))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))

        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.Dense1Pattern)
        item.setForeground(brush)
        self.label_22 = QtGui.QLabel(self.groupBox_10)
        self.label_22.setGeometry(QtCore.QRect(440, 20, 31, 16))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.comboBox_4 = QtGui.QComboBox(self.groupBox_10)
        self.comboBox_4.setGeometry(QtCore.QRect(480, 20, 91, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        
        self.label_23 = QtGui.QLabel(self.groupBox_10)
        self.label_23.setGeometry(QtCore.QRect(40, 30, 81, 16))
        self.label_23.setObjectName(_fromUtf8("label_23"))

        self.label_24 = QtGui.QLabel(self.groupBox_10)
        self.label_24.setGeometry(QtCore.QRect(30, 250, 81, 16))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(780, 560, 121, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(910, 560, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.groupBox_6.setTitle(_translate("Dialog", "ข้อสอบ", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Dialog", "New Item", None))
        item = self.listWidget.item(1)
        item.setText(_translate("Dialog", "New Item", None))
        item = self.listWidget.item(2)
        item.setText(_translate("Dialog", "New Item", None))
        item = self.listWidget.item(3)
        item.setText(_translate("Dialog", "New Item", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_8.setTitle(_translate("Dialog", "รายละเอียดการตรวจ", None))
        self.label_13.setText(_translate("Dialog", "คะแนนเฉลี่ย", None))
        self.label_14.setText(_translate("Dialog", "วิชา", None))
        self.label_11.setText(_translate("Dialog", "คะแนนสูงสุด", None))
        self.label_12.setText(_translate("Dialog", "คะแนนต่ำสุด", None))
        self.label_10.setText(_translate("Dialog", "คะแนนเต็ม", None))
        self.label_9.setText(_translate("Dialog", "จำนวนข้อสอบ", None))
        self.groupBox_9.setTitle(_translate("Dialog", "รายละเอียดแต่ละข้อ", None))
        self.label_16.setText(_translate("Dialog", "ข้อ", None))
        self.label_17.setText(_translate("Dialog", "รหัสนิสิต", None))
        self.label_18.setText(_translate("Dialog", "ตอบถูก", None))
        self.label_19.setText(_translate("Dialog", "ตอบผิด", None))
        self.label_20.setText(_translate("Dialog", "ว่าง", None))
        self.label_21.setText(_translate("Dialog", "ฝนเกิน", None))
        self.groupBox_7.setTitle(_translate("Dialog", "กราฟ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "ข้อมูลทั่วไป", None))
        self.groupBox_2.setTitle(_translate("Dialog", "กราฟ", None))
        self.groupBox.setTitle(_translate("Dialog", "ความยากง่ายของข้อสอบ", None))

        self.label.setText(_translate("Dialog", "ความยากของข้อสอบโดยรวม", None))
        self.label_3.setText(_translate("Dialog", "เฉลย", None))
        self.comboBox.setItemText(0, _translate("Dialog", "ชุดที่1", None))
        self.comboBox.setItemText(1, _translate("Dialog", "ชุดที่2", None))
        self.comboBox.setItemText(2, _translate("Dialog", "ชุดที่3", None))
        self.comboBox.setItemText(3, _translate("Dialog", "ชุดที่4", None))
        self.label_2.setText(_translate("Dialog", "ชุดข้อสอบ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "ความยากง่ายของข้อสอบ", None))
        self.groupBox_3.setTitle(_translate("Dialog", "กลุ่มคะแนน", None))
 
        self.label_5.setText(_translate("Dialog", "กลุ่มเก่ง", None))
        
        self.label_6.setText(_translate("Dialog", "กลุ่มอ่อน", None))
        self.groupBox_4.setTitle(_translate("Dialog", "ข้อสอบ", None))
        self.label_7.setText(_translate("Dialog", "เฉลย", None))
        self.comboBox_3.setItemText(0, _translate("Dialog", "ชุดที่1", None))
        self.comboBox_3.setItemText(1, _translate("Dialog", "ชุดที่2", None))
        self.comboBox_3.setItemText(2, _translate("Dialog", "ชุดที่3", None))
        self.comboBox_3.setItemText(3, _translate("Dialog", "ชุดที่4", None))
       
        self.groupBox_5.setTitle(_translate("Dialog", "กราฟ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "การจําแนกผู้สอบตามระดับความสามารถ", None))
        self.groupBox_10.setTitle(_translate("Dialog", "GroupBox", None))
 
        self.label_22.setText(_translate("Dialog", "เฉลย", None))
        self.comboBox_4.setItemText(0, _translate("Dialog", "ชุดที่1", None))
        self.comboBox_4.setItemText(1, _translate("Dialog", "ชุดที่2", None))
        self.comboBox_4.setItemText(2, _translate("Dialog", "ชุดที่3", None))
        self.comboBox_4.setItemText(3, _translate("Dialog", "ชุดที่4", None))
        
        self.label_23.setText(_translate("Dialog", "กลุ่มคะแนนสูง", None))

        self.label_24.setText(_translate("Dialog", "กลุ่มคะแนนต่ำ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Dialog", " ประสิทธิภาพของตัวลวง", None))
        self.pushButton.setText(_translate("Dialog", "บันทึกการวิเคราะห์", None))
        self.pushButton_2.setText(_translate("Dialog", "ยกเลิก", None))


        self.listWidget.currentItemChanged.connect(self.ShowDetail)

        self.connect(self.comboBox, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.SDifficulty )
        self.connect(self.comboBox_3, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.Distin )
        self.connect(self.comboBox_4, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.Distracter )
        self.Distin()
        self.List_main=[]

        #####################################################################

        for name in os.listdir("inspected\SC\onekey"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\SC\onekey\{:>}".format(name))

        for name in os.listdir("inspected\SC\k1"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\SC\k1\{:>}".format(name))

        for name in os.listdir("inspected\SC\k2"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\SC\k2\{:>}".format(name))

        for name in os.listdir("inspected\SC\k3"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\SC\k3\{:>}".format(name))

        for name in os.listdir("inspected\SC\k4"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\SC\k4\{:>}".format(name))
        #####################################################################
        for name in os.listdir("inspected\M1\onekey"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\M1\onekey\{:>}".format(name))

        for name in os.listdir("inspected\M1\k1"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\M1\k1\{:>}".format(name))

        for name in os.listdir("inspected\M1\k2"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\M1\k2\{:>}".format(name))

        for name in os.listdir("inspected\M1\k3"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\M1\k3\{:>}".format(name))

        for name in os.listdir("inspected\M1\k4"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\M1\k4\{:>}".format(name))

        ##########################################################################
        for name in os.listdir("inspected\M2\onekey"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\M2\onekey\{:>}".format(name))

        for name in os.listdir("inspected\M2\k1"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\M2\k1\{:>}".format(name))

        for name in os.listdir("inspected\M2\k2"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\M2\k2\{:>}".format(name))

        for name in os.listdir("inspected\M2\k3"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\M2\k3\{:>}".format(name))

        for name in os.listdir("inspected\M2\k4"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\M2\k4\{:>}".format(name))

        ##########################################################################
        for name in os.listdir("inspected\M3\onekey"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\M3\onekey\{:>}".format(name))

        for name in os.listdir("inspected\M3\k1"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\M3\k1\{:>}".format(name))

        for name in os.listdir("inspected\M3\k2"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\M3\k2\{:>}".format(name))

        for name in os.listdir("inspected\M3\k3"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\M3\k3\{:>}".format(name))

        for name in os.listdir("inspected\M3\k4"):
            if name.endswith(".txt"):
                #print(name)
                self.List_main.append("inspected\M3\k4\{:>}".format(name))














        file = open("setting/SelectKey.txt", "r")
        list_file=file.readlines()
        file.close()
        if(list_file[0].strip()=="single"):
            self.comboBox.setEnabled(False)
        else:
            self.comboBox.setEnabled(True)



 


        for i in range(len(self.List_main)):

                    file = open(str(self.List_main[i]), "r")
                    list_file=file.readlines()
                    file.close()
                    item = QtGui.QListWidgetItem()
                    self.listWidget.addItem(item)
                    item = self.listWidget.item(i)
                     
                    item.setText(_translate("Dialog", str(list_file[1]).strip(), None))

         
        self.lineEdit_6.setText(str(self.MinScore()).replace("[", "").replace("]", ""))
        self.lineEdit_7.setText(str(self.MaxScore()).replace("[", "").replace("]", ""))
        self.lineEdit_8.setText(str(self.AverageScore()))
        self.SDifficulty(1)
        self.Distracter(1)
        
    def test(self):
        print "Test"
    def ShowDetail(self): 
        index=self.listWidget.currentRow()
        print self.List_main[index]
        file = open(str(self.List_main[index]).strip(), "r")
        list_inspected=file.readlines()
        file.close()

        file = open("setting/format_tab2.txt", "r")
        format =file.readlines()
        file.close()
        if (format[0].strip()=="Yes"):
            self.lineEdit_10.setText(list_inspected[1])
            self.lineEdit_11.setText(list_inspected[4])
            self.lineEdit_12.setText(list_inspected[5])
            self.lineEdit_13.setText(list_inspected[6])
            self.lineEdit_14.setText(list_inspected[7])
        else:
            self.lineEdit_10.setText(list_inspected[1])
            self.lineEdit_11.setText(list_inspected[5])
            self.lineEdit_12.setText(list_inspected[6])
            self.lineEdit_13.setText(list_inspected[7])
            self.lineEdit_14.setText(list_inspected[8])


    def MaxScore(self):
        Score=[]

        for i in range(len(self.List_main)):
                file = open(str(self.List_main[i]).strip(), "r")
                list_inspected=file.readlines()
                file.close()
                Score.append([float(list_inspected[3].strip())])
        return min(Score)
    def MinScore(self):
        Score=[]
 
        for i in range(len(self.List_main)):
                file = open(str(self.List_main[i]).strip(), "r")
                list_inspected=file.readlines()
                file.close()
                Score.append([float(list_inspected[3].strip())])
        return max(Score)
    def AverageScore(self):
        Score=[]
      
        for i in range(len(self.List_main)):
                file = open(str(self.List_main[i]).strip(), "r")
                list_inspected=file.readlines()
                file.close()
                Score.append([float(list_inspected[3].strip())])
        #return sum(Score) 
        Sum=0.0
        for i in range(len(Score)):
            Sum=Sum+float(str(Score[i]).replace("[", "").replace("]", ""))
            
        return  Sum/len(Score)

    def SDifficulty(self,Key): 
        LIST_D=[]
        LIST_C=[]
        NUM=0
         
        Key=self.comboBox.currentIndex()+1
        self.D=difficulty.Difficulty(0)
        LIST_D,LIST_C,NUM,SUM,LIST_VALUE=self.D.main(Key)
        #self.CD=Cart_diff.Cart_diff(0)
        #self.CD.main(LIST_VALUE)
        #self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("chart/foo.png")))
        print LIST_C
        Aert=""     
        if SUM <=25:
            Aert="Very Difficult"   
        elif SUM> 25 and SUM <75: 
            Aert="Medium"   
        elif SUM >=75:
            Aert="Very Easy"   
        self.lineEdit.setText(Aert)
        if self.Statediff==False:
            self.tableWidget = QtGui.QTableWidget(self.groupBox)
            self.tableWidget.setGeometry(QtCore.QRect(10, 70, 421, 291))
            self.tableWidget.setAutoScrollMargin(10)
            self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            self.tableWidget.setProperty("showDropIndicator", True)
            self.tableWidget.setDragEnabled(False)
            self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
            self.tableWidget.setColumnCount(4)
            self.tableWidget.setRowCount(120)
        
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        for i in range(120):
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setVerticalHeaderItem(i, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(i, 0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(i, 1, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(i, 2, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(i, 3, item)

        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ข้อที่", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "ตอบผิด", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "ตอบถูก", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "ระดับ", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        for i in range(120):
 
            diff=""

            if LIST_D[i]=="ve":
                diff="Very Easy"
            elif LIST_D[i]=="e":
                diff="Easy"
            elif LIST_D[i]=="m":
                diff="Medium"
            elif LIST_D[i]=="c":
                diff="Difficult"
            elif LIST_D[i]=="vc":
                diff="Very Difficult"
 
            item = self.tableWidget.item(i, 0)
            item.setText(_translate("Dialog", str(i+1), None))
            item = self.tableWidget.item(i, 1)
            item.setText(_translate("Dialog",str(NUM-LIST_C[i]) , None))
            item = self.tableWidget.item(i, 2)
            item.setText(_translate("Dialog", str(LIST_C[i]), None))
            item = self.tableWidget.item(i, 3)
            item.setText(_translate("Dialog", diff, None)) 

        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.Statediff=True



    def Distracter(self,Key):
        Key=self.comboBox_4.currentIndex()+1
        self.H=distracter.Distracter(0)
        List_DIS,List_Si,List_Gi,ReadKey,LisT=self.H.SelectExam(Key)
        if self.Distracter_state==False:
            self.tableWidget_6 = QtGui.QTableWidget(self.groupBox_10)
            self.tableWidget_6.setGeometry(QtCore.QRect(30, 50, 381, 192))
            self.tableWidget_6.setObjectName(_fromUtf8("tableWidget_6"))
            self.tableWidget_6.setColumnCount(5)
        self.tableWidget_6.setRowCount(len(List_Gi))


        
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, item)

        for i in range(len(List_Gi)):
            item = QtGui.QTableWidgetItem()
            self.tableWidget_6.setVerticalHeaderItem(i, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_6.setItem(i, 0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_6.setItem(i, 1, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_6.setItem(i, 2, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_6.setItem(i, 3, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_6.setItem(i, 4, item)
        
        
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ตัวเลือก1", None))
        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "ตัวเลือก2", None))
        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "ตัวเลือก3", None))
        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "ตัวเลือก5", None))
        item = self.tableWidget_6.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "คำตอบ", None))
        __sortingEnabled = self.tableWidget_6.isSortingEnabled()
        self.tableWidget_6.setSortingEnabled(False)

        for i in range(len(List_Gi)):
            item = self.tableWidget_6.verticalHeaderItem(i)
            item.setText(_translate("Dialog", "ข้อ"+str(i+1), None))
            item = self.tableWidget_6.item(i, 0)
            item.setText(_translate("Dialog", str(List_Gi[i][0]), None))
            item = self.tableWidget_6.item(i, 1)
            item.setText(_translate("Dialog", str(List_Gi[i][1]), None))
            item = self.tableWidget_6.item(i, 2)
            item.setText(_translate("Dialog", str(List_Gi[i][2]), None))
            item = self.tableWidget_6.item(i, 3)
            item.setText(_translate("Dialog", str(List_Gi[i][3]), None))
            item = self.tableWidget_6.item(i, 4)
            item.setText(_translate("Dialog", str(LisT[i]), None))

        self.tableWidget_6.setSortingEnabled(__sortingEnabled)   
        

        ##################################################################
        if self.Distracter_state==False:

            self.tableWidget_7 = QtGui.QTableWidget(self.groupBox_10)
            self.tableWidget_7.setGeometry(QtCore.QRect(30, 270, 381, 192))
            self.tableWidget_7.setObjectName(_fromUtf8("tableWidget_7"))
            self.tableWidget_7.setColumnCount(5)

        self.tableWidget_7.setRowCount(len(List_Si))

        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, item)

        for i in range(len(List_Si)):
            item = QtGui.QTableWidgetItem()
            self.tableWidget_7.setVerticalHeaderItem(i, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_7.setItem(i, 0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_7.setItem(i, 1, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_7.setItem(i, 2, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_7.setItem(i, 3, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_7.setItem(i, 4, item)
       
        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ตัวเลือก1", None))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "ตัวเลือก2", None))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "ตัวเลือก3", None))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "ตัวเลือก5", None))
        item = self.tableWidget_7.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "คำตอบ", None))
        __sortingEnabled = self.tableWidget_7.isSortingEnabled()
        self.tableWidget_7.setSortingEnabled(False)

        for i in range(len(List_Si)):       
            item = self.tableWidget_7.verticalHeaderItem(i)
            item.setText(_translate("Dialog", "ข้อ"+str(i+1), None))
            item = self.tableWidget_7.item(i, 0)
            item.setText(_translate("Dialog", str(List_Si[i][0]), None))
            item = self.tableWidget_7.item(i, 1)
            item.setText(_translate("Dialog", str(List_Si[i][1]), None))
            item = self.tableWidget_7.item(i, 2)
            item.setText(_translate("Dialog", str(List_Si[i][2]), None))
            item = self.tableWidget_7.item(i, 3)
            item.setText(_translate("Dialog", str(List_Si[i][3]), None))
            item = self.tableWidget_7.item(i, 4)
            item.setText(_translate("Dialog", str(LisT[i]), None))

        self.tableWidget_7.setSortingEnabled(__sortingEnabled)
        ######################################################################
        if self.Distracter_state==False:
            self.tableWidget_5 = QtGui.QTableWidget(self.groupBox_10)
            self.tableWidget_5.setGeometry(QtCore.QRect(440, 50, 481, 371))
            self.tableWidget_5.setObjectName(_fromUtf8("tableWidget_5"))
            self.tableWidget_5.setColumnCount(4)
            self.tableWidget_5.setRowCount(120)

        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)



        for i in range(len(List_DIS)): 
            item = QtGui.QTableWidgetItem()
            self.tableWidget_5.setVerticalHeaderItem(i, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_5.setItem(i, 0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_5.setItem(i, 1, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_5.setItem(i, 2, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_5.setItem(i, 3, item)



        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ตัวเลือก1", None))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "ตัวเลือก2", None))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "ตัวเลือก3", None))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "ตัวเลือก5", None))
        __sortingEnabled = self.tableWidget_5.isSortingEnabled()
        self.tableWidget_5.setSortingEnabled(False)


        for i in range(len(List_DIS)):

            item = self.tableWidget_5.verticalHeaderItem(i)
            item.setText(_translate("Dialog", "ข้อ"+str(i+1), None))
            item = self.tableWidget_5.item(i, 0)
            item.setText(_translate("Dialog", self.Calcul(List_DIS[i][0]), None))
            item = self.tableWidget_5.item(i, 1)
            item.setText(_translate("Dialog", self.Calcul(List_DIS[i][1]), None))
            item = self.tableWidget_5.item(i, 2)
            item.setText(_translate("Dialog", self.Calcul(List_DIS[i][2]), None))
            item = self.tableWidget_5.item(i, 3)
            item.setText(_translate("Dialog", self.Calcul(List_DIS[i][3]), None))


        self.tableWidget_5.setSortingEnabled(__sortingEnabled)
        self.Distracter_state=True

    def Calcul(self,Value):
        message=""
        if Value<=0.05:
            message="No"
        elif  Value<0.5 and Value>0.05:
            message="Medium"
        elif  Value>=0.5 and Value<=1 :
            message="Good"
        elif Value==10:
            message="Answer"

        return message    
    def Distin(self):

        
        


        Key=self.comboBox_3.currentIndex()+1
        self.M=distinguish.Distinguish(0)




        List_silly,List_gin,List_count_gin,List_count_silly,List_final=self.M.main(1)
        List_silly,List_gin,List_count_gin,List_count_silly,List_final=self.M.main(2)
        List_silly,List_gin,List_count_gin,List_count_silly,List_final=self.M.main(3)
        List_silly,List_gin,List_count_gin,List_count_silly,List_final=self.M.main(4)
        List_silly,List_gin,List_count_gin,List_count_silly,List_final=self.M.main(Key)

        #tableWidget_List_gin
        if self.State==False:
            self.tableWidget_2 = QtGui.QTableWidget(self.groupBox_3)
            self.tableWidget_2.setGeometry(QtCore.QRect(10, 50, 221, 192))
            self.tableWidget_2.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            self.tableWidget_2.setObjectName(_fromUtf8("tableWidget_2"))
            self.tableWidget_2.setColumnCount(2)
        self.tableWidget_2.setRowCount(len(List_gin))



        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)


        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        for i in range(len(List_gin)):
            item = QtGui.QTableWidgetItem()
            self.tableWidget_2.setItem(i, 0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_2.setItem(i, 1, item)
 




        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1", None))



        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "รหัสนิสิต", None))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "คะแนน", None))
        __sortingEnabled = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)

        List_gin.sort(reverse=True)

        for i in range(len(List_gin)):
            item = self.tableWidget_2.item(i, 0)
            item.setText(_translate("Dialog", List_gin[i][2], None))
            item = self.tableWidget_2.item(i, 1)

            item.setText(_translate("Dialog", str(List_gin[i][0]), None))
        ######################################################################
        if self.State==False:
            self.tableWidget_3 = QtGui.QTableWidget(self.groupBox_3)
            self.tableWidget_3.setGeometry(QtCore.QRect(10, 270, 221, 192))
            self.tableWidget_3.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            self.tableWidget_3.setObjectName(_fromUtf8("tableWidget_3"))
            self.tableWidget_3.setColumnCount(2)
        self.tableWidget_3.setRowCount(len(List_silly))





        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, item)


        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, item)
        for i in range(len(List_silly)):
            item = QtGui.QTableWidgetItem()
            self.tableWidget_3.setItem(i, 0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_3.setItem(i, 1, item)
 
     



        item = self.tableWidget_3.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1", None))



        item = self.tableWidget_3.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "รหัสนิสิต", None))
        item = self.tableWidget_3.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "คะแนน", None))
        __sortingEnabled = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)


        List_silly.sort(reverse=True)
        for i in range(len(List_silly)):
            item = self.tableWidget_3.item(i, 0)
            item.setText(_translate("Dialog", List_silly[i][2], None))
            item = self.tableWidget_3.item(i, 1)
            item.setText(_translate("Dialog", str(List_silly[i][0]), None))
         

        self.tableWidget_3.setSortingEnabled(__sortingEnabled)

        ##################tableWidget_4###################

        if self.State==False:
            self.tableWidget_4 = QtGui.QTableWidget(self.groupBox_4)
            self.tableWidget_4.setGeometry(QtCore.QRect(10, 50, 321, 411))
            self.tableWidget_4.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
            self.tableWidget_4.setObjectName(_fromUtf8("tableWidget_4"))
            self.tableWidget_4.setColumnCount(3)
            self.tableWidget_4.setRowCount(120)


        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)


        for i in range(120):
            item = QtGui.QTableWidgetItem()
            self.tableWidget_4.setVerticalHeaderItem(i, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_4.setItem(i, 0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_4.setItem(i, 1, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget_4.setItem(i, 2, item)

        item = self.tableWidget_4.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "ข้อ1", None))
        item = self.tableWidget_4.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "เก่งตอบถูก/คน", None))
        item = self.tableWidget_4.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "อ่อนตอบถูก/คน", None))
        item = self.tableWidget_4.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "ระดับการจำแนก", None))
        __sortingEnabled = self.tableWidget_4.isSortingEnabled()
        self.tableWidget_4.setSortingEnabled(False)
        Best=0.0
        Better=0.0
        Good=0.0
        Medium=0.0
        Low=0.0
        Lowly=0.0
        No=0.0
        for i in range(len(List_final)):

            message=""
            item = self.tableWidget_4.verticalHeaderItem(i)
            item.setText(_translate("Dialog", "ข้อ "+str(i+1), None))
            item = self.tableWidget_4.item(i, 0)
            item.setText(_translate("Dialog", str(List_count_gin[i]), None))
            item = self.tableWidget_4.item(i, 1)
            item.setText(_translate("Dialog", str(List_count_silly[i]), None))

            if List_final[i]==1.0:
                messag="Best"
                Best=Best+1
            elif List_final[i]>=0.80 and List_final[i]<=0.99:
                messag="Better "
                Better=Better+1
            elif List_final[i]>=0.60 and List_final[i]<=0.79:
                messag="Good"
                Good=Good+1
            elif List_final[i]>=0.40 and List_final[i]<=0.59:
                messag="Medium "
                Medium=Medium+1
            elif List_final[i]>=0.20 and List_final[i]<=0.39:
                messag="Low "
                Low=Low+1
            elif List_final[i]>=0.00 and List_final[i]<=0.19:
                messag="Lowly "
                Lowly=Lowly+1
            elif List_final[i]<0.00 :
                messag="Can't"
                No=No+1



            item = self.tableWidget_4.item(i, 2)
            item.setText(_translate("Dialog",messag , None))
        Best=(Best*100)/120.0
        Better=(Better*100)/120.0
        Good=(Good*100)/120.0
        Medium=(Medium*100)/120.0
        Low=(Low*100)/120.0
        Lowly=(Lowly*100)/120.0
        No=(No*100)/120.0           
        #print "Fuck",Best, Better, Good, Medium,Low,Lowly,No


        if Key==1:
            if self.sta1==0:
                self.Ch1=Chart_distinguish1.Chart_distinguish(0)
                self.Ch1.Main(Best, Better, Good, Medium,Low,Lowly,No,"c1")
            self.label_8.setPixmap(QtGui.QPixmap(_fromUtf8("chart/c1.png")))
            self.sta1=1;
        elif Key==2:
            if self.sta2==0:
                self.Ch2=Chart_distinguish2.Chart_distinguish(0)
                self.Ch2.Main(Best, Better, Good, Medium,Low,Lowly,No,"c2")
            self.label_8.setPixmap(QtGui.QPixmap(_fromUtf8("chart/c2.png")))
            self.sta2=1
        elif Key==3:
            if self.sta3==0:
                self.Ch3=Chart_distinguish3.Chart_distinguish(0)
                self.Ch3.Main(Best, Better, Good, Medium,Low,Lowly,No,"c3")
            self.label_8.setPixmap(QtGui.QPixmap(_fromUtf8("chart/c3.png")))
            self.sta3=1
        elif Key==4:
            if self.sta4==0:
                self.Ch4=Chart_distinguish4.Chart_distinguish(0)
                self.Ch4.Main(Best, Better, Good, Medium,Low,Lowly,No,"c4")
            self.label_8.setPixmap(QtGui.QPixmap(_fromUtf8("chart/c4.png")))
            self.sta4=1

        
        
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)
 
  
        
        self.State=True 

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_()) 

