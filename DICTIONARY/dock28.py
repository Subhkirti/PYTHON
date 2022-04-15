num_list = [1, 2, 3, 4]
e = {}
dic=e
for i in num_list:
    e[i] = {}
    e=e[i]
print(dic)
