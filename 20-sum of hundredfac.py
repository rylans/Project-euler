def Factorial(n):
    #its the factorial function
    p = 1
    while n > 1:
        p=p*n
        n=n-1

    return p


def Get_nth_digit(n,d):
    #(486128,3) returns int(6)
    if d == 0:
        return "ERROR"  
    digitlist = []
    i = 1
    while (exp(10,i)) <= int(n):
        i = i + 1
    digits = i
    h = digits - d
    big = exp(10,h)
    ntr =  (long(n)) / long(big)
    if ntr <= 9:
        return ntr
    else:
        stx = str(ntr)
        stx = stx[(len(stx)-1):]
        return int(stx)

fhk = Factorial(100)
zum = 0
for i in str(fhk):
    zum = zum + int(i)

print zum
