import math
import time
#start number = n
then = time.time()
n = 48
length = 0
global hashtable
hashtable = {1:1,2:2}


##def ChainLeng(n):
##    #input starting number
##    #ouput length of the chain
##    length=0
##    while n > 1:
##        length += 1
##        if (n%2 == 0):
##            n = (n/2)
##        else:
##            n = ((3*n) +1)
##    length += 1     
##    return length

def LengHash(n,l):
    #start at l=1
    if n in hashtable:
        
        return (hashtable[n])   
    elif n%2 == 0:
        n = n/2
    else:
        n = (3*n)+1

    #print n , " " , (l+1)
    return (LengHash(n,l+1))

        

    
biggest = 0
bv =0
i=60000
while i > 1:
    #print ChainLeng(i), biggest
    if ChainLeng(i) > biggest:
        biggest = ChainLeng(i)
        bv = i
    if i%10000 == 0:
        print ". ",
    if i%100000 == 0:
        print
    i=i-1

now = time.time()
print
print bv , "  in  ", now-then , " seconds"
print hashtable
