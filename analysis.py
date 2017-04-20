# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'analysis.ui'
#
# Created: Thu Dec 18 13:17:18 2014
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui
import sys,os
import difficulty
import distracter
import Cart_diff
import Chart_distinguish
import DocAnalysis
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
    Diff_sent1=[]
    Diff_sent2=[]
    Diff_sent3=[]
    Diff_sent4=[]
    Diff_num=[]
    Diff_LIST_VALUE1=[]
    Diff_LIST_VALUE2=[]
    Diff_LIST_VALUE3=[]
    Diff_LIST_VALUE4=[]
    Diff_num1=0
    Diff_num2=0
    Diff_num3=0
    Diff_num4=0
    Diff_num=0
    Diff_level1=[]
    Diff_level2=[]
    Diff_level3=[]
    Diff_level4=[]
    Distin_sent=[]
    Distract_sent=[]


    Distracter_List_main_1=[]
    Distracter_List_main_2=[]
    Distracter_List_main_3=[]
    Distracter_List_main_4=[]

    Distracter_List_High_1=[]
    Distracter_List_High_2=[]
    Distracter_List_High_3=[]
    Distracter_List_High_4=[]

    Distracter_List_Low_1=[]
    Distracter_List_Low_2=[]
    Distracter_List_Low_3=[]
    Distracter_List_Low_4=[]

    distinguish_L1=[]
    distinguish_L2=[]
    distinguish_L3=[]
    distinguish_L4=[]


    distinguish_H1=[]
    distinguish_H2=[]
    distinguish_H3=[]
    distinguish_H4=[]

    List_count_gin_1=[]
    List_count_gin_2=[]
    List_count_gin_3=[]
    List_count_gin_4=[]

    List_count_silly_1=[]
    List_count_silly_2=[]
    List_count_silly_3=[]
    List_count_silly_4=[]

    List_final_1=[]
    List_final_2=[]
    List_final_3=[]
    List_final_4=[]
    number=0
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
        self.groupBox_6.setGeometry(QtCore.QRect(140, 30, 721, 461))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.listWidget = QtGui.QListWidget(self.groupBox_6)
        self.listWidget.setGeometry(QtCore.QRect(10, 30, 231, 411))
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
        self.groupBox_8.setGeometry(QtCore.QRect(290, 20, 391, 221))
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
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 40, 281, 20))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.groupBox_9 = QtGui.QGroupBox(self.groupBox_6)
        self.groupBox_9.setGeometry(QtCore.QRect(290, 240, 391, 201))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.label_16 = QtGui.QLabel(self.groupBox_9)
        self.label_16.setGeometry(QtCore.QRect(60, 20, 21, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.groupBox_9)
        self.label_17.setGeometry(QtCore.QRect(160, 20, 46, 13))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.groupBox_9)
        self.label_18.setGeometry(QtCore.QRect(30, 50, 46, 13))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.groupBox_9)
        self.label_19.setGeometry(QtCore.QRect(30, 80, 46, 13))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.groupBox_9)
        self.label_20.setGeometry(QtCore.QRect(50, 110, 21, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.groupBox_9)
        self.label_21.setGeometry(QtCore.QRect(30, 140, 41, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))

        self.lineEdit_26 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_26.setGeometry(QtCore.QRect(210, 140, 71, 20))
        self.lineEdit_26.setObjectName(_fromUtf8("lineEdit_26"))
        self.label_8 = QtGui.QLabel(self.groupBox_9)
        self.label_8.setGeometry(QtCore.QRect(170, 140, 41, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))        
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_9.setGeometry(QtCore.QRect(80, 20, 71, 20))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_10.setGeometry(QtCore.QRect(210, 20, 101, 20))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_11.setGeometry(QtCore.QRect(80, 50, 71, 20))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.lineEdit_12 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_12.setGeometry(QtCore.QRect(80, 80, 71, 20))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.lineEdit_13 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_13.setGeometry(QtCore.QRect(80, 110, 71, 20))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.lineEdit_14 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_14.setGeometry(QtCore.QRect(80, 140, 71, 20))
        self.lineEdit_14.setReadOnly(True)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.label_15 = QtGui.QLabel(self.groupBox_9)
        self.label_15.setGeometry(QtCore.QRect(170, 50, 31, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_32 = QtGui.QLabel(self.groupBox_9)
        self.label_32.setGeometry(QtCore.QRect(170, 80, 31, 16))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.label_33 = QtGui.QLabel(self.groupBox_9)
        self.label_33.setGeometry(QtCore.QRect(170, 110, 31, 16))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.lineEdit_22 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_22.setGeometry(QtCore.QRect(210, 50, 71, 20))
        self.lineEdit_22.setObjectName(_fromUtf8("lineEdit_22"))
        self.lineEdit_23 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_23.setGeometry(QtCore.QRect(210, 80, 71, 20))
        self.lineEdit_23.setObjectName(_fromUtf8("lineEdit_23"))
        self.lineEdit_24 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_24.setGeometry(QtCore.QRect(210, 110, 71, 20))
        self.lineEdit_24.setObjectName(_fromUtf8("lineEdit_24"))
        self.label_34 = QtGui.QLabel(self.groupBox_9)
        self.label_34.setGeometry(QtCore.QRect(20, 170, 51, 20))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.lineEdit_25 = QtGui.QLineEdit(self.groupBox_9)
        self.lineEdit_25.setGeometry(QtCore.QRect(80, 170, 71, 20))
        self.lineEdit_25.setReadOnly(True)
        self.lineEdit_25.setObjectName(_fromUtf8("lineEdit_25"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(490, 60, 451, 441))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 421, 301))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("../icon/sdftled.JPG")))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.label_5.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
         
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 250, 81, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(270, 20, 351, 481))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 31, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))


        self.comboBox_3 = QtGui.QComboBox(self.groupBox_4)
        self.comboBox_3.setGeometry(QtCore.QRect(40, 20, 121, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
         
        self.groupBox_5 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(630, 20, 331, 481))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.lineEdit_15 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_15.setGeometry(QtCore.QRect(150, 20, 101, 20))
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        #self.lineEdit_15.setStyleSheet('color: yellow')
        self.lineEdit_16 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_16.setGeometry(QtCore.QRect(150, 50, 101, 20))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.lineEdit_17 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_17.setGeometry(QtCore.QRect(150, 80, 101, 20))
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.lineEdit_18 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_18.setGeometry(QtCore.QRect(150, 110, 101, 20))
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.lineEdit_19 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_19.setGeometry(QtCore.QRect(150, 140, 101, 20))
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.lineEdit_20 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_20.setGeometry(QtCore.QRect(150, 170, 101, 20))
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.lineEdit_21 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_21.setGeometry(QtCore.QRect(150, 200, 101, 20))
        self.lineEdit_21.setObjectName(_fromUtf8("lineEdit_21"))
        self.label_25 = QtGui.QLabel(self.groupBox_5)
        self.label_25.setGeometry(QtCore.QRect(90, 20, 46, 13))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_26 = QtGui.QLabel(self.groupBox_5)
        self.label_26.setGeometry(QtCore.QRect(90, 50, 46, 13))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(self.groupBox_5)
        self.label_27.setGeometry(QtCore.QRect(90, 80, 46, 13))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(self.groupBox_5)
        self.label_28.setGeometry(QtCore.QRect(90, 110, 46, 13))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.label_29 = QtGui.QLabel(self.groupBox_5)
        self.label_29.setGeometry(QtCore.QRect(90, 140, 46, 13))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_30 = QtGui.QLabel(self.groupBox_5)
        self.label_30.setGeometry(QtCore.QRect(90, 170, 46, 13))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_31 = QtGui.QLabel(self.groupBox_5)
        self.label_31.setGeometry(QtCore.QRect(90, 200, 46, 13))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox_10 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_10.setGeometry(QtCore.QRect(20, 10, 951, 471))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
         
        item = QtGui.QTableWidgetItem()
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
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox_5)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 220, 311, 251))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.label_35 = QtGui.QLabel(self.groupBox_7)
        self.label_35 = QtGui.QLabel(self.groupBox_7)
        self.label_35.setGeometry(QtCore.QRect(20, 20, 271, 221))
        self.label_35.setText(_fromUtf8(""))
        self.label_35.setPixmap(QtGui.QPixmap(_fromUtf8("")))
        self.label_35.setScaledContents(True)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_35.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(2)
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
        self.label_17.setText(_translate("Dialog", "Free Score", None))
        self.label_18.setText(_translate("Dialog", "ตอบถูก", None))
        self.label_19.setText(_translate("Dialog", "ตอบผิด", None))
        self.label_20.setText(_translate("Dialog", "ว่าง", None))
        self.label_21.setText(_translate("Dialog", "ฝนเกิน", None))
        self.label_15.setText(_translate("Dialog", "ช่วง1", None))
        self.label_32.setText(_translate("Dialog", "ช่วง2", None))
        self.label_33.setText(_translate("Dialog", "ช่วง3", None))
        self.label_34.setText(_translate("Dialog", "ฝนไม่พอ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Dialog", "ข้อมูลทั่วไป", None))
        self.groupBox_2.setTitle(_translate("Dialog", "กราฟ", None))
        self.groupBox.setTitle(_translate("Dialog", "ความยากง่ายของข้อสอบ", None))
        self.groupBox_7.setTitle(_translate("Dialog", "Chart", None))         
        self.label.setText(_translate("Dialog", "ความยากของข้อสอบโดยรวม", None))
        self.label_3.setText(_translate("Dialog", "เฉลย", None))
        self.label_8.setText(_translate("Dialog", "Total", None))
        self.comboBox.setItemText(0, _translate("Dialog", "ชุดที่1", None))
        self.comboBox.setItemText(1, _translate("Dialog", "ชุดที่2", None))
        self.comboBox.setItemText(2, _translate("Dialog", "ชุดที่3", None))
        self.comboBox.setItemText(3, _translate("Dialog", "ชุดที่4", None))
        self.label_2.setText(_translate("Dialog", "ชุดข้อสอบ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "ความยากง่ายของข้อสอบ", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Score Group", None))
        
        self.label_5.setText(_translate("Dialog", "High Group", None))
         
        self.label_6.setText(_translate("Dialog", "Low Group", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Exam", None))
        self.label_7.setText(_translate("Dialog", "Key", None))
        self.comboBox_3.setItemText(0, _translate("Dialog", "Key 1", None))
        self.comboBox_3.setItemText(1, _translate("Dialog", "Key 2", None))
        self.comboBox_3.setItemText(2, _translate("Dialog", "Key 3", None))
        self.comboBox_3.setItemText(3, _translate("Dialog", "Key 4", None))
         
        self.groupBox_5.setTitle(_translate("Dialog", "Aggregate", None))
        self.label_25.setText(_translate("Dialog", "Best", None))

        self.label_26.setText(_translate("Dialog", "Better", None))
        self.label_27.setText(_translate("Dialog", "Good", None))
        self.label_28.setText(_translate("Dialog", "Medium", None))
        self.label_29.setText(_translate("Dialog", "Low", None))
        self.label_30.setText(_translate("Dialog", "Lowly", None))
        self.label_31.setText(_translate("Dialog", "Can\'t", None))
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
        self.pushButton.clicked.connect(self.SaveAnalysis)
        self.List_main=[]
        self.label_35.mousePressEvent=self.alert_char_distin 
        self.label_4.mousePressEvent=self.alert_char_deff
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
            self.comboBox_3.setEnabled(False)
            self.comboBox_4.setEnabled(False)
        else:
            self.comboBox.setEnabled(True)
            self.comboBox_3.setEnabled(True)
            self.comboBox_4.setEnabled(True)



 


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
        file = open("setting/SelectKey.txt", "r")
        SUB =file.readlines()
        file.close()

        self.lineEdit_5.setText(str(self.TotalScore()))
        if SUB[0].strip()=="multiple":
            self.lineEdit_3.setText(SUB[1]+" "+SUB[2]+" "+SUB[3])
        else:
            self.lineEdit_3.setText(SUB[1])

        
       

        file = open("setting/format_tab2_down.txt", "r")
        NUMBER_C =file.readlines()
        file.close()

 
        if NUMBER_C[0].strip()=="Yes":
            if self.Check_type()=="C1":
                out=NUMBER_C[3].strip().split('-')        
                self.lineEdit_4.setText(str(out[1]))
                self.number=int(out[1])
                print "gggg"
            elif self.Check_type()=="C2":
                out=NUMBER_C[9].strip().split('-')
                self.lineEdit_4.setText(str(out[1]))
                self.number=int(out[1])
            elif self.Check_type()=="C3":
                out=NUMBER_C[15].strip().split('-')
                self.lineEdit_4.setText(str(out[1]))
                self.number=int(out[1])
        else:
            self.lineEdit_4.setText("120")
            self.number=120
        print "JJJJJJJJJJJ",self.number

        self.SDifficulty(4)
        self.SDifficulty(3)
        self.SDifficulty(2)
        self.SDifficulty(1)


        
        try:
            self.Distin(4)
        except:
            pass
        try:
            self.Distin(3)
        except:
            pass
        try:
            self.Distin(2)
        except:
            pass
        try:
            self.Distin(1)
        except:
            pass

        try:
            self.Distracter(4)
        except:
            pass
        try:
            self.Distracter(3)
        except:
            pass

        try:
            self.Distracter(2)
        except:
            pass

        try:
            self.Distracter(1)
        except:
            pass


        try:
            self.Distracter(4)
        except:
            pass
        try:
            self.Distracter(3)
        except:
            pass

        try:
            self.Distracter(2)
        except:
            pass

        try:
            self.Distracter(1)
        except:
            pass

    def SaveAnalysis(self):
        self.D=DocAnalysis.Doc(0)
        count=0
        if  self.Diff_sent1!=[]:
            count=count+1  
        if  self.Diff_sent2!=[]:
            count=count+1    
        if  self.Diff_sent3!=[]:
            count=count+1    
        if  self.Diff_sent4!=[]:
            count=count+1 
 
        self.D.Difficulty(count,self.Diff_sent1,self.Diff_sent2,self.Diff_sent3,self.Diff_sent4,self.Diff_level1,self.Diff_level2,self.Diff_level3,self.Diff_level4,self.Diff_LIST_VALUE1,self.Diff_LIST_VALUE2,self.Diff_LIST_VALUE3,self.Diff_LIST_VALUE4,self.Diff_num1,self.Diff_num2,self.Diff_num3,self.Diff_num4)  









        self.D.Distracter(self.Distracter_List_main_1,self.Distracter_List_main_2,self.Distracter_List_main_3,self.Distracter_List_main_4,self.Distracter_List_High_1,self.Distracter_List_High_2,self.Distracter_List_High_3,self.Distracter_List_High_4,self.Distracter_List_Low_1,self.Distracter_List_Low_2,self.Distracter_List_Low_3,self.Distracter_List_Low_4)
        self.D.Distinguish(self.distinguish_L1,self.distinguish_L2,self.distinguish_L3,self.distinguish_L4,self.distinguish_H1,self.distinguish_H2,self.distinguish_H3,self.distinguish_H4,self.List_count_gin_1,self.List_count_gin_2,self.List_count_gin_3,self.List_count_gin_4,self.List_count_silly_1,self.List_count_silly_2,self.List_count_silly_3,self.List_count_silly_4,self.List_final_1,self.List_final_2,self.List_final_3,self.List_final_4)
    def TotalScore(self):
        file = open("setting/format_tab2.txt", "r")
        NUMBER_S =file.readlines()
        file.close()
        file = open("setting/format_tab2_down.txt", "r")
        NUMBER_C =file.readlines()
        file.close()

 
        if NUMBER_C[0].strip()=="Yes":
            if self.Check_type()=="C1":
                out=NUMBER_C[3].strip().split('-') 
                Score=((int(out[1])-int(out[0]))+1)*float(NUMBER_C[4].strip())
                return  Score

                
            elif self.Check_type()=="C2":
                out=NUMBER_C[3].strip().split('-')
                Score=((int(out[1])-int(out[0]))+1)*float(NUMBER_C[4].strip())

                out=NUMBER_C[9].strip().split('-')
                Score=Score+((int(out[1])-int(out[0]))+1)*float(NUMBER_C[10].strip())
                return  Score
            elif self.Check_type()=="C3":
                
                out=NUMBER_C[3].strip().split('-')
                Score=((int(out[1])-int(out[0]))+1)*float(NUMBER_C[4].strip())

                out=NUMBER_C[9].strip().split('-')
                Score=Score+((int(out[1])-int(out[0]))+1)*float(NUMBER_C[10].strip())

                out=NUMBER_C[15].strip().split('-')
                Score=Score+((int(out[1])-int(out[0]))+1)*float(NUMBER_C[16].strip())
                return Score
        else:
            #self.lineEdit_4.setText("120")
            return  120*float(NUMBER_S[1].strip())
    def ShowDetail(self): 
        index=self.listWidget.currentRow()
        print self.List_main[index]
        file = open(str(self.List_main[index]).strip(), "r")
        list_inspected=file.readlines()
        file.close()

        file = open("setting/format_tab2_down.txt", "r")
        format =file.readlines()
        file.close()
        if (format[0].strip()=="No"):
            #self.lineEdit_10.setText(list_inspected[1])
            self.lineEdit_11.setText(list_inspected[4])
            self.lineEdit_12.setText(list_inspected[5])
            self.lineEdit_13.setText(list_inspected[6])
            self.lineEdit_14.setText(list_inspected[7])
            self.lineEdit_25.setText(list_inspected[8])
            self.lineEdit_22.setText("-")#c1
            self.lineEdit_23.setText("-")#c2                
            self.lineEdit_24.setText("-")#c3
            self.lineEdit_26.setText(list_inspected[3])#score
        else:
            if(format[2].strip()=="1Yes" and format[8].strip()=="1No" and format[14].strip()=="1No"):

                #self.lineEdit_10.setText(list_inspected[1])
                self.lineEdit_11.setText(list_inspected[4])
                self.lineEdit_12.setText(list_inspected[5])
                self.lineEdit_13.setText(list_inspected[6])
                self.lineEdit_14.setText(list_inspected[7])
                self.lineEdit_25.setText(list_inspected[8])

                self.lineEdit_22.setText(list_inspected[3])#c1
                self.lineEdit_23.setText("-")#c2                
                self.lineEdit_24.setText("-")#c3  
            self.lineEdit_26.setText(list_inspected[3])#score
            if(format[2].strip()=="1Yes" and format[8].strip()=="1Yes" and format[14].strip()=="1No"):
                #self.lineEdit_10.setText(list_inspected[1])
                self.lineEdit_11.setText(list_inspected[6])#cor
                self.lineEdit_12.setText(list_inspected[7])#inc
                self.lineEdit_13.setText(list_inspected[8])#Emp
                self.lineEdit_14.setText(list_inspected[9])#over
                self.lineEdit_25.setText(list_inspected[10])#less
 

                self.lineEdit_22.setText(list_inspected[3])#c1
                self.lineEdit_23.setText(list_inspected[4])#c2                
                self.lineEdit_24.setText("-")#c3  
                self.lineEdit_26.setText(list_inspected[5])#score
            if(format[2].strip()=="1Yes" and format[8].strip()=="1Yes" and format[14].strip()=="1Yes"):  
                #self.lineEdit_10.setText(list_inspected[1])
                self.lineEdit_11.setText(list_inspected[7])#cor
                self.lineEdit_12.setText(list_inspected[8])#inc
                self.lineEdit_13.setText(list_inspected[9])#Emp
                self.lineEdit_14.setText(list_inspected[10])#over
                self.lineEdit_25.setText(list_inspected[11])#less
 


                self.lineEdit_22.setText(list_inspected[3])#c1
                self.lineEdit_23.setText(list_inspected[4])#c2                
                self.lineEdit_24.setText(list_inspected[5])#c3   
                self.lineEdit_26.setText(list_inspected[6])#score 
        file = open("setting/format_tab3.txt", "r")
        list_fs=file.readlines()
        file.close()
        if list_fs[0].strip()=="Yes": 
            self.lineEdit_10.setText(list_fs[1].strip()) 
        else:
            self.lineEdit_10.setText("-")     
    def Check_type(self):
        file = open("setting/format_tab2_down.txt", "r")
        format =file.readlines()
        file.close()
        if (format[0].strip()=="No"):
            print "hhhh"
            return "SC"
            
        else:
            if(format[2].strip()=="1Yes" and format[8].strip()=="1No" and format[14].strip()=="1No"):
                print "hhhh"
                return "C1"

            elif(format[2].strip()=="1Yes" and format[8].strip()=="1Yes" and format[14].strip()=="1No"):
                return "C2"
            elif(format[2].strip()=="1Yes" and format[8].strip()=="1Yes" and format[14].strip()=="1Yes"):  
                return "C3"
    def MaxScore(self):
        Score=[]
        VAA=self.Check_type()
        for i in range(len(self.List_main)):
                file = open(str(self.List_main[i]).strip(), "r")
                list_inspected=file.readlines()
                file.close()
                if VAA=="SC" or VAA=="C1" :
                    Score.append([float(list_inspected[3].strip())])
                elif VAA=="C2":
                    Score.append([float(list_inspected[5].strip())])
                elif VAA=="C3":    
                    Score.append([float(list_inspected[6].strip())])
        return min(Score)
    def MinScore(self):
        Score=[]
        VAA=self.Check_type()
        for i in range(len(self.List_main)):
                file = open(str(self.List_main[i]).strip(), "r")
                list_inspected=file.readlines()
                file.close()
                if VAA=="SC" or VAA=="C1":
                    Score.append([float(list_inspected[3].strip())])
                elif VAA=="C2":
                    Score.append([float(list_inspected[5].strip())])
                elif VAA=="C3":    
                    Score.append([float(list_inspected[6].strip())])
                #print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&",Score
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
    def alert_char_deff(self,event):
        Key=self.comboBox.currentIndex()+1
        self.D=difficulty.Difficulty(0)
        LIST_D,LIST_C,NUM,SUM,LIST_VALUE=self.D.main(Key,self.number)
        self.CD=Cart_diff.Cart_diff(0)
        self.CD.main_Show(LIST_VALUE,str(Key),self.number)

    def SDifficulty(self,Key): 
        LIST_D=[]
        LIST_C=[]
        try:
          print "KEYYYY:",Key
        except:
            Key=self.comboBox.currentIndex()+1
        
        
        
        NUM=0
        
         
        self.D=difficulty.Difficulty(0)
        LIST_D,LIST_C,NUM,SUM,LIST_VALUE=self.D.main(Key,self.number)
        print LIST_D,LIST_C,NUM,SUM,LIST_VALUE
        self.Diff_num=NUM
        print "++++++++++++",NUM
        if Key==1:
            self.Diff_num1=NUM
            self.Diff_LIST_VALUE1=[]
            self.Diff_LIST_VALUE1=LIST_VALUE
            self.Diff_sent1=[]
            self.Diff_sent1=LIST_C
            self.Diff_level1=LIST_D
        if Key==2:
            self.Diff_num2=NUM
            self.Diff_LIST_VALUE2=[]
            self.Diff_LIST_VALUE2=LIST_VALUE
            self.Diff_sent2=[]
            self.Diff_sent2=LIST_C
            self.Diff_level2=LIST_D
        if Key==3:
            self.Diff_num3=NUM
            self.Diff_LIST_VALUE3=[]
            self.Diff_LIST_VALUE3=LIST_VALUE
            self.Diff_sent3=[]
            self.Diff_sent3=LIST_C
            self.Diff_level3=LIST_D
        if Key==4:
            self.Diff_num4=NUM
            self.Diff_LIST_VALUE4=[]
            self.Diff_LIST_VALUE4=LIST_VALUE
            self.Diff_sent4=[]
            self.Diff_sent4=LIST_C
            self.Diff_level4=LIST_D



        self.CD=Cart_diff.Cart_diff(0)
        self.CD.main(LIST_VALUE,str(Key),self.number)
        if(Key==1):
            self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("chart/1.png")))
        elif(Key==2):
            self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("chart/2.png")))
        elif(Key==3):
            self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("chart/3.png")))
        elif(Key==4):
            self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("chart/4.png")))
        print LIST_C
        Aert=""     
        if SUM >=0.8:
            Aert="Very Easy"     
        elif SUM>= 0.6 and SUM <=0.79: 
            Aert="Easy"  
        elif SUM>= 0.4 and SUM <=0.59: 
            Aert="Medium" 
        elif SUM>= 0.2 and SUM <=0.39:   
            Aert="Difficult"   
        elif SUM<  0.2 : 
             Aert="Very Difficult"
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
        self.tableWidget.setRowCount(self.number)
        
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)

        for i in range(self.number):
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
        item.setText(_translate("Dialog", "", None))
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
        for i in range(self.number):
 
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
        try:
            print Key
        except:
            Key=self.comboBox_4.currentIndex()+1
        self.H=distracter.Distracter(0)
        print "KEY",Key
        List_DIS,List_Si,List_Gi,ReadKey,LisT=self.H.SelectExam(Key,self.number)
        if self.Distracter_state==False:
            self.tableWidget_6 = QtGui.QTableWidget(self.groupBox_10)
            self.tableWidget_6.setGeometry(QtCore.QRect(30, 50, 381, 192))
            self.tableWidget_6.setObjectName(_fromUtf8("tableWidget_6"))
            self.tableWidget_6.setColumnCount(6)
        self.tableWidget_6.setRowCount(len(List_Gi))
        if Key==1:
            self.Distracter_List_main_1=List_DIS
            print "DDDD",List_DIS
            self.Distracter_List_Low_1=List_Si
            self.Distracter_List_High_1=List_Gi
        if Key==2:
            self.Distracter_List_main_2=List_DIS
            self.Distracter_List_Low_2=List_Si
            self.Distracter_List_High_2=List_Gi
        if Key==3:
            self.Distracter_List_main_3=List_DIS
            self.Distracter_List_Low_3=List_Si
            self.Distracter_List_High_3=List_Gi
        if Key==4:
            self.Distracter_List_main_4=List_DIS
            self.Distracter_List_Low_4=List_Si
            self.Distracter_List_High_4=List_Gi 

        for i in range(len(List_DIS)):
            print List_DIS[i]
        
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
        item = QtGui.QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, item)
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
            item = QtGui.QTableWidgetItem()
            self.tableWidget_6.setItem(i, 5, item)        
        
        item = self.tableWidget_6.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ตัวเลือก1", None))

        item = self.tableWidget_6.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "ตัวเลือก2", None))

        item = self.tableWidget_6.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "ตัวเลือก3", None))

        item = self.tableWidget_6.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "ตัวเลือก4", None))

        item = self.tableWidget_6.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "ตัวเลือก5", None))

        item = self.tableWidget_6.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "answer", None))

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
            item.setText(_translate("Dialog", str(List_Gi[i][4]), None))
            item = self.tableWidget_6.item(i, 5)
            item.setText(_translate("Dialog", str(LisT[i]), None))
        self.tableWidget_6.setSortingEnabled(__sortingEnabled)   
        

        ##################################################################
        if self.Distracter_state==False:

            self.tableWidget_7 = QtGui.QTableWidget(self.groupBox_10)
            self.tableWidget_7.setGeometry(QtCore.QRect(30, 270, 381, 192))
            self.tableWidget_7.setObjectName(_fromUtf8("tableWidget_7"))
            self.tableWidget_7.setColumnCount(6)

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
        item = QtGui.QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(5, item)


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
            item = QtGui.QTableWidgetItem()
            self.tableWidget_7.setItem(i, 5, item)


        item = self.tableWidget_7.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ตัวเลือก1", None))
        item = self.tableWidget_7.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "ตัวเลือก2", None))
        item = self.tableWidget_7.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "ตัวเลือก3", None))
        item = self.tableWidget_7.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "ตัวเลือก4", None))
        item = self.tableWidget_7.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "ตัวเลือก5", None))
        item = self.tableWidget_7.horizontalHeaderItem(5)
        item.setText(_translate("Dialog", "answer", None))
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
            item.setText(_translate("Dialog", str(List_Si[i][4]), None))
            item = self.tableWidget_7.item(i, 5)
            item.setText(_translate("Dialog", str(LisT[i]), None))
        self.tableWidget_7.setSortingEnabled(__sortingEnabled)
        ######################################################################
        if self.Distracter_state==False:
            self.tableWidget_5 = QtGui.QTableWidget(self.groupBox_10)
            self.tableWidget_5.setGeometry(QtCore.QRect(440, 50, 481, 371))
            self.tableWidget_5.setObjectName(_fromUtf8("tableWidget_5"))
            self.tableWidget_5.setColumnCount(5)
        self.tableWidget_5.setRowCount(self.number)

        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, item)


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
            item = QtGui.QTableWidgetItem()
            self.tableWidget_5.setItem(i, 4, item)


        item = self.tableWidget_5.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "ตัวเลือก1", None))
        item = self.tableWidget_5.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "ตัวเลือก2", None))
        item = self.tableWidget_5.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "ตัวเลือก3", None))
        item = self.tableWidget_5.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "ตัวเลือก4", None))        
        item = self.tableWidget_5.horizontalHeaderItem(4)
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
            item = self.tableWidget_5.item(i, 4)
            item.setText(_translate("Dialog", self.Calcul(List_DIS[i][4]), None))

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
    def Distin(self,Key):

       
        
        self.M=distinguish.Distinguish(0)

        Key=self.comboBox_3.currentIndex()+1
        



        try:
            self.distinguish_L1=[]
            self.distinguish_H1=[]
            List_silly,List_gin,List_count_gin,List_count_silly,List_final=self.M.main(1,self.number)
            self.distinguish_L1=List_silly
            self.distinguish_H1=List_gin
            self.List_count_gin_1=List_count_gin
            self.List_count_silly_1=List_count_silly
            self.List_final_1=List_final 
 

  


        except:
            pass
        try:
            self.distinguish_L2=[]
            self.distinguish_H2=[]
            List_silly,List_gin,List_count_gin,List_count_silly,List_final=self.M.main(2,self.number)
            self.distinguish_L2=List_silly
            self.distinguish_H2=List_gin

            self.List_count_gin_2=List_count_gin
            self.List_count_silly_2=List_count_silly
            self.List_final_2=List_final


        except:
            pass
        try:    
            self.distinguish_L3=[]
            self.distinguish_H3=[]
            List_silly,List_gin,List_count_gin,List_count_silly,List_final=self.M.main(3,self.number)
            self.distinguish_L3=List_silly
            self.distinguish_H3=List_gin

            self.List_count_gin_3=List_count_gin
            self.List_count_silly_3=List_count_silly
            self.List_final_3=List_final


        except:
            pass
        try:    
            self.distinguish_L4=[]
            self.distinguish_H4=[]
            List_silly,List_gin,List_count_gin,List_count_silly,List_final=self.M.main(4,self.number)
            self.distinguish_L4=List_silly
            self.distinguish_H4=List_gin

            self.List_count_gin_4=List_count_gin
            self.List_count_silly_4=List_count_silly
            self.List_final_4=List_final


        except:
            pass
        try:
            List_silly,List_gin,List_count_gin,List_count_silly,List_final=self.M.main(Key,self.number)
        except:
            pass
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
        self.tableWidget_4.setRowCount(self.number)


        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, item)


        for i in range(self.number):
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
        self.Best=0.0
        self.Better=0.0
        self.Good=0.0
        self.Medium=0.0
        self.Low=0.0
        self.Lowly=0.0
        self.No=0.0





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
                self.Best=self.Best+1
            elif List_final[i]>=0.80 and List_final[i]<=0.99:
                messag="Better "
                self.Better=self.Better+1
            elif List_final[i]>=0.60 and List_final[i]<=0.79:
                messag="Good"
                self.Good=self.Good+1
            elif List_final[i]>=0.40 and List_final[i]<=0.59:
                messag="Medium "
                self.Medium=self.Medium+1
            elif List_final[i]>=0.20 and List_final[i]<=0.39:
                messag="Low "
                self.Low=self.Low+1
            elif List_final[i]>=0.00 and List_final[i]<=0.19:
                messag="Lowly "
                self.Lowly=self.Lowly+1
            elif List_final[i]<0.00 :
                messag="Can't"
                self.No=self.No+1



            item = self.tableWidget_4.item(i, 2)
            item.setText(_translate("Dialog",messag , None))
        self.lineEdit_15.setText(str(int(self.Best)))   
        self.lineEdit_16.setText(str(int(self.Better)))  
        self.lineEdit_17.setText(str(int(self.Good)))    
        self.lineEdit_18.setText(str(int(self.Medium)))  
        self.lineEdit_19.setText(str(int(self.Low)))  
        self.lineEdit_20.setText(str(int(self.Lowly)))  
        self.lineEdit_21.setText(str(int(self.No)))  


        self.Best =(self.Best*100)*120
        self.Better =(self.Better*100)*120
        self.Good =(self.Good*100)*120
        self.Medium =(self.Medium*100)*120
        self.Low =(self.Low*100)*120
        self.Lowly =(self.Lowly*100)*120
        self.No  =(self.No*100)*120

        self.Dis=Chart_distinguish.Chart_distinguish(0)
        self.Dis.Main(self.Best,self.Better,self.Good,self.Medium,self.Low,self.Lowly,self.No,"distinguish")
        self.label_35.setPixmap(QtGui.QPixmap(_fromUtf8("chart/distinguish.png")))

        #print "Fuck",Best, Better, Good, Medium,Low,Lowly,No


         

        
        
        self.tableWidget_4.setSortingEnabled(__sortingEnabled)
 
  
        
        self.State=True 
    def alert_char_distin(self,event):
        self.Dis.Main_Show(self.Best,self.Better,self.Good,self.Medium,self.Low,self.Lowly,self.No,"distinguish")
"""if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())  """
