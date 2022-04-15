l= [[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
max=0
i=0
while i<len(l):
    j=0
    while j<len(l[i]):
        if l[i][j]>max:
            max=l[i][j]
            j+=1
        i+=1
print(max)