#READING AND WRITING NEW DATA FROM THE DATA GENERATED WITH THE DATA GENERATOR

import biblioteca

def times():
    #hours unpacking 
    hour=[]
    docuh=open("hours.txt")
    for line in docuh:
        line=line.strip()
        hour.append(line)
    docuh.close()

    #Verify pico y placa hours with created library time function
    a=open("hbool.txt","w")
    for i in range(len(hour)):
        a.write(str(int(biblioteca.time(hour[i])))+'\n')
    a.close()

def days():
    #days unpacking
    date=[]
    docud=open("dates.txt")
    for line in docud:
        line=line.strip()
        date.append(line)
    docud.close()

    #Obtaining days from the full date entered
    b=open("dbool.txt","w")
    for j in range(len(date)):
        b.write(str(biblioteca.day(date[j]))+'\n')
    b.close()
    
def plates():
    #plate unpacking
    plates=[]
    docup=open("plates.txt")
    for line in docup:
        line=line.strip()
        plates.append(line)
    docup.close()

    #Obtaining the last digit of the plate
    c=open("pbool.txt","w")
    for k in range(len(plates)):
        c.write(str(int(biblioteca.plate(plates[k])))+'\n')
    c.close()
    





