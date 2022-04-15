l1=["0","1","2","3"]
l2=["red","green","blue","white"]
l3=["100","200","300","400"]
x=[]
i=0
while i<len(l3):
    k=l1[i]+l2[i]+l3[i]
    x.append(k)
    i+=1
print(x)