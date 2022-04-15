
def list(num1,num2):
    i=0
    while i<len(num1):
        if num1[i]%2==0 and num2[i]%2==0:
            print("even")
        else:
            print("odd")
        i=i+1
num1=[2,6,18,10]
num2=[2,4,7,8]
list(num1,num2)




