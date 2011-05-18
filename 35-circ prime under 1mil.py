import math
import time
past = time.time()

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
            if n%(f+2) == 0:
                return False
            f=f+6

       #print n, ' is prime'
        return True


def Swap(string, index1, index2):
    tmp = string[index2]
    string[index2] = string[index1]
    string[index1] = tmp
    return string
    
def all_perms(st):
    if len(st) <= 1:
        yield st
    else:
        for perm in all_perms(st[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + st[0:1] + perm[i:]


def ListToInt(lst):
    strang = ''
    for i in range(len(lst)):
        strang += str(lst[i])
    return int(strang)

def isCircPrime(n):
    """A number is circ prime when all rotations of digits
        are prime """
    if (n<10):
        return isPrime(n)
    else:
        ns = str(n)
        nl = []
        for i in ns:
            nl.append(int(i))

        for p in all_perms(nl):
            q = ListToInt(p)
            
            if isPrime(q) == False:

                return False

        return True
        
    
    
u = 2
limit = 10000
count=0
while u < limit:
    if isCircPrime(u):
        count += 1
        print u
    if u%1000 == 0:
        print ":",

    u+=1

print
now = time.time()
print "There are : " , count , " circ primes under " , limit
print "time elapsed: " , now - past    


print isCircPrime(1193)
print isCircPrime(197)
