def exp(x,y):
    if (y==0):
        return 1
    q = x
    i = 1
    while i < y:
	    q = q*x
	    i=i+1
    return q

    
def isPalindromic(n):
    digitlist = []
    if n < 10:
        return True
    else:
        i = 1
        while (exp(10,i)) <= n:
            i = i + 1
        digits = i
        #print "digits= ",digits

        x = n
        #print x
        z = 0
        while x > 0:
            count = 0
            z = z + 1 
            while x >= (exp(10,(digits-z))):
                       x = x - (exp(10,(digits-z)))
                       count = count + 1

            #print "Count = ", count
            #print "X = " , x
            
            digitlist.append(count)


        while len(digitlist) < digits:
            digitlist.append(0)

        #print digitlist

        foo = (digits-1)
        #print foo
        bar = 0
        #print digitlist[foo]
        isPal = True
        donothing = 0
        
        while foo > 0:
            if digitlist[foo] == digitlist[bar]:
                donothing = 2
            else:
                #print "no no no"
                isPal = False
                
            foo = foo - 1
            bar = bar + 1
            

        return isPal



def Iterate():
    i = 998001
    largest = 950000
    while i > largest:
        if isPalindromic(i):
            print i
        i = i - 1


def Iterate2():
    largest = 0
    a =1
    am = 999
    b = 1
    bm = 999

    while am > a:
        bm = 999
        while bm > b:
            #print am, ' ', bm
            if (isPalindromic(am*bm)):
                #print (am * bm)
                if (am*bm) > largest:
                    largest = (am*bm)
                    print largest
            bm = bm - 1
        am = am - 1

    return largest

Iterate2()

