a=[[78,76,94,86],[22,11,33,44],[34,32,65,42]]
i=0
sum=0
while i<len(a):
	j=0
	while j<len(a[i]):
		sum=sum+a[i][j]
		j+=1
	i+=1
print(sum)