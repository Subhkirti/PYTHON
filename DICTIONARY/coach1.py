t='my name is kirti'
h=t.split( )
j=0
while j<len(h):
    if j%2!=0:
        h.insert(j," ")
    j+=1
        
a=h
c=1
i=0
dic={}
s="space"
count=1
while i<len(a):
    if a[i]==" ":
        dic[c]=s+str(count)
        count+=1
    else:
        dic[c]=a[i]
    c+=1
    i+=1
print(dic)