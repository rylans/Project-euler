import time
import math
past = time.time()

def power5(n):
    return (n*n*n*n*n)

def power4(n):
    return (n*n*n*n)

def digits(n):
    m = str(n)
    zum = 0
    for i in m:
        zum = zum + power5(int(i))
        

    
    if n==zum:
        print n,' ',zum
        return True
    else:
        return False



i=2
finalsum=0
while i < 1000000:
    if(digits(i)):
        finalsum=finalsum+i
    if(i%10000==0):
        print '.',
    i=i+1



print finalsum
now = time.time()
print "Elapsed: ", now-past
