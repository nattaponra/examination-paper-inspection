import cv2
import numpy as np
import math 
 




class TR(object):
 	"""docstring for TR"""
 	def __init__(self, arg):
 		super(TR, self).__init__()
 		self.arg = arg
 		
		

	def Threshold(self,img):
	 	img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	 	thresh = 226
		im_bw = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]
		"""		img_  = img
		mask   = img
	  
		# Convert BGR to HSV
		hsv = cv2.cvtColor(img_, cv2.COLOR_BGR2HSV)
	   
		# define range of blue color in HSV
		     
		hsv_lower = cv2.cvtColor(np.uint8([[[255,180,0 ]]]),cv2.COLOR_BGR2HSV)
		hsv_upper = cv2.cvtColor(np.uint8([[[255,245,0 ]]]),cv2.COLOR_BGR2HSV)
		     
		 
		lower_blue = np.array([0,0,170], dtype=np.uint8)
		upper_blue = np.array([255 ,105,255], dtype=np.uint8)

		    # Threshold the HSV image to get only blue colors
		mask = cv2.inRange(hsv, lower_blue, upper_blue)
		 
		    # Bitwise-AND mask and original image
		res = cv2.bitwise_and(img_,img_, mask= mask)
	 
		 
		#cv2.imshow('res',res)
		#cv2.imwrite('out.png',mask)"""
		return im_bw


	def Find(self,img):

		Y = img.shape[0]-1
		X = img.shape[1]-1
		print X,Y
		for i in range(3000):
			if(img[i,X/1.5][0]==0):
				#cv2.circle(img,(int(X/1.5),i),5,(0,255,0),2)
				y1=i
				break
		for i in range(3000):
			if(img[i,X/1.2][0]==0):
				#cv2.circle(img,(int(X/1.2),i),5,(0,255,0),2)
				y2=i
				break


		print math.fabs(y2-y1)
		#cv2.imwrite('Find.png',img)
		if(math.fabs(y2-y1)<2):
			return "NoRotate"
		else:
			return "Rotate"
	def rotateImage(self,image, angle):

	 
	  image_center = tuple(np.array(image.shape)/2)
	  rot_mat = cv2.getRotationMatrix2D(image_center,angle,1.0)
	  result = cv2.warpAffine(image, rot_mat, image.shape,flags=cv2.INTER_LINEAR)
	  
	  return result
	def autoRotate(self,img):
			Y = img.shape[0]-1
			X = img.shape[1]-1
			print X,Y
			y=0
			k=0
			right=0
			left=0
			side="None"
		 	for j in range(10):
				for i in range(X):
					if(img[y,i][0]==0):
						print y,i
						print X/2
						if(i<(X/2)):
							side="right"
							right=i
						elif(i>(X/2)):
							side="left"
							left=i
						#cv2.circle(img,(i,y),5,(0,255,0),2)
						k=1
						break
					#img[y,i]=[255,255, 0]
					if(k==1):
						break
				y=y+10

			
			print  side
			if(side=="left"):
				for i in range(3000):
					if (img[Y-i,X/1.1][0]==0):
						y2=Y-i
					 	break
					#img[Y-i,X/1.1]=[255,0,0]
			    
				for i in range(3000):
					if (img[Y-i,(X/1.1)-(X*10)/100  ][0]==0):
						y1=Y-i
					 	break
					#img[Y-i,(X/1.1)-(X*10)/100  ]=[255,0,0]		
				#cv2.imwrite('autoRotate.png',img)
				A=math.fabs(y2-y1)
				B=math.fabs((X/1.7)-((X/1.7)-(X*10)/100))
				#print B
				C=math.sqrt(math.pow(A, 2)+math.pow(B, 2))
				#print C
				print  math.degrees(math.atan(A/B))
				return math.degrees(math.atan(A/B)),"L"

			elif(side=="right"):
				for i in range(3000):
					if (img[Y-i,X/1.7][0]==0):
						y2=Y-i
					 	break
					#img[Y-i,X/1.7]=[255,0,0]
			    
				for i in range(3000):
					if (img[Y-i,(X/1.7)-(X*10)/100  ][0]==0):
						y1=Y-i
					 	break
					img[Y-i,(X/1.7)-(X*10)/100  ]=[255,0,0]		
			 
				A=math.fabs(y2-y1)
				B=math.fabs((X/1.7)-((X/1.7)-(X*10)/100))
				print B
				C=math.sqrt(math.pow(A, 2)+math.pow(B, 2))
				print C

		        print math.degrees(math.atan(A/B))
	    	 	return math.degrees(math.atan(A/B)),"R"
	    

		 
		
	def floodFill_Rotate(self,img):
	          
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
	        
	        #cv2.imwrite('floodFill.png',img)
	        return img


	def autoCropRotate(self,img):
			top=0
			but=0
	 		Y = img.shape[0]-1
			X = img.shape[1]-1
			#top
			for i in range(3000):

				if img[i,X/2][0]==0:
					top=i
					#cv2.circle(img,(i,X/2),5,(0,255,0),2)
					break
				#img[i,X/2]=[255,0,0]
			#But
			for i in range(3000):

				if img[Y-i,X/2][0]==0:
					but=Y-i
					#cv2.circle(img,(Y-i,X/2),5,(0,255,0),2)
					break
				#img[Y-i,X/2]=[255,0,0]		 
			img=img[top-50:but+50, 0:X]
	 	 	 
	 		Y = img.shape[0]-1
			X = img.shape[1]-1
			print X,Y
			#left
			#####################################################
 	
			for i in range(3000):

				if img[Y/3,i][0]==0:
					L1=i
					#cv2.circle(img,(Y/3,i),5,(0,255,0),2)
					break
				#img[Y/3,i]=[255,0,0]	
			for i in range(3000):

				if img[Y/2,i][0]==0:
					L2=i
					#cv2.circle(img,(Y/2,i),5,(0,255,0),2)
					break
				#img[Y/2,i]=[255,0,0]
			cv2.imwrite('TR/Ts.png'  ,img)	 
			##########################################
			#Right
			for i in range(3000):

				if img[Y/2,X-i][0]==0:
					R=X-i
					#cv2.circle(img,(Y/2,X-i),5,(0,255,0),2)
					break
				#img[Y/2,X-i]=[255,0,0]		 

			L=self.L(L1,L2)
	 		img=img[0:Y, L-50:R+50]
		    
			return img
	def L(self,L1,L2):
			if(L1<L2):
				L=L1
			elif(L1>L2):
				L=L2
			else:
				L=L1

			return L
	def cropNormal(self,img):
			img=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
			top=0
			but=0
	 		Y = img.shape[0]-1
			X = img.shape[1]-1
			#top
			for i in range(3000):

				if img[i,X/2][0]==0:
					top=i
					#cv2.circle(img,(i,X/2),5,(0,255,0),2)
					break
				#img[i,X/2]=[255,0,0]
			
			#But
			for i in range(3000):

				if img[Y-i,X/2][0]==0:
					but=Y-i
					#cv2.circle(img,(Y-i,X/2),5,(0,255,0),2)
					break
				#img[Y-i,X/2]=[255,0,0]		 
			img=img[top-50:but+50, 0:X]
	 	 	
	 		Y = img.shape[0]-1
			X = img.shape[1]-1
			print X,Y
			L=0
			R=0
		     

			 
			#Right
			for i in range(0,3000):

				if img[Y/2,X-i][0]==0:

					R=X-i
					cv2.circle(img,(Y/2,X-i),5,(0,255,0),2)
					break
				 

				    #img[Y/2,X-i]=[255,0,0]		

			for i in range(0,3000):
				 
				if(img[i,X/2][0]==0):
					L=i
					break
				 
					#img[i,X/2]=[255,0,0]	
			img=img[0:Y, L-50:R+50]
	 
		   	return img  
			 




	def Main_Rotate(self,img,ID):
		

		 
		img=self.Threshold(img)
		img=cv2.cvtColor(img,cv2.COLOR_GRAY2RGB)
		cv2.imwrite('TR/T{:>}.png'.format(ID),img)
		img=cv2.imread('TR/T{:>}.png'.format(ID))
		 
		if self.Find(img)=="Rotate":
		    
		   angle,side= self.autoRotate(img)
		   print angle ,side
		   if side=="R":
			   img=cv2.imread('TR/T{:>}.png'.format(ID),0) 
			   
			   cv2.imwrite('TR/autoRotate{:>}.png'.format(ID),self.floodFill_Rotate(self.rotateImage(img,angle)))
			   img=cv2.imread('TR/autoRotate{:>}.png'.format(ID))
			   #cv2.imwrite('autoCropRotate.png',autoCropRotate(img))
			   return self.autoCropRotate(img)

		   elif side=="L":
			   img=cv2.imread('TR/T{:>}.png'.format(ID),0) 
			   cv2.imwrite('TR/autoRotate{:>}.png'.format(ID),self.floodFill_Rotate(self.rotateImage(img,-angle)))
			   img=cv2.imread('TR/autoRotate{:>}.png'.format(ID))
			   #cv2.imwrite('autoCropRotate.png',autoCropRotate(img))	
			   return self.autoCropRotate(img)

		else:
		   return "NO"

	def ThresholdAndRotate(self,img,Id):
		#img=cv2.imread('Rright25.png')

		if(self.Main_Rotate(img,Id)=="NO"):
			 
				img=self.Threshold(img)
				#cv2.imwrite('final.png',img)
				#cv2.imwrite('final.png',cropNormal(img))
				#print cropNormal(img)
				return self.cropNormal(img)
		else:

			#cv2.imwrite('final.png',Threshold(Main_Rotate(img)))
	  		return self.Threshold(self.Main_Rotate(img,Id))

"""M=TR(0)
img=cv2.imread('F:\15-JAN-2015\\154007.BMP')

cv2.imwrite('final.png',M.ThresholdAndRotate(img,"1"))"""