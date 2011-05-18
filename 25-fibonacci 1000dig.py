import time
import math

past = time.time()


def fibonacci_gen():
    f1 = 1
    yield f1
    f2 = 1
    yield f2

    while 1:
        fn = f1+f2
        yield fn
        f2=f1
        f1=fn

def numberofdigits(n):
    #this returns the number of digits of n
    m = str(n)
    return len(m)
    
a=fibonacci_gen()


i=1
nm = 0
while nm <= 1000:
    q = a.next()
    nm = numberofdigits(q)

    if nm==1000:
        print q, ' -- ', nm , ' ', i

    i=i+1


now=time.time()
print "Elapsed time: " , now-past


