from random import *
import calendar
import random

day=[]
d=open("dbool.txt")
for line in d:
    line=line.strip()
    day.append(line)
d.close()

plate=[]
p=open("pbool.txt")
for line in p:
    line=line.strip()
    plate.append(line)
p.close()

hour=[]
h=open("hbool.txt")
for line in h:
    line=line.strip()
    hour.append(line)
h.close()
   
a=open("FINALDOC.txt","w")
for i in range(len(day)):
    if (day[i]=="Monday") and (plate[i]=="1" or plate[i]=="2") and (hour[i]=="1"):
        a.write('1'+'\n')
    elif (day[i]=="Tuesday") and (plate[i]=="3" or plate[i]=="4") and (hour[i]=="1"):
        a.write('1'+'\n')
    elif (day[i]=="Wednesday") and (plate[i]=="5" or plate[i]=="6") and (hour[i]=="1"):
        a.write('1'+'\n')
    elif (day[i]=="Thursday") and (plate[i]=="7" or plate=="8") and (hour[i]=="1"):
        a.write('1'+'\n')
    elif (day[i]=="Friday") and (plate[i]=="9" or plate[i]=="0") and (hour[i]=="1"):
        a.write('1'+'\n')
    else:
        a.write('0'+'\n')
a.close()
        

    
