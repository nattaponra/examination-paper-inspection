# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogAddKeyFormCheck.ui'
#
# Created: Wed Oct 29 13:57:11 2014
#      by: PyQt4 UI code generator 4.11.1
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

class  DialogAddKeyFormCheck(QtGui.QDialog):
    C=[1,1,1,1,1]
    List_Main=[]
     

    List_number=[]
    for i in range(120):
        List_number.append([0,0,0,0,0])

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 480)
        font = QtGui.QFont()
        font.setPointSize(10)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon/Key-icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 40, 601, 391))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.scrollArea = QtGui.QScrollArea(self.groupBox_2)
        self.scrollArea.setGeometry(QtCore.QRect(10, 30, 231, 301))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 229, 299))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.groupBox = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(280, 20, 221, 91))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setEnabled(False)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 31, 31))
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_3.setMouseTracking(True)
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-remove-icon.png")))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setEnabled(True)
        self.label_4.setGeometry(QtCore.QRect(60, 20, 31, 31))
        self.label_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_4.setMouseTracking(True)
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-remove-icon.png")))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QtCore.QRect(100, 20, 31, 31))
        self.label_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_5.setMouseTracking(True)
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-remove-icon.png")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QtCore.QRect(140, 20, 31, 31))
        self.label_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_6.setMouseTracking(True)
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-remove-icon.png")))
        self.label_6.setOpenExternalLinks(False)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setEnabled(True)
        self.label_7.setGeometry(QtCore.QRect(180, 20, 31, 31))
        self.label_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label_7.setMouseTracking(True)
        self.label_7.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_7.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.label_7.setAcceptDrops(True)
        self.label_7.setAutoFillBackground(False)
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setTextFormat(QtCore.Qt.AutoText)
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-remove-icon.png")))
        self.label_7.setScaledContents(False)
        self.label_7.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_13 = QtGui.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(30, 60, 171, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.listWidget = QtGui.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 31, 231, 301))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
 
        self.groupBox_3 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_3.setGeometry(QtCore.QRect(280, 250, 301, 131))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_8 = QtGui.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(20, 30, 81, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 30, 61, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 60, 113, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_14 = QtGui.QLabel(self.groupBox_3)
        self.label_14.setGeometry(QtCore.QRect(50, 60, 46, 13))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 90, 113, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.label_15 = QtGui.QLabel(self.groupBox_3)
        self.label_15.setGeometry(QtCore.QRect(50, 90, 41, 20))
        self.label_15.setObjectName(_fromUtf8("label_15"))
      
 
        self.label_16 = QtGui.QLabel(self.groupBox_3)
        self.label_16.setGeometry(QtCore.QRect(170, 30, 41, 20))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.groupBox_4 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_4.setGeometry(QtCore.QRect(280, 110, 301, 131))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label = QtGui.QLabel(self.groupBox_4)
        self.label.setGeometry(QtCore.QRect(40, 30, 41, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit.setGeometry(QtCore.QRect(80, 30, 51, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_9 = QtGui.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(30, 62, 46, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 60, 51, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(80, 90, 51, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_11 = QtGui.QLabel(self.groupBox_4)
        self.label_11.setGeometry(QtCore.QRect(140, 60, 46, 13))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(140, 90, 46, 13))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(460, 440, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 440, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "เพิ่มเฉลย", None))
        self.groupBox_2.setTitle(_translate("Dialog", "เฉลย", None))
        self.groupBox.setTitle(_translate("Dialog", "ตัวเลือก", None))
        self.label_13.setText(_translate("Dialog", "1        2        3        4        5", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
 
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.groupBox_3.setTitle(_translate("Dialog", "ตั้งค่าเฉลย", None))
        self.label_8.setText(_translate("Dialog", "จำนวนข้อที่ใช้:", None))
        self.label_14.setText(_translate("Dialog", "รหัสวิชา:", None))
        self.label_15.setText(_translate("Dialog", "ชื่อวิชา:", None))
     
        
        self.groupBox_4.setTitle(_translate("Dialog", "สถานะ", None))
        self.label.setText(_translate("Dialog", "ข้อที่ :", None))
        self.label_9.setText(_translate("Dialog", "เพิ่มแล้ว:", None))
        self.label_10.setText(_translate("Dialog", "ยังไม่ได้เพิ่ม:", None))
        self.label_11.setText(_translate("Dialog", "ข้อ", None))
        self.label_12.setText(_translate("Dialog", "ข้อ", None))
        self.label_2.setText(_translate("Dialog", "เพิ่มเฉลย", None))
        self.pushButton.setText(_translate("Dialog", "จัดเก็บเฉลย", None))
        self.pushButton_2.setText(_translate("Dialog", "ยกเลิก", None))




        self.lineEdit_3.setText("0") 
        self.lineEdit_4.setText("120") 
        self.pushButton.clicked.connect(self.save)

        if self.listWidget.currentRow()==-1:
           self.label_3.setEnabled(False)
           self.label_4.setEnabled(False)
           self.label_5.setEnabled(False)
           self.label_6.setEnabled(False)
           self.label_7.setEnabled(False)





      
        for i in range(120):
            item = QtGui.QListWidgetItem()
            self.listWidget.addItem(item)                                                                                                                                                                        
            item = self.listWidget.item(i)
            item.setText(_translate("Dialog", ("Number: "+str(i+1)+str("")), None)) 

        self.label_3.mousePressEvent = self.C1 
        self.label_4.mousePressEvent = self.C2 
        self.label_5.mousePressEvent = self.C3 
        self.label_6.mousePressEvent = self.C4 
        self.label_7.mousePressEvent = self.C5 
        self.listWidget.currentItemChanged.connect(self.on_item_changed)
        self.pushButton_2.clicked.connect(self.cancel)

    def cancel(self):
            import DialogKey

            self.ui=DialogKey.Ui_Dialog_SetKey()
            self.ui.setModal(True)
            self.ui.show()
            super(DialogAddKeyFormCheck, self).accept()
    def save(self):
        
            print "Save"
 

            file = open("key/{:>}.txt".format(self.lineEdit_5.text()), "w")
           
            file.write(str(self.lineEdit_2.text())+"\n")
            file.write(str("1")+"\n") 
            file.write(str("1")+"\n") 
            file.write(str("1")+"\n") 

            for i in range(len(self.List_number)):
                file.write(str(self.List_number[i])+"\n")
                
            file.close()



            import DialogKey

            self.ui=DialogKey.Ui_Dialog_SetKey()
            self.ui.setModal(True)
            self.ui.show()
            super(DialogAddKeyFormCheck, self).accept()
    def update_list(self):
                index=int(self.listWidget.currentRow())
                #item = QtGui.QListWidgetItem()
                #self.listWidget.addItem(item)                                                                                                                                                                        
                item = self.listWidget.item(index)                                                                                                                                              
                item.setText(_translate("Dialog", ("Number: "+str(index+1)+str(self.update_data())), None)) 



                number_=0
                for i in range(120):
                       #print self.List_number[i][0],self.List_number[i][1],self.List_number[i][2],self.List_number[i][3],self.List_number[i][4]
                       if self.List_number[i][0]==1 or self.List_number[i][1]==1 or self.List_number[i][2]==1 or self.List_number[i][3]==1 or self.List_number[i][4]==1 :
                                number_=number_+1

                self.lineEdit_3.setText(str(number_)) 
                self.lineEdit_4.setText(str(120-number_)) 

    def update_data(self):
        list_an=[]
        for i in range(len(self.List_number[int(self.listWidget.currentRow())])):
            if(self.List_number[int(self.listWidget.currentRow())][i]==1):
                    list_an.append([i+1])

        return list_an
    def on_item_changed(self):
        lis_c=self.List_number[int(self.listWidget.currentRow())] 
        
        self.lineEdit.setText(str(self.listWidget.currentRow()+1)) 

        self.label_3.setEnabled(True)
        self.label_4.setEnabled(True)
        self.label_5.setEnabled(True)
        self.label_6.setEnabled(True)
        self.label_7.setEnabled(True)
        #print self.listWidget.currentRow()
        


        self.C[0]=lis_c[0]
        self.C[1]=lis_c[1]
        self.C[2]=lis_c[2]
        self.C[3]=lis_c[3]
        self.C[4]=lis_c[4]




        if self.C[0]==1:
            self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-apply-icon.png")))

        else:
            self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-remove-icon.png")))

        if self.C[1]==1:
            self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-apply-icon.png")))
        else:
            self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-remove-icon.png")))
        if self.C[2]==1:
            self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-apply-icon.png")))
        else:
            self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-remove-icon.png")))
        if self.C[3]==1:
            self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-apply-icon.png")))
        else:
            self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-remove-icon.png")))
        if self.C[4]==1:
            self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-apply-icon.png")))
        else:
            self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-remove-icon.png")))

    def C1(self,num):
        if(self.C[0]==0):
             self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-apply-icon.png")))
             self.C[0]=1
             self.List_number[int(self.listWidget.currentRow())][0]=1
        else:
             self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-remove-icon.png")))
             self.C[0]=0
             self.List_number[int(self.listWidget.currentRow())][0]=0
        
        self.update_list()
    def C2(self,num):
        if(self.C[1]==0):
             self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-apply-icon.png")))
             self.C[1]=1
             self.List_number[int(self.listWidget.currentRow())][1]=1
        else:
             self.label_4.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-remove-icon.png")))
             self.C[1]=0
             self.List_number[int(self.listWidget.currentRow())][1]=0
        self.update_list()
         
    def C3(self,num):
        if(self.C[2]==0):
             self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-apply-icon.png")))
             self.C[2]=1
             self.List_number[int(self.listWidget.currentRow())][2]=1
        else:
             self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-remove-icon.png")))
             self.C[2]=0
             self.List_number[int(self.listWidget.currentRow())][2]=0
        self.update_list() 
         
    def C4(self,num):
        if(self.C[3]==0):
             self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-apply-icon.png")))
             self.C[3]=1
             self.List_number[int(self.listWidget.currentRow())][3]=1
        else:
             self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-remove-icon.png")))
             self.C[3]=0
             self.List_number[int(self.listWidget.currentRow())][3]=0
        self.update_list()
         
    def C5(self,num):
        if(self.C[4]==0):
             self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-apply-icon.png")))
             self.C[4]=1
             self.List_number[int(self.listWidget.currentRow())][4]=1
        else:
             self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8("icon/Circle-remove-icon.png")))
             self.C[4]=0
             self.List_number[int(self.listWidget.currentRow())][4]=0
        self.update_list() 
       
 

