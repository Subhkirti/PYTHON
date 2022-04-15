my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
l=list(my_dict.values())
j=[]
i=0
max=0
while i<len(l):
    if l[i]>max:
        max=l[i]
    i+=1
j=0
smax=0
while j< len(l):
    if l[j]<max:
        if l[j]>smax:
            smax=l[j]
    j+=1

k=0
tmax=0
while k<len(l):
    if l[k]<max:
        if l[k]<smax:
            if l[k]>tmax:
                tmax=l[k]
    k+=1
print(tmax,smax,max)