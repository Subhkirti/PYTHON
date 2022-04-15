def showNumbers(limit):
    for i in range(0,limit+1):
        if i%2==0:
            print('even:',i,end="  ")
        else:
            print("odd:",i,end='  ')
showNumbers(int(input("enter your no:")))