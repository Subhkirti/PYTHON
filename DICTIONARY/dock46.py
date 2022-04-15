p=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
i=0
l={}
q={}
s=[]
while i<len(p):
    t=p[0]
    y=p[1]
    i+=1
    for j in t:
        l[j]=float(t[j])
    for r in y:
        q[r]=float(y[r])
s.append(l)
s.append(q)
print(s)





    