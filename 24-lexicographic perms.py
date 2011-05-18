import time
import math
from itertools import permutations
tnow = time.time()
OBJECTS = [0,1,2,3]
OBJECTS2 = [0,1,2,3,4,5,6,7,8,9]
##
##def switch(a,b,lst):
##    #switches the a,b position in lst
##    x = lst[a]
##    y = lst[b]
##    lst[a],lst[b]=y,x
##    return lst
##    
##def NPerms(lst):
##    #returns the factorial of length of lst
##    q = len(lst)+1
##    n=1
##    for i in range(1,q):
##        n*=i
##    return n
##        
##
##elements = OBJECTS
##
##permuts = []
##for i in range(len(elements)):
##    print elements
##    switch((len(elements)-1),i,elements)
##
##    
##    
##    
##    
    
def permutations (orig_list):
    if not isinstance(orig_list, list):
        orig_list = list(orig_list)

    yield orig_list

    if len(orig_list) == 1:
        return

    for n in sorted(orig_list):
        new_list = orig_list[:]
        pos = new_list.index(n)
        del(new_list[pos])
        new_list.insert(0, n)
        for resto in permutations(new_list[1:]):
            if new_list[:1] + resto <> orig_list:
                yield new_list[:1] + resto


fqg = list(permutations(OBJECTS2))

print fqg[999999]
print fqg[1000000]

sorted(

tk = time.time()
print "time: ",tk-tnow

