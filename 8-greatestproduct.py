import time
import math
now = time.time()

number = ''
lst = []
text_file = open("8-1000digtnumb.txt","r")
lines=text_file.readlines()
for line in lines:
    lst = []
    for a in line:
        lst.append(a)
    if '\n' in lst:
        lst.pop(len(lst)-1)
    for i in lst:
        number = number + i
text_file.close()

#print number
#print (int(number))


nmb = []
for n in number:
    nmb.append(int(n))


#print nmb
indx = 0

consec = 5
limit = 1000-consec
lip = []
biggest=0

while indx <= limit:
    lip=[]
    section = number[(indx):((consec+(indx)))]
    for i in section:
        lip.append(int(i))

    product = 1
    for i in lip:
        product = product *i


    if product > biggest:
        biggest = product
    

    indx=indx+1
    






then = time.time()
print "biggest is: ", biggest
print "runtime: ", then-now

