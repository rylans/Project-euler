def isEven(n):
    if n%2 == 0:
        return True
    else:
        return False




f1=1
f2=2
temp = 42
upto = 32
i = 1
current = 0
thesum = 0
while i <= upto:
    if i == 1:
        print i, ":", f1
        current = f1
        if isEven(current):
            thesum = thesum + current
    elif i == 2:
        print i, ":",  f2
        current = f2
        if isEven(current):
            thesum = thesum + current
    else:
        f3 = f1 + f2
        temp = f2
        f2 = f3
        f1 = temp

        print i, ":",  f3
        current = f3
        if isEven(current):
            thesum = thesum + current
    


    i=i+1


print "-----"
print thesum
    
