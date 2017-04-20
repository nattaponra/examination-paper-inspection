import os,sys


class Difficulty(object):
	"""docstring for Difficulty"""
	LIST_Number=[]
	List_count=[]
	List_Diffic=[]

	#print List_count
	
	def __init__(self, arg):
		super(Difficulty, self).__init__()
		self.arg = arg
		 


	def CheckAnswer(self,Str):
		#print str(Str).replace(",", "").replace("'", "").replace("(", "").replace(")", "") .replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("0", "").strip()
			
		if str(Str).replace(",", "").replace("'", "").replace("(", "").replace(")", "") .replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("0", "").strip()=="Yes":
			return True
		else:
			return False

	def main(self,Key,num):
			self.LIST_Number=[]
			self.List_count=[]
			self.List_Diffic=[]

			print "|||||||||||||||||||||||",num
			for i in range(num):
				self.LIST_Number.append(0.0)
				self.List_count.append(0)
				self.List_Diffic.append("")

			Start=0
			for i in range(num):
				self.List_count[i]=0
				self.LIST_Number[i]=0.0
			 
				self.List_Diffic[i]=""
			Dir=""
			file = open("setting/SelectKey.txt" , "r")
			list_key=file.readlines()
			file.close() 
			file = open("setting/format_tab2_down.txt" , "r")
			list_c=file.readlines()
			file.close() 

			if(list_key[0].strip()=="single"): #single key
				 
				if list_c[0].strip()=="No":
					print "single key & 1C"
					Dir="inspected\SC\onekey"
					Start=9
				elif  list_c[0].strip()=="Yes":

					if list_c[2].strip()=="1Yes" and list_c[8].strip()=="1No" and list_c[14].strip()=="1No":
						print "single key & 1MC"
						Dir="inspected\M1\onekey"
						Start=9
					if list_c[2].strip()=="1Yes" and list_c[8].strip()=="1Yes" and list_c[14].strip()=="1No":
						print "single key & 2MC"
						Dir="inspected\M2\onekey"
						Start=11
					if list_c[2].strip()=="1Yes" and list_c[8].strip()=="1Yes" and list_c[14].strip()=="1Yes":
						print "single key & 3MC"
						Dir="inspected\M3\onekey"
						Start=12
			elif(list_key[0].strip()=="multiple"):

				if list_c[0].strip()=="No":
					print "Multi key & 1C key=",Key
					Dir="inspected\SC\k{:>}".format(Key)
					Start=9
				elif  list_c[0].strip()=="Yes":

					if list_c[2].strip()=="1Yes" and list_c[8].strip()=="1No" and list_c[14].strip()=="1No":
						print "Multi key & 1MC key=",Key
						Dir="inspected\M1\k{:>}".format(Key)
						Start=9
					if list_c[2].strip()=="1Yes" and list_c[8].strip()=="1Yes" and list_c[14].strip()=="1No":
						print "Multi key & 2MC key=",Key
						Dir="inspected\M2\k{:>}".format(Key)
						Start=11
					if list_c[2].strip()=="1Yes" and list_c[8].strip()=="1Yes" and list_c[14].strip()=="1Yes":
						print "Multi key & 3MC key=",Key
						Dir="inspected\M3\k{:>}".format(Key)
						Start=12
			print Dir
	 		self.LI=os.listdir(Dir) 
	 		print num
			for i in range(len(self.LI)):
				print Dir+"\\"+self.LI[i]
				file = open(Dir+"\\"+self.LI[i], "r")
				list_answer=file.readlines() 
 				file.close
				for j in range(Start,num+Start):
						 
						if self.CheckAnswer(str(list_answer[j]))==True:
 							self.List_count[j-Start]=self.List_count[j-Start]+1								 	
						
			for i in range(len(self.List_count)):
 						 
						self.LIST_Number[i]=self.List_count[i]/float(len(self.LI))
					 
			for i in range(len(self.LIST_Number)):

						
						                                    if(self.LIST_Number[i]<0.20):
						                                        #print 'vc'
						                                        self.List_Diffic[i]="vc"
						                                    elif(self.LIST_Number[i]>=0.20 and self.LIST_Number[i]<=0.39):
						                                        #print 'c'
						                                        self.List_Diffic[i]="c"
						                                    elif(self.LIST_Number[i]>=0.40 and self.LIST_Number[i]<=0.59):
						                                        #print 'm'
						                                        self.List_Diffic[i]="m"
						                                    elif(self.LIST_Number[i]>=0.60 and self.LIST_Number[i]<=0.79):
						                                        #print 'e'    
						                                        self.List_Diffic[i]="e"
						                                    elif(self.LIST_Number[i]>=0.80 and self.LIST_Number[i]<=1.0):
						                                        #print 've'
						                                        self.List_Diffic[i]="ve"

		 	print sum(self.LIST_Number)/num
			return self.List_Diffic,self.List_count,len(self.LI), sum(self.LIST_Number)/num,self.LIST_Number
						
		   

"""M=Difficulty(0)
A,B,C,D,u=M.main(4,10) """
 
 