import os
import csv
import sys


class Save_csv(object):
	List_all=[]
	List_final=[]
	"""docstring for Save_csv"""
	def __init__(self, arg):
		super(Save_csv, self).__init__()
		self.arg = arg

	def AddList(self,LI,N,D):
		for i in range(len(LI)):
			self.List_all.append((LI[i],N,D))
	def main(self,name):
		SCON=os.listdir("inspected\SC\onekey")
		self.AddList(SCON,1,"inspected\SC\onekey")
		SCk1=os.listdir("inspected\SC\k1")
		self.AddList(SCk1,1,"inspected\SC\k1") 
		SCk2=os.listdir("inspected\SC\k2")
		self.AddList(SCk2,1,"inspected\SC\k2") 
		SCk3=os.listdir("inspected\SC\k3")
		self.AddList(SCk3,1,"inspected\SC\k3") 
		SCk4=os.listdir("inspected\SC\k4")
		self.AddList(SCk4,1,"inspected\SC\k4") 

		M1ON=os.listdir("inspected\M1\onekey")
		self.AddList(M1ON,1,"inspected\M1\onekey") 
		M1k1=os.listdir("inspected\M1\k1")
		self.AddList(M1k1,1,"inspected\M1\k1") 
		M1k2=os.listdir("inspected\M1\k2")
		self.AddList(M1k2,1,"inspected\M1\k2") 
		M1k3=os.listdir("inspected\M1\k3")
		self.AddList(M1k3,1,"inspected\M1\k3") 
		M1k4=os.listdir("inspected\M1\k4")
		self.AddList(M1k4,1,"inspected\M1\k4") 

		M2ON=os.listdir("inspected\M2\onekey")
		self.AddList(M2ON,2,"inspected\M2\onekey") 
		M2k1=os.listdir("inspected\M2\k1")
		self.AddList(M2k1,2,"inspected\M2\k1") 
		M2k2=os.listdir("inspected\M2\k2")
		self.AddList(M2k2,2,"inspected\M2\k2") 
		M2k3=os.listdir("inspected\M2\k3")
		self.AddList(M2k3,2,"inspected\M2\k3") 
		M2k4=os.listdir("inspected\M2\k4")
		self.AddList(M2k4,2,"inspected\M2\k4")  


		M3ON=os.listdir("inspected\M3\onekey")
		self.AddList(M3ON,3,"inspected\M3\onekey") 
		M3k1=os.listdir("inspected\M3\k1")
		self.AddList(M3k1,3,"inspected\M3\k1") 
		M3k2=os.listdir("inspected\M3\k2")
		self.AddList(M3k2,3,"inspected\M3\k2") 
		M3k3=os.listdir("inspected\M3\k3")
		self.AddList(M3k3,3,"inspected\M3\k3") 
		M3k4=os.listdir("inspected\M3\k4")
		self.AddList(M3k4,3,"inspected\M3\k4")  


		for i in range(len(self.List_all)):
		    if self.List_all[i][1]==3:
		    	#print self.List_all[i]	
		        file = open(self.List_all[i][2]+"\\"+self.List_all[i][0], "r")
		        Score =file.readlines()
		        file.close()  
		        #print Score[1] ,Score[6] 
		        self.List_final.append((Score[1].strip(),Score[6].strip())) 
		    if self.List_all[i][1]==2:
		    	#print self.List_all[i]	
		        file = open(self.List_all[i][2]+"\\"+self.List_all[i][0], "r")
		        Score =file.readlines()
		        file.close()  
		        #print Score[1] ,Score[5]
		        self.List_final.append((Score[1].strip(),Score[5].strip()))  	
			if self.List_all[i][1]==1:
				#print self.List_all[i]
				pass 
		        file = open(self.List_all[i][2]+"\\"+self.List_all[i][0], "r")
		        Score =file.readlines()
		        file.close()
		        self.List_final.append((Score[1].strip(),Score[3].strip()))
		        #print Score[1] ,Score[3]





		 
		file = open("{:>}.csv".format(name), "w")
		file.write("STUDENT ID ,SCORE\n")
		for i in range(len(self.List_final)):
			score= str(float(self.List_final[i][1]))
			print score
			file.write(self.List_final[i][0]+" ,")
			file.write(score)
			 
			file.write("\n") 


"""M=Save_csv(0)
M.main("asdasd")"""