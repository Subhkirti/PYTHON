n=int(input("enter:"))#5
i=1
while i<=n:
    s= i**2
    if s%2==0:
        print("+"+str(s),end="")
    elif s==1:
        print("1",end="")
    else:
        print("-"+str(s),end="")
    i+=1
    
