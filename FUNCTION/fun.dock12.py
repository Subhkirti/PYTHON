def plan(num):
    n=list(num)
    if n[-1]=="0":
        n.remove(n[-1])
        i=0
        while i<len(n):
            print(n[i])
            i+=1
plan(num=input('enter:'))