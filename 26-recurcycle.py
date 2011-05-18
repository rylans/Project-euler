import time
import math
past = time.time()

def redig(z):
    s = repr(z)
    s = s[2:]
    lst = []
    for i in range(len(s)):
        lst.append(s[i])

    print lst



curmax = 0
i = 2
while i < 20:
    redig(1.0/i)

    i=i+1

    
