import time
import math

tpast = time.time()

amicable_numbers_under_tenthousand = []

def d(n):
    sam = 0
    for i in range(1,(n/2)+1):
        if n%i == 0: sam=sam+i
    return sam

def isamicable(n):
    b = d(n)
    q = d(b)
    if n == b:
        return False
    else:
        if q==n:
            return True
        else:
            return False


for i in range(1,10001):
    if isamicable(i):
        amicable_numbers_under_tenthousand.append(i)
        print ".",
        
sumy = 0
for i in amicable_numbers_under_tenthousand:
    sumy = sumy + i



tnow=time.time()
print "Sum = ", sumy
print "This took: ", tnow-tpast

