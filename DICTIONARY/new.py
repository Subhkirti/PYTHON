l=[1,2,3,4,5,6,7,8]
dic={}
i=0
b=[]
while i<len(l):
    j=0
    c=[]
    while j<=3:
        c.append(l[i])
        j+=1
        i+=1
    b.append(c)
a=b
j=0
while j<len(a):
    dic["C1"]=a[0]
    dic["C2"]=a[1]
    j+=1
print(dic)