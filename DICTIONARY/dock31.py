my_dict={"item1": 45.50,"item2":35, "item3": 41.30, "item4":55,"item5": 24}
max=0
sec_max=0
third_max=0
l=[]
for i in my_dict:
    if my_dict[i]>max:
        max=my_dict[i]
        max_key=i
#print(max)
for j in my_dict:
    if my_dict[j]<max:
        if my_dict[j]>sec_max:
            sec_max=my_dict[j]
            sec_key=j
#print(sec_max)
for k in my_dict:
    if my_dict[k]<max:
        if my_dict[k]<sec_max:
            if my_dict[k]>third_max:
                third_max=my_dict[k]
                third_key=k
#print(third_max)
print(max_key,max)
print(sec_key,sec_max)
print(third_key,third_max)


