import time
import math
now = time.time()

def lettervalue(a):
    """A returns 1, B returns 2 , etc"""
    x = a.upper()
    if x=='A':
        return 1
    elif x=='B':
        return 2
    elif x=='C':
        return 3
    elif x=='D':
        return 4
    elif x=='E':
        return 5
    elif x=='F':
        return 6
    elif x=='G':
        return 7
    elif x=='H':
        return 8
    elif x=='I':
        return 9
    elif x=='J':
        return 10
    elif x=='K':
        return 11
    elif x=='L':
        return 12
    elif x=='M':
        return 13
    elif x=='N':
        return 14
    elif x=='O':
        return 15
    elif x=='P':
        return 16
    elif x=='Q':
        return 17
    elif x=='R':
        return 18
    elif x=='S':
        return 19
    elif x=='T':
        return 20
    elif x=='U':
        return 21
    elif x=='V':
        return 22
    elif x=='W':
        return 23
    elif x=='X':
        return 24
    elif x=='Y':
        return 25
    elif x=='Z':
        return 26

def lettervalue2(a):
    """A returns 1, B returns 2 , etc"""
    x = a.upper()
    return (ord(x)-64)
    

def metascore(string):
    """COLIN is worth 3+15+12+9+14=53"""
    slist = []
    for i in string:
        slist.append(i)

    #print slist
    added = 0
    for i in slist:
        added = added+(lettervalue2(i))

    return added


txt_file = open("22-names.txt","r")
lines=txt_file.read()
txt_file.close()

namelist = lines.split(',')
for i in range(len(namelist)):
    a = namelist[i]
    a = a[1:-1]
    namelist[i]=a

namelist.sort()



totalscore = 0
for i in namelist:
    #print i,' ',namelist.index(i)+1,' ',metascore(i)
    totalscore = totalscore + (namelist.index(i)+1)*metascore(i)


print totalscore
future=time.time()
print "Elapsed: ", future-now



    
