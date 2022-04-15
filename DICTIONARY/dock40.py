l1=['S001', 'S002', 'S003', 'S004']
l2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
l3=[85, 98, 89, 92]
d={}
l=[]
for i in l1:
    for j in l2:
        for n in l3:
            d[i]={j:n}
            l2.remove(j)
            break
        l3.remove(n)
        break
         
print(d)

# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]
