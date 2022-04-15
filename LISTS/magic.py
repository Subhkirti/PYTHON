# a=[[8,3,4],[1,5,9],[6,7,2]]
# i=0
# r1,r2,r3,c1,c2,c3,d1,d2=0,0,0,0,0,0,0,0
# while i<len(a):
#     r1=r1+a[0][i]
#     r2=r2+a[1][i]
#     r3=r3+a[2][i]
#     c1=c1+a[i][0]
#     c2=c2+a[i][1]
#     c3=c3+a[i][2]
#     d1=d1+a[i][i]
#     d2=d2+a[i][2-i]
#     i=i+1
# if r1==r2==r3==c1==c2==c3==d1==d2:
#     print("magic square")
# else:
#     print("not")

marks= [[8,3,4],[1,5,9],[6,7,2]]
i=0
while i<len(marks):
    sum1=0
    j=0
    while j<len(marks[i]):
        sum1=sum1+marks[j][i]
        j+=1
    i+=1
i=0
while i<len(marks):
    sum2=0
    j=0
    while j<len(marks[i]):
        sum2=sum2+marks[i][j]

        j+=1
    i+=1
p= 0
s= 0
for i in range(len(marks)):
    for j in range(len(marks[i])):
        if (i == j):
            p+= marks[i][j]
        if ((i + j) == (len(marks)- 1)):
            s+= marks[i][j]
if sum1==sum2==p==s:
    print("magic square")
else:
    print("Not Magic square")



    

