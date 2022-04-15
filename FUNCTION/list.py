def calculator():
    numx=[5,10,50,20]
    numy=[2,20,3,5]
    i=0
    k=[]
    while i<len(numx):
        sum=numx[i]*numy[i]
        k.append(sum)
        i+=1
    print(k)
calculator()



