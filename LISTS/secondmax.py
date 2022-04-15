a=[50,40,23,70,56,12,5,10,7]
i=0
max=0
while i<len(a):
    if a[i]>max:
       max=a[i]
    i+=1
print("max:",max)
j=0
smax=0
while j<len(a):
    if a[j]<max:
        if a[j]>smax:
            smax=a[j]
    j+=1
print("second max:",smax)

