num=int(input("enter num"))
i=num
sum=0
while i!=0:
	digit=i%10
	sum=sum+digit
	i=int(sum/10)
if num%sum==0:
	print(num,"harshad no")
else:
	print(num,'not a harshad')


