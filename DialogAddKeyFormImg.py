# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAddKeyFormImg.ui'
#
# Created: Tue Oct 28 15:07:17 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import cv2
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


class Ui_DialogAddKeyFormImg(QtGui.QDialog):
    List_answer_main=[]
    List_M=[]
    for i in range(120):
        List_M.append([0,0,0,0,0,])
    
    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
    def setupUi(self, DialogAddKeyFormImg):
        DialogAddKeyFormImg.setObjectName(_fromUtf8("DialogAddKeyFormImg"))
        DialogAddKeyFormImg.resize(749, 609)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../icon/Key-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogAddKeyFormImg.setWindowIcon(icon)
        self.groupBox = QtGui.QGroupBox(DialogAddKeyFormImg)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 711, 301))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.pushButton = QtGui.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(550, 30, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 30, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(90, 30, 451, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.groupBox_2 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 60, 241, 141))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 20, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(30, 50, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(50, 80, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 20, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 50, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 80, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(70, 110, 46, 13))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(110, 110, 61, 20))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.progressBar = QtGui.QProgressBar(self.groupBox)
        self.progressBar.setGeometry(QtCore.QRect(20, 210, 241, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 240, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(280, 70, 261, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setKerning(True)
        self.label_2.setFont(font)
        self.label_2.setAcceptDrops(False)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setStyleSheet(_fromUtf8(" border-style: solid;\n"
"    border-width: 2px;"))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8("../image2/input/input.png")))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(False)
        self.label_2.setOpenExternalLinks(False)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox_4 = QtGui.QGroupBox(DialogAddKeyFormImg)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 330, 711, 261))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.scrollArea = QtGui.QScrollArea(self.groupBox_4)
        self.scrollArea.setGeometry(QtCore.QRect(10, 20, 181, 231))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.scrollArea.setFont(font)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 179, 229))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.listWidget = QtGui.QListWidget(self.scrollAreaWidgetContents)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 181, 231))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))

        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_3.setGeometry(QtCore.QRect(420, 20, 281, 221))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_9 = QtGui.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(20, 40, 46, 13))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.comboBox = QtGui.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(70, 30, 69, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(20, 110, 46, 20))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_7.setGeometry(QtCore.QRect(70, 110, 151, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(70, 80, 113, 20))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(20, 80, 46, 13))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(70, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_4 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_4.setGeometry(QtCore.QRect(170, 160, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_4)
        self.groupBox_5.setGeometry(QtCore.QRect(210, 20, 201, 221))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 30, 91, 20))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.checkBox_5 = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox_5.setGeometry(QtCore.QRect(90, 140, 70, 17))
        self.checkBox_5.setObjectName(_fromUtf8("checkBox_5"))
        self.checkBox_4 = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox_4.setGeometry(QtCore.QRect(90, 120, 70, 17))
        self.checkBox_4.setObjectName(_fromUtf8("checkBox_4"))
        self.checkBox = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox.setGeometry(QtCore.QRect(90, 60, 31, 17))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.label_7 = QtGui.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.checkBox_3 = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox_3.setGeometry(QtCore.QRect(90, 100, 70, 17))
        self.checkBox_3.setObjectName(_fromUtf8("checkBox_3"))
        self.label_6 = QtGui.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(40, 60, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.checkBox_2 = QtGui.QCheckBox(self.groupBox_5)
        self.checkBox_2.setGeometry(QtCore.QRect(90, 80, 70, 17))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))

        self.retranslateUi(DialogAddKeyFormImg)
        QtCore.QMetaObject.connectSlotsByName(DialogAddKeyFormImg)

    def retranslateUi(self, DialogAddKeyFormImg):
        DialogAddKeyFormImg.setWindowTitle(_translate("DialogAddKeyFormImg", "เพิ่มเฉลยจากภาพ", None))
        self.groupBox.setTitle(_translate("DialogAddKeyFormImg", "File", None))
        self.pushButton.setText(_translate("DialogAddKeyFormImg", "เลือกไฟล์", None))
        self.label.setText(_translate("DialogAddKeyFormImg", "ไฟล์ภาพ:", None))
        self.groupBox_2.setTitle(_translate("DialogAddKeyFormImg", "Detail", None))
        self.label_3.setText(_translate("DialogAddKeyFormImg", "ผลการประมวลผล:", None))
        self.label_4.setText(_translate("DialogAddKeyFormImg", "จำนวนข้อที่ใช้:", None))
        self.label_5.setText(_translate("DialogAddKeyFormImg", "ชุดข้อสอบ:", None))
        self.label_8.setText(_translate("DialogAddKeyFormImg", "เทอม :", None))
        self.pushButton_2.setText(_translate("DialogAddKeyFormImg", "ประมวลผลภาพ", None))
        self.groupBox_4.setTitle(_translate("DialogAddKeyFormImg", "Answer", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        
          
       
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_3.setTitle(_translate("DialogAddKeyFormImg", "Setting", None))
        self.label_9.setText(_translate("DialogAddKeyFormImg", "ชุดที่ใช้:", None))
        self.comboBox.setItemText(0, _translate("DialogAddKeyFormImg", "ชุดที่1", None))
        self.comboBox.setItemText(1, _translate("DialogAddKeyFormImg", "ชุดที่2", None))
        self.comboBox.setItemText(2, _translate("DialogAddKeyFormImg", "ชุดที่3", None))
        self.comboBox.setItemText(3, _translate("DialogAddKeyFormImg", "ชุดที่4", None))
 
        self.label_10.setText(_translate("DialogAddKeyFormImg", "ชื่อวิชา :", None))
        self.label_11.setText(_translate("DialogAddKeyFormImg", "รหัสวิชา:", None))
        self.pushButton_3.setText(_translate("DialogAddKeyFormImg", "จัดเก็บเฉลย", None))
        self.pushButton_4.setText(_translate("DialogAddKeyFormImg", "ยกเลิก", None))
        self.groupBox_5.setTitle(_translate("DialogAddKeyFormImg", "Edit", None))
        self.checkBox_5.setText(_translate("DialogAddKeyFormImg", "5", None))
        self.checkBox_4.setText(_translate("DialogAddKeyFormImg", "4", None))
        self.checkBox.setText(_translate("DialogAddKeyFormImg", "1", None))
        self.label_7.setText(_translate("DialogAddKeyFormImg", "คำตอบล่าสุด:", None))
        self.checkBox_3.setText(_translate("DialogAddKeyFormImg", "3", None))
        self.label_6.setText(_translate("DialogAddKeyFormImg", "คำตอบ:", None))
        self.checkBox_2.setText(_translate("DialogAddKeyFormImg", "2", None))




        self.pushButton_4.clicked.connect(self.cancel)
        self.checkBox.clicked.connect(self.checkBox1)
        self.checkBox_2.clicked.connect(self.checkBox2)
        self.checkBox_3.clicked.connect(self.checkBox3)
        self.checkBox_4.clicked.connect(self.checkBox4)
        self.checkBox_5.clicked.connect(self.checkBox5)


        for i in range(120):
            item = QtGui.QListWidgetItem()
            self.listWidget.addItem(item)

        self.checkBox.setEnabled(False) 
        self.checkBox_2.setEnabled(False) 
        self.checkBox_3.setEnabled(False) 
        self.checkBox_4.setEnabled(False) 
        self.checkBox_5.setEnabled(False) 

        #self.lineEdit.setText("")
        self.lineEdit_2.setText("Ready")
        self.lineEdit_3.setText("None")
        self.lineEdit_4.setText("None")


        self.listWidget.currentItemChanged.connect(self.ClickList)
        self.pushButton_2.clicked.connect(self.process)
        self.pushButton.clicked.connect(self.setExistingDirectory)
        self.pushButton_3.clicked.connect(self.add2list)
    def UpdateList(self):
           list_c=[]
           for i in range(len(self.List_M)):
                if self.List_M[i][0]==1:
                    list_c.append(1)

                if self.List_M[i][1]==1:
                    list_c.append(2)

                if self.List_M[i][2]==1:
                    list_c.append(3)

                if self.List_M[i][3]==1:
                    list_c.append(4)

                if self.List_M[i][4]==1:
                    list_c.append(5)

                print list_c
                item = self.listWidget.item(i)
                item.setText(_translate("DialogAddKeyFormImg", str(i+1)+":    "+str(list_c), None))
                list_c=[]

    def checkBox1(self):
        index=self.listWidget.currentRow()
        if self.checkBox.isChecked():
            self.List_M[index][0]=1
            print "Yes"
        else:
            self.List_M[index][0]=0
            print "No"

        self.UpdateList()
    def checkBox2(self):
        index=self.listWidget.currentRow()
        if self.checkBox_2.isChecked():
            self.List_M[index][1]=1
            print "Yes"
        else:
            self.List_M[index][1]=0
            print "No"

        self.UpdateList()
    def checkBox3(self):
        index=self.listWidget.currentRow()
        if self.checkBox_3.isChecked():
            self.List_M[index][2]=1
            print "Yes"
        else:
            self.List_M[index][2]=0
            print "No"

        self.UpdateList()
    def checkBox4(self):
        index=self.listWidget.currentRow()
        if self.checkBox_4.isChecked():
            self.List_M[index][3]=1
            print "Yes"
        else:
            self.List_M[index][3]=0
            print "No"

        self.UpdateList()
    def checkBox5(self):
        index=self.listWidget.currentRow()
        if self.checkBox_5.isChecked():
            self.List_M[index][4]=1
            print "Yes"
        else:
            self.List_M[index][4]=0
            print "No"

        self.UpdateList()


       
    def setExistingDirectory(self):
            self.openFilesPath = ''
            print "setExistingDirectory"
            directory = QtGui.QFileDialog.getOpenFileName(self,
                "QFileDialog.getOpenFileNames()", self.openFilesPath,"Image Files (*.png);;Image Files (*.BMP);;Image Files (*.JPEG)" )

            self.lineEdit.setText(directory)
            self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8(directory)))

    def ClickList(self):
        self.checkBox.setEnabled(True) 
        self.checkBox_2.setEnabled(True) 
        self.checkBox_3.setEnabled(True) 
        self.checkBox_4.setEnabled(True) 
        self.checkBox_5.setEnabled(True) 

        self.checkBox.setChecked(False) 
        self.checkBox_2.setChecked(False) 
        self.checkBox_3.setChecked(False) 
        self.checkBox_4.setChecked(False) 
        self.checkBox_5.setChecked(False) 
        #print self.listWidget.currentRow()
        index=self.listWidget.currentRow()
        
        print "############################"
        #print self.List_answer_main[index]
        for i in range(len(self.List_answer_main[index])):
            print self.List_answer_main[index][i]
            if self.List_answer_main[index][i]==1:
                self.checkBox.setChecked(True) 
            if self.List_answer_main[index][i]==2:
                self.checkBox_2.setChecked(True) 
            if self.List_answer_main[index][i]==3:
                self.checkBox_3.setChecked(True) 
            if self.List_answer_main[index][i]==4:
                self.checkBox_4.setChecked(True) 
            if self.List_answer_main[index][i]==5:
                self.checkBox_5.setChecked(True) 
    def process(self):
      
        #self.pushButton_2.setEnabled(False)
        import TR
        self.List_answer=[]
        self.List_M=[]
        for i in range(120):
            self.List_M.append([0,0,0,0,0,])
        import process
        M=TR.TR(0)
        img=cv2.imread(str(self.lineEdit.text()))
        cv2.imwrite("keyimg\\key.png",M.ThresholdAndRotate(img,1))
        self.P=process.MainProcess(0)
        code,List_answer,Set,Tearm=self.P.Process('keyimg\\key.png')
        self.List_answer_main= List_answer                      
        print "Number:",self.checkNumber(List_answer) 
        self.lineEdit_2.setText("Finish")
        self.lineEdit_3.setText(str(self.checkNumber(List_answer)))
        try:
            self.lineEdit_4.setText(str(Set[0]))
        except:
            self.lineEdit_4.setText(str("None"))



        for i in range(len(List_answer)): 
            print List_answer[i]
            item = self.listWidget.item(i)
            item.setText(_translate("DialogAddKeyFormImg", str(i+1)+":    "+str(List_answer[i]), None))

        for i in range(120):
            print "########################################"
            for j in range(len(self.List_answer_main[i])):
                    print self.List_answer_main[i][j]

                    if self.List_answer_main[i][j]==1:
                        self.List_M[i][0]=1
                    if self.List_answer_main[i][j]==2:
                        self.List_M[i][1]=1
                    if self.List_answer_main[i][j]==3:
                        self.List_M[i][2]=1
                    if self.List_answer_main[i][j]==4:
                        self.List_M[i][3]=1
                    if self.List_answer_main[i][j]==5:
                        self.List_M[i][4]=1
        for i in range(120):
             print i+1,":",self.List_M[i]
    def cancel(self):
            import DialogKey

            self.ui=DialogKey.Ui_Dialog_SetKey()
            self.ui.setModal(True)
            self.ui.show()
            super(Ui_DialogAddKeyFormImg, self).accept()
    def add2list(self):
            print "setkey"
            file = open("key/{:>}.txt".format(self.lineEdit_8.text()), "w")
           
            file.write("1\n")
            file.write("1\n")
            file.write("1\n")
            file.write("1\n")
            for i in range(len(self.List_M)):
                file.write(str(self.List_M[i])+"\n")
                print self.List_M[i]
            file.close()




 
            import DialogKey

            self.ui=DialogKey.Ui_Dialog_SetKey()
            self.ui.setModal(True)
            self.ui.show()
            super(Ui_DialogAddKeyFormImg, self).accept()
    def checkNumber(self,list_a):
      num=len(list_a)-1
      for i in range(100):
        self.progressBar.setProperty("value", i+1)
      for i in range(len(list_a)):
        #print list_a[num-i]
        
        if(len(list_a[num-i])!=0):

          #print (num-i)+1 ,"Num"
          return (num-i)+1
          break


    def progressBarConverse(self):
    
            print i,":",(i*100)/120          

 

