l=[12,67,98,341]
i=0
while i<len(l):
    k=l[i]%10
    k1=l[i:]//10
    sum=k+k1
    print(sum,end=" ")
    i+=1