l=[123,144,136,12,123345]
i=0
while i<len(l):
    if l[i]//10//10==1:
        print(l[i]//10//10,"same")
    else:
        print(l[i]//10//10,"not same")
    i+=1
