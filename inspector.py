import os 
import csv
import sys
class Inspector(object):
	num=0
	L=[]
 
	"""docstring for Inspector"""
	def __init__(self, arg):
		super(Inspector, self).__init__()
		self.arg = arg
		

	def Text2List(self,NameFile):
		List_Main=[]
		file = open(NameFile, "r")           
		list_setting2=file.readlines()
		file.close()
		List_main=[]
		for i in range(len(list_setting2)):
			#print list_setting2[i].replace("[", " ").replace("]", " ");
			List_main.append(list_setting2[i].replace("[", " ").replace("]", " "))


		for i in range(4,self.num+4):
			#print  List_main[4]  
			#print List_main[i][4] 
			#print List_main[i][7] 
			#print List_main[i][10] 
			#print List_main[i][13] 
			List_Main.append([int(List_main[i][1]),int(List_main[i][4]),int(List_main[i][7]),int(List_main[i][10]),int(List_main[i][13]),])
			#print "#####################"
			if List_main[2].strip()=="":
				k=0
			else:
				k=int(List_main[2].strip())
			if List_main[3].strip()=="":
				t=0
			else:
				t=int(List_main[3].strip())
		return List_Main,List_main[0],str(List_main[1]).strip(),k ,t 
	def Create_list_Error(self):
		List=[]
		for i in range(self.num):
			List.append((i+1,"Key"))
		return List

	def FindSingleCh(self,List):
		for i in range(5):
			#print List[i]
			if int(List[i])==1:
				#print i 
				return i
				break
		return 9

	def Seclect_c(self):

			
	        file = open("setting/format_tab2_down.txt", "r")
	        format_f =file.readlines()
	        file.close()
	        self.L=[]
	        if self.Check_Type()=="C1":
		            L1=format_f[3].strip().split('-')
		            CH1=int(format_f[5].strip())
		            self.L.append((int(L1[0]),int(L1[1]),CH1))

 
 
	        elif self.Check_Type()=="C2":
		        L1=format_f[3].strip().split('-')	        	 
	        	L2=format_f[9].strip().split('-')
	        	CH1=int(format_f[5].strip())
	        	CH2=int(format_f[11].strip())

	        	self.L.append((int(L1[0]),int(L1[1]),CH1))
	        	self.L.append((int(L2[0]),int(L2[1]),CH2))

 				
	        elif self.Check_Type()=="C3":
	         
	        	L1=format_f[3].strip().split('-')
	        	L2=format_f[9].strip().split('-')
	        	L3=format_f[15].strip().split('-')
	        	CH1=int(format_f[5].strip())
	        	CH2=int(format_f[11].strip())
	        	CH3=int(format_f[17].strip())
	        	self.L.append((int(L1[0]),int(L1[1]),CH1))
	        	self.L.append((int(L2[0]),int(L2[1]),CH2))
	        	self.L.append((int(L3[0]),int(L3[1]),CH3))
 				
 				
  				

	def Check_FS(self,num):
		file = open("setting/format_tab3.txt", "r")
		list_fs=file.readlines()
		file.close()
		if list_fs[0].strip()=="No":
			return False
		L=list_fs[1].strip().split(',') 
		LIST=[]
		for i in range(len(L)):
			LIST.append(int(L[i]))
		print LIST
		for i in range(len(LIST)):
			if num==LIST[i]:
				return True
		return False

	 
	def Check_Type(self):
                file = open("setting/format_tab2_down.txt", "r")
                format =file.readlines()
                file.close()
                if (format[0].strip()=="No"):
                    return "SC"
                else:
                    if(format[2].strip()=="1Yes" and format[8].strip()=="1No" and format[14].strip()=="1No"):
                        return "C1"
                    elif(format[2].strip()=="1Yes" and format[8].strip()=="1Yes" and format[14].strip()=="1No"):
                        return "C2"
                    elif(format[2].strip()=="1Yes" and format[8].strip()=="1Yes" and format[14].strip()=="1Yes"):  
                        return "C3"

	def SingleKey_mc(self,Exam,Key,num,C):


 		
 

		List_answer=[]
		correct=0 
		incorrect=0
		illegality=0
		empty=0
		over=0
		less=0

		if self.Check_Type()=="SC":

			for i in range(num):
		 

				if int(Exam[i][0])+int(Exam[i][1])+int(Exam[i][2])+int(Exam[i][3])+int(Exam[i][4])==C:
					if self.Check_FS(i+1)==True:
						    List_answer.append((i+1,"Yes"))
						    correct=correct+1
					elif   int(Exam[i][0])==int(Key[i][0]) and int(Exam[i][1])==int(Key[i][1]) and int(Exam[i][2])==int(Key[i][2])and int(Exam[i][3])==int(Key[i][3])and int(Exam[i][4])==int(Key[i][4]):
							#print i+1,"Yes"
							List_answer.append((i+1,"Yes"))
							correct=correct+1

					else:
						    #print i+1,"No"
						    List_answer.append((i+1,"No"))
						    incorrect=incorrect+1
				elif int(Exam[i][0])+int(Exam[i][1])+int(Exam[i][2])+int(Exam[i][3])+int(Exam[i][4])==0:
					#print i+1 ,"empty"
					List_answer.append((i+1,"empty"))
					empty=empty+1

				elif int(Exam[i][0])+int(Exam[i][1])+int(Exam[i][2])+int(Exam[i][3])+int(Exam[i][4])>C:
					#print i+1,"Over"
					List_answer.append((i+1,"Over"))
					over=over+1
				elif int(Exam[i][0])+int(Exam[i][1])+int(Exam[i][2])+int(Exam[i][3])+int(Exam[i][4])<C and int(Exam[i][0])+int(Exam[i][1])+int(Exam[i][2])+int(Exam[i][3])+int(Exam[i][4])!=0:
					#print i+1,"Over"
					List_answer.append((i+1,"less"))
					less=less+1
		else:

			for j in range(len(self.L)):
				#print "###########################"
				for i in range(int(self.L[j][0])-1,int(self.L[j][1])):
			 		#print i

					if int(Exam[i][0])+int(Exam[i][1])+int(Exam[i][2])+int(Exam[i][3])+int(Exam[i][4])==self.L[j][2]:
						if self.Check_FS(i+1)==True:
							    List_answer.append((i+1,"Yes"))
							    correct=correct+1
						elif int(Exam[i][0])==int(Key[i][0]) and int(Exam[i][1])==int(Key[i][1]) and int(Exam[i][2])==int(Key[i][2])and int(Exam[i][3])==int(Key[i][3])and int(Exam[i][4])==int(Key[i][4]):
								#print i+1,"Yes"
								List_answer.append((i+1,"Yes"))
								correct=correct+1
						else:
							    #print i+1,"No"
							    List_answer.append((i+1,"No"))
							    incorrect=incorrect+1
					elif int(Exam[i][0])+int(Exam[i][1])+int(Exam[i][2])+int(Exam[i][3])+int(Exam[i][4])==0:
						#print i+1 ,"empty"
						List_answer.append((i+1,"empty"))
						empty=empty+1

					elif int(Exam[i][0])+int(Exam[i][1])+int(Exam[i][2])+int(Exam[i][3])+int(Exam[i][4])>self.L[j][2]:
						#print i+1,"Over"
						List_answer.append((i+1,"Over"))
						over=over+1
					elif int(Exam[i][0])+int(Exam[i][1])+int(Exam[i][2])+int(Exam[i][3])+int(Exam[i][4])<self.L[j][2] and int(Exam[i][0])+int(Exam[i][1])+int(Exam[i][2])+int(Exam[i][3])+int(Exam[i][4])!=0:
						#print i+1,"Over"
						List_answer.append((i+1,"less"))
						less=less+1

		return List_answer,correct,incorrect,empty,over,less

	def CheckKey(self):
		file = open("setting/SelectKey.txt", "r")
            
		list_setting2=file.readlines()
		            
		file.close()
		 

		return list_setting2[0].strip()  
 	def readF(self,NameFile):
 		file = open(NameFile, "r")
		list_setting2=file.readlines()
				            
		file.close()
		return list_setting2
	def GetDetail(self,File):
		file = open(File, "r")
		list_setting=file.readlines()
		file.close()
		return  list_setting[0].strip(),list_setting[1].strip(),list_setting[2].strip(),list_setting[3].strip()
	def SK(self,PathKey,PathExam):
		score=0
		print PathKey
		value=self.readF("setting/format_tab2.txt")
		#print value[1].strip()
		Score=float(value[1].strip())
		choice=int(value[2].strip())
		div=value[3].strip()
		L,Path,C,S,T= self.Text2List(PathExam)
		print "ddd",S
		Lk,Pathk,Ck,Sk,Tk= self.Text2List(PathKey)
		List,correct,incorrect,empty,over,less= self.SingleKey_mc(L,Lk,self.num,choice)
		score=correct*Score
		#print "correct,incorrect,empty,over,less"
		#print correct,incorrect,empty,over,less
	 	if div=="Yes":
	 		score=(score*Score)-((self.num-correct)*Score)
	 	return  Path,List,score,C,S,T,correct,incorrect,empty,over,less
		 
		 

 
		




	def MK(self,PathExam):
		print ":",PathExam
		v1=0
		v2=0
		v3=0
		v4=0
		answer=False
		score=0
		Tab1=self.readF("setting/format_tab1.txt")
		value=self.readF("setting/format_tab2.txt")

		Key_=self.readF("setting/SelectKey.txt")
		if Key_[9].strip()=="No":
			v1=0
		else:
			v1=1
		if Key_[10].strip()=="No":
			v2=0
		else:
			v2=1
		if Key_[11].strip()=="No":
			v3=0
		else:
			v3=1
		if Key_[12].strip()=="No":
			v4=0
		else:
			v4=1
	 	
	 	print v1,v2,v3,v4


		#print value[1].strip()
		Score=float(value[1].strip())
		choice=int(value[2].strip())
		div=value[3].strip()
		 
		L,Path,C,S,T= self.Text2List(PathExam)
		print ":::::::",div
		print ":::",S
		if S==1 :
			if v1==1:
				answer=True
				Lk,Pathk,Ck,Sk,Tk= self.Text2List(self.SKeyReadC(int(S)))
		if S==2 :
			if v2==1:
				answer=True
				Lk,Pathk,Ck,Sk,Tk= self.Text2List(self.SKeyReadC(int(S)))
		if S==3 :
			if v3==1:
				answer=True
				Lk,Pathk,Ck,Sk,Tk= self.Text2List(self.SKeyReadC(int(S)))
		if S==4 :
			if v4==1:
				answer=True
				Lk,Pathk,Ck,Sk,Tk= self.Text2List(self.SKeyReadC(int(S)))
		 


		if answer==True :
			List,correct,incorrect,empty,over,less= self.SingleKey_mc(L,Lk,self.num,choice)
			if div=="Yes":
				if Tab1[1].strip()=="1" and Tab1[2].strip()=="1":
					score=(correct*Score)-((self.num-correct)*Score)
				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="1":
					score=(correct*Score)-((self.num-correct)*Score)
					score=score-(over*Score)
				elif Tab1[1].strip()=="1" and Tab1[2].strip()=="0":
					score=(correct*Score)-((self.num-correct)*Score)
					score=score-(empty*Score)
				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="0":
					score=(correct*Score)-((self.num-correct)*Score)
					score=score-(empty*Score)
					score=score-(over*Score)
			else:
				if Tab1[1].strip()=="1" and Tab1[2].strip()=="1":
					score=(correct*Score) 
				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="1":
					score=(correct*Score) 
					score=score-(over*Score)
				elif Tab1[1].strip()=="1" and Tab1[2].strip()=="0":
					score=(correct*Score) 
					score=score-(empty*Score)
				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="0":
					score=(correct*Score) 
					score=score-(empty*Score)
					score=score-(over*Score)				
			
			
			
			 
			return  Path,List,score,C,S,T,correct,incorrect,empty,over,less
 		else:
 			FList=[]

	 		for i in range(self.num):
	 			FList.append((i+1,"NOKEY"))
			return  Path,FList,0,C,S,T,0,0,0,0,0
	 

		

	def MultiNum(self,PathKey,PathExam,F):
		score=0
		value=self.readF("setting/format_tab2_down.txt")
		L,Path,C,S,T= self.Text2List(PathExam)
		try:
			Lk,Pathk,Ck,Sk,Tk= self.Text2List(PathKey)
		except:
			L=self.Create_list_Error()
			if F=="F1":
				return Path,L,9999,C,S,T,0,0,0,0,0
			elif F=="F2":
				return 0,0,Path,List,9999,C,S,T,0,0,0,0,0
			elif F=="F3":
				return 0,0,0,Path,List,9999,C,S,T,0,0,0,0,0

		 

		
		if F=="F1":

			Score=float(value[4].strip())
			choice=int(value[5].strip())
			div=value[6].strip()

			List,correct,incorrect,empty,over,less= self.SingleKey_mc(L,Lk,self.num,choice)


			Num=value[3].split("-")
			print Num[0],Num[1]
			for i in range(int(Num[0])-1,int(Num[1])):
 					#print List[i][1]
 					if List[i][1].strip()=="Yes":
 							score=score+1
 			print score*Score
 			if div=="1Yes":
 					score=(score*Score)-((self.num-correct)*Score)
 				 	return	Path,List,score,C,S,T,correct,incorrect,empty,over,less
 			else:
 				score=score*Score

 				print Path,List,score,C,S,T,correct,incorrect,empty,over,less
 				return	Path,List,score,C,S,T,correct,incorrect,empty,over,less

		if F=="F2":    
			C1=0
			Score=float(value[4].strip())
			choice=int(value[5].strip())
			div=value[6].strip()

			List,correct,incorrect,empty,over,less= self.SingleKey_mc(L,Lk,self.num,choice)

	 
			print "#################################"
			Num=value[3].split("-")
			#print Num[0],Num[1]
			for i in range(int(Num[0])-1,int(Num[1])):
 					#print List[i]
 					if List[i][1].strip()=="Yes":
 							C1=C1+1
 			#print Num[0],Num[1],":",C1
 			#print (int(Num[1])+1)-int(Num[0])
 			if div=="1Yes":
 				#print ((int(Num[1])+1)-int(Num[0]))-C1

 				C1=(C1*Score)-((((int(Num[1])+1)-int(Num[0]))-C1)*Score)
 			else:
 				C1=(C1*Score)

 			###################################

			C2=0
			Score=float(value[10].strip())
			choice=int(value[11].strip())
			div=value[12].strip()

			Num=value[9].split("-")
			List,correct,incorrect,empty,over,less= self.SingleKey_mc(L,Lk,self.num,choice)
			for i in range(int(Num[0])-1,int(Num[1])):
 					#print List[i] 
 					if List[i][1].strip()=="Yes":
 							C2=C2+1
 			#print Num[0],Num[1],":",C2
  			if div=="1Yes":
 				#print ((int(Num[1])+1)-int(Num[0]))-C2

 				#print "C2:",(C2*Score)-((((int(Num[1])+1)-int(Num[0]))-C2)*Score)
 				C2=(C2*Score)-((((int(Num[1])+1)-int(Num[0]))-C2)*Score)
 			else:
 				C2=(C2*Score)
 				#print "C2:",(C2*Score)
 			#print Score,choice,div
 			score=C1+C2
 			return C1,C2,Path,List,score,C,S,T,correct,incorrect,empty,over,less
		    #################################################################################
		if F=="F3":
			C1=0
			Score=float(value[4].strip())
			choice=int(value[5].strip())
			div=value[6].strip()

			List,correct,incorrect,empty,over,less= self.SingleKey_mc(L,Lk,self.num,choice)

			#for i in range(len(List)):
			#	print List[i]
			print "#################################"
			Num=value[3].split("-")
			#print Num[0],Num[1]
			for i in range(int(Num[0])-1,int(Num[1])):
 					#print List[i]
 					if List[i][1].strip()=="Yes":
 							C1=C1+1
 			#print Num[0],Num[1],":",C1
 			#print (int(Num[1])+1)-int(Num[0])
  			if div=="1Yes":
 				#print ((int(Num[1])+1)-int(Num[0]))-C1

 				#print "C1:",(C1*Score)-(((int(Num[1])+1)-int(Num[0]))-C1)
 				C1=(C1*Score)-((((int(Num[1])+1)-int(Num[0]))-C1)*Score)
 			else:
 				C1=(C1*Score)
 				#print "C1:",(C1*Score)

 			###################################

			C2=0
			Score=float(value[10].strip())
			choice=int(value[11].strip())
			div=value[12].strip()

			Num=value[9].split("-")
			List,correct,incorrect,empty,over,less= self.SingleKey_mc(L,Lk,self.num,choice)
			for i in range(int(Num[0])-1,int(Num[1])):
 					#print List[i] 
 					if List[i][1].strip()=="Yes":
 							C2=C2+1
 			#print Num[0],Num[1],":",C2
  			if div=="1Yes":
 				#print ((int(Num[1])+1)-int(Num[0]))-C2

 				#print "C2:",(C2*Score)-(((int(Num[1])+1)-int(Num[0]))-C2)
 				C2=(C2*Score)-((((int(Num[1])+1)-int(Num[0]))-C2)*Score)
 			else:
 				C2=(C2*Score)
 				#print "C2:",(C2*Score)
 			#print Score,choice,div




			C3=0
			Score=float(value[16].strip())
			choice=int(value[17].strip())
			div=value[18].strip()

			Num=value[15].split("-")
			List,correct,incorrect,empty,over,less= self.SingleKey_mc(L,Lk,self.num,choice)
			for i in range(int(Num[0])-1,int(Num[1])):
 					#print List[i] 
 					if List[i][1].strip()=="Yes":
 							C3=C3+1
 			#print Num[0],Num[1],":",C3
  			if div=="1Yes":
 				#print ((int(Num[1])+1)-int(Num[0]))-C3

 				#print "C3:",(C3*Score)-(((int(Num[1])+1)-int(Num[0]))-C3)
 				C3=(C3*Score)-((((int(Num[1])+1)-int(Num[0]))-C3)*Score)
 			else:
 				C3=(C3*Score)
 				#print "C3:",(C3*Score)
 			#print Score,choice,div
 			score=C1+C2+C3
 			return C1,C2,C3,Path,List,score,C,S,T,correct,incorrect,empty,over,less
 	def MultiNum_MK(self,PathExam,F):
		score=0
		Tab1=self.readF("setting/format_tab1.txt")
		value=self.readF("setting/format_tab2_down.txt")
		L,Path,C,S,T= self.Text2List(PathExam)
		try:
			Lk,Pathk,Ck,Sk,Tk= self.Text2List(self.SKeyReadC(int(S)))
		except:
			L=self.Create_list_Error()
			if F=="F1":
				return  Path,L,9999,C,S,T,0,0,0,0,0
			elif F=="F2":
				return 0,0,Path,L,9999,C,S,T,0,0,0,0,0
			elif F=="F3":
				return 0,0,0,Path,L,9999,C,S,T,0,0,0,0,0
		if F=="F1":

			Score=float(value[4].strip())
			choice=int(value[5].strip())
			div=value[6].strip()

			List,correct,incorrect,empty,over,less= self.SingleKey_mc(L,Lk,self.num,choice)


			Num=value[3].split("-")
			#print Num[0],Num[1]
			for i in range(int(Num[0])-1,int(Num[1])):
 					#print List[i][1]
 					if List[i][1].strip()=="Yes":
 							score=score+1
 			#print score*Score
 			if div=="1Yes":
 
				if Tab1[1].strip()=="1" and Tab1[2].strip()=="1":
					score=(correct*Score)-((self.num-correct)*Score)
				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="1":
					score=(correct*Score)-((self.num-correct)*Score)
					score=score-(over*Score)
				elif Tab1[1].strip()=="1" and Tab1[2].strip()=="0":
					score=(correct*Score)-((self.num-correct)*Score)
					score=score-(empty*Score)
				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="0":
					score=(correct*Score)-((self.num-correct)*Score)
					score=score-(empty*Score)
					score=score-(over*Score)
			else:
				if Tab1[1].strip()=="1" and Tab1[2].strip()=="1":
					score=(correct*Score) 
				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="1":
					score=(correct*Score) 
					score=score-(over*Score)
				elif Tab1[1].strip()=="1" and Tab1[2].strip()=="0":
					score=(correct*Score) 
					score=score-(empty*Score)
				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="0":
					score=(correct*Score) 
					score=score-(empty*Score)
					score=score-(over*Score)	



 			 
 			return	Path,List,score,C,S,T,correct,incorrect,empty,over,less

		if F=="F2":    
			C1=0
			O1=0
			E1=0
			Score=float(value[4].strip())
			choice=int(value[5].strip())
			div=value[6].strip()

			List,correct,incorrect,empty,over,less= self.SingleKey_mc(L,Lk,self.num,choice)

	 
			print "#################################"
			Num=value[3].split("-")
			#print Num[0],Num[1]
			for i in range(int(Num[0])-1,int(Num[1])):
 					#print List[i]
 					if List[i][1].strip()=="Yes":
 							C1=C1+1
 					if List[i][1].strip()=="Over":
 						    O1=O1+1
 					if List[i][1].strip()=="empty":
 						    E1=E1+1


 			#print Num[0],Num[1],":",C1
 			#print (int(Num[1])+1)-int(Num[0])
 			if div=="1Yes":
 				#print ((int(Num[1])+1)-int(Num[0]))-C1
 				if Tab1[1].strip()=="1" and Tab1[2].strip()=="1":
 					c1=(C1*Score)-((((int(Num[1])+1)-int(Num[0]))-C1)*Score)
 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="1":
 					c1=(C1*Score)-((((int(Num[1])+1)-int(Num[0]))-C1)*Score)
 					c1=c1-(O1*Score)
  				elif Tab1[1].strip()=="1" and Tab1[2].strip()=="0":
 					c1=(C1*Score)-((((int(Num[1])+1)-int(Num[0]))-C1)*Score)
 					c1=c1-(E1*Score)
 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="0":
 					c1=(C1*Score)-((((int(Num[1])+1)-int(Num[0]))-C1)*Score)
 					c1=c1-(O1*Score)
 					c1=c1-(E1*Score)

 			else:
 				if Tab1[1].strip()=="1" and Tab1[2].strip()=="1":
 					c1=(C1*Score) 
 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="1":
 					c1=(C1*Score) 
 					c1=c1-(O1*Score)
  				elif Tab1[1].strip()=="1" and Tab1[2].strip()=="0":
 					c1=(C1*Score) 
 					c1=c1-(E1*Score)
 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="0":
 					c1=(C1*Score) 
 					c1=c1-(O1*Score)
 					c1=c1-(E1*Score)
 			print "CCC",c1
 			###################################

			C2=0
			O2=0
			E2=0
			Score=float(value[10].strip())
			choice=int(value[11].strip())
			div=value[12].strip()

			Num=value[9].split("-")
			List,correct,incorrect,empty,over,less= self.SingleKey_mc(L,Lk,self.num,choice)
			for i in range(int(Num[0])-1,int(Num[1])):
 					#print List[i] 
 					#print List[i]
 					if List[i][1].strip()=="Yes":
 							C2=C2+1
 					if List[i][1].strip()=="Over":
 						    O2=O2+1
 					if List[i][1].strip()=="empty":
 						    E2=E2+1
 			 
  			if div=="1Yes":
 				if Tab1[1].strip()=="1" and Tab1[2].strip()=="1":
 					c2=(C2*Score)-((((int(Num[1])+1)-int(Num[0]))-C2)*Score)
 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="1":
 					c2=(C2*Score)-((((int(Num[1])+1)-int(Num[0]))-C2)*Score)
 					c2=c2-(O2*Score)

  				elif Tab1[1].strip()=="1" and Tab1[2].strip()=="0":
 					c2=(C2*Score)-((((int(Num[1])+1)-int(Num[0]))-C2)*Score)
 					c2=c2-(E2*Score)

 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="0":
 					c2=(C2*Score)-((((int(Num[1])+1)-int(Num[0]))-C2)*Score)
 					c2=c2-(O2*Score)
 					c2=c2-(E2*Score)

 			else:
 				if Tab1[1].strip()=="1" and Tab1[2].strip()=="1":
 					c2=(C2*Score) 
 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="1":
 					c2=(C2*Score) 
 					c2=c2-(O2*Score)
 					print ")))))))",c2
  				elif Tab1[1].strip()=="1" and Tab1[2].strip()=="0":
 					c2=(C2*Score) 
 					c2=c2-(E2*Score)
 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="0":
 					c2=(C2*Score) 
 					c2=c2-(O2*Score)
 					c2=c2-(E2*Score)
 			print "CCC",c2
 			score=c1+c2
 			return c1,c2,Path,List,score,C,S,T,correct,incorrect,empty,over,less
		    #################################################################################
		if F=="F3":
			C1=0
			O1=0
			E1=0
			Score=float(value[4].strip())
			choice=int(value[5].strip())
			div=value[6].strip()

			List,correct,incorrect,empty,over,less= self.SingleKey_mc(L,Lk,self.num,choice)

			#for i in range(len(List)):
			#	print List[i]
			print "#################################"
			Num=value[3].split("-")
			#print Num[0],Num[1]
			for i in range(int(Num[0])-1,int(Num[1])):
 					#print List[i]
 					if List[i][1].strip()=="Yes":
 							C1=C1+1
 					if List[i][1].strip()=="Over":
 						    O1=O1+1
 					if List[i][1].strip()=="empty":
 						    E1=E1+1
 			#print Num[0],Num[1],":",C1
 			#print (int(Num[1])+1)-int(Num[0])
  			if div=="1Yes":
 				if Tab1[1].strip()=="1" and Tab1[2].strip()=="1":
 					c1=(C1*Score)-((((int(Num[1])+1)-int(Num[0]))-C1)*Score)
 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="1":
 					c1=(C1*Score)-((((int(Num[1])+1)-int(Num[0]))-C1)*Score)
 					c1=c1-(O1*Score)
  				elif Tab1[1].strip()=="1" and Tab1[2].strip()=="0":
 					c1=(C1*Score)-((((int(Num[1])+1)-int(Num[0]))-C1)*Score)
 					c1=c1-(E1*Score)
 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="0":
 					c1=(C1*Score)-((((int(Num[1])+1)-int(Num[0]))-C1)*Score)
 					c1=c1-(O1*Score)
 					c1=c1-(E1*Score)

 			else:
 				if Tab1[1].strip()=="1" and Tab1[2].strip()=="1":
 					c1=(C1*Score) 
 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="1":
 					c1=(C1*Score) 
 					c1=c1-(O1*Score)
  				elif Tab1[1].strip()=="1" and Tab1[2].strip()=="0":
 					c1=(C1*Score) 
 					c1=c1-(E1*Score)
 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="0":
 					c1=(C1*Score) 
 					c1=c1-(O1*Score)
 					c1=c1-(E1*Score)

 			###################################

			C2=0
			O2=0
			E2=0
			Score=float(value[10].strip())
			choice=int(value[11].strip())
			div=value[12].strip()

			Num=value[9].split("-")
			List,correct,incorrect,empty,over,less= self.SingleKey_mc(L,Lk,self.num,choice)
			for i in range(int(Num[0])-1,int(Num[1])):
 					#print List[i] 
 					if List[i][1].strip()=="Yes":
 							C2=C2+1
 					if List[i][1].strip()=="Over":
 						    O2=O2+1
 					if List[i][1].strip()=="empty":
 						    E2=E2+1
 			#print Num[0],Num[1],":",C2
  			if div=="1Yes":
 				#print ((int(Num[1])+1)-int(Num[0]))-C2
 				if Tab1[1].strip()=="1" and Tab1[2].strip()=="1":
 					c2=(C2*Score)-((((int(Num[1])+1)-int(Num[0]))-C2)*Score)
 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="1":
 					c2=(C2*Score)-((((int(Num[1])+1)-int(Num[0]))-C2)*Score)
 					c2=c2-(O2*Score)

  				elif Tab1[1].strip()=="1" and Tab1[2].strip()=="0":
 					c2=(C2*Score)-((((int(Num[1])+1)-int(Num[0]))-C2)*Score)
 					c2=c2-(E2*Score)

 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="0":
 					c2=(C2*Score)-((((int(Num[1])+1)-int(Num[0]))-C2)*Score)
 					c2=c2-(O2*Score)
 					c2=c2-(E2*Score)

 			else:
 				if Tab1[1].strip()=="1" and Tab1[2].strip()=="1":
 					c2=(C2*Score) 
 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="1":
 					c2=(C2*Score) 
 					c2=c2-(O2*Score)
 					print ")))))))",c2
  				elif Tab1[1].strip()=="1" and Tab1[2].strip()=="0":
 					c2=(C2*Score) 
 					c2=c2-(E2*Score)
 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="0":
 					c2=(C2*Score) 
 					c2=c2-(O2*Score)
 					c2=c2-(E2*Score)



			C3=0
			O3=0
			E3=0
			Score=float(value[16].strip())
			choice=int(value[17].strip())
			div=value[18].strip()

			Num=value[15].split("-")
			List,correct,incorrect,empty,over,less= self.SingleKey_mc(L,Lk,self.num,choice)
			for i in range(int(Num[0])-1,int(Num[1])):
 					#print List[i] 
 					if List[i][1].strip()=="Yes":
 							C3=C3+1
 					if List[i][1].strip()=="Over":
 						    O3=O3+1
 					if List[i][1].strip()=="empty":
 						    E3=E3+1
 			#print Num[0],Num[1],":",C3
  			if div=="1Yes":
 				if Tab1[1].strip()=="1" and Tab1[2].strip()=="1":
 					c3=(C3*Score)-((((int(Num[1])+1)-int(Num[0]))-C3)*Score)
 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="1":
 					c3=(C3*Score)-((((int(Num[1])+1)-int(Num[0]))-C3)*Score)
 					c3=c3-(O3*Score)

  				elif Tab1[1].strip()=="1" and Tab1[2].strip()=="0":
 					c3=(C3*Score)-((((int(Num[1])+1)-int(Num[0]))-C3)*Score)
 					c3=c3-(E3*Score)

 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="0":
 					c3=(C3*Score)-((((int(Num[1])+1)-int(Num[0]))-C3)*Score)
 					c3=c3-(O3*Score)
 					c3=c3-(E3*Score)

 			else:
 				if Tab1[1].strip()=="1" and Tab1[2].strip()=="1":
 					c3=(C3*Score) 
 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="1":
 					c3=(C3*Score) 
 					c3=c3-(O3*Score)
 					print ")))))))",c3
  				elif Tab1[1].strip()=="1" and Tab1[2].strip()=="0":
 					c3=(C3*Score) 
 					c3=c3-(E3*Score)
 				elif Tab1[1].strip()=="0" and Tab1[2].strip()=="0":
 					c3=(C3*Score) 
 					c3=c3-(O3*Score)
 					c3=c3-(E3*Score)
 			score=c1+c2+c3
 			return c1,c2,c3,Path,List,score,C,S,T,correct,incorrect,empty,over,less
 	def SaveCSV(self):
 		file = open("setting.csv", "w")
 	def SKeyReadC(self,index):
	 		file = open('setting/SelectKey.txt', "r")
			list_setting2=file.readlines()
					            
			file.close()
			print "key/"+str(list_setting2[index].strip())
			return "key/"+str(list_setting2[index].strip())
 	def SKeyRead(self):
	 		file = open('setting/SelectKey.txt', "r")
			list_setting2=file.readlines()
					            
			file.close()
			return "key/"+str(list_setting2[1].strip())

	def wtextc2(self,C1,C2,Path,List,score,C,S,T,correct,incorrect,empty,over,less,Dir):
			    
			    file = open(str(Dir)+"/{:>}.txt".format(C), "w") 
			    file.write(str(Path))
			    file.write(str(C)+"\n")
			    file.write(str(S)+"\n")
			    file.write(str(C1)+"\n")
			    file.write(str(C2)+"\n")
			    file.write(str(score)+"\n")
			    file.write(str(correct)+"\n")
			    file.write(str(incorrect)+"\n")
			    file.write(str(empty)+"\n")
			    file.write(str(over)+"\n")
			    file.write(str(less)+"\n")
			    for i in range(len(List)):
			    		file.write(str(List[i])+"\n")
			     
			    file.close()

	def wtextc3(self,C1,C2,C3,Path,List,score,C,S,T,correct,incorrect,empty,over,less,Dir):
			    
			    file = open(str(Dir)+"/{:>}.txt".format(C), "w") 
			    file.write(str(Path))
			    file.write(str(C)+"\n")
			    file.write(str(S)+"\n")
			    file.write(str(C1)+"\n")
			    file.write(str(C2)+"\n")
			    file.write(str(C3)+"\n")
			    file.write(str(score)+"\n")
			    file.write(str(correct)+"\n")
			    file.write(str(incorrect)+"\n")
			    file.write(str(empty)+"\n")
			    file.write(str(over)+"\n")
			    file.write(str(less)+"\n")
			    for i in range(len(List)):
			    		file.write(str(List[i])+"\n")
			     
			    file.close()

	      	      
 	def WTEXT(self,Path,List,score,C,S,T,correct,incorrect,empty,over,less,Dir):
            print str(Dir)+"/{:>}.txt".format(C)
            file = open(str(Dir)+"/{:>}.txt".format(C), "w")
           
            file.write(str(Path))
            file.write(str(C)+"\n")
            file.write(str(S)+"\n")
            file.write(str(score)+"\n")
            file.write(str(correct)+"\n")
            file.write(str(incorrect)+"\n")
            file.write(str(empty)+"\n")
            file.write(str(over)+"\n")
            file.write(str(less)+"\n")
            for i in range(len(List)):
                file.write(str(List[i])+"\n")
               
            file.close()

	def Main(self,num):

		self.Seclect_c()
		 
		self.num=num
		List_C=[]
		if self.CheckKey()=="single":
				LI=os.listdir("exam")  
				value=self.readF("setting/format_tab2.txt")
				if value[0].strip()=="Yes":#sing seem score
							 print "1c"
							 print self.SKeyRead()
							 for i in range(len(LI)):
								 	
									 	  Path,List,score,C,S,T,correct,incorrect,empty,over,less=self.SK(self.SKeyRead(),"exam/{:>}".format(LI[i]) )
									 	  #print  Path,score,C,S,T,correct,incorrect,empty,over,less
									 	  #print   score,correct,incorrect,empty,over,less
									 	  if(score!=9999):
											 	self.WTEXT(Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\SC\onekey")
										  else:
										  		self.WTEXT(Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\\nokey")
									 	  #self.WTEXT(Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\SC\k1")
											

				else:			  
					value=self.readF("setting/format_tab2_down.txt")
					if value[2].strip()=="1Yes" and value[8].strip()=="1No" and value[14].strip()=="1No" :
					        print "F1"
					        for i in range(len(LI)):
					  			try:	
						  			Path,List,score,C,S,T,correct,incorrect,empty,over,less=self.MultiNum(self.SKeyRead(),("exam/{:>}".format(LI[i])),"F1")
						  			if score!=9999:
										self.WTEXT(Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\M1\onekey") 
									else:
										self.WTEXT(Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\\nokey")
								 	print Path ,score,C,S,T,correct,incorrect,empty,over,less
							 	except:
							 		pass
							 
					elif value[2].strip()=="1Yes" and value[8].strip()=="1Yes" and value[14].strip()=="1No" :
					    
 						 	for i in range(len(LI)):
 						 		try:
 						 			C1,C2,Path,List,score,C,S,T,correct,incorrect,empty,over,less=self.MultiNum(self.SKeyRead(),("exam/{:>}".format(LI[i])),"F2")
	 								print  LI[i],"C1:",C1,"C2:",C2
	 								if score!=9999:
										self.wtextc2(C1,C2,Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\M2\onekey")
	 								else:
	 									self.wtextc2(C1,C2,Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\\nokey")
	 							except:
	 								pass
					elif value[2].strip()=="1Yes" and value[8].strip()=="1Yes" and value[14].strip()=="1Yes" :
					        print "F3"	
					        for i in range(len(LI)):
					        	try:
						        	C1,C2,C3,Path,List,score,C,S,T,correct,incorrect,empty,over,less=self.MultiNum(self.SKeyRead(),("exam/{:>}".format(LI[i])),"F3")
						        	print  LI[i],"C1:",C1,"C2:",C2,"C3:",C3		
						        	self.wtextc3(C1,C2,C3,Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\M3\onekey")
					        	except:
					        		pass
					else:		
							print "No"	        





		else :
				LI=os.listdir("exam")  
				value=self.readF("setting/format_tab2.txt")
				if value[0].strip()=="Yes":#sing seem score
							 print "1c"
							 
							 for i in range(len(LI)):
							 	  
								 	  #print LI[i]
								 	  Path,List,score,C,S,T,correct,incorrect,empty,over,less=self.MK("exam/{:>}".format(LI[i]) )
								 	  #print  Path,score,C,S,T,correct,incorrect,empty,over,less
								 	  
								 	  #print Path,score,C,S,T,correct,incorrect,empty,over,less
								 	  print "score:",score,"Code:",C
								 	  if(S==1 and score!=9999):
								 	  	print "1"
								 	  	self.WTEXT(Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\SC\k1")
								 	  elif(S==2 and score!=9999):
								 	  	print "2"
								 	  	self.WTEXT(Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\SC\k2")
								 	  elif(S==3 and score!=9999):
								 	  	print "3"
								 	  	self.WTEXT(Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\SC\k3")
								 	  elif(S==4 and score!=9999):
								 	  	print "4"
								 	  	self.WTEXT(Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\SC\k4")
							 	 	  else:
							 	 	  	print "ok"
							 	 	  	self.WTEXT(Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected/nokey")
				
				else:					

					file = open('setting/SelectKey.txt', "r")
					list_setting2=file.readlines()
 					file.close() 
 					#if list_setting2[9].strip()=="Yes" and list_setting2[10].strip()=="Yes" and list_setting2[11].strip()=="Yes" and list_setting2[12].strip()=="No" :




					value=self.readF("setting/format_tab2_down.txt")
					if value[2].strip()=="1Yes" and value[8].strip()=="1No" and value[14].strip()=="1No" :
					        print "F1"

					        for i in range(len(LI)):
					        	try:
									  Path,List,score,C,S,T,correct,incorrect,empty,over,less=self.MultiNum_MK(("exam/{:>}".format(LI[i])),"F1")
								 	  if(S==1 and score!=9999):
								 	  	print "1"
								 	  	self.WTEXT(Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\M1\k1")
								 	  elif(S==2 and score!=9999):
								 	  	print "2"
								 	  	self.WTEXT(Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\M1\k2")
								 	  elif(S==3 and score!=9999):
								 	  	print "3"
								 	  	self.WTEXT(Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\M1\k3")
								 	  elif(S==4 and score!=9999):
								 	  	print "4"
								 	  	self.WTEXT(Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\M1\k4")
								 	  else:
								 	  	self.WTEXT(Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\\nokey")
					        	except :
					        		 pass
						  			  

					elif value[2].strip()=="1Yes" and value[8].strip()=="1Yes" and value[14].strip()=="1No" :
					    
 						 	for i in range(len(LI)):
 						 		try:
 						 			  C1,C2,Path,List,score,C,S,T,correct,incorrect,empty,over,less=self.MultiNum_MK(("exam/{:>}".format(LI[i])),"F2")
	 								  print  LI[i],"C1:",C1,"C2:",C2


								 	  if(S==1 and score!=9999):
								 	  	print "1"
								 	  	self.wtextc2(C1,C2,Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\M2\k1")
								 	  elif(S==2 and score!=9999):
								 	  	print "2"
								 	  	self.wtextc2(C1,C2,Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\M2\k2")
								 	  elif(S==3 and score!=9999):
								 	  	print "3"
								 	  	self.wtextc2(C1,C2,Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\M2\k3")
								 	  elif(S==4 and score!=9999):
								 	  	print "4"
								 	  	self.wtextc2(C1,C2,Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\M2\k4")
								 	  else:
								 	  	self.wtextc2(C1,C2,Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\\onkey")
								except:
									pass

	 								 
					elif value[2].strip()=="1Yes" and value[8].strip()=="1Yes" and value[14].strip()=="1Yes" :
					        print "F3"	
					        for i in range(len(LI)):
					        	try:
						        	    C1,C2,C3,Path,List,score,C,S,T,correct,incorrect,empty,over,less=self.MultiNum_MK(("exam/{:>}".format(LI[i])),"F3")
						        	    print  LI[i],"C1:",C1,"C2:",C2,"C3:",C3		
						        	    if S==1 and score!=9999:
						        	    	self.wtextc3(C1,C2,C3,Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\M3\k1")
						        	    elif S==2 and score!=9999:
						        	    	self.wtextc3(C1,C2,C3,Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\M3\k2")
						        	    elif S==3 and score!=9999:
						        	    	self.wtextc3(C1,C2,C3,Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\M3\k3")
						        	    elif S==4 and score!=9999:
						        	    	self.wtextc3(C1,C2,C3,Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\M3\k4")
						        	    else:
						        	   		self.wtextc3(C1,C2,C3,Path,List,score,C,S,T,correct,incorrect,empty,over,less,"inspected\\nokey") 	

						       	except:
						       		pass
	 
 
					 				       	       
					else:		
							print "No"	    

		return List_C

"""m=Inspector(0)
List_C=m.Main(60) """

 
 







 

 

