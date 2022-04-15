d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
list2=[]
e={}
dic={}
p={}
l={}
for i in d:
    e[i]=d[i][0]
    dic[i]=d[i][1]
    p[i]=d[i][2]
    l[i]=d[i][3]
print([e,dic,p,l])


  
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
