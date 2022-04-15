a=[[1,2,4],[2,4,4],[1,2]]
i=0
sum=0
while i<len(a):
    j=0
    sum=0
    while j<len(a[i]):
        sum=sum+a[j][i]
        j+=1
    print(sum)
    i+=1
