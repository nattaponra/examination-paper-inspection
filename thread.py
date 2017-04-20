import threading
import process
List=[]
def worker(name,n):
       
      U=process.MainProcess(0)
      code,list_final,List_Set_main,List_term_main=U.Process(name)
      print code,List_Set_main,List_term_main
      List.append((code))
      file = open("exam/{:>}.txt".format(n), "w")
      file.write(str(n)+"\n") 
      file.write(str(code)+"\n")   
      file.close()



def P1():
    for i in range(2):
      U=process.MainProcess(0)
      code,list_final,List_Set_main,List_term_main=U.Process("image\input\\00001.png")
      print "P1",code,List_Set_main,List_term_main
      for j in range(len(list_final)):
        print list_final[j]
      List.append((code))
      file = open("exam/{:>}.txt".format(i), "w")
      file.write(str(i)+"\n") 
      file.write(str(code)+"\n")   
      file.close() 

def P2():
    for i in range(10):
      U=process.MainProcess(0)
      code,list_final,List_Set_main,List_term_main=U.Process("image\input\\00001.png")
      print "P2",code,List_Set_main,List_term_main
      List.append((code))
      file = open("exam/{:>}.txt".format(i), "w")
      file.write(str(i)+"\n") 
      file.write(str(code)+"\n")   
      file.close() 



t = threading.Thread(target=P1,)
t.start()
t = threading.Thread(target=P2,)
t.start()