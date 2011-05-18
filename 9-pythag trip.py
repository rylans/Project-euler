#pythagorean triplet
# a < b < c
#a^2 + b^2 = c^2
#find abc when a + b + c = 1000
import math
import time

for i in range(430):
    #print i,': ',(i*i)
    sqrt = (i*i)

    triplist = []
    for q in range(i):
        sqrt2 = (q*q)
        test = math.sqrt(float(sqrt) - float(sqrt2))
        if int(test) == float(test):
            triplist.append(test)

    if len(triplist)>=3:
        if len(triplist)==3:
            c = triplist.pop(0)
            b = triplist.pop(0)
            a = triplist.pop(0)
            print "a,b,c = ", a,' ',b,' ',c
            if (a + b + c) == 1000:
                print "-----"
                print "Eureka!! ", a*b*c
                print a , b , c
                print "-----"

        else:
            c = triplist.pop(0)
            notrps = (len(triplist))/2
            leng = (len(triplist)-1)
            #print "there are ", notrps, ' in ' ,i

            for i in range(notrps):
                #print triplist[i], ' ',triplist[leng-i]
                a,b=triplist[i],triplist[leng-i]
                
                print "a,b,c = ", a,' ',b,' ',c                
                if(a + b + c) == 1000:            
                    print "-----"
                    print "Eureka!! ", a*b*c
                    print a , b , c
                    print "-----"

                    
            
