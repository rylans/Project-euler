import math
import time

past = time.time()

#How big is the spiral n x n
n = 1001

def spiralrecur(n, l):
    if n==1:
        return l+1
    a = ((n*n - n +1) + n*n)/2
    b = a - (2*n - 2)
    outermostlayer = (a*2) + (b*2)
    outermostlayer += l
    return spiralrecur((n-2),outermostlayer)



print "Sum of diagnols in ", n,'x',n, 'square is: ',spiralrecur(n,0)

now = time.time()

print "Elapsed: ", now - past

