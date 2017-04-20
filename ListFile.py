import cv2
 
import math 
import os
class ListFile(object):
	"""docstring for ListFile"""
	def __init__(self, arg):
		super(ListFile, self).__init__()
		self.arg = arg
	def testfile(self):	
		img=cv2.imread('image/input/input.png')
		for i in range(0,100):
			cv2.imwrite('image/input/{:>05}.png'.format(i+1),img)
	def listfile(self,directory): 	 
   
		List_pp=[]     
		addList=[] 
		if directory:
		            items = os.listdir(directory)
		            newlist = []
		            for names in items:
		                if names.endswith(".png"):
		                    newlist.append(names)
		            #print newlist
		            for i in range(len(newlist)):
		                print newlist[i]
		                List_pp.append(newlist[i])
		#print List_pp
		return List_pp