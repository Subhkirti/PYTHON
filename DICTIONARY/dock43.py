l=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
p={}
c=[]
t=[]
m=[]
for k,v in l:
    if k=="yellow":
        c.append(v)
        p[k]=c
    elif k=="blue":
        t.append(v)
        p[k]=t
    elif k=="red":
        m.append(v)
        p[k]=m
print(p)








