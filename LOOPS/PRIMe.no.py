n=int(input("enter the number"))
i=1
while i<=n:
    j=1
    c=0
    while j<=i:
        if i%j==0:
            c+=1
        j+=1
    i+=1
if c==2:
    print(n,"prime number")
else:
    print(n,"not prime number")
     


# 1 to 100 prime
# i=1
# while i<=100:
#     j=1
#     c=0
#     while j<=i:
#         if i%j==0:
#             c+=1
#         j+=1
#     if c==2:
#         print(i,"prime")
#     else:
#         print(i,"not prime")
#     i+=1