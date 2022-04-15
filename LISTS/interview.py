a="I am kirti"
b=a.split()
i=0
l=[]
c=0
while i<len(b):
    if b[i] in b:
        l.append(b[i])
    if b[i]!=" " and c<len(b)-1:
        c+=1
        l.append("space"+str(c))
    i+=1
print(l)
