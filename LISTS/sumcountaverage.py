l=[1,2,3,4,5,6,7,8]
i=0
se=0
ce=0
co=0
so=0
while i<len(l):
	if l[i]%2==0:
		se=se+l[i]
		ce+=1
	else:
		so=so+l[i]
		co+=1
	i+=1
print('sum of even:',se)
print('sum of odd:',so)
print('Total sum',se+so)
print('Average of even:',se/len(l))
print('Average of odd:',so/len(l))
print('Toatal Average:',(se/len(l))+(so/len(l)))
print('count of even:',ce)
print('countof odd:',co)
print('Toatl count:',ce+co)