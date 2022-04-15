l=[1,2,3,4,5,7]
j=1
i=0
x=[]
while j<len(l):
    d=l[j]-l[i]
    x.append(d)
    j+=1
    i+=1
print(x)