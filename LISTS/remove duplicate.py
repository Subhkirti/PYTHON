l=[1,2,3,2,2,1]
l1=[]
i=1
while i<len(l):
    if i in l:
        if i not in l1:
            l1.append(i)
    i+=1
print(l1)