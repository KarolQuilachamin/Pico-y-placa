#Hacedor de documentos
from random import *
import calendar
import random
import string

#NUMBER OF DATA
n=100

#HOURS GENERATOR
a=open("hours.txt", "w")
for i in range(n):
    h=randint(0,24)
    if h<10:
        h='0'+str(h)
    else:
        h=str(h)
    m=randint(0,59)
    if m<10:
        m='0'+str(m)
    else:
        m=str(m)
    a.write(":".join([h,m])+'\n')
a.close()

#DATES GENERATOR
b=open("dates.txt", "w")
for j in range(n):
    Y = randint(2000, 2025)
    M = randint(1, 12)
    if M == 2:
        if calendar.isleap(Y + 1850):
            Dmax = 28
        else:
            Dmax = 29
    elif M in [4, 6, 9, 11]:
        Dmax = 30
    else:
        Dmax = 31

    D = randint(1, Dmax)
    if D<10:
        d='0'+str(D)
    else:
        d=str(D)

    if M<10:
        ms='0'+str(M)
    else:
        ms=str(M)
    y=str(Y)
    
    b.write("/".join([d,ms,y])+'\n')
b.close()

#PLATE GENERATOR
c=open("plates.txt", "w")
for k in range(n):
    l=(''.join(random.sample((string.ascii_uppercase),3)))
    n=(''.join(random.sample((string.digits),4)))
    if len(n)<3:
        n='0'+str(n)
    else:
        n=str(n)
#ECUADORIAN PLATES DO NOT HAVE"D"
    if l == 'D':
        l=l=(''.join(random.sample((string.ascii_uppercase),D)))
    c.write(l+n+'\n')
c.close()


