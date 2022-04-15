l=[1,-6,9,-7,5,8,-8]
i=0
c=0
c1=0
while i<len(l):
    if l[i]>0:
        c+=1
    else:
        c1+=1
    i+=1
print("positive",c)
print("Negative",c1)
