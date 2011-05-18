#Problem 69 - Project Euler - Nov 10, 2010


def phi(n):
    c = 1
    inc = 1
    for i in range(2,n):
        if(n%i>0):
            for j in range(2 , (n/i)+1):
                if(i*j == n):
                    inc = 0
            if(inc):
                c += 1
            inc = 1

                   
    return c


for i in range(2,11):
    print i, phi(i)
