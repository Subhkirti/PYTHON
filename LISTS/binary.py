num=1001
sum=0
i=0
while i<len(num):
	r=num[i]%10
	sum=sum+r*pow(2,i)
	num[i]=int(num[i]/10)
	i+=1
print('decimal no. is:',sum)