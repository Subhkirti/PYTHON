list=[6,1,3,5,6,3,1]
l1=[]
i=1
while i<len(list):
    if i in list:
        if i not in l1:
            l1.append(i)
      
    i+=1
m=1
for j in l1:
    m=m*j
print("Product is:",m)

