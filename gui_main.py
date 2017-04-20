# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Mon Oct 13 22:51:56 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!
import cv2
import threading
import numpy as np
import math 
import process
from PyQt4 import QtCore, QtGui
import os
import sys
import TR
import multiprocessing
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
List_Final=[]
Directory="pp"
class Ui_MainWindow(QtGui.QMainWindow):
    newlist = []
    font = cv2.FONT_HERSHEY_SIMPLEX  
    List_term_main=[]
    List_Set_main=[]

    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.setEnabled(True)
        MainWindow.resize(1370, 724)
        font = QtGui.QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon/up.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 261, 391))
        self.groupBox.setStyleSheet(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.listWidget = QtGui.QListWidget(self.groupBox)
        self.listWidget.setGeometry(QtCore.QRect(20, 70, 221, 291))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
 
        self.lineEdit_13 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_13.setEnabled(False)
        self.lineEdit_13.setGeometry(QtCore.QRect(120, 40, 113, 20))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.label_25 = QtGui.QLabel(self.groupBox)
        self.label_25.setGeometry(QtCore.QRect(20, 40, 91, 16))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(570, 400, 461, 211))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 46, 13))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.progressBar = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar.setGeometry(QtCore.QRect(20, 40, 441, 23))
        self.progressBar.setStyleSheet(_fromUtf8(""))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 71, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.progressBar_2 = QtGui.QProgressBar(self.groupBox_2)
        self.progressBar_2.setGeometry(QtCore.QRect(20, 90, 441, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 61, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_22 = QtGui.QLabel(self.groupBox_2)
        self.label_22.setGeometry(QtCore.QRect(50, 150, 46, 13))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.groupBox_2)
        self.label_23.setGeometry(QtCore.QRect(90, 120, 46, 13))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_24 = QtGui.QLabel(self.groupBox_2)
        self.label_24.setGeometry(QtCore.QRect(90, 150, 46, 13))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.pushButton_pause = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_pause.setGeometry(QtCore.QRect(240, 130, 91, 41))
        self.pushButton_pause.setObjectName(_fromUtf8("pushButton_pause"))
        self.pushButton_stop = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_stop.setGeometry(QtCore.QRect(340, 130, 81, 41))
        self.pushButton_stop.setStyleSheet(_fromUtf8(""))
        self.pushButton_stop.setObjectName(_fromUtf8("pushButton_stop"))
        self.groupBox_6 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(860, 0, 481, 391))
        self.groupBox_6.setStyleSheet(_fromUtf8(""))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.label_13 = QtGui.QLabel(self.groupBox_6)
        self.label_13.setGeometry(QtCore.QRect(100, 30, 21, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_9.setEnabled(False)
        self.lineEdit_9.setGeometry(QtCore.QRect(130, 30, 111, 20))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_10.setEnabled(False)
        self.lineEdit_10.setGeometry(QtCore.QRect(130, 60, 113, 20))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_11.setEnabled(False)
        self.lineEdit_11.setGeometry(QtCore.QRect(130, 90, 113, 20))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.label_14 = QtGui.QLabel(self.groupBox_6)
        self.label_14.setGeometry(QtCore.QRect(70, 60, 61, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.groupBox_6)
        self.label_15.setGeometry(QtCore.QRect(80, 90, 46, 13))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.groupBox_6)
        self.label_16.setGeometry(QtCore.QRect(90, 120, 46, 13))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.lineEdit_12 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_12.setEnabled(False)
        self.lineEdit_12.setGeometry(QtCore.QRect(130, 120, 113, 20))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.scrollArea = QtGui.QScrollArea(self.groupBox_6)
        self.scrollArea.setGeometry(QtCore.QRect(280, 20, 191, 361))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 189, 359))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.listWidget_2 = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 0, 231, 361))
        self.listWidget_2.setObjectName(_fromUtf8("listWidget_2"))
         

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.pushButton_detail = QtGui.QPushButton(self.groupBox_6)
        self.pushButton_detail.setGeometry(QtCore.QRect(130, 150, 91, 23))
        self.pushButton_detail.setObjectName(_fromUtf8("pushButton_detail"))
        self.label_26 = QtGui.QLabel(self.groupBox_6)
        self.label_26.setGeometry(QtCore.QRect(40, 200, 161, 16))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.lineEdit_14 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_14.setEnabled(False)
        self.lineEdit_14.setGeometry(QtCore.QRect(130, 200, 101, 20))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.label_27 = QtGui.QLabel(self.groupBox_6)
        self.label_27.setGeometry(QtCore.QRect(10, 230, 121, 16))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(self.groupBox_6)
        self.label_28.setGeometry(QtCore.QRect(70, 260, 46, 13))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.lineEdit_15 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_15.setEnabled(False)
        self.lineEdit_15.setGeometry(QtCore.QRect(130, 230, 101, 20))
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.lineEdit_16 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_16.setEnabled(False)
        self.lineEdit_16.setGeometry(QtCore.QRect(130, 260, 101, 20))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(300, 0, 541, 391))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label = QtGui.QLabel(self.groupBox_3)
        self.label.setGeometry(QtCore.QRect(30, 30, 491, 341))
        self.label.setText(_fromUtf8(""))
        
        self.label.setScaledContents(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 400, 551, 211))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.treeWidget = QtGui.QTreeWidget(self.groupBox_4)
        self.treeWidget.setGeometry(QtCore.QRect(10, 50, 271, 101))
        self.treeWidget.setAutoFillBackground(False)
        self.treeWidget.setStyleSheet(_fromUtf8(""))
        self.treeWidget.setTabKeyNavigation(False)
        self.treeWidget.setDragEnabled(False)
        self.treeWidget.setAlternatingRowColors(False)
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setObjectName(_fromUtf8("treeWidget"))
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        item_0 = QtGui.QTreeWidgetItem(self.treeWidget)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.treeWidget.header().setDefaultSectionSize(59)
        self.treeWidget.header().setHighlightSections(False)
        self.label_5 = QtGui.QLabel(self.groupBox_4)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_4)
        self.label_6.setGeometry(QtCore.QRect(300, 120, 71, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox_4)
        self.label_7.setGeometry(QtCore.QRect(320, 150, 46, 13))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(310, 180, 71, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit.setEnabled(False)
        self.lineEdit.setGeometry(QtCore.QRect(370, 120, 161, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_2.setEnabled(False)
        self.lineEdit_2.setGeometry(QtCore.QRect(370, 150, 161, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setEnabled(False)
        self.lineEdit_3.setGeometry(QtCore.QRect(370, 180, 161, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(330, 30, 46, 13))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(320, 60, 46, 13))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setEnabled(False)
        self.lineEdit_4.setGeometry(QtCore.QRect(370, 30, 113, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_5.setEnabled(False)
        self.lineEdit_5.setGeometry(QtCore.QRect(370, 60, 113, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(335, 90, 41, 20))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_6.setEnabled(False)
        self.lineEdit_6.setGeometry(QtCore.QRect(370, 90, 113, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.pushButton = QtGui.QPushButton(self.groupBox_4)
        self.pushButton.setGeometry(QtCore.QRect(490, 90, 41, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(1040, 410, 321, 161))
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setPixmap(QtGui.QPixmap(_fromUtf8("icon/logo.png")))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(39, 37))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionSelect_Directory = QtGui.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("icon/Download-Folder-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelect_Directory.setIcon(icon1)
        self.actionSelect_Directory.setObjectName(_fromUtf8("actionSelect_Directory"))
        self.actionSelect_Key = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("icon/Key-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSelect_Key.setIcon(icon2)
        self.actionSelect_Key.setObjectName(_fromUtf8("actionSelect_Key"))
        self.actionStart = QtGui.QAction(MainWindow)
        self.actionStart.setCheckable(False)
        self.actionStart.setEnabled(True)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("icon/Play-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionStart.setIcon(icon3)
        self.actionStart.setObjectName(_fromUtf8("actionStart"))
        self.actionSetting = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("icon/Categories-preferences-system-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSetting.setIcon(icon4)
        self.actionSetting.setObjectName(_fromUtf8("actionSetting"))
        self.actionHelp = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("icon/Actions-help-about-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionHelp.setIcon(icon5)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionFormat = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8("icon/checklist-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionFormat.setIcon(icon6)
        self.actionFormat.setObjectName(_fromUtf8("actionFormat"))
        self.actionScore_Analysis = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8("icon/SEO-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionScore_Analysis.setIcon(icon7)
        self.actionScore_Analysis.setObjectName(_fromUtf8("actionScore_Analysis"))
        self.actionSetting_2 = QtGui.QAction(MainWindow)
        self.actionSetting_2.setObjectName(_fromUtf8("actionSetting_2"))
        self.actionDeveloper = QtGui.QAction(MainWindow)
        self.actionDeveloper.setObjectName(_fromUtf8("actionDeveloper"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionHelp_2 = QtGui.QAction(MainWindow)
        self.actionHelp_2.setObjectName(_fromUtf8("actionHelp_2"))
        self.toolBar.addAction(self.actionSelect_Directory)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSelect_Key)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionFormat)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionStart)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionScore_Analysis)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSetting)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionHelp)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "โปรแกรมตรวจข้อสอบ มหาวิทยาลัยพะเยา", None))
        self.groupBox.setTitle(_translate("MainWindow", "List File", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_25.setText(_translate("MainWindow", "จำนวนไฟล์ที่พบ:", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Status", None))
        self.label_2.setText(_translate("MainWindow", "Process", None))
        self.label_3.setText(_translate("MainWindow", "Process Total", None))
        self.label_4.setText(_translate("MainWindow", "Status Key:", None))
        self.label_22.setText(_translate("MainWindow", "Error:", None))
        self.label_23.setText(_translate("MainWindow", "No", None))
        self.label_24.setText(_translate("MainWindow", "0", None))
        self.pushButton_pause.setText(_translate("MainWindow", "Pause", None))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Detail", None))
        self.label_13.setText(_translate("MainWindow", "ID:", None))
        self.label_14.setText(_translate("MainWindow", "Incorrect:", None))
        self.label_15.setText(_translate("MainWindow", "Correct:", None))
        self.label_16.setText(_translate("MainWindow", "Score:", None))
        __sortingEnabled = self.listWidget_2.isSortingEnabled()
        self.listWidget_2.setSortingEnabled(False)

      
        self.listWidget_2.setSortingEnabled(__sortingEnabled)
        self.pushButton_detail.setText(_translate("MainWindow", "ดูรายละเอียด", None))
        self.label_26.setText(_translate("MainWindow", "ผ่านการตรวจ:", None))
        self.label_27.setText(_translate("MainWindow", "ไม่สามารถตรวจได้:", None))
        self.label_28.setText(_translate("MainWindow", "ตรวจได้:", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Picture Detai ", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Format Detail", None))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "ช่วงที่:", None))
        self.treeWidget.headerItem().setText(1, _translate("MainWindow", "ข้อ:", None))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "1", None))
        self.treeWidget.topLevelItem(0).setText(1, _translate("MainWindow", "1,20", None))
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "2", None))
        self.treeWidget.topLevelItem(1).setText(1, _translate("MainWindow", "21-30", None))
        self.treeWidget.topLevelItem(2).setText(0, _translate("MainWindow", "3", None))
        self.treeWidget.topLevelItem(2).setText(1, _translate("MainWindow", "31-150", None))
        self.treeWidget.topLevelItem(3).setText(0, _translate("MainWindow", "4", None))
        self.treeWidget.topLevelItem(3).setText(1, _translate("MainWindow", "151-160", None))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("MainWindow", "ช่วงข้อ", None))
        self.label_6.setText(_translate("MainWindow", "แบบคำตอบ:", None))
        self.label_7.setText(_translate("MainWindow", "คะแนน:", None))
        self.label_8.setText(_translate("MainWindow", "หมายเหตุ:", None))
        self.label_9.setText(_translate("MainWindow", "Input:", None))
        self.label_10.setText(_translate("MainWindow", "Output:", None))
        self.label_12.setText(_translate("MainWindow", "Key:", None))
        self.pushButton.setText(_translate("MainWindow", "ดู", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionSelect_Directory.setText(_translate("MainWindow", "Select Directory", None))
        self.actionSelect_Key.setText(_translate("MainWindow", "Select Key", None))
        self.actionStart.setText(_translate("MainWindow", "Start", None))
        self.actionSetting.setText(_translate("MainWindow", "Setting", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionOpen.setText(_translate("MainWindow", "Open", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionFormat.setText(_translate("MainWindow", "Format ", None))
        self.actionFormat.setToolTip(_translate("MainWindow", "Format ", None))
        self.actionScore_Analysis.setText(_translate("MainWindow", "Score Analysis", None))
        self.actionScore_Analysis.setToolTip(_translate("MainWindow", "Score Analysis", None))
        self.actionSetting_2.setText(_translate("MainWindow", "Setting", None))
        self.actionDeveloper.setText(_translate("MainWindow", "Developer", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))
        self.actionHelp_2.setText(_translate("MainWindow", "Help", None))
        ######Event Menu
        self.connect(self.actionSelect_Directory, QtCore.SIGNAL('triggered()'), self.OpenFile)
        self.connect(self.actionSelect_Key, QtCore.SIGNAL('triggered()'), self.SetKey)
        self.connect(self.actionFormat, QtCore.SIGNAL('triggered()'), self.Format)
        self.connect(self.actionStart, QtCore.SIGNAL('triggered()'), self.start)
        self.connect(self.actionSetting, QtCore.SIGNAL('triggered()'), self.Setting)
        #self.connect(self.actionHelp, QtCore.SIGNAL('triggered()'), self.Help)

        self.listWidget.currentItemChanged.connect(self.ShowImg)
        self.listWidget_2.currentItemChanged.connect(self.click_list2)

        self.update_list2()
    def ShowImg(self):
        index=self.listWidget.currentRow()
        #print str(self.directory)+"\\"+str(self.newlist[index])
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8(str(self.newlist[index]))))
    def addListOri(self,List_Key):
                    self.listWidget.clear() 
                    for i in range(len(List_Key)):
                        item = QtGui.QListWidgetItem()
                        self.listWidget.addItem(item)                                                                                                                                                                        
                        item = self.listWidget.item(i)                                                                                                                                              
                        item.setText(_translate("Dialog", ("No: "+str(i+1)+" "+str(List_Key[i])), None))  
    def OpenFile(self):

        self.newlist=[]
  
        self.openFilesPath = ''
        file=open("setting/setting.txt","r")
        TypeFile=file.readlines()
        file.close()         
         
        files = QtGui.QFileDialog.getOpenFileNames(self,
                "QFileDialog.getOpenFileNames()", self.openFilesPath,"Image Files (*{:>})".format(str(TypeFile[3]).strip()) )#"Text Files (*.png);;Text Files (*.BMP)"
        for i in range(len(files)):
                print   files[i] 
                self.newlist.append((files[i]))
        #    print  files 
        #    self.openFilesPath = files[0]
        #    #self.openFileNamesLabel.setText("[%s]" % ', '.join(files)) 
        #    print  "[%s]" % ', '.join(files)
        self.addListOri(self.newlist)

    def setExistingDirectory(self):
            self.newlist=[]
            print "setExistingDirectory"
            self.directory = QtGui.QFileDialog.getExistingDirectory(self)
            Directory =self.directory
            #print  self.directory
            file=open("setting/setting.txt","r")
            TypeFile=file.readlines()
            file.close()
            if self.directory:
                items = os.listdir(self.directory)
                
                for names in items:
                    if names.endswith(''):
                        self.newlist.append(names)
                        List_Final.append(names)
                #print newlist
                for i in range(len(self.newlist)):
                    print self.newlist[i]

                    #List_pp.append(newlist[i])
                #self.addList(newlist) 

                #print "List_p",List_pp
                #return newlist
                self.addListOri(self.newlist)
                print self.newlist
    def SetKey(self):
            print "setkey"
            import DialogKey

            self.ui=DialogKey.Ui_Dialog_SetKey()
        
            self.ui.show()
    def Setting(self):
        
 
       
        import DialogSetting
        self.ui=DialogSetting.Ui_Dialog_Setting()
        self.ui.show()
         
        print "Setting"

    def start(self):
        #self.Process_main()
        #Start_()
        t = threading.Thread(target=self.Process_main,)
        t.start()
 
    def Clear_fo(self,Path):
            folder = Path
            for the_file in os.listdir(folder):
                file_path = os.path.join(folder, the_file)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception, e:
                    print e 
    def Process_main(self):
            self.Clear_fo("image\input")
            self.Clear_fo("exam")
            
            List_input=[]
            M=TR.TR(0)

            Pc=process.MainProcess(0)
            for i in range(len(self.newlist)):
                                    print  str(self.newlist[i])
                                    img=cv2.imread( str(self.newlist[i]))

                                    cv2.imwrite("image\input\\exam{:>}.png".format(i),M.ThresholdAndRotate(img,str(i)))
                                    List_input.append((self.newlist[i]))
                                    #code,list_a,Set,Term=Pc.Process("image\input\\"+str(self.newlist[i]))
                                 
                                    #self.progressBar_2.setProperty("value", i)
                                    #code,list_a,Set,Term=self.Process(str(self.directory)+"\\"+str(self.newlist[i]))
                                    #print  code,Set,Term
            LI=os.listdir("image\input\\") 
            for i in range(len(LI)):
                    print LI[i]  
                    code,list_a,Set,Term=Pc.Process("image\input\\"+str(LI[i]))                    
                    print  code,Set,Term

                    file = open("exam/{:>}.txt".format(i), "w")
                    file.write(str(List_input[i])+"\n")
                    file.write(str(code)+"\n")
                    file.write(str(Set)+"\n")
                    file.write(str(Term)+"\n")
                    L =self.List_stand(list_a)
                    for i in range(len(L)):
                            file.write(str(L[i])+"\n") 
                    file.close()
    def Format(self):
        import DialogFormat
        self.ui=DialogFormat.Ui_format()
        self.ui.show()
        print "Ui_format"
    ###############################################################################
    def update_list2(self):
        file = open("setting/format_tab2_down.txt", "r")    
        list_setting=file.readlines()            
        file.close()
        if list_setting[0].strip()=="Yes":

            if list_setting[2].strip()=="1Yes" and list_setting[8].strip()=="1No" and list_setting[14].strip()=="1No":
                LI=os.listdir("inspected\M1")
            elif list_setting[2].strip()=="1Yes" and list_setting[8].strip()=="1Yes" and list_setting[14].strip()=="1No":
                LI=os.listdir("inspected\M2")
            elif list_setting[2].strip()=="1Yes" and list_setting[8].strip()=="1Yes" and list_setting[14].strip()=="1Yes": 
                LI=os.listdir("inspected\M3")
        else:


            LI=os.listdir("inspected\SC")




        
        for i in range(len(LI)):
            item = QtGui.QListWidgetItem()
            self.listWidget_2.addItem(item)
            item = self.listWidget_2.item(i)
            item.setText(_translate("MainWindow",(LI[i]), None))
    def click_list2(self):
        
        file = open("setting/format_tab2_down.txt", "r")    
        list_setting=file.readlines()            
        file.close()
        if list_setting[0].strip()=="Yes":

            if list_setting[2].strip()=="1Yes" and list_setting[8].strip()=="1No" and list_setting[14].strip()=="1No":
                print "M1"
                print self.listWidget_2.currentRow()
                LI=os.listdir("inspected\M1")
                print "Code:", 
                file = open("inspected\M1\{:>}".format(str(LI[self.listWidget_2.currentRow()]).strip()), "r")
                list_s=file.readlines()
                file.close()

                print "Path",list_s[0]
                print "Code",list_s[1]
                self.lineEdit_9.setText(list_s[1])
                self.lineEdit_10.setText(list_s[2])
            elif list_setting[2].strip()=="1Yes" and list_setting[8].strip()=="1Yes" and list_setting[14].strip()=="1No":
                print "M2"
                print self.listWidget_2.currentRow()
                LI=os.listdir("inspected\M2")
                print "Code:", 
                file = open("inspected\M2\{:>}".format(str(LI[self.listWidget_2.currentRow()]).strip()), "r")
                list_s=file.readlines()
                file.close()

                print "Path",list_s[0]
                print "Code",list_s[1]
                self.lineEdit_9.setText(list_s[1])
                self.lineEdit_10.setText(list_s[2])
            elif list_setting[2].strip()=="1Yes" and list_setting[8].strip()=="1Yes" and list_setting[14].strip()=="1Yes": 
                print "M3"  
                print self.listWidget_2.currentRow()
                LI=os.listdir("inspected\M3")
                print "Code:", 
                file = open("inspected\M3\{:>}".format(str(LI[self.listWidget_2.currentRow()]).strip()), "r")
                list_s=file.readlines()
                file.close()

                print "Path",list_s[0]
                print "Code",list_s[1]
                self.lineEdit_9.setText(list_s[1]) 
        else:


            print "SC"
            print self.listWidget_2.currentRow()
            LI=os.listdir("inspected\SC")
            print "Code:", 
            file = open("inspected\SC\{:>}".format(str(LI[self.listWidget_2.currentRow()]).strip()), "r")
            list_s=file.readlines()
            file.close()

            print "Path",list_s[0]
            print "Code",list_s[1]
            self.lineEdit_9.setText(list_s[1])

    ###############################################################################
    def List_stand(self,st):
        list_main=[]
        for i in range(120):
            list_main.append([0,0,0,0,0])

        for j in range(len(st)):
            for i in range(len(st[j])):
                if st[j][i]==1:
                    list_main[j][0]=1;
                if st[j][i]==2:
                    list_main[j][1]=1;
                if st[j][i]==3:
                    list_main[j][2]=1;
                if st[j][i]==4:
                    list_main[j][3]=1;
                if st[j][i]==5:
                    list_main[j][4]=1;
             
        return list_main
     

 
           
def Process_():
     import process

     #m=process.MainProcess(0)
     #code,list_a,Set,Term=m.Process('input.png')


def Main( ):

    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
     
    ui.setupUi(MainWindow)
  
    MainWindow.show()
    sys.exit(app.exec_())
if __name__ == "__main__":

    p = multiprocessing.Process(target=Main  )
    p.start()


 