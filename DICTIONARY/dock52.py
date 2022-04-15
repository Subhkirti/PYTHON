my_dict={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8,"i":89}
f=int(input("enter a number for first fifth only:"))
max=0
sec_max=0
third_max=0
fourth_max=0
fifth_max=0
six_max=0

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
for y in my_dict:
    if my_dict[y]<max:
        if my_dict[y]<sec_max:
            if my_dict[y]<third_max:
                if my_dict[y]>fourth_max:
                    fourth_max=my_dict[y]
                    fourth_key=y
for p in my_dict:
    if my_dict[p]<max:
        if my_dict[p]<sec_max:
            if my_dict[p]<third_max:
                if my_dict[p]<fourth_max:
                    if my_dict[p]>fifth_max:
                        fifth_max=my_dict[p]
                        fifth_key=p
l.append(max_key)
l.append(sec_key)
l.append(third_key)
l.append(fourth_key)
l.append(fifth_key)
if f==2:
    print([l[0],l[1]])
elif f==1:
    print([l[0]])
elif f==3:
    print([l[0],l[1],l[2]])
elif f==4:
    print([l[0],l[1],l[2],l[3]])
elif f==5:
    print([l[0],l[1],l[2],l[3],l[4]])



