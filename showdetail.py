# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'showdetail.ui'
#
# Created: Tue Jan 13 00:07:02 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!
import platform
import subprocess,os
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

class SDetail(QtGui.QDialog):
    ID=""
    T=""
    Num=0
    def __init__(self,D,Type,N):
        QtGui.QDialog.__init__(self)
        self.setupUi(self,D,Type,N)
         

    def setupUi(self, Dialog,D,Type,N):
        self.ID=D
        self.T=Type
        self.Num=N
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(574, 601)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 521, 571))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 221, 231))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label = QtGui.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(40, 200, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit.setGeometry(QtCore.QRect(80, 20, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 50, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 80, 113, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 200, 113, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_18 = QtGui.QLabel(self.groupBox_2)
        self.label_18.setGeometry(QtCore.QRect(30, 110, 41, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.groupBox_2)
        self.label_19.setGeometry(QtCore.QRect(40, 140, 31, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.groupBox_2)
        self.label_20.setGeometry(QtCore.QRect(40, 170, 31, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.lineEdit_18 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_18.setGeometry(QtCore.QRect(80, 110, 113, 20))
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.lineEdit_19 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(80, 140, 113, 20))
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.lineEdit_20 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_20.setGeometry(QtCore.QRect(80, 170, 113, 20))
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 50, 221, 91))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(50, 20, 31, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 20, 113, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(80, 50, 113, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(50, 50, 31, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(10, 380, 501, 181))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_8 = QtGui.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(40, 30, 46, 13))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(40, 60, 46, 13))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(40, 90, 46, 13))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(100, 30, 61, 20))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(100, 60, 61, 20))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(100, 90, 61, 20))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.label_11 = QtGui.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(250, 120, 71, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(320, 120, 61, 20))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(170, 30, 31, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(170, 60, 31, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(170, 90, 31, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit_12 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_12.setGeometry(QtCore.QRect(210, 30, 61, 20))
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.lineEdit_13 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_13.setGeometry(QtCore.QRect(210, 60, 61, 20))
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.lineEdit_14 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_14.setGeometry(QtCore.QRect(210, 90, 61, 20))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.label_15 = QtGui.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(280, 30, 41, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.groupBox_4)
        self.label_16.setGeometry(QtCore.QRect(280, 60, 41, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.groupBox_4)
        self.label_17.setGeometry(QtCore.QRect(280, 90, 41, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.lineEdit_15 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_15.setGeometry(QtCore.QRect(320, 30, 61, 20))
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.lineEdit_16 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_16.setGeometry(QtCore.QRect(320, 60, 61, 20))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.lineEdit_17 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_17.setGeometry(QtCore.QRect(320, 90, 61, 20))
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.lineEdit_28 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_28.setGeometry(QtCore.QRect(320, 150, 61, 20))
        self.lineEdit_28.setText(_fromUtf8(""))
        self.lineEdit_28.setObjectName(_fromUtf8("lineEdit_28"))
        self.label_28 = QtGui.QLabel(self.groupBox_4)
        self.label_28.setGeometry(QtCore.QRect(290, 150, 31, 16))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 30, 31, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(60, 30, 361, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(430, 30, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def List(self,num,List,S):        

        self.tableWidget = QtGui.QTableWidget(self.groupBox)
        self.tableWidget.setGeometry(QtCore.QRect(240, 60, 271, 311))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(num)

        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        for i in range(num):
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(i, 0, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(i, 1, item)
            item = QtGui.QTableWidgetItem()
            self.tableWidget.setItem(i, 2, item)

        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Dialog", "1", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "No", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "Result", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "***", None))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)

        for i in range(num):
        

            item = self.tableWidget.item(i, 0)
            item.setText(_translate("Dialog", str(i+1), None))
            item = self.tableWidget.item(i, 1)
            item.setText(_translate("Dialog", str(self.rep(List[i+S+1])), None))
            item = self.tableWidget.item(i, 2)
            item.setText(_translate("Dialog", "", None))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Show Detail", None))
        self.groupBox.setTitle(_translate("Dialog", "Detail", None))

        self.groupBox_2.setTitle(_translate("Dialog", "Output", None))
        self.label.setText(_translate("Dialog", "ID Student", None))
        self.label_4.setText(_translate("Dialog", "Score", None))
        self.label_3.setText(_translate("Dialog", "Incorrect", None))
        self.label_2.setText(_translate("Dialog", "Correct", None))
        self.label_18.setText(_translate("Dialog", "Empty", None))
        self.label_19.setText(_translate("Dialog", "Over", None))
        self.label_20.setText(_translate("Dialog", "Less", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Input", None))
        self.label_6.setText(_translate("Dialog", "File", None))
        self.label_7.setText(_translate("Dialog", "Key", None))
        self.groupBox_4.setTitle(_translate("Dialog", "GroupBox", None))
        self.label_8.setText(_translate("Dialog", "Phase 1", None))
        self.label_9.setText(_translate("Dialog", "Phase 2", None))
        self.label_10.setText(_translate("Dialog", "Phase 3", None))
        self.label_11.setText(_translate("Dialog", "Free Score", None))
        self.label_12.setText(_translate("Dialog", "Point", None))
        self.label_13.setText(_translate("Dialog", "Point", None))
        self.label_14.setText(_translate("Dialog", "Point", None))
        self.label_15.setText(_translate("Dialog", "Result", None))
        self.label_16.setText(_translate("Dialog", "Result", None))
        self.label_17.setText(_translate("Dialog", "Result", None))
        self.label_28.setText(_translate("Dialog", "Total", None))
        self.label_5.setText(_translate("Dialog", "Path", None))
        self.pushButton.setText(_translate("Dialog", "Go to File..", None))


        

        self.pushButton.clicked.connect(self.open_file)

        file = open("setting/format_tab2_down.txt", "r")
        format_tab2 =file.readlines()
        file.close()       


        self.lineEdit_12.setText(format_tab2[4].strip())
        self.lineEdit_13.setText(format_tab2[10].strip())
        self.lineEdit_14.setText(format_tab2[16].strip())
        file = open(self.ID, "r")
        format =file.readlines()
        file.close()

        if self.T=="SC" or self.T=="C1":
            self.List(self.Num,format,8)
        elif self.T=="C2":
            self.List(self.Num,format,10)
        elif self.T=="C3":
            self.List(self.Num,format,11)

        print self.ID
        if self.T=="SC":
            self.lineEdit_5.setText(format[0].strip())#path

            self.lineEdit_7.setText(format[2].strip())#key
            self.lineEdit.setText(format[1].strip())#ID
            self.lineEdit_2.setText(format[4].strip())#C
            self.lineEdit_3.setText(format[5].strip())#in
            self.lineEdit_4.setText(format[3].strip())#score


            self.lineEdit_18.setText(format[6].strip())
            self.lineEdit_19.setText(format[7].strip())
            self.lineEdit_20.setText(format[8].strip())

            self.lineEdit_15.setText("-")#1
            self.lineEdit_16.setText("-")#2
            self.lineEdit_17.setText("-")#3

            self.lineEdit_28.setText(format[3].strip())#total
        elif self.T=="C1":
            self.lineEdit_5.setText(format[0].strip())#path

            self.lineEdit_7.setText(format[2].strip())#key
            self.lineEdit.setText(format[1].strip())#ID
            self.lineEdit_2.setText(format[4].strip())#C
            self.lineEdit_3.setText(format[5].strip())#in
            self.lineEdit_4.setText(format[3].strip())#score

            self.lineEdit_18.setText(format[6].strip())
            self.lineEdit_19.setText(format[7].strip())
            self.lineEdit_20.setText(format[8].strip())


            S,E=self.Check_pp(3)
            self.lineEdit_8.setText(str(self.Count_yes("C1",S,E,self.ID)))
            self.lineEdit_9.setText("-")
            self.lineEdit_10.setText("-")
            self.lineEdit_15.setText(format[3].strip())#1
            self.lineEdit_16.setText("-")#2
            self.lineEdit_17.setText("-")#3

            self.lineEdit_28.setText(format[3].strip())#total

        if self.T=="C2":
            self.lineEdit_5.setText(format[0].strip())

            self.lineEdit_7.setText(format[2].strip())
            self.lineEdit.setText(format[1].strip())
            self.lineEdit_2.setText(format[6].strip())
            self.lineEdit_3.setText(format[7].strip())
            self.lineEdit_4.setText(format[5].strip())

            S,E=self.Check_pp(3)
            self.lineEdit_8.setText(str(self.Count_yes("C2",S,E,self.ID)))
            S,E=self.Check_pp(9)
            self.lineEdit_9.setText(str(self.Count_yes("C2",S,E,self.ID)))
            self.lineEdit_10.setText("-")

            self.lineEdit_18.setText(format[8].strip())
            self.lineEdit_19.setText(format[9].strip())
            self.lineEdit_20.setText(format[10].strip())


            self.lineEdit_15.setText(format[3].strip())
            self.lineEdit_16.setText(format[4].strip())
            self.lineEdit_17.setText("-")

            self.lineEdit_28.setText(format[5].strip())
        elif self.T=="C3":
            self.lineEdit_5.setText(format[0].strip())#path

            self.lineEdit_7.setText(format[2].strip())#key
            self.lineEdit.setText(format[1].strip())#ID
            self.lineEdit_2.setText(format[6].strip())#C
            self.lineEdit_3.setText(format[7].strip())#in
            self.lineEdit_4.setText(format[6].strip())#score

            S,E=self.Check_pp(3)
            self.lineEdit_8.setText(str(self.Count_yes("C3",S,E,self.ID)))
            S,E=self.Check_pp(9)
            self.lineEdit_9.setText(str(self.Count_yes("C3",S,E,self.ID)))
            S,E=self.Check_pp(15)
            self.lineEdit_10.setText(str(self.Count_yes("C3",S,E,self.ID)))


            self.lineEdit_18.setText(format[9].strip())
            self.lineEdit_19.setText(format[10].strip())
            self.lineEdit_20.setText(format[11].strip())


            self.lineEdit_15.setText(format[3].strip())#1
            self.lineEdit_16.setText(format[4].strip())#2
            self.lineEdit_17.setText(format[5].strip())#3

            self.lineEdit_28.setText(format[6].strip())#total
  

    def open_file(self):
        path=self.lineEdit_5.text()
        print path
        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])
    def Check_pp(self,i):
        file = open("setting/format_tab2_down.txt", "r")
        format_tab2 =file.readlines()
        file.close()    


        data=format_tab2[i].strip().split('-') 
        return int(data[0]),int(data[1])
     

     

    def rep(self,Str):

        data= Str.strip().split(',') #replace("[", " ")
        print data[1].replace("\'", " ").replace(")", " ")
        return data[1].replace("\'", " ").replace(")", " ").strip()

    def Count_yes(self,T,S,E,P):
        start=0  
        count=0
        file = open(P, "r")
        format_tab2 =file.readlines()
        file.close()

     
        if T=="SC":
            start=8
            for i in range(start+S,start+E+1):
                print self.rep(format_tab2[i])
                if self.rep(format_tab2[i])=="Yes":
                    count=count+1
            return count

        elif T=="C1":
            start=8
            for i in range(start+S,start+E+1):
                print self.rep(format_tab2[i])
                if self.rep(format_tab2[i])=="Yes":
                    count=count+1 
             
            return count
        elif T=="C2":
            print "C2"
            start=10
            for i in range(start+S,start+E+1):
                print self.rep(format_tab2[i])
                if self.rep(format_tab2[i])=="Yes":
                    count=count+1
            return count
        elif T=="C3":
            start=11
            for i in range(start+S,start+E+1):
                print self.rep(format_tab2[i])
                if self.rep(format_tab2[i])=="Yes":
                    count=count+1
            return count


 
