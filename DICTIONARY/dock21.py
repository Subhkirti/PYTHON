l=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

i=0
empty=[]
while i<len(l):
    for key in l[i]:
        if l[i][key] not in empty:
            empty.append(l[i][key])
        i+=1
print(empty)
