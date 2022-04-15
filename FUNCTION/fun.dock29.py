def multiples(limit):
    for i in range(1,limit+1):
        if i%3==0 or i%5==0:
            print(i,end=" ")
multiples(int(input("enter:")))
        
