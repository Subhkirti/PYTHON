d={1:24,2:56,3:54,4:67}
k=list(d.values())
max=0
i=0
while i<len(k):
    if  k[i]>max:
        max=k[i]
    i+=1
print(max,"max")
min=k[0]
for i in k:
    if i<min:
        min=i
print(min,"min")

