#Problem 50
#May 17, 2011
#Which prime, below one-million, can be written as the sum of the most consecutive primes?
import math

BELOW_WHAT = 1000000

def isPrime(n):
    if n==0:
       return False
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
            if n%(f+2) == 0:
                return False
            f=f+6
        return True

#Generate a prime 
def primeGen():
    n = 1
    while 1:
        n += 1
        if(isPrime(n)):
            yield n


sos = {} #sums of sequences
def sumOfSequence(start,end,seq):
    outerkey = start
    innerkey = end

    if outerkey in sos:
        if (innerkey-1) in sos[outerkey]:
            val = sos[outerkey][innerkey-1] + seq[innerkey]
            d = {innerkey:val}
            sos[outerkey] = d
            return val
    
    val = sum(seq[start:end])
    d = {innerkey:val}
    sos[outerkey] = d
    return val

    

g = primeGen()
primelist = []
while True:
    p = g.next()
    if(p>=BELOW_WHAT):
        break
    primelist.append(p)


mx = 0
manchurian_candidate = 0
for i in range(len(primelist)):
    if(i%1000==0):
        print '.',
        
    for j in range(len(primelist)):
         if(i > j): continue
         sm = sumOfSequence(i,j,primelist)
         if(sm > BELOW_WHAT):
             break

         if(isPrime(sm)):
             l = len(primelist[i:j])
             if(l > mx):
                 mx = l
                 manchurian_candidate = sm
    
       
print
print manchurian_candidate
