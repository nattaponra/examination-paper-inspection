# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Process_f.ui'
#
# Created: Wed Nov 05 20:56:31 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!
import cv2
import numpy as np
import math 
import multiprocessing 
import DirMain
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

class Ui_Dialog_process(QtGui.QDialog):
    D=DirMain.dire(0)  
    D.create()
    font = cv2.FONT_HERSHEY_SIMPLEX  
    List_term_main=[]
    List_Set_main=[]
    def __init__(self):
        
        QtGui.QDialog.__init__(self)
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 323)
        font = QtGui.QFont()
        font.setPointSize(11)
        Dialog.setFont(font)
        self.progressBar = QtGui.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(40, 40, 581, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progressBar_2 = QtGui.QProgressBar(Dialog)
        self.progressBar_2.setGeometry(QtCore.QRect(40, 90, 581, 23))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName(_fromUtf8("progressBar_2"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 20, 131, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 121, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.listView = QtGui.QListView(Dialog)
        self.listView.setGeometry(QtCore.QRect(40, 120, 551, 131))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(520, 270, 75, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(424, 270, 91, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Process", None))
        self.label.setText(_translate("Dialog", "การตรวจทั้งหมด", None))
        self.label_2.setText(_translate("Dialog", "การตรวจต่อแผ่น", None))
        self.pushButton.setText(_translate("Dialog", "ยกเลิก", None))
        self.pushButton_2.setText(_translate("Dialog", "หยุดชั่วคราว", None))

        self.pushButton_2.clicked.connect(self.Process_main)

    def Process_main(self):
        print "UUU"
        code,list_a,Set,Term=self.Process('image2\input\input.png')
        print "Yes"
        





     

     

     
    def Check_Location(self,img,List):
         List_c=[]
         
         for i in range(len(List)):
           #print i+1,List[i][0][1],List[i][0][0]
           List_c.append((List[i][0][1],List[i][0][0]))
         
         img,List_Center_Point1,List_c=self.Inspector_Sort(img,List_c)   
          
         for i in range(len(List_c)):
           #print List_c[i]
           #print i+1,List_c[i][0][0],List_c[i][1][0],List_c[i][2][0],List_c[i][3][0],List_c[i][4][0]
           if((List_c[i][1][0]-List_c[i][0][0])<30):
            print "NoPass1"
            return "No"
           if((List_c[i][2][0]-List_c[i][1][0])<30):
            print "NoPass2"
            return "No"
           if((List_c[i][3][0]-List_c[i][2][0])<30):
            print "NoPass3"  
            return "No" 
           if((List_c[i][4][0]-List_c[i][3][0])<30):
            print "NoPass4" 
            return "No" 

         return "Yes"

    def Resize(self,img):
            Y = img.shape[0]
            X = img.shape[1] 
            while X!=1231:
              Y=Y+1
              X=X+1
            return cv2.resize(img, (X, Y)) 



    def Circle_Drawing(self,List,img):
        try:
          for i in range(len(List)):
              #print List[i][0]
              #cv2.circle(img,(List[0],List[1]),List[2],(0,255,0),2)
              cv2.circle(img,(List[i][0]),2,(0,0,255),3)
          return img
        except:
          print "Don't drawing"
       
    def crop_top_AND_But_full(self,img):
            Y = img.shape[0]
            X = img.shape[1]  

            YY=0
            x=X
            y=Y
             
            for i in range(0,1000):
                if(img[YY+1,X/2][0]==0): 
                           font = cv2.FONT_HERSHEY_SIMPLEX
                           cv2.putText(img, str(YY+1),(X/2,YY+1),font, 0.5,(0,255,0),2)
                           
                           top=YY 
                           break 
                   
                YY=YY+1
            for i in range(0,1000):
                if(img[Y-1,X/2][0]==0): 
                           font = cv2.FONT_HERSHEY_SIMPLEX
                           cv2.putText(img, str(Y-1),(X/2,Y-1), font, 0.5,(0,255,0),2)
                            
                           but=Y 
                           break 
                   
                Y=Y-1 
            
           
            #print top,but
            #font = cv2.FONT_HERSHEY_SIMPLEX
            #cv2.putText(img, str("wewerwe"),(X/2,top), font, 0.5,(222,255,122),2)
                          
            return img[top:but, 0:X]

          







    def crop_CodeStudent_area(self,X,Y,img):#function µÑ´àÍÒà©¾ÒÐ ¢éÍÊÍºËÅÑ¡ returnà»ç¹ä¿ÅìÀÒ¾
            YY=0
            x=X
            y=Y
             
            for i in range(0,1000):
                if(img[YY+1,X/2][0]==0): 
                           font = cv2.FONT_HERSHEY_SIMPLEX
                           cv2.putText(img, str(YY+1),(X/2,YY+1), font, 0.5,(0,255,0),2)
                           
                           top=YY 
                           break 
                   
                YY=YY+1
            for i in range(0,1000):
                if(img[Y-1,X/2][0]==0): 
                           font = cv2.FONT_HERSHEY_SIMPLEX
                           cv2.putText(img, str(Y-1),(X/2,Y-1), font, 0.5,(0,255,0),2)
                            
                           but=Y 
                           break 
                   
                Y=Y-1 
            #cv2.imwrite('image/flax/sss.png',img) 
            XR=0
            XL=0
            SX=X
            X=x
            Y=y
            start=0
            ######################################################## 
            for i in range(0,1000):
                   # print img[Y/2,X-1][0]
                    if(img[Y/2,X-1][0]==0): 
                           #img[Y/2,X-1] = [0,255,0]
                           XR=X 
                           break 
                   
                    X=X-1
            ########################################################
            X=0        
            for i in range(0,1000):
                    #print img[Y/2,X][0]
                    if(img[Y/2,X][0]==0): 
                           #img[Y/2,X] = [0,255,0]
                           XL=X-1
                           break 
                   
                    X=X+1
            ########################################################
            f=((XR- XL)*20)/100
            e=((XR- XL)*40)/100
            crop_img = img[0:y, f:e]
            #cv2.imwrite('image/flax/begin.png',crop_img) 
            f=((but- top)*66)/100
            print but-top
            crop_img = crop_img[f:but, 0:x]

            #crop_TopAndBut_main(X,Y)
            return crop_img #return ¢Íº´éÒ¹«éÒÂ ¢ÇÒ
       


    def crop_TopAndBut_main(self,X,Y,img): #µÑ´¢Íº ÊèÇ¹ÂèÍÂ¢Í§main
       
            """  YR=0
            YL=0
            SX=X
            
            start=0
            ######################################################## 
            for i in range(0,1000):
                    print img[Y/2,X-1][0]
                    img[Y/2,X-1] = [0,255,45]
                    if(img[Y-1,X/3][0]==0): 
                           
                           YR=Y 
                           break 
                   
                    Y=Y-1
            ########################################################
            Y=0        
            for i in range(0,1000):
                    #print img[Y/2,X][0]
                    if(img[Y-1,X/3][0]==0): 
                           img[Y/2,X-1] = [0,255,45]
                           YL=Y-1
                           break 
                   
                    Y=Y+1
            ########################################################
            cv2.imwrite('image/test_crop.png',img)
            pic1 = img[YL:YR, 0:X] """

            print "X=",X,"Y=", Y
            x=X-1
            y=Y-1
            for i in range(0,1000):
                j=0
                for j in range(0,100):
                     
                    # print img[(y-j),(x-i)]
                    if(img[(y-j),(x-i)][0]==0):
                        img[(y-j),(x-i)]=[0,240,150]
                        break
     
                         

            #cv2.imwrite('image/test_crop.png',img)                      

                              
                         
                         
                           
                             

                         
                          

                         


            
             
    def flax_size_main(self,X,Y,pers,pere,img):#function  µÑ´mainà»ç¹4ÊèÇ¹
       
            XR=0
            XL=0
            SX=X
            
            start=0
            ######################################################## 
            for i in range(0,1000):
                   # print img[Y/2,X-1][0]
                    if(img[Y/2,X-1][0]==0): 
                           #img[Y/2,X-1] = [0,255,0]
                           XR=X 
                           break 
                   
                    X=X-1
            ########################################################
            X=0        
            for i in range(0,1000):
                    #print img[Y/2,X][0]
                    if(img[Y/2,X][0]==0): 
                           #img[Y/2,X] = [0,255,0]
                           XL=X-1
                           break 
                   
                    X=X+1
            ########################################################
            ps=((XR)*pers)/100
            pe=((XR)*pere)/100
            pic1 = img[0:Y, ps:XR-pe] 
            return pic1 #return ¢Íº´éÒ¹«éÒÂ ¢ÇÒ
    def fine_size_main_final(self,img):#¤Ñ´ ¿ÔÇº¹ 
            Y = img.shape[0]
            X = img.shape[1]  
            p=((Y)*12)/100
           
            pic1 = img[p:Y, 0:X] 
            #cv2.imwrite('image/flax/full.png',pic1)
            return pic1 #return      
       
      
    def detect_circle(self,img,code):#µÃÇ¨ËÒÇ§¡ÅÁ
          List_Main=[]


           
         



          
          y = img.shape[0]
          x = img.shape[1]
          cv2.imwrite('image/process/pro_flax{:>}.png'.format(code),img)
          grey = cv2.imread('image/process/pro_flax{:>}.png'.format(code),0)
          pocess=grey

          print "--------------------------------"
           
          try:
            for Param2 in range(11,14):

              for MinRadius in range(12,15):

                  for MaxRadius in range(21,23):
                    #print Param2,MinRadius,MaxRadius
                    
                    #grey=pocess
                    List_Center_Point=[]
                    ret, thresh = cv2.threshold(grey,50,255,cv2.THRESH_BINARY)
                    circles = cv2.HoughCircles(thresh,cv2.cv.CV_HOUGH_GRADIENT,1,11,param1=2,param2=Param2,minRadius=MinRadius,maxRadius=MaxRadius)
                     
                     
                    try:
                      for i in circles[0,:]:
                              #print k
                              #print i[0],i[1]
                              List_Center_Point.append(((i[0],i[1]),i[0],i[1]))
                          
                              #draw the outer circle
                              #cv2.circle(img,(i[0],i[1]),i[2],(0,255,0),2)
                              #draw the centre of the circle
                               
                              #cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
                               
                               
                    except:
                      pass
                     
                    #print "######=",len(List_Center_Point),"##=",g,t
                    if(len(List_Center_Point)==150):
                       
                      print "yes"
                      List_Main=List_Center_Point
                      for i in range(len(List_Main)):
                         cv2.circle(img,(List_Main[i][0][0],List_Main[i][0][1]),15,(0,255,0),2)
                         #print List_Main[i][0][0]
                      break 
                  if(len(List_Main)==150):
                      break 
              if(len(List_Main)==150):
                      break 




          except:
            pass
          if(len(List_Main)==150):
             
              #print "List_Main",len(List_Main)
              return img,List_Main
          else:
              #print "List_Main",len(List_Main)
              for i in range(len(List_Main)):
                         cv2.circle(img,(List_Main[i][0][0],List_Main[i][0][1]),15,(0,255,0),2)
                         #print List_Main[i][0][0]
              #cv2.imwrite('detect_circle2.png',img)
              return None,None

               
                    
                 
               



          

          
    def Inspector(self,img,List):
        List_in=[]
        for i in range(len(List)):
             
             #print img[List[i][0][1],List[i][0][0]][0]
             if(img[List[i][0][1],List[i][0][0]][0]==0):
                 List_in.append((List[i][0][1],List[i][0][0]))
                 cv2.circle(img,(List[i][0][0],List[i][0][1]),2,(12,121,255),3)
             else:
                 List_in.append((List[i][0][1],List[i][0][0]))
        return img,List_in     
    def Inspector_Sort(self,img,List):
            List.sort()
            List_out=[]
            List_loca=[]
            List_small=[]

            #print len(List)
            num=1
            j=0
            for i in range(0,30):
              #print j+1 ,j+5
              d=j+1
              List_small=[]
              for h in range(j,j+5):
                #print  List[d-1]
                List_small.append((List[d-1][1],List[d-1][0]))
                d=d+1
              List_small.sort()
              for f in range(len(List_small)):

                 #print List_small[f][1],List_small[f][0]
                 List_out.append((List_small[f][1],List_small[f][0]))
                 font = cv2.FONT_HERSHEY_SIMPLEX
                 cv2.putText(img, str(num),(List_small[f][0],List_small[f][1]), font, 0.5,(0,255,0),2)
                 
                 num=num+1

              j=j+5
              List_loca.append((List_small[0],List_small[1],List_small[2],List_small[3],List_small[4]))

            return img,List_out,List_loca
              #print List[i]
              #
              #cv2.putText(img, str(i),(List[i][1],List[i][0]), font, 0.5,(0,255,0),2)
              #cv2.putText(img, str(i),(70,18), font, 0.5,(0,255,0),2)


    def Detect_Circle_all(self,img,Range,code):

        List_main=[]
        y = img.shape[0]
        x = img.shape[1]
         
        cv2.imwrite('image/process/Detect_Circle_all{:>}.png'.format(code),img)
        grey = cv2.imread('image/process/Detect_Circle_all{:>}.png'.format(code),0)
        #print x,y 

        for MinRadius in range(12,15):
            for MaxRadius in range(21,23):
                try:
                  ret, thresh = cv2.threshold(grey,50,255,cv2.THRESH_BINARY)
                  circles = cv2.HoughCircles(thresh,cv2.cv.CV_HOUGH_GRADIENT,1,10,param1=1,param2=14,minRadius=MinRadius,maxRadius=MaxRadius)
                  j=1
                  l=[]
                  for i in circles[0,:]:
                          #print i[0],i[1]
                          l.append(((i[0],i[1])))
                      
                          #draw the outer circle
                          #cv2.circle(img,(i[0],i[1]),i[2],(0,255,23),2)
                          #draw the centre of the circle
                           
                          #cv2.circle(img,(i[0],i[1]),2,(0,0,255),3)
                          j=j+1
                  #print len(l)
                  if(len(l)==Range):
                    List_main=l
                    #print "yes",len(l)
                    break
                except:
                    pass
            if(len(List_main)==Range):
                    break
        if(len(List_main)==Range):
            return List_main
        else:
            return None


    def Check_Num(self,img,List_Loca):
        List_num=[]
        
        for i in range(len(List_Loca)):
          #print List_Loca[i]
          List_process=[]
          #print "#=",i+1 
          #print i+1,img[List_Loca[i][0][1],List_Loca[i][0][0]][0]
          #print List_Loca[i][0][1],List_Loca[i][0][0]
          if(img[List_Loca[i][0][1],List_Loca[i][0][0]][0]==0):
            #print "1"
            List_process.append(1)
          if(img[List_Loca[i][1][1],List_Loca[i][1][0]][0]==0):
            #print "2" 
            List_process.append(2)    
          if(img[List_Loca[i][2][1],List_Loca[i][2][0]][0]==0):
            #print "3"
            List_process.append(3)
          if(img[List_Loca[i][3][1],List_Loca[i][3][0]][0]==0):
            #print "4"
            List_process.append(4)
          if(img[List_Loca[i][4][1],List_Loca[i][4][0]][0]==0):
            #print "5"
            List_process.append(5)
             
          List_num.append((i+1,List_process))
           
          #print len(List_num)
        return List_num #return [[1, 3, 5], [2, 3], [3], [4], [5], [4], [3], [1, 2, 3, 4, 5], [1], [3], [4], [5], [2], [2], [2], [2]]

    def Crop_Mini_case2_Top(self,img):
        Y = img.shape[0]
        X = img.shape[1] 
       
        Per=(Y*4)/100
        img=img[0:Per, 0:X]
        cv2.circle(img,(X/2,Y/2),2,(12,121,255),3)
        return img
    def Crop_Mini_case2_But(self,img):
        Y = img.shape[0]
        X = img.shape[1] 
       
        Per=(Y*5)/100
        img=img[Y-Per:Y, 0:X]
        cv2.circle(img,(X/2,Y/2),2,(12,121,255),3)
        Loca=Y-Per
        return img,Loca

    def Main_case2(self,name_file,code):

        img=cv2.imread(name_file)
        IMG=img
        List_mini=[]

        img=self.Crop_Mini_case2_Top(img)
        
           
        List_mini=self.Detect_Circle_all(img,5,code)
        #print len(List_mini)


        img=IMG
        y = img.shape[0]
        x = img.shape[1]


        List_mini.sort()
        #print "FUCK" 
        List_NumBer=[] 
        #print List_mini[0][0] ,List_mini[1][0] 
        k=0
        for i in range(0,15):

            List_c=[]
            for j in range(0,5):
                
                #cv2.circle(img,( List_mini[j][0] ,int(List_mini[j][1]+k)),2,(0,k*j,255),3)
                #font = cv2.FONT_HERSHEY_SIMPLEX
                #cv2.putText(img, str(j),(List_mini[j][0] ,int(List_mini[j][1]+k)), font, 0.5,(0,255,0),2)
                List_c.append((List_mini[j][0],int(List_mini[j][1]+k)))
            k=k+(y/30)
             
            List_NumBer.append((i+1,List_c))
        #cv2.imwrite('image/flax/test.png',img)



        List_mini=[]
        img=IMG
        img,Loca=self.Crop_Mini_case2_But(img)

        List_mini=self.Detect_Circle_all(img,5,code)
        img=IMG
        #print List_mini
        y = img.shape[0]
        x = img.shape[1]



        List_mini.sort()
         
        #print List_mini[0][0] ,List_mini[1][0] 
        k=0
        num=30
        for i in range(0,15):

            List_c=[]
            for j in range(0,5):
                
                cv2.circle(img,(int(List_mini[j][0]) ,int(List_mini[j][1]+Loca-k)),2,(0,k*j,255),3)
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(img, str(j),(int(List_mini[j][0]) ,int(List_mini[j][1]-k+Loca)), font, 0.5,(0,255,0),2)
                List_c.append((int(List_mini[j][0]),int(List_mini[j][1]+Loca-k)))
            k=k+(y/30)
            List_NumBer.append((num,(List_c)))
            num=num-1
        #cv2.imwrite('image/flax/test.png',img)
        List_NumBer.sort()


        List_Out=[]

        img=cv2.imread(name_file)
        for i in range(len(List_NumBer)):
           List_c=[]
           #print List_NumBer[i][1][0][0],List_NumBer[i][1][0][1] 
           #print img[List_NumBer[i][1][0][1],List_NumBer[i][1][0][0]][0] 
           if(img[List_NumBer[i][1][0][1],List_NumBer[i][1][0][0]][0]==0):
                  List_c.append((1))
                   
                  cv2.circle(img,(List_NumBer[i][1][0][0] ,List_NumBer[i][1][0][1]),5,(0,255,23),6)
           if(img[List_NumBer[i][1][1][1],List_NumBer[i][1][1][0]][0]==0):
                  List_c.append((2))
                  cv2.circle(img,(List_NumBer[i][1][1][0] ,List_NumBer[i][1][1][1]),5,(0,255,23),6)
           if(img[List_NumBer[i][1][2][1],List_NumBer[i][1][2][0]][0]==0):
                  List_c.append((3))
                  cv2.circle(img,(List_NumBer[i][1][2][0] ,List_NumBer[i][1][2][1]),5,(0,255,23),6)
           if(img[List_NumBer[i][1][3][1],List_NumBer[i][1][3][0]][0]==0):
                  List_c.append((4))
                  cv2.circle(img,(List_NumBer[i][1][3][0] ,List_NumBer[i][1][3][1]),5,(0,255,23),6)
           if(img[List_NumBer[i][1][4][1],List_NumBer[i][1][4][0]][0]==0):
                  List_c.append((5))
                  cv2.circle(img,(List_NumBer[i][1][4][0] ,List_NumBer[i][1][4][1]),5,(0,255,23),6)
           List_Out.append((i+1,(List_c)))
        #cv2.imwrite('image/flax/output2.png',img)
        return List_Out
    def Select_Case(self,Namefile,code):
        List_Center_Point1=[]
        List_Loca=[]
        img=cv2.imread(Namefile)
        img,List_Center_Point1= self.detect_circle(img,code)
        if(List_Center_Point1!=None and self.Check_Location(img,List_Center_Point1)!="No"):
          print "Case1"
          img,List_Sorted=self.Inspector(img,List_Center_Point1)
          List_Sorted.sort()
          for i in range(len(List_Sorted)):
              #print List_Sorted[i]
              cv2.putText(img, str(i),(List_Sorted[i][0]  ,int(List_Sorted[i][1])), self.font, 0.5,(0,255,0),2)
            
          #cv2.imwrite('image/flax/f_Process1.png',img)

          img,List_Center_Point1,List_Loca=self.Inspector_Sort(img,List_Sorted)
          img=cv2.imread(Namefile)
          List_Loca=self.Check_Num(img,List_Loca)
          #for i in range(len(List_Loca)): 
              #print "Number:",i+1,"Ans:",List_Loca[i]

          return List_Loca
          #cv2.imwrite('image/flax/f_Process2.png',img)
        else:
              print "Case2"
              List_Output=self.Main_case2(Namefile,code)
              #for i in range(len(List_Output)):
                   #print List_Output[i] 
                   #print "Number:",i+1,"Ans:",List_Output[i]
              return List_Output
    def Print_List_Type_Row(self,List):
        for i in range(len(List)):
          print "Number:",i+1,List[i]
        #####################################MAIN#################################
        #####################################First_Crop_Side#################################
    def SideLeft(self,SR,pic1):

          # pic1=cv2.imread('image/crop_top_down.png') 
          pic1 = pic1[None:None, None:SR]
          y = pic1.shape[0]-1 
          x = pic1.shape[1]-1  
       
          si=1.4
          DE=0
          for i in range(0,1000):
              if(DE==1):
                  break
              for j in range(0,1000):
                  #print i,j 
                 # pic1[(j),((x-i)/2)]=[0,255,255]
              
                     
                  if(j>y/2):
                      
                      DE=1
                      SideLeft= (x-i)/si
                      #print "SideLeft=",SideLeft
                      
                      #cv2.putText(pic1, str(int((x-i)/si)),(int((x-i)/si),j), font, 2,(255,0,0),2)
                      #cv2.circle(pic1,(int((x-i)/si),y/2),2,(0,0,255),3)
                      break
                  elif(pic1[(j),((x-i)/si)][0]==0):
                      #pic1[(j),((x-i)/si)]=[0,0,255]
                      break
                  elif(pic1[(j),((x-i)/si)][0]==255):
                      #pic1[(j),((x-i)/si)]=[0,0,255]
                      pass

                   
          #pic1 = img[None:None, SideRight:SideLeft]
          #cv2.imwrite('image/crop_left_s.png',pic1) 
          
          picr=pic1
          pic1 = pic1[None:None, SideLeft:None]
          #cv2.imwrite('image/crop_left.png',pic1) 

          return picr,SideLeft,pic1

    def SideRight(self,pic1):
          #pic1=cv2.imread('image/crop_top_down.png')
          y = pic1.shape[0]-10
          x = pic1.shape[1]-1   
          #print x,y
          SideRight=0
          SideLeft=0
          DE=0
          for i in range(0,2000):#X Start
                  if(DE==1):

                      break
                  else:
                      for j in range(0,y):#Y
                          if(pic1[(y-j),(x-i)][0]==0):
                              if(j<y/2):
                                  pic1[(y-j),(x-i)]=[0,240,150]

                              elif(j>y/2):

                                  pic1[(y-j),(x-i)]=[0,0,255]
                                  #print (y-j),(x-i)
                                  DE=1
                                  SideRight=x-i
                                  #print "SideRight=",x-i
                                  font = cv2.FONT_HERSHEY_SIMPLEX  
                                  cv2.putText(pic1, str(x-i),(x-i,y-j), font, 1,(0,255,0),2)
                                  break


                          else:
                              break

          #cv2.imwrite('image/crop_right.png',pic1)  
          return(SideRight)            
    def crop(self,nameFile):
          img  = cv2.imread(nameFile) 

          y = img.shape[0]
          x = img.shape[1] 
          #print x,y
          x=x-1
          y=y-1
          #botton
          for i in range(0,5000):
            
            #print img[(y-i),x/1.5] 
            #print img[(y-i),x/1.2] 
               
            if(img[(y-i),(x/1.7)][0]==0 and img[(y-i),(x/1.4)][0]==0):
              #img[(y-i),x/1.7] =[0,255,0]
              #img[(y-i),x/1.4] =[0,255,0]
              #print "YB=",y-i
              YB=y-i
              break
            #img[(y-i),x/1.7] =[0,255,0]
              #img[(y-i),x/1.4] =[0,255,0]
          #Top
          for i in range(0,5000):
            
            #print img[(y-i),x/1.5] 
            #print img[(y-i),x/1.2] 
               
            if(img[(i),(x/1.7)][0]==0 and img[(i),(x/1.4)][0]==0):
              #img[(i),x/1.7] =[0,255,0]
              #img[(i),x/1.4] =[0,255,0]
              #print "YT=",i 
              YT=i
              break
            #img[(i),x/1.7] =[0,255,0]
              #img[(i),x/1.4] =[0,255,0]

          #cv2.imwrite('image/crop_top_down_s.png',img) 
          pic1 = img[YT-2:YB, None:None]
          #cv2.imwrite('image/crop_top_down.png',pic1)
          pic=pic1 
          SR=self.SideRight(pic)
           
          picr,SideL,pic=self.SideLeft(SR,pic)
          self.term_exam(picr,SideL,(YB-YT))
          cv2.imwrite('image/crop_fianal.png',pic) 
          self.Fcode(picr,YB-YT,SideL)
          code=self.Detect_code_Student(SR-SideL,picr,YB-YT)
          #print "SR=",SR
          #print "SL=",SideL
          return pic,code
      
    def Fcode(self,pic,BT,SideLeft ):
          y = pic.shape[0]-1
          x = pic.shape[1]-1
          #print "YB-YT=",BT
          size=((BT)*32)/100
          #print  ((BT)*10)/100
          

          for i in range(0,size):
              pic[y-i,SideLeft]=[255,0,0]
          #print y-i

          #cv2.imwrite('image/Fcode.png',pic)
          pic_to = pic[y-i:y+1, None:SideLeft-5] 
            
          #cv2.imwrite('image/Fcode2.png',pic)
          #print "x=",x
          q=x-SideLeft
       
          sizeL=((q)*36)/100
         
          #print sizeL
          #for i in range(0,int(sizeL)):
              #pic[y/1.5,SideLeft-i]=[255,0,0]
          #print SideLeft-i
          L=SideLeft-i


          sizeR=((q)*6)/100
          #print sizeR
          #for i in range(0,int(sizeR)):
              #pic[y/1.3,SideLeft-i]=[255,0,0]
          #print SideLeft-i
          R=SideLeft-i

          pic = pic_to[None:None, L:R]
          #cv2.imwrite('image/Fcode.png',pic)
          ####################################
    def Detect_code_Student(self,size,Img,BT):
              y = Img.shape[0]-1
              x = Img.shape[1] 
              #29.7,26.7,23.7,20.7,17.5,14.4,11.3,8.1,5,2

              listRow=[29.7,26.7,23.7,20.7,17.5,14.4,11.3,8.1,5,2]
               
              listColu=[33.9,30.2,26.5,22.9,19.1,15.5,11.7,8]
              
              #8 ,11.7,15.5,19.1,22.9,26.5,30.2,33.9
              #33.9,30.2,26.5,22.9,19.1,15.5,11.7,8
              list_code=[]
              num=1
              for k in range(len(listRow)):
                  BB=int(((BT)*listRow[k])/100)
                  # print "            ",BB,"   ",listRow[k]

                  #BT=int(((BT)*29)/100)
               
                  for j in range(len(listColu)):
                      size_m=int(((size)*listColu[j])/100)
                      
                      for i in range(0,size_m):
                         pass   
                         # Img[y-(j*2),(x-size)-i]=[255,0,0]
                      #cv2.putText(Img, str(num),(int((x-size)-i),y-BB), font, 1,(0,255,0),2)
                      #print int((x-size)-i),y-BB
                      list_code.append((int((x-size)-i),y-BB))
                      num=num+1
                      #cv2.circle(Img,(int( (x-size)-i),y-BB),2,(0,255,255),3) 
              
              list_case=[]
              i=0
              for k in range(0,10):
                     #print  list_code[i]
                     list_case.append((list_code[i],list_code[i+1],list_code[i+2],list_code[i+3],list_code[i+4],list_code[i+5],list_code[i+6],list_code[i+7]))
                     
                     #print "i=",i
                     i=i+8
                     #cv2.putText(Img, str(k),list_code[k], font, 1,(0,255,0),2)
              list_casec=[]
              k=0
                

              for k in range(0,8) :
                  list_casec.append(( list_case[0][k] ,list_case[1][k],list_case[2][k],list_case[3][k],list_case[4][k],list_case[5][k],list_case[6][k],list_case[7][k],list_case[8][k],list_case[9][k]))
                  #list_casec.append("1")
                  #print  list_case[i][0],list_case[i+1][0],list_case[i+2][0],list_case[i+3][0],list_case[i+4][0],list_case[i+5][0],list_case[i+6][0] 
                   
              list_code_final=[]
              for l in range(0,8) :  
                  list_i=[]      
                  for i in range(len(list_casec[l])):
                      #print list_casec[l][i]
                      
                       
                      #cv2.circle(Img,(list_casec[0][i][0]-7,list_casec[0][i][1]),1,(255,0,255),3) 
                      #cv2.circle(Img,(list_casec[0][i][0]+7,list_casec[0][i][1]),1,(255,0,255),3) 
                      #cv2.circle(Img,(list_casec[0][i][0],list_casec[0][i][1]-7),1,(255,0,255),3) 
                      #cv2.circle(Img,(list_casec[0][i][0],list_casec[0][i][1]+7),1,(255,0,255),3) 
                      if(Img[list_casec[l][i][1],list_casec[l][i][0]][0]==0 and Img[list_casec[l][i][1],list_casec[l][i][0]-7][0]==0 and Img[list_casec[l][i][1],list_casec[l][i][0]+7][0]==0 and Img[list_casec[l][i][1]+7,list_casec[l][i][0]][0]==0 and Img[list_casec[l][i][1],list_casec[l][i][0]-7][0]==0):
                          cv2.circle(Img,(list_casec[l][i][0]-7,list_casec[l][i][1]),1,(255,0,255),3) 
                          cv2.circle(Img,(list_casec[l][i][0]+7,list_casec[l][i][1]),1,(255,0,255),3) 
                          cv2.circle(Img,(list_casec[l][i][0],list_casec[l][i][1]+7),1,(255,0,255),3) 
                          cv2.circle(Img,(list_casec[l][i][0],list_casec[l][i][1]-7),1,(255,0,255),3) 
                          cv2.circle(Img,(list_casec[l][i][0],list_casec[l][i][1]),1,(255,0,255),3) 
                          list_i.append((i))
                          #print i
                  list_code_final.append(list_i)
                  #print "##################"
              #print list_code_final
              #cv2.imwrite('image/Detect_code_Student.png',Img) 
              return list_code_final
    def code_convese(self,code):
            code_list=[]
             
            for i in range(len(code)):
                   
                  if(code[i]!=[]and len(code[i])==1):
                       
                      code_list.append(str(code[i][0]))
                  else:
                      code_list.append('X')
                       

             
            #print num
            #print code_list
               
            #code_list.append(str(code[0][0]))
       
            
            ans = ''.join(code_list)
                           
            return ans
    def term_exam(self,pic,SideL,Hight):
            try:
              #print SideL
              sizey=((Hight)*9.4)/100
              
              
              y = pic.shape[0] 
              x = pic.shape[1]
              cv2.circle(pic,( int(SideL)  , int(sizey)),5,(255,0,0),5)
              
              ######################SET 
              #print "V:",x,y 
              List_term_set=[]
              List_term_term=[]
              
              List_term=[34.8,26.48,18.1,10]
              for i in range(len(List_term)):
                sizex=((x-SideL)*List_term[i])/100
                
                List_term_set.append((SideL-sizex,sizey))
                #cv2.circle(pic,( int(SideL-sizex)  , int(sizey)),6,(255,0,0),6)
              
              sizey=((Hight)*13.3)/100
              #cv2.circle(pic,( int(SideL)  , int(sizey)),5,(255,0,0),5)
              #######################TERM
              List_term=[34.9  ,17.9 ]
              for i in range(len(List_term)):
                sizex=((x-SideL)*List_term[i])/100
                #print pic[int(SideL-sizex), int(sizey)]
                
                List_term_term.append((SideL-sizex,sizey))
                #cv2.circle(pic,( int(SideL-sizex)  , int(sizey)),6,(255,0,0),6)
              #print List_term_set
              #print List_term_term

              List_term_final=[]
              list_set_final=[]
              for i in range(len(List_term_set)):
                 #print  pic[List_term_set[i][1],List_term_set[i][0]]
                 if(pic[List_term_set[i][1],List_term_set[i][0]][0]==0 and pic[List_term_set[i][1],List_term_set[i][0]+2][0]==0):
                      #print i+1
                      list_set_final.append(i+1)
              for i in range(len(List_term_term)):
                 #print  pic[List_term_set[i][1],List_term_set[i][0]]
                 if(pic[List_term_term[i][1],List_term_term[i][0]][0]==0 and pic[List_term_term[i][1],List_term_term[i][0]+2][0]==0):
                      # print i+1  
                      List_term_final.append(i+1)        
              #print "Term=",List_term_final
              #print "Set=",list_set_final
              self.List_term_main=List_term_final
              self.List_Set_main=list_set_final
              cv2.imwrite('image/test.png',pic) 
            except:
               
              print "Don't Detect set and term"
    def percent(self,main,per):
          return int((main*per)/100)
    def NewInspector(self,img):
              Y = img.shape[0] 
              X = img.shape[1]

              #print X,Y
            
              List_all=[]    
                   
              CY=[13.7,16.5,19.5,22.4,25.3,28.2,30.9,33.8,36.7,39.5,42.4,45.4,48.3,51.1,54.1,57,59.9,62.7,65.5,68.4,71.3,74.1,77,80,82.9,85.8,88.8,91.7,94.6     ,97.5]
              CX=[7.4,11.3,15.2,19.1,22.9,  32.2,36.2,40,43.8,47.7    ,57,60.9,64.7,68.5,72.5    ,81.9,85.7,89.6,93.4,97.3]
              for j in range(len(CY)):
                for i in range(len(CX)):
                     
                    #cv2.circle(img,( self.percent(X,CX[i]), self.percent(Y,CY[j])),6,(255,0,0),6)
                    List_all.append((self.percent(X,CX[i]),self.percent(Y,CY[j])))
              #List_all.sort()
              #for i in range(len(List_all)):
                  #cv2.circle(img,( List_all[i][0] ,List_all[i][1]  ),6,(255,0,0),6)
                  #pass
                  #cv2.putText(img, str(i),(List_all[i]), self.font, 0.5,(0,255,0),2)
              
              List_main=[]
              #1#########################################
              c1=0
              c2=1
              c3=2
              c4=3
              c5=4
              for i in range(30):
                #print c1,c2,c3,c4,c5
                List_main.append((c1,c2,c3,c4,c5))
                c1=c1+20
                c2=c2+20
                c3=c3+20
                c4=c4+20
                c5=c5+20
              #2#########################################
              c1=5
              c2=6
              c3=7
              c4=8
              c5=9
              for i in range(30):
                #print c1,c2,c3,c4,c5
                List_main.append((c1,c2,c3,c4,c5))
                c1=c1+20
                c2=c2+20
                c3=c3+20
                c4=c4+20
                c5=c5+20
              #3#########################################
              c1=10
              c2=11
              c3=12
              c4=13
              c5=14
              for i in range(30):
                #print c1,c2,c3,c4,c5
                List_main.append((c1,c2,c3,c4,c5))
                c1=c1+20
                c2=c2+20
                c3=c3+20
                c4=c4+20
                c5=c5+20
              #4#########################################
              c1=15
              c2=16
              c3=17
              c4=18
              c5=19
              for i in range(30):
                #print c1,c2,c3,c4,c5
                List_main.append((c1,c2,c3,c4,c5))
                c1=c1+20
                c2=c2+20
                c3=c3+20
                c4=c4+20
                c5=c5+20


              #self.Print_List_Type_Row(List_main)
              list_final=[]
              List_Ku=[]
              size=6
              for i in range(len(List_main)):
                  #print  "Num:",i+1,":"
                  #print  List_all[List_main[i][0]]
                  cv2.circle(img,(List_all[List_main[i][0]]),1,(255,0,0),1)
            
                  if(img[List_all[List_main[i][0]][1],List_all[List_main[i][0]][0]][0]==0 and img[List_all[List_main[i][0]][1]+size,List_all[List_main[i][0]][0]][0]==0 and img[List_all[List_main[i][0]][1]-size,List_all[List_main[i][0]][0]][0]==0 and img[List_all[List_main[i][0]][1],List_all[List_main[i][0]][0]+size][0]==0 and img[List_all[List_main[i][0]][1],List_all[List_main[i][0]][0]-size][0]==0):
                      
                      List_Ku.append((1))
                  if(img[List_all[List_main[i][1]][1],List_all[List_main[i][1]][0]][0]==0  and img[List_all[List_main[i][1]][1]+size,List_all[List_main[i][1]][0]][0]==0  and img[List_all[List_main[i][1]][1]-size,List_all[List_main[i][1]][0]][0]==0  and img[List_all[List_main[i][1]][1],List_all[List_main[i][1]][0]+size][0]==0  and img[List_all[List_main[i][1]][1],List_all[List_main[i][1]][0]-size][0]==0):
                    
                      List_Ku.append((2))
                  if(img[List_all[List_main[i][2]][1],List_all[List_main[i][2]][0]][0]==0 and img[List_all[List_main[i][2]][1]+size,List_all[List_main[i][2]][0]][0]==0 and img[List_all[List_main[i][2]][1]-size,List_all[List_main[i][2]][0]][0]==0  and img[List_all[List_main[i][2]][1],List_all[List_main[i][2]][0]+size][0]==0  and img[List_all[List_main[i][2]][1],List_all[List_main[i][2]][0]-size][0]==0):
                      
                      List_Ku.append((3))
                  if(img[List_all[List_main[i][3]][1],List_all[List_main[i][3]][0]][0]==0  and img[List_all[List_main[i][3]][1]+size,List_all[List_main[i][3]][0]][0]==0 and img[List_all[List_main[i][3]][1]-size,List_all[List_main[i][3]][0]][0]==0 and img[List_all[List_main[i][3]][1],List_all[List_main[i][3]][0]+size][0]==0 and img[List_all[List_main[i][3]][1],List_all[List_main[i][3]][0]-size][0]==0):
                    
                     List_Ku.append((4))
                  if(img[List_all[List_main[i][4]][1],List_all[List_main[i][4]][0]][0]==0  and img[List_all[List_main[i][4]][1]+size,List_all[List_main[i][4]][0]][0]==0  and img[List_all[List_main[i][4]][1]-size,List_all[List_main[i][4]][0]][0]==0  and img[List_all[List_main[i][4]][1],List_all[List_main[i][4]][0]+size][0]==0  and img[List_all[List_main[i][4]][1],List_all[List_main[i][4]][0]-size][0]==0 ):
                   
                     List_Ku.append((5))
                  list_final.append(List_Ku)
                  List_Ku=[]
                  #cv2.circle(img,(List_all[List_main[i][0]]),6,(255,0,0),6)
              
              cv2.imwrite('image/YYY.png',img)
              return list_final
    def Process(self,FileName):
          lsit_answer=[]
          try:
            #FileName='image/input/input.png'
            img,code=self.crop(FileName)
            #print "1:",code



            code=self.code_convese(code)
            cv2.imwrite('image/submain/{:>05}.png'.format(code),img) 
            
            list_final=self.NewInspector(img)
            #print self.Print_List_Type_Row(list_final) 
            #print code
            #print "SET:",self.List_Set_main
            #print "TERM:",self.List_term_main



            #List_NameFilE=self.flax_f(img,code)
            #lsit_answer=self.Inspector_final(List_NameFilE,code)
            
            return code,list_final,self.List_Set_main,self.List_term_main
          except:
                return "Detect Error"
        #####################################First_Crop_Side#################################
    def Inspector_final(self,List_NameFilE,code):
            List_NameFile=List_NameFilE
            list_final=[]
         
            for i in range(len(List_NameFile)):
              
                #print List_NameFile[i]
                List_Ans=[]
                print List_NameFile[i]
                List_Ans= self.Select_Case("image/sub/"+List_NameFile[i],code) 
                #print List_Ans
                for j in range(len(List_Ans)):
                  #print List_Ans[j][1]
                  list_final.append((List_Ans[j][1]))
            #self.Print_List_Type_Row(list_final)
            return list_final
     
       
        # ####################################crop_TopAndBut_main#################################
        #def ProcessFlax():
    def flax_f(self,fileimg,code):
        list_flax=[]
        img  =  fileimg
        y = img.shape[0]
        x = img.shape[1] 
     
        """    cv2.imwrite('image/flax/f1.png',self.fine_size_main_final(self.flax_size_main(x,y,5,75,img))) 
            cv2.imwrite('image/flax/f2.png',self.fine_size_main_final(self.flax_size_main(x,y,30,50,img))) 
            cv2.imwrite('image/flax/f3.png',self.fine_size_main_final(self.flax_size_main(x,y,55,25,img))) 
            cv2.imwrite('image/flax/f4.png',self.fine_size_main_final(self.flax_size_main(x,y,80, 0,img))) 
        """


        list_flax.append(self.fine_size_main_final(self.flax_size_main(x,y,5,75,img)))
        list_flax.append(self.fine_size_main_final(self.flax_size_main(x,y,30,50,img))) 
        list_flax.append(self.fine_size_main_final(self.flax_size_main(x,y,55,25,img)) )
        list_flax.append(self.fine_size_main_final(self.flax_size_main(x,y,80, 0,img)) )
        List_NameFilE=[]

        for i in range(len(list_flax)):
          name=str(code)+"_F"+str(i)
          cv2.imwrite('image/sub/{:>05}.png'.format(name) ,list_flax[i])
          List_NameFilE.append(name+".png")
        #print List_NameFilE
        return List_NameFilE
        #####################################crop_TopAndBut_main#################################
         
     
     
    #print m.List_Set_main
    #print m.List_term_main
     


    """def task1():
        m=MainProcess(0)
        code,list_a,Set,Term=m.Process('input.png')
    def task2():
        m=MainProcess(0)
        code,list_a,Set,Term=m.Process('input.png')

    if __name__ == "__main__":
     
      
      for i in range(10):
          p = multiprocessing.Process(target=task1 )
          p.start()
     """
        
        
     