def upper():
    i=0
    count=0
    c=0
    while i<len(l):
        if l[i]>="A" and l[i]<="Z":
            c+=1         
        elif l[i]>='a' and l[i]<='z':
            count+=1
        i+=1
    print('lowercase',count)
    print('uppercase',c)
l="The quick Brown Fox"
upper()