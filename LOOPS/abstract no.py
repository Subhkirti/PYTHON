num=int(input("enter:"))
while num!=0:
    d=num%10
    n=num//10
    sum=d+n
    if sum==9:
        print(num,'abstract no')
        break
    else:
        print(num,'not abstract no')
        break