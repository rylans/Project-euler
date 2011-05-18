#product of 4  numbers on a line in 20x20 grid
import time
import math
now = time.time()

number = ''
y=0
array = []
text_file = open("11-2020grid.txt","r")
lines=text_file.readlines()


for line in lines:
    lst= []
    current = ''
    for a in line:
        lst.append(a)
    if '\n' in lst:
        lst.pop(len(lst)-1)
        lst.append(' ')
        #print lst
    for i in lst:
        number = number + i
        current = current + i
    array.append(current)
text_file.close()


ko = []
for u in array:
    ko.append(u.split(' '))
    

#iterate thru one by one
rowpos = 0
colpos = 0
biggest = 0

while rowpos <= 19:
    colpos=0
    while colpos <= 19:
        prod = 1

        #check down
        if rowpos <= 16:
            alpha = int(ko[rowpos][colpos])
            beta = int((ko[rowpos+1][colpos]))
            gamma = int((ko[rowpos+2][colpos]))
            delta = int((ko[rowpos+3][colpos]))

            prod = alpha * beta * gamma * delta


##            print "ABGD"
##            print alpha,beta,gamma,delta       
##            prod = int(ko[rowpos][colpos])
##            prod = prod * int((ko[rowpos+1][colpos]))
##            prod = prod * int((ko[rowpos+2][colpos]))
##            prod = prod * int((ko[rowpos+3][colpos]))
            if prod > biggest:
                biggest = prod
                #print "GOT BIG first"

        prod = 1
        #check right
        if colpos<=16:
            alpha = int(ko[rowpos][colpos])
            beta = int((ko[rowpos][colpos+1]))
            gamma = int((ko[rowpos][colpos+2]))
            delta = int((ko[rowpos][colpos+3]))

            prod = alpha * beta * gamma * delta

##            print "ABGD2"
##            print alpha,beta,gamma,delta            
##            prod = int(ko[rowpos][colpos])
##            prod = prod * int((ko[rowpos][colpos+1]))
##            prod = prod * int((ko[rowpos][colpos+2]))
##            prod = prod * int((ko[rowpos][colpos+3]))
            
            if prod > biggest:
                biggest = prod
                #print "GOT BIG sec"

        prod = 1
        #check downright diag
        if colpos<=16:
             if rowpos <=16:

                alpha = int(ko[rowpos][colpos])
                beta = int((ko[rowpos+1][colpos+1]))
                gamma = int((ko[rowpos+2][colpos+2]))
                delta = int((ko[rowpos+3][colpos+3]))

                prod = alpha * beta * gamma * delta
                
##                print "ABGD3"
##                print alpha,beta,gamma,delta                   
##                prod = int(ko[rowpos][colpos])
##                prod = prod * int((ko[rowpos+1][colpos+1]))
##                prod = prod * int((ko[rowpos+2][colpos+2]))
##                prod = prod * int((ko[rowpos+3][colpos+3]))
                if prod > biggest:
                    biggest = prod
                    #print "GOT BIG thirdt"


        #check downleft diag
        prod = 1
        if colpos>=3:
             if rowpos <=16:

                alpha = int(ko[rowpos][colpos])
                beta = int((ko[rowpos+1][colpos-1]))
                gamma = int((ko[rowpos+2][colpos-2]))
                delta = int((ko[rowpos+3][colpos-3]))

                prod = alpha * beta * gamma * delta

                
                if prod > biggest:
                    biggest = prod
                    #print "GOT BIG fourth"

        #print int(ko[rowpos][colpos]), ":: current biggst ", biggest

##        print ko[rowpos][colpos],
##        if colpos == 19:
##            print
##            
        colpos=colpos+1
    rowpos=rowpos+1


then = time.time()
print "biggest is: ", biggest
print "runtime: ", then-now

