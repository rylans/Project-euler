#find the sum of all primes below 2 million

import math
import time
past=time.time()
below_what=2000000

def isPrime(n):
    if n==1:
        return False
    elif n<4:
        return True
    elif n%2 == 0:
        return False
    elif n<9:
        return True
    elif n%3 == 0:
        return False
    else:
        r = int(math.sqrt(n)+1)
        f=5
        while f<=r:
            if n%f == 0:
                return False
            if n%(f+2)== 0:
                return False
            f=f+6
        return True


def sum_of_primes(n):
    i= 1
    som = 0
    while i < n:
        if isPrime(i):
            som=som+i
        i=i+1

        if (i%1000==0):
            print '.',
        if(i%50000==0):
            print

    return som


print sum_of_primes(below_what)

present = time.time()
print "Runtime: " , present-past
        
