num=30
n=[10,11,23,87,19,17,18,12,13]
i=0
x=[]
while i<len(n):
    j=i
    y=[]
    while j<len(n):
        if n[i]+n[j]==num:
            y.append(n[i])
            y.append(n[j])
            x.append(y)
        j+=1
    i+=1
print(x)