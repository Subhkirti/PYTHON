l=["red","blue","yellow"]
k=[45,898,87]
d={}
for i in l:
    for j in k:
        d[i]=j
        k.remove(j)
        break
print(d)