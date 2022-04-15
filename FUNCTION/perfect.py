def function(num):
    sum=0
    i=1
    while i<num:
        if num%i==0:
            sum=sum+i
        i+=1
    if num==sum:
        print(num,"perfect no")
    else:
        print(num,"not perfect")
num=int(input("enter a number"))
function(num)

    