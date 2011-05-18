import math
import time
past = time.time()

def fac(n):
    i=1
    z=1
    while i <= n:
        z=z*i
        i=i+1
    return z
        
def checkcurious(n):
    m = str(n)
    zum = 0
    for i in (m):
        zum = zum + (fac(int(i)))

    if n==zum:
        return True
    else:
        return False



i=3
tsum=0
while i < 100000:
    if(checkcurious(i)):
        tsum=tsum+i


    i=i+1


print tsum
now=time.time()
print "Elapsed: " , now-past
