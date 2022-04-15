marks=[[78,76,96,86,88],[91,71,98,65,76],[95,45,78,52,49]]
i=0
c=0
sum=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        sum=sum+marks[i][j]
        c+=1
        j+=1
    i+=1
print(sum,"Average",sum/c)