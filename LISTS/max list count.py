l=[[0],[1,3],[5,7],[9,11],[13,15,17]]
i=0
max=0
while i<len(l):
    j=0
    while j<len(l[i]):
        a=len(l[i])
        if max<a:
            max=a
            t=l[i]
        j+=1
    i+=1
print("max list:",max,"count:",t)
