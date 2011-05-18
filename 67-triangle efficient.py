import math
import time
past = time.time()

## -- Just getting the stuff out of the file
triangle_file = open('67-trianglenum.txt')
tri_lst = triangle_file.readlines()
tri_str = ''
for i in tri_lst:
    tri_str += i
tri_lst = tri_str.split('\n')
while '' in tri_lst:
    tri_lst.remove('')
    
j=0
while j < len(tri_lst):
    tri_lst[j] = str(tri_lst[j]).split(' ')
    j+=1

def inty(tri):
    len_c = len(tri)
    j=0
    
    while j < len_c:
        i=0
        while i < len(tri[j]):

            tri[j][i] = int(tri[j][i])   
            i+=1
        j+=1

    return tri



## -- Put in example triangle
tri_lst2 = [[3],[7,4],[2,4,6],[8,5,9,3]]


def makesumtriangle(tri):
    ##sum triangle is like the original triangle but you add it up
    sumtri = tri

    len_c = len(tri)

    j=0
    while j < len_c:
        i=0
        #print
        while i < len(tri[j]):
            #print tri[j][i],


            a=0
            b=0
            if j>i:
                b = sumtri[j-1][i]

            if j>0 and i>0:
                a = sumtri[j-1][i-1]
 
            c = tri[j][i]
            sumtri[j][i] = max(a+c,b+c)        
            i+=1
        j+=1
    return sumtri


#real one
tri_lst = inty(tri_lst)


f = makesumtriangle(tri_lst)

lf = len(f)
lf = lf-1

print "Max = " , max(f[lf])
print "Elapsed: ", time.time() - past


