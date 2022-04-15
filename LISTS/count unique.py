l=[1,2,2,5,8,4,4,8]
l1=[]
i=0
c=0
while i<=len(l):
    if i in l:
        if i not in l1:
            l1.append(i)
        c+=1
    i+=1
print(l1,"count is:",c)