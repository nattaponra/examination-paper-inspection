import csv
import sys
ID_STUDENT=[54020573,5423423]  
NAME_LASTNAME=[1,2] 
SCORE=[10,9] 
f = open('test.csv', 'wt')
try:
    fieldnames = ('ID_STUDENT', 'NAME&LASTNAM', 'SCORE')
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    headers = dict( (n,n) for n in fieldnames )
    writer.writerow(headers)
    for i in range(len(ID_STUDENT)):
        writer.writerow({ 'ID_STUDENT':ID_STUDENT[i],
                          'NAME&LASTNAM':NAME_LASTNAME[i],
                          'SCORE':SCORE[i],
                          })
finally:
    f.close()

print open('test.csv', 'rt').read()
