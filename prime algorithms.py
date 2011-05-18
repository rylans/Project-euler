import time
import math

n=46842

#slow, primative method
def isPrime(n):
    #n is prime if it is not divisible by any number before it
    i=2 
    if (n==1):
        return False
    while i < n:
        if(n%i == 0):
            return False
        i=i+1
    return True


#is prime half
def isPrime2(n):
    #n is prime if it is not divisible by any number before it
    i=2 
    if (n==1):
        return False
    while i < ((n/2)+1):
        if(n%i == 0):
            return False
        i=i+1
    return True

#is prime upto sqrt
def isPrime3(n):
    #n is prime if it is not divisible by any number before it
    i=2 
    if (n==1):
        return False
    while i < int(math.sqrt(n)+1):
        if(n%i == 0):
            return False
        i=i+1
    return True


#from psuedo code on euler
def isPrime4(n):
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

    
def Get_nth_prime(n):
    #primes found
    pf = 0
    i=1
    while pf<n:
        if(isPrime(i)):
            pf=pf+1
        if(i%1000==0):
            print '.',
        if(i%10000==0):
            print            
        
        i=i+1
    print
    print (i-1)
    return (i-1)

def Get_nth_prime2(n):
    #primes found
    pf = 0
    i=1
    while pf<n:
        if(isPrime2(i)):
            pf=pf+1
        if(i%1000==0):
            print '.',
        if(i%10000==0):
            print            
        
        i=i+1
    print
    print (i-1)
    return (i-1)

def Get_nth_prime3(n):
    #primes found
    pf = 0
    i=1
    while pf<n:
        if(isPrime3(i)):
            pf=pf+1
        if(i%1000==0):
            print '.',
        if(i%10000==0):
            print            
        
        i=i+1
    print
    print (i-1)
    return (i-1)

def Get_nth_prime4(n):
    #primes found
    pf = 0
    i=1
    while pf<n:
        if(isPrime4(i)):
            pf=pf+1
        if(i%1000==0):
            print '.',
        if(i%10000==0):
            print            
        
        i=i+1
    print
    print (i-1)
    return (i-1)


##now = time.time()
##Get_nth_prime(n)
##then = time.time()
##print "Runtime = ", then-now
##print
##
##now = time.time()
##Get_nth_prime2(n)
##then = time.time()
##print "Runtime = ", then-now
##print

now = time.time()
Get_nth_prime3(n)
then = time.time()
print "Runtime = ", then-now
print

now = time.time()
Get_nth_prime4(n)
then = time.time()
print "Runtime = ", then-now
print


