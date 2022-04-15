l=["1","2","3","4","5","6"]
i=0
p=[]
while i<len(l)-1:
    j=1
    while j<len(l):
        k=l[i]+l[j]
        p.append(k)
        j+=1
        i+=1
print(p)