i=int(input("enter:"))#131,767
re=0
x=i
while i>0:
    re=(re*10)+i%10
    i=i//10
if x==re:
    print("polindrome")
else:
    print("not polindrome")
