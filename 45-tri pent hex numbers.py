#Triangle Tn = n(n+1)/2
#Pentagonal Pn =n(3n-1)/2
#Hexagonal Hn = n(2n-1
grthan = 40755
INF = 500000

T = lambda n: n*(n+1)/2
P = lambda n: n*((3*n)-1)/2
H = lambda n: n*(2*n -1)

TL = map(T,range(1,INF))
PL = map(P,range(1,INF))
HL = map(H,range(1,INF))


##a1 = set(TL).intersection(set(PL))
##a2 = filter(lambda n: n>grthan, a1)
##a3 = set(a2).intersection(set(HL))
##print filter(lambda x: x, a3)

#print filter(lambda x: x, set(filter(lambda n: n>grthan, set(TL).intersection(set(PL)))).intersection(set(HL)))


print filter(lambda x:x, set(HL).intersection(set(PL)))





