i=int(input("enter no:"))
r=0
while i>0:
    r=(r*10)+i%10
    i=i//10
print("reverse:",r)