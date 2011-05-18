import math
import time
import random

tstart = time.time()

maxim = 0


triangle = "3   \
           7 5  \
          2 4 6 \
         8 5 9 3"


triangle2 = "75  \
            95 64  \
        17 47 82  \
        18 35 87 10  \
        20 04 82 47 65  \
        19 01 23 75 03 34  \
        88 02 77 73 07 63 67  \
        99 65 04 28 06 16 70 92  \
        41 41 26 56 83 40 80 70 33  \
        41 48 72 33 47 32 37 16 94 29  \
        53 71 44 65 25 43 91 52 97 51 14  \
        70 11 33 28 77 73 17 78 39 68 17 57  \
        91 71 52 38 17 14 91 43 58 50 27 29 48  \
        63 66 04 68 89 53 67 30 73 16 69 87 40 31  \
        04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"


def children(w):
    m = random.randrange(0,2)
    return (w+m)

def iterate(rows):
    #start at rows[a][b]
    a,b=0,0
    j= len(rows)-1
    k = len(rows[j])-1
    #end at rows[j][k]
    big = 0

    tmp = ''

    npaths = 2**k
    paths = []
    print npaths
    pathlist = []

    n=0        
    while n < npaths:
        print n


        tmp = ''
        a=0
        currentindex = 0
        tbig=0
        while a <= j:
            
            tmp = tmp +' '+ str(rows[a][currentindex])
            
            tbig=tbig+int(rows[a][currentindex])
            currentindex=children(currentindex)
            a=a+1
        

        if tmp not in pathlist:
            print tmp
            print "BIG>",big
            pathlist.append(tmp)
            if tbig>big:
                big=tbig
            n=n+1

    return big


def do(rows):
    big=0
    tmp=0
    for i in range(0, len(rows) - 1):
        j = 0
        for k in rows[i+1]:
            rows[i+1][j] = max(int(k) + int(rows[i][j]),int(k) + int(rows[i][j+1]))
            j +=1

def recur(r,c,s):
    global rows
    global maxim
    #print "recur(",r,',',c,',',s,')'
    r+=1

    if r==len(rows):
        if s>maxim:
            maxim = s
        return
        

    for i in [0,1]:
        recur(r,c+i,s+int(rows[r][c+i]))
          


rows = triangle2.split('  ')

while '' in rows:
    rows.remove('')

for i in range(len(rows)):
    rows[i] = rows[i].split(' ')


    
recur(0,0,int(rows[0][0]))

timenow = time.time()

print maxim
print "Duration: " , timenow-tstart
#do(rows)
#print iterate(rows)
