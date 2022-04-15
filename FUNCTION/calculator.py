def calculator(numx,numy,operation):
    if op=="+":
        add=numx+numy
        return add
    elif op=="-":
        sub=numx-numy
        return sub
    elif op=="*":
        multi=numx*numy
        return multi
    elif op=="/":
        divide=numx/numy
        return divide
numx=int(input("enter:"))
numy=int(input("enter:"))
op=input("enter operator:")
print(calculator(numx,numy,op))



