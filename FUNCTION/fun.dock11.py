def step(min,max,step):
   
    j=min
    k=[]
    while j<=max:
        k.append(j)
        j+=step
    print(k)
step(min=int(input("enter your minimum no:")),max=int(input("entetr your maximum no:")),step=int(input("enter your steps:")))

