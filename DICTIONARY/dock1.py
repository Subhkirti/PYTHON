dict1 = {'a': 100, 'b': 200, 'c':200}
dict2 = {'a': 300, 'b': 200, 'd':400}
dic={}
for i in dict1:
    for j in dict2:
        if i in dict2:
            dic[i] = dict2[i] + dict1[i]
        elif j not in dict1:
            dic[j]=dict2[j]
        elif i not in dict2:
            dic[i]=dict1[i]
print(dic)