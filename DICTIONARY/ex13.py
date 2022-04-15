my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20,}
max=0
sec_max=0
third_max=0
l=[]
for i in my_dict:
    if my_dict[i]>max:
        max=my_dict[i]
        max_key=i
for j in my_dict:
    if my_dict[j]<max:
        if my_dict[j]>sec_max:
            sec_max=my_dict[j]
            sec_key=j
for k in my_dict:
    if my_dict[k]<max:
        if my_dict[k]<sec_max:
            if my_dict[k]>third_max:
                third_max=my_dict[k]
                third_key=k

l.append(max_key)
l.append(max)
l.append(sec_key)
l.append(sec_max)
l.append(third_key)
l.append(third_max)
print(l)
  
