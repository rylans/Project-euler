import math
import time

past = time.time()

i=1000
s=0

while i>0:
    s=s+pow(i,i)

    i=i-1

print s

print "Elapsed: ", time.time() - past
