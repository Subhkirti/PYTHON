l=[23,9.0,89,-67,"76","python","c#"]
i=0
k=[]
while i<len(l):
    if type(l[i])==int:
        k.append(l[i])
    i+=1
print(k)
