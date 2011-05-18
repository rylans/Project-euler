#square of sums minus sum of squares for the first n nat numbers
n = 100
sdc=0
cds=0

for i in range(n):
    sdc=(sdc+((i+1)*(i+1)))
    cds = cds+(i+1)

cds = cds*cds

print "Answer for ", n , "terms is " , cds-sdc
