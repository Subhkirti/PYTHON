

l=[1,2,3,4,5,6,7,8]
i=0
se=0
so=0
while i<len(l):
	if l[i]%2==0:
		se=se+l[i]
	else:
		so=so+l[i]
	i+=1
print('sum of even:',se)
print('sum of odd:',so)