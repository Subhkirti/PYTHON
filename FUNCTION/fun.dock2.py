def max(n):
    i=0
    max=0
    while i<len(n):
        if n[i]>max:
            max=n[i]
        i+=1
    print(max)
    j=0
    smax=0
    while j<len(n):
        if n[j]<max:
            if n[j]>smax:
                smax=n[j]
        j+=1
    print(smax)
    k=0
    tmax=0
    while k<len(n):
        if n[k]<max:
            if n[k]<smax:
                if n[k]>tmax:
                    tmax=n[k]
        k+=1
    print(tmax)

max(n=[50,40,23,70,56,12,5,10,7])
