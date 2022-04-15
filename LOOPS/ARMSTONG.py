i=int(input("enter no:"))
org=i
sum=0
while i>0:
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
if org==sum:
    print("Armstrong")
else:
    print("Not Armstrong")