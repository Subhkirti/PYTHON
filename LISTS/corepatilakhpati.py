p=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
i=0
count=0
k=0
j=0
while i<len(p):
	if p[i]>=10000000:
		count+=1
	elif p[i]>=100000:
		j+=1
	else:
		k+=1
	i+=1
print(count,'crorepati')
print(j,'lakhpati')
print(k,'dilwale')