num=input("enter your number:")
a="0"
i=0
while i<len(num):
    if a in num and num[0]!=a:
        print("Duck number!")
        break
    else:
        print("not duck number")
        break
    i+=1