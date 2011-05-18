import time
import math
past=time.time()


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
            if n%(f+2)== 0:
                return False
            f=f+6
        return True


def FactorN(n):
    #factors like 28 into 1,2,4,7,14,28
    #returns 6, cuz thats how many
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 2
    count = 0
    i = 1
    while i < (n/2)+1:
        if n%i==0:
            count=count+1
        i=i+1
    return (count+1)


def Factor2(n):
    #tries to factor things with sqrt'd not halved
    if n==0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 2
    if n==5:
        return 2
    if n==7:
        return 2
    if n==3:
        return 2
    count = 0
    i = 1
    while i < int(math.sqrt(n)+1):
        if n%i==0:
            count=count+1
        i=i+1
    return (2*count)    

def split(n):
    #takes 9 and returns (3,3)
    #takes 14 returns (2,7)
    i = 2
    while i < n:
        if n%i == 0:
            return [i,(n/i)]
        i=i+1
    return 0




def Factor3(n):
    #resolve to prime factors then use
    #d(n) = (a+1)(b+1)(c+1)
    product = 1
    
    uniquelist = []
    exponent = 1
    for i in n:
        if i not in uniquelist:
            uniquelist.append(i)
    many = len(uniquelist)
    
    exp=[]
    for i in range(many):
        exp.append(int(0))

    i=0
    while i<=(many-1):
        exp[i] = n.count(uniquelist[i])
        product = product * (exp[i] +1)
        i=i+1

    print product
        
    

def GetPrimeFacts(n):
    #takes 28 and returns [2,2,7]
    #takes [12,9] and returns [2,2,3,3,3]
    allgood = True
    for z in n:
        if not isPrime(z):
            allgood = False
    if allgood == True:
        Factor3(n)
        return n
    m = []
    for i in n:
        if isPrime(i):
            m.append(i)
        if not isPrime(i):
            splut = split(i)
            m.append(splut.pop(0))
            m.append(splut.pop(0))
            GetPrimeFacts(m)

       
        

def GetFactors(n):
    #takes 28 and returns (1,2,4,7,14,28)
    if n==0:
        return 0
    if n==1:
        print " A ONE JUST HAPPEND ZOMG"
        return 0
    if n==2:
        return 2
    if n==3:
        return 3
    if n==5:
        return 5
    if n==7:
        return 7
    
    factors = []
    i=2
    while i <=(int(math.sqrt(n)+1)):
        if n%i == 0:
            factors.append(i)
            if n/i not in factors:
                factors.append(n/i)
        i=i+1

    factors.sort()

    primes=[]

    subsid=[]
    for i in factors:
        if isPrime(i):
            primes.append(i)
        else:
            subsid.append((split(i)))


    for k in subsid:
        tmp = []
        tmp = subsid.pop(0)
        for j in tmp:
            if isPrime(j):
                primes.append(j)
            else:
                GetFactors(j)

            


    
    factors.sort()

    return primes

    

    



def Triangles(n):
    #find first triangle number with over n factors
    done = False
    i=1
    trang = 0
    while not done:
        z = 1
        trang=trang+i
        if i%10 == 0:
            print '.',
        if i%100 == 0:
            print
        if (Factor2(trang))>n:
            done = True
        i=i+1
    return trang


def PrintTri(n):
    i=1
    trang = 0
    while i < n:
        z = 1
        trang=trang+i
        i=i+1
        print trang

    
#PrintTri(50)
print Triangles(80)

now = time.time()
print "Runtime: ", now - past
    
    
