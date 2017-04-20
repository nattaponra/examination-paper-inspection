


import os


class Distracter(object):
	"""docstring for Distracter"""
	List_Set1=[]
	List_Set2=[]
	List_Set3=[]
	List_Set4=[]
	def __init__(self, arg):
		super(Distracter, self).__init__()
		self.arg = arg

	def Text2List(self,NameFile,num):
		List_Main=[]
		file = open(NameFile, "r")           
		list_setting2=file.readlines()
		file.close()
		List_main=[]
		for i in range(len(list_setting2)):
			#print list_setting2[i].replace("[", " ").replace("]", " ");
			List_main.append(list_setting2[i].replace("[", " ").replace("]", " "))


		for i in range(4,num+4):
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

	def FindFile(self,INPUT):
			LI=os.listdir('exam') 	
 			for i in range(len(LI)):
 				#print LI[i]
 				file = open("exam/{:>}".format(LI[i]), "r")
				LIST=file.readlines()
				file.close() 
				#print LIST[0]
				#print INPUT
			 
				if INPUT.strip()==LIST[0].strip():
					#print i,INPUT,"=",LIST[0].strip() ,LI[i]
					break
				if len(LI)-1==i:
					print "asdasd"
			return LI[i]

	def	SelectExam(self,Key,num):
			List_silly=[]
			List_gin=[]
			nameKey=""
			file = open("setting/SelectKey.txt", "r")
			type_key=file.readlines()
			file.close() 
			print type_key[0],"|||||||||||"
			if type_key[0].strip()=="multiple":
				if Key==1 or Key==2 or Key==3 or Key==4  :


					if Key==1:
						nameKey=type_key[1].strip()
					elif Key==2:
						nameKey=type_key[2].strip()
					elif Key==3:
						nameKey=type_key[3].strip()
					elif Key==4:
						nameKey=type_key[4].strip()


					file = open("distracter/s{:>}/List_silly.txt".format(Key), "r")
					silly=file.readlines()
					file.close() 
					for i in range(len(silly)):
						#print silly[i].strip()
						if silly[i].strip()!="":
							List_silly.append(silly[i].strip())


					file = open("distracter/s{:>}/List_gin.txt".format(Key), "r")
					gin=file.readlines()
					file.close() 
					for i in range(len(gin)):
						#print gin[i].strip()
						if gin[i].strip()!="":
							List_gin.append(gin[i].strip())
			 
			else:
				nameKey=type_key[1].strip()

				file = open("distracter/Sc/List_silly.txt" , "r")
				silly=file.readlines()
				file.close() 
				for i in range(len(silly)):
					#print silly[i].strip()
					if silly[i].strip()!="":
						List_silly.append(silly[i].strip())


				file = open("distracter/Sc/List_gin.txt" , "r")
				gin=file.readlines()
				file.close() 
				for i in range(len(gin)):
					#print gin[i].strip()
					if gin[i].strip()!="":
						List_gin.append(gin[i].strip())

			 
	 		print List_silly
	 		print List_gin
	 		SI=[]
	 		GI=[]
	 		

	 		for i in range(len(List_silly)):
	 			file = open(List_silly[i], "r")
				LIST=file.readlines()
				file.close() 
				 
				#print self.FindFile(LIST[0].strip())
 				SI.append(self.FindFile(LIST[0].strip()))
 				#print  LIST[0].strip()

	 		for i in range(len(List_gin)):
	 			file = open(List_gin[i], "r")
				LIST=file.readlines()
				file.close() 
				 
				#print self.FindFile(LIST[0].strip())
 				GI.append(self.FindFile(LIST[0].strip()))
 				#print  LIST[0].strip()
	 		 

 			#print SI
 			#print GI
  			List_Gi=[]
  			List_Si=[]
  			for i in range(num):
  				List_Gi.append([0,0,0,0,0])
		 		List_Si.append([0,0,0,0,0])

 			for i in range(len(GI)):
 				List_an,b,c,d,f =self.Text2List("exam/{:>}".format(GI[i]),num)
				 
				for j in range(num):
				 
					#print List_Gi[j][0]
					#print j+1,List_an[j] 
					#print j+1, List_an[j+4][0],List_an[j+4][1],List_an[j+4][2],List_an[j+4][3],List_an[j+4][4]
					if List_an[j][0]+List_an[j][1]+List_an[j][2]+List_an[j][3]+List_an[j][4]==1:
						if List_an[j][0]==1:
							 List_Gi[j][0]=List_Gi[j][0]+1

						if List_an[j][1]==1:
							 List_Gi[j][1]=List_Gi[j][1]+1

						if List_an[j][2]==1:
							 List_Gi[j][2]=List_Gi[j][2]+1

						if List_an[j][3]==1:
							 List_Gi[j][3]=List_Gi[j][3]+1

						if List_an[j][4]==1:
							 List_Gi[j][4]=List_Gi[j][4]+1


 			for i in range(len(SI)):
 				List_an,b,c,d,f =self.Text2List("exam/{:>}".format(SI[i]),num)
				 
				for j in range(num):
				 
					#print List_Gi[j][0]
					#print j+1,List_an[j] 
					#print j+1, List_an[j+4][0],List_an[j+4][1],List_an[j+4][2],List_an[j+4][3],List_an[j+4][4]
					if List_an[j][0]+List_an[j][1]+List_an[j][2]+List_an[j][3]+List_an[j][4]==1:
						if List_an[j][0]==1:
							 List_Si[j][0]=List_Si[j][0]+1

						if List_an[j][1]==1:
							 List_Si[j][1]=List_Si[j][1]+1

						if List_an[j][2]==1:
							 List_Si[j][2]=List_Si[j][2]+1

						if List_an[j][3]==1:
							 List_Si[j][3]=List_Si[j][3]+1

						if List_an[j][4]==1:
							 List_Si[j][4]=List_Si[j][4]+1


			#print nameKey
 
			ReadKey,A,B,C,D=self.Text2List("key/{:>}".format(nameKey.strip()),num)
 			LisT=[]
 			List_DIS=[]
 			for i in range(num):
 				List_DIS.append([0,0,0,0,0])
			for i in range(len(ReadKey)):
			 	#print i+1,ReadKey[i]

			 	#print i+1,ReadKey[i][0],ReadKey[i][1],ReadKey[i][2],ReadKey[i][3],ReadKey[i][4]
			 	if   ReadKey[i][0]==1:
			 		 LisT.append(1)

			 	elif ReadKey[i][1]==1:
			 		 LisT.append(2)

			 	elif ReadKey[i][2]==1:
			 		 LisT.append(3)

			 	elif ReadKey[i][3]==1:
			 		 LisT.append(4)

			 	elif ReadKey[i][4]==1:
			 		 LisT.append(5)
			 	else:
			 		 LisT.append(0)

			for i in range(num):
				 
				

				if LisT[i]==1:
					List_DIS[i][0]=10
					List_DIS[i][1]=(List_Si[i][1]-List_Gi[i][1])/float(len(List_gin))
				 	List_DIS[i][2]=(List_Si[i][2]-List_Gi[i][2])/float(len(List_gin))
				 	List_DIS[i][3]=(List_Si[i][3]-List_Gi[i][3])/float(len(List_gin))
				 	List_DIS[i][4]=(List_Si[i][4]-List_Gi[i][4])/float(len(List_gin))				   
				elif LisT[i]==2:
					List_DIS[i][0]=(List_Si[i][0]-List_Gi[i][0])/float(len(List_gin))
					List_DIS[i][1]=10
				 	List_DIS[i][2]=(List_Si[i][2]-List_Gi[i][2])/float(len(List_gin))
				 	List_DIS[i][3]=(List_Si[i][3]-List_Gi[i][3])/float(len(List_gin))
				 	List_DIS[i][4]=(List_Si[i][4]-List_Gi[i][4])/float(len(List_gin))	
				elif LisT[i]==3:
					List_DIS[i][0]=(List_Si[i][0]-List_Gi[i][0])/float(len(List_gin))
					List_DIS[i][1]=(List_Si[i][1]-List_Gi[i][1])/float(len(List_gin))
				 	List_DIS[i][2]=10
				 	List_DIS[i][3]=(List_Si[i][3]-List_Gi[i][3])/float(len(List_gin))
				 	List_DIS[i][4]=(List_Si[i][4]-List_Gi[i][4])/float(len(List_gin))	
				elif LisT[i]==4:
					List_DIS[i][0]=(List_Si[i][0]-List_Gi[i][0])/float(len(List_gin))
					List_DIS[i][1]=(List_Si[i][1]-List_Gi[i][1])/float(len(List_gin))
				 	List_DIS[i][2]=(List_Si[i][2]-List_Gi[i][2])/float(len(List_gin))
				 	List_DIS[i][3]=10
				 	List_DIS[i][4]=(List_Si[i][4]-List_Gi[i][4])/float(len(List_gin))	
				elif LisT[i]==5:
					List_DIS[i][0]=(List_Si[i][0]-List_Gi[i][0])/float(len(List_gin))
					List_DIS[i][1]=(List_Si[i][1]-List_Gi[i][1])/float(len(List_gin))
				 	List_DIS[i][2]=(List_Si[i][2]-List_Gi[i][2])/float(len(List_gin))
				 	List_DIS[i][3]=(List_Si[i][3]-List_Gi[i][3])/float(len(List_gin))
				 	List_DIS[i][4]=10


				#print i+1,List_Si[i] ,":",List_Si[i],ReadKey[i],List_Gi[i] , List_DIS[i]
				#print LisT	


			return List_DIS,List_Si,List_Gi,ReadKey,LisT
"""M=Distracter(0)
List_DIS,List_Si,List_Gi,ReadKey,LisT=M.SelectExam(1,10)
for i in range(len(LisT)):
	print i+1,LisT[i] """