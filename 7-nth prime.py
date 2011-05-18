#find the nth prime Number
import time
now = time.time()


n=10001


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
    
def Get_nth_prime(n):
    #primes found
    pf = 0
    i=1
    while pf<n:
        if(isPrime(i)):
            pf=pf+1
        if(i%1000==0):
            print '.'
        
        i=i+1

    print (i-1)
    return (i-1)

def List_primes(n):
    #lists primes upto n
    pf = 0
    i=1
    while pf<n:
        if(isPrime(i)):
            pf=pf+1
            print pf,": ",i

        i=i+1

#List_primes(n)
Get_nth_prime(n)


then = time.time()
runtime = then - now
print "Runtime = ", runtime
