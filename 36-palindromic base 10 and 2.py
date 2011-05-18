import math
import time


def DecToBin(n):
    ##converts like 56 to 11100
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 10
    
    binlst = []

    iop=[]

    while n>0:
        i = 1
        while math.pow(2,i) <= n:
            i=i+1
        i=i-1

        mp = math.pow(2,i)
        n=n-mp

        iop.append(int((math.log(mp,2))))

    for q in range(iop[0]):
        binlst.append(0)
    binlst.append(0)

    for l in iop:
        binlst[(-1*(l+1))] = 1

    
    strint = ''
    for i in binlst:
        strint+=str(i)

    return int(strint)
        

    



for i in range(0, 8):
    print DecToBin(i)
        
    
