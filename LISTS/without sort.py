# l=[3,5,9,54,34]
# i=0
# l1=[]
# max=0
# while i<len(l):
#     if l[i]>max:
#         max=l[i]
#     i+=1
# j=0
# while j<=max:
#     if j in l:
#         l1.append(j)
#     j+=1
# print(l1)
l=[[0],[1,2,3],[2,1],[2,3,4,5,6],[7,8,9,10],[11,12]]
i=0
l1=[]
max=0
while i<len(l):
    if len(l[i])>max:
        max=len(l[i])
        k=l[i]
    i+=1
j=0
while j<=max:
    if len(l[j])<max:
        l1.append(l[j])
    
    j+=1
l1.append(k)
print(l1)

# l=["a","bc","abc","sd","mk"]
# i=0
# l1=[]
# max=0
# k=0
# while i<len(l):
#     if len(l[i])>max:
#         max=len(l[i])
#         k=l[i]
#     i+=1
# j=0
# smax=0
# while j<len(l):
#     if len(l[j])<len(k):
#         if len(l[j])>smax:
#             smax=len(l[j])
#             p=l[j]
#     j+=1
# print(smax**max)