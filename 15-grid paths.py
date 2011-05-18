import time
import math
then = time.time()
# nxn grid
n = 20

def fct(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    pr = 1
    while n>1:
        pr = pr *n
        n=n-1
    return pr


paths = (fct(n*2))/((fct(n))*(fct(n)))
now = time.time()
print paths , "    in " , now-then , " seconds"
