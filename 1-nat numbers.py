#below what
bw = 1000

#multiples of what
m1 = 3
m2 = 5


i = 1
mc=0
while i < bw:
    if i%m1 == 0 or i%m2 == 0:
        print i
        mc = mc + i
        

    i = i + 1

print "----"
print mc
