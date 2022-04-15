l1=[5,6,[],5,7,[]]
k=[]
i=0
b=[]
while i<len(l1):
    if l1[i]!=k:
        b.append(l1[i])
    i+=1
print(b)