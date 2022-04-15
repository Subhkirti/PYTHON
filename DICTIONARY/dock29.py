dict={"anjali":67,"lucky":45,"bobby":90,"dad":56}
max1=0
for j in dict:
    if j>str(max1):
        max1=j
h=(max1)
l=[]
for i in dict:
    if i<h:
        if i in dict:
            if i not in l:
                l.append(i)
l.append(h)
print(l)


 

