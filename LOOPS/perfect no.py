a=int(input("enter:"))
i=1
sum=0
while i<a:
    if a%i==0:
        sum=sum+i
    i+=1
if sum==a:
    print(i,"is perfect")
else:
    print(i,"not perfect")
#whose sum of the factors is equal to numbers
#like 6=1x6
#     6=3x2
#     6=3x2
#     6=6x1

#  1+2+3=6