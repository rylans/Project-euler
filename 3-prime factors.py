#prime factors

def isPrime(n):
    i = 2
    while i < n:
        if n%i == 0:
            return False
        i=i+1

    return True
           
value = 600851475143
cval = value
largest = 0
pfl = []
i = 2
while i < value:
    if value%i == 0:
        if isPrime(i):
            if i > largest:
                largest = i
            value = value/i
            i = 1
    i = i + 1

if value>largest:
    largest = value
    
print largest
