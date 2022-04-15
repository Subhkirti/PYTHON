# dic1={1:20,2:30,3:50}
# dic2={7:56,9:90,5:78}
# dic={}
# dic.update(dic1)
# dic.update(dic2)
# print(dic)

dic1={1:20,2:30,3:50}
dic2={7:56,9:90,5:78}
dic={}
for i in dic1:
    for k in dic2:
        dic[i]=dic1[i]
        dic[k]=dic2[k]
print(dic)


