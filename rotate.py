import cv2
import numpy as np
import math 
import cv
 
def floodFill_Rotate(FilePath):
        img = cv2.imread(FilePath)
        h, w = img.shape[:2]
        mask = np.zeros((h+2, w+2), np.uint8)
        #LT
        cv2.floodFill(img, mask, (2,2), (255, 255, 255), (10,)*3, (200,)*3, 4)
        
        #RT
        cv2.floodFill(img, mask, (w-2,2), (255, 255, 255), (10,)*3, (200,)*3, 4) 

        #BR
        cv2.floodFill(img, mask, (w-2,h-2), (255, 255, 255), (10,)*3, (200,)*3, 4) 
        
        #BR
        cv2.floodFill(img, mask, (2,h-2), (255, 255, 255), (10,)*3, (200,)*3, 4) 
        
        cv2.imwrite('floodFill.png',img)
        return img
 


def rotate(namefile,Angle,Type ):
	img = cv2.imread(namefile,0)
	rows = img.shape[0]
	cols = img.shape[1]
	if(Type=="R"):#Right
		#print rows,cols
		M = cv2.getRotationMatrix2D((cols/2,rows/2),-Angle,1)
		dst = cv2.warpAffine(img,M,(cols,rows))
		cv.Flip(dst, dst=None, flipMode=1)  
	 	cv2.imwrite('ImgTest/rotate.png',dst)
	 	return dst
	elif(Type=="L"):#Right
 		#print rows,cols
		M = cv2.getRotationMatrix2D((cols/2,rows/2),Angle,1)
		dst = cv2.warpAffine(img,M,(cols,rows))
		#cv.Flip(dst, dst=None, flipMode=1)  
	 	cv2.imwrite('ImgTest/rotate.png',dst)
	  
	 	return dst



def Check_rotate(FileName):
	img = cv2.imread(FileName)
	IMG=img
	y = img.shape[0]
	x = img.shape[1]
	print x,y
	print "P=",(x*10)/100
	Y=y-1
    
	Start= (x/2)+(x*10)/100 
	End= ((x/2)+(x*15)/100) 

		 
		 
	 
	################################
	for i in range(0,1000):
			if(img[Y-i,Start][0]==255):
			  img[Y-i,Start]=(0,255,0)
			if(img[Y-i,Start][0]==0 and img[(Y-i)-1,Start][0]==0 and img[(Y-i)-3,Start][0]==0):
	 			cv2.circle(img,(Start,Y-i),2,(0,0,255),3)
	            
	 			cv2.imwrite('ImgTest/rotate1.png',img)
	 			print "Start=", "Y=",Y-i,"X=",Start
	 			Start_Y=Y-i
	 			Start_X=Start
				break
	         
	         
	for i in range(0,1000):
			if(img[Y-i,End][0]==255):
			  img[Y-i,End]=(0,255,0)
			if(img[Y-i,End][0]==0 and img[(Y-i)-1,End][0]==0 and img[(Y-i)-1,End][0]==0):
	 			cv2.circle(img,(End,Y-i),2,(0,0,255),3)
	 			 
	 			cv2.imwrite('ImgTest/rotate1.png',img)
	 			print "End=","Y=",Y-i,"X=",End
	 			End_Y=Y-i
	 			End_X=End
	 			break

	if(Start_Y!=End_Y):

		 
		print "Y=",math.fabs(Start_Y-End_Y)
		Y=math.fabs(Start_Y-End_Y)

		print "X=",End-Start
		X=End-Start
		 
		 
		print "R=",math.sqrt(math.pow(Y, 2)+math.pow(X, 2))
		R=math.sqrt(math.pow(Y, 2)+math.pow(X, 2))
		print 
		#print math.asin(0.71)
		#print Y/R
		print  math.degrees(math.atan(Y/X)) 

		print Start_Y,End_Y
		if(Start_Y<End_Y):
			 
			return 'L',math.degrees(math.atan(Y/X)) 
		elif(Start_Y>End_Y):
			 
			return 'R',math.degrees(math.atan(Y/X)) 

		

	else:
		print "Yes"
		return IMG,None
def Main(NameFile):
	direction,A=Check_rotate(NameFile)

	#print "direction:",direction ,A
	if(A!=None):
	 	img=rotate(NameFile,A,direction)
	 	img=floodFill_Rotate('ImgTest/rotate.png')
	 	#cv2.imwrite('image/input/final.png',img)
		return img
	return direction

cv2.imwrite('ImgTest/final.png',AutoRotate('image/input/input_rotate.png'))