import csv
import sys
import os
class writecsv(object):
  """docstring for writecsv"""
  def __init__(self, arg):
    super(writecsv, self).__init__()
    self.arg = arg
  def wcsv_MK_SC(self,NameC):

    STUDENT_ID=[]
    SET=[]
    EMPTY=[]
    LESS=[]
    OVER=[]
    CORRECT=[]
    INCORRECT=[]
    SCORE=[]
    LI=os.listdir("inspected\SC") 
    for i in range(len(LI)):
        file = open("inspected\SC\{:>}".format(LI[i]), "r")
        DATA=file.readlines()
        file.close()
        STUDENT_ID.append((DATA[1].strip()))
        SET.append((DATA[2].strip()))
        EMPTY.append((DATA[6].strip()))
        LESS.append((DATA[8].strip()))
        OVER.append((DATA[7].strip()))
        CORRECT.append((DATA[4].strip()))
        INCORRECT.append((DATA[5].strip()))
        SCORE.append((DATA[3].strip()))
    print "STUDENT_ID=",STUDENT_ID
    print "SET=",SET
    print "EMPTY=",EMPTY
    print "LESS=",LESS
    print "OVER=",OVER
    print "CORRECT=",CORRECT
    print "INCORRECT=",INCORRECT
    print "SCORE=",SCORE
    f = open('csv/{:>}.csv'.format(NameC), 'wt')
    try:



        fieldnames = ('STUDENT_ID', 'SET', 'EMPTY' ,'LESS' ,'OVER', 'CORRECT','INCORRECT','SCORE')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        headers = dict( (n,n) for n in fieldnames )
        writer.writerow(headers)
        for i in range(len(STUDENT_ID)):
            writer.writerow({ 'STUDENT_ID':STUDENT_ID[i], 
                              'SET':SET[i], 
                              'EMPTY':EMPTY[i],
                              'LESS':LESS[i],
                              'OVER':OVER[i],
                              'CORRECT':CORRECT[i],
                              'INCORRECT':INCORRECT[i],
                              'SCORE':SCORE[i],
                              })
    finally:
        f.close()

    print open('csv/{:>}.csv'.format(NameC), 'rt').read()
  def wcsv_MK_M1(self,NameC):

    STUDENT_ID=[]
    SET=[]
    EMPTY=[]
    LESS=[]
    OVER=[]
    CORRECT=[]
    INCORRECT=[]
    SCORE=[]
    LI=os.listdir("inspected\M1") 
    for i in range(len(LI)):
        file = open("inspected\M1\{:>}".format(LI[i]), "r")
        DATA=file.readlines()
        file.close()
        STUDENT_ID.append((DATA[1].strip()))
        SET.append((DATA[2].strip()))
        EMPTY.append((DATA[6].strip()))
        LESS.append((DATA[8].strip()))
        OVER.append((DATA[7].strip()))
        CORRECT.append((DATA[4].strip()))
        INCORRECT.append((DATA[5].strip()))
        SCORE.append((DATA[3].strip()))
    print "STUDENT_ID=",STUDENT_ID
    print "SET=",SET
    print "EMPTY=",EMPTY
    print "LESS=",LESS
    print "OVER=",OVER
    print "CORRECT=",CORRECT
    print "INCORRECT=",INCORRECT
    print "SCORE=",SCORE
    f = open('csv/{:>}.csv'.format(NameC), 'wt')
    try:



        fieldnames = ('STUDENT_ID', 'SET', 'EMPTY' ,'LESS' ,'OVER', 'CORRECT','INCORRECT','SCORE')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        headers = dict( (n,n) for n in fieldnames )
        writer.writerow(headers)
        for i in range(len(STUDENT_ID)):
            writer.writerow({ 'STUDENT_ID':STUDENT_ID[i], 
                              'SET':SET[i], 
                              'EMPTY':EMPTY[i],
                              'LESS':LESS[i],
                              'OVER':OVER[i],
                              'CORRECT':CORRECT[i],
                              'INCORRECT':INCORRECT[i],
                              'SCORE':SCORE[i],
                              })
    finally:
        f.close()

    print open('csv/{:>}.csv'.format(NameC), 'rt').read()
  def wcsv_MK_M2(self,NameC):

    STUDENT_ID=[]
    SET=[]
    EMPTY=[]
    LESS=[]
    OVER=[]
    CORRECT=[]
    INCORRECT=[]
    SCORE=[]
    C1=[]
    C2=[]
    LI=os.listdir("inspected\M2") 
    for i in range(len(LI)):
        file = open("inspected\M2\{:>}".format(LI[i]), "r")
        DATA=file.readlines()
        file.close()
        STUDENT_ID.append((str(DATA[1]).strip()))
        SET.append((str(DATA[1]).strip()))
        EMPTY.append((str(DATA[1]).strip()))
        LESS.append((str(DATA[1]).strip()))
        OVER.append((str(DATA[1]).strip()))
        CORRECT.append((str(DATA[1]).strip()))
        INCORRECT.append((str(DATA[1]).strip()))
        SCORE.append((str(DATA[1]).strip()))
        C1.append((str(DATA[1]).strip()))
        C2.append((str(DATA[1]).strip()))
    print "STUDENT_ID=",STUDENT_ID
    print "SET=",SET
    print "EMPTY=",EMPTY
    print "LESS=",LESS
    print "OVER=",OVER
    print "CORRECT=",CORRECT
    print "INCORRECT=",INCORRECT
    print "SCORE=",SCORE
    f = open('csv/{:>}.csv'.format(NameC), 'wt')
    try:



        fieldnames = ('STUDENT_ID', 'SET', 'EMPTY' ,'LESS' ,'OVER', 'CORRECT','INCORRECT','SCORE','C1','C2')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        headers = dict( (n,n) for n in fieldnames )
        writer.writerow(headers)
        for i in range(len(STUDENT_ID)):
            print i
            writer.writerow({ 'STUDENT_ID':STUDENT_ID[i], 
                              'SET':SET[i], 
                              'EMPTY':EMPTY[i],
                              'LESS':LESS[i],
                              'OVER':OVER[i],
                              'CORRECT':CORRECT[i],
                              'INCORRECT':INCORRECT[i],
                              'SCORE':SCORE[i],
                              'C1':C1[i],
                              'C2':C2[i],
                              })
    finally:
        f.close()

    print open('csv/{:>}.csv'.format(NameC), 'rt').read()


  def wcsv_MK_M3(self,NameC):

    STUDENT_ID=[]
    SET=[]
    EMPTY=[]
    LESS=[]
    OVER=[]
    CORRECT=[]
    INCORRECT=[]
    SCORE=[]
    C1=[]
    C2=[]
    C3=[]
    LI=os.listdir("inspected\M3") 
    for i in range(len(LI)):
        file = open("inspected\M3\{:>}".format(LI[i]), "r")
        DATA=file.readlines()
        file.close()
        STUDENT_ID.append((DATA[1].strip()))
        SET.append((DATA[2].strip()))
        EMPTY.append((DATA[9].strip()))
        LESS.append((DATA[11].strip()))
        OVER.append((DATA[10].strip()))
        CORRECT.append((DATA[7].strip()))
        INCORRECT.append((DATA[8].strip()))
        SCORE.append((DATA[6].strip()))
        C1.append((DATA[3].strip()))
        C2.append((DATA[4].strip()))
        C3.append((DATA[5].strip())) 
    print "STUDENT_ID=",STUDENT_ID
    print "SET=",SET
    print "EMPTY=",EMPTY
    print "LESS=",LESS
    print "OVER=",OVER
    print "CORRECT=",CORRECT
    print "INCORRECT=",INCORRECT
    print "SCORE=",SCORE
    f = open('csv/{:>}.csv'.format(NameC), 'wt')
    try:



        fieldnames = ('STUDENT_ID', 'SET', 'EMPTY' ,'LESS' ,'OVER', 'CORRECT','INCORRECT','SCORE','C1','C2','C3')
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        headers = dict( (n,n) for n in fieldnames )
        writer.writerow(headers)
        for i in range(len(STUDENT_ID)):
            writer.writerow({ 'STUDENT_ID':STUDENT_ID[i], 
                              'SET':SET[i], 
                              'EMPTY':EMPTY[i],
                              'LESS':LESS[i],
                              'OVER':OVER[i],
                              'CORRECT':CORRECT[i],
                              'INCORRECT':INCORRECT[i],
                              'SCORE':SCORE[i],
                              'C1':C1[i],
                              'C2':C2[i],
                              'C3':C3[i],
                              })
    finally:
        f.close()

    print open('csv/{:>}.csv'.format(NameC), 'rt').read()
w=writecsv(0)
#w.wcsv_MK_4C("kkk")
w.wcsv_MK_M2("re")