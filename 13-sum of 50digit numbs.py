#Work out the first ten digits of the sum of the following
#one-hundred 50-digit numbers.
import time
import math
now = time.time()



def exp(x,y):
    if (y==0):
        return 1
    q = x
    i = 1
    while i < y:
	    q = q*x
	    i=i+1
    return q

def Get_nth_digit(n,d):
    #(486128,3) returns int(6)
    if d == 0:
        return "ERROR"  
    digitlist = []
    i = 1
    while (exp(10,i)) <= int(n):
        i = i + 1
    digits = i
    h = digits - d
    big = exp(10,h)
    ntr =  (long(n)) / long(big)
    if ntr <= 9:
        return ntr
    else:
        stx = str(ntr)
        stx = stx[(len(stx)-1):]
        return int(stx)


number = ''
y=0
array = []
text_file = open("13.txt","r")
lines=text_file.readlines()

for line in lines: 
    array.append(line)
text_file.close()

while y <= (len(array)-1):
    
    if '\n' in array[y]:
        tmp = array[y]
        array[y] = tmp[:(len(tmp)-1)]

    y += 1

primsum = 0
for po in range(len(array)):
    print primsum
    primsum = long(primsum) + long(array[po])

print primsum , ">>>>><<<<"


print array
#print len(array[0])
colsum = []
for i in range(len(array[0])-2):
    print Get_nth_digit((array[0]),(i+1)), ' ',

ui = 0
s= 0
up = 1

while up <= len(array[0]):
    ui=0
    s=0
    while ui < len(array):
        #print ui
        z = (Get_nth_digit((array[ui]),(up)))
        #print "z= " , z
        s=s+z
        ui=ui+1
    colsum.append(s)
    up=up+1
    
print colsum

    

