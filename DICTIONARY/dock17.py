dict={"a":45,"d":97,"b":99,"c":7}
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