l=[12,4,7,8,8,7,9,7]
k=[]
i=0
occur=int(input("enter:"))
while i<len(l):
    if l[i]!=occur:
        k.append(l[i])
    i+=1
print(k)