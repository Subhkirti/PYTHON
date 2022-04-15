row=int(input("neter no of rows:"))
a=[]
for i in range(row):
    a.append([int(j) for j in input("enter:").split()])


# updation of array
a[0]=[2,3]
print(a)
