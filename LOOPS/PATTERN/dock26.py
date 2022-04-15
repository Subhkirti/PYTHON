r=1
s=8
while r<=5:
    print(" "*s,end=" ")
    c=r
    while c>1:
        print(c,end=" ")
        c=c-1
    k=0
    while k<r:
        print(c,end=" ")
        c+=1
        k+=1
    print()
    s=s-2
    r+=1

