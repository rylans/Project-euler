import math
import time

def exp(x,y):
    v=1
    if x==0:
        return 0
    if y==0:
        return 1   
    i = 1
    while i<=y:
        v = v*x
        i=i+1
    return v

def add_digits(x):
    sx = str(x)
    sm=0
    lst = []
    for i in sx:
        lst.append(i)
    for i in lst:
        sm = sm + int(i)

    return sm

timepast = time.time()
print add_digits(exp(2,1000))
timenow = time.time()

print "Duration: ", timenow - timepast

    
