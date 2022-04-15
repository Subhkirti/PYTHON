i=1
while i<=1000:
    a=i
    sum=0
    while a>0:
        digit=a%10
        sum=sum+digit
        a=a//10
    if i%sum==0:
        print(i,"Harshad no")
    i+=1