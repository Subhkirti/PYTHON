my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]} 
for j in my_dict:
    print(j,end=" ")
print(" ")
i=0
while i<len(my_dict):
    for k in my_dict:
        print(my_dict[k][i],end='  ')
    print()
    i+=1

    



 