dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic={}
for i in dic1:
    for j in dic2:
        for f in dic3:
            dic.update(dic1)
            dic.update(dic2)
            dic.update(dic3)
print(dic)