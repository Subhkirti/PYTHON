l=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5, 'Zachary Simon', 'VII']]
d={}
for i in l:
    j=0
    while j<len(i):
        d[i[0]]=[i[1],i[2]]
        j+=1
print(d)
