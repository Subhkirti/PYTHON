def unique():
    i=0
    p=[]
    while i<len(l):
        if i in l:
            if i not in p:
                p.append(i)
        i+=1
    print(p)
l=[1,2,3,3,3,4,4,3,7,5,2,7]
unique()