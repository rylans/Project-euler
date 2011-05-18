#smallest numb evenly divis by 1 to 20


def isDiviz(n,m):
    #checks if divizible by 1 to 20
    i = 1
    while i <= m:
        if n%i != 0:
            return False
        i=i+1
    return True

def isPrime(n):
    i = 2
    while i < n:
        if n%i == 0:
            return False
        i=i+1
    return True


def Primes(n):
    #finds primes from 2 upto and including n then multiplies them
    i = 2
    p = 1
    while i <= n:
        if isPrime(i):
            p = p * i
        i=i+1
    return p



def Do(n):
    z = Primes(n)
    #print z 
    if isDiviz(z,n):
        return z
    else:
        npl=[]
        i = 1
        while i <= n:
            if (not (isPrime(i))):
                npl.append(i)
            i=i+1
            
        #print npl
        rx = z
        
        for index in npl:
            rx = rx * index
            #print rx
            if isDiviz(rx,n):
                #print "rx = ", rx
                Nextstep(rx,n)
                return 0


def Nextstep(z,n):
    numba = z
    #clean the number x times
    x = 5
    
    
    npl=[]
    i = 1
    while i <= n:
        npl.append(i)
        i=i+1
        
    while x > 0:

        for index in npl:
            #print numba, index
            if isDiviz((numba/index),n):
                numba = numba/index
                #print "Dividing ", numba , " by " ,index

        x=x-1
            
                
    print "---"
    print numba
            

Do(20)
    
