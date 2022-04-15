l=["a","b","c","d","e","f","g"]
p=3
k=[]
while p<len(l):
    k.append(l[p])
    p+=1
    i=0
    m=[]
    while i<3:
        m.append(l[i])
    i+=1
print(k+m)