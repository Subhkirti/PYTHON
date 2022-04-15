d={'V': [1, 4, 6, 10], 'VI': [1,3, 4, 12], 'VII': [1,3, 8]}
h={}
for i in d:
    k=d[i]
    q=[]
    for j in k:
        if j%2==0:
            q.append(j)
    h[i]=q
print(h)


     
