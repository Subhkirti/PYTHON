l=[3,5,4,7,5,14,2,3,5,9]
i=4
while i<len(l):
    if i%4==0:
        l.insert(i,20)
    i+=4
print(l)