import os,sys


class Distinguish(object):
	"""docstring for Distinguish"""
	LIST_Number=[]
	List_count=[]
	List_Diffic=[]

	#print List_count
	
	def __init__(self, arg):
		super(Distinguish, self).__init__()
		self.arg = arg
		


	def CheckAnswer(self,Str):
		#print str(Str).replace(",", "").replace("'", "").replace("(", "").replace(")", "") .replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("0", "").strip()
			
		if str(Str).replace(",", "").replace("'", "").replace("(", "").replace(")", "") .replace("1", "").replace("2", "").replace("3", "").replace("4", "").replace("5", "").replace("6", "").replace("7", "").replace("8", "").replace("9", "").replace("0", "").strip()=="Yes":
			return True
		else:
			return False

	def main(self,Key,num):
			Start=0
			for i in range(num):
				self.LIST_Number.append(0.0)
				self.List_count.append(0)
				self.List_Diffic.append("")

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
			List_Score=[]
			List_silly=[]
			List_gin=[]
	 		self.LI=os.listdir(Dir) 
			for i in range(len(self.LI)):
				#print Dir+"\\"+self.LI[i]
				file = open(Dir+"\\"+self.LI[i], "r")
				list_answer=file.readlines()
				List_Score.append((float(list_answer[3].strip()),Dir+"\\"+self.LI[i],list_answer[1].strip()))
						
			 
			 

				
			List_Score.sort()
			print List_Score 
			for i in range(len(List_Score)):
				print	List_Score[i]
				if(i<len(List_Score)/2):
					List_silly.append(List_Score[i])
				else:
					List_gin.append(List_Score[i])
			
			#print "######################"
			List_count_silly=[]
			List_count_gin=[]
			for i in range(num):
				List_count_silly.append(0)
				List_count_gin.append(0)


			for i in range(len(List_silly)):
				#print "::::",List_silly[i][1]

				file = open(List_silly[i][1], "r")
				list_answer=file.readlines()
				
				for j in range(Start,num+Start):
									 
									if self.CheckAnswer(str(list_answer[j]))==True:	
										#print j-Start,":", "yes"
										List_count_silly[j-Start]=List_count_silly[j-Start]+1
									else:
										#print j-Start,":", "No"
										pass
			#print  List_count_silly 



			for i in range(len(List_gin)):
				#print List_gin[i]
				file = open(List_gin[i][1], "r")
				list_answer=file.readlines()
				for j in range(Start,num+Start):
									 
									if self.CheckAnswer(str(list_answer[j]))==True:	
										#print j-Start,":", "yes"
										List_count_gin[j-Start]=List_count_gin[j-Start]+1
									else:
										#print j-Start,":", "No"
										pass
			#print  List_count_gin 
			#cal
			print Key 
			print len(List_silly)
			if Dir!="inspected\SC\onekey" and list_key[0].strip()!="single":
				if len(List_silly)!=0:
					file = open("distracter/s{:>}/List_silly.txt".format(Key), "w")
					for i in range(len(List_silly)):
						 file.write(str(List_silly[i][1])+"\n")
			         
			         
					file.close()
					file = open("distracter/s{:>}/List_gin.txt".format(Key), "w")
					for i in range(len(List_gin)):
						print List_gin[i][1]
						file.write(str(List_gin[i][1])+"\n")

					file.close()
			else:
				print "1k"
				print "=============================================="
				print List_silly
				if len(List_silly)!=0:
					file = open("distracter/Sc/List_silly.txt" , "w")
					for i in range(len(List_silly)):
						 file.write(str(List_silly[i][1])+"\n")
			         
			         
					file.close()
					file = open("distracter/Sc/List_gin.txt" , "w")
					for i in range(len(List_gin)):
						print List_gin[i][1]
						file.write(str(List_gin[i][1])+"\n")

					file.close() 






			List_final=[]
			for i in range(num):
				pass
				#print float(len(List_gin))
				#print List_count_gin[i],List_count_silly[i] ,(List_count_gin[i]-List_count_silly[i])/float(len(List_gin))
				#print List_count_gin[i],":",List_count_silly[i],"   =",(List_count_gin[i]-List_count_silly[i])/float(len(List_gin))
				List_final.append((List_count_gin[i]-List_count_silly[i])/float(len(List_gin)))
			return List_silly,List_gin,List_count_gin,List_count_silly,List_final

"""M=Distinguish(1)
List_silly,List_gin,List_count_gin,List_count_silly,List_final=M.main(4,10)

print  List_final"""