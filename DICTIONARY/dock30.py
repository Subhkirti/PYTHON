l={'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
k=" "
r={}
for i in l:
    str1=""
    for j in i:
        if j!=k:
            str1+=j
    r[str1]=l[i]
print(r)