def table(num):
    i=1
    while i<=num:
        j=1
        while j<=10:
            print(i,"*",j,"=",i*j)
            j+=1
        print()
        i+=1
table(int(input("enter a table ")))
        