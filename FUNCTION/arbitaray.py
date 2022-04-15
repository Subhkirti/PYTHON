def multy(*l):
    i=0
    mul=1
    while i<len(l):
        mul=mul*l[i]
        i+=1
    print(mul)
multy(1,2,3,4,5,6)