#1st question:-
i=0
while i <=1000:
    if i%3==0:
        print("nav")
    if i%7==0:
        print("gurukul")
    if i%21==0:
        print("navgurukul")
    else:
        print(i)
    i+=1

 #2nd Question:-
student=int(input("enter no of students:"))
kharcha=int(input("enter kharcha"))
tk=student*kharcha
if tk<=50000:
    print("Hum budget ke ander hai")
else:
    print("Hum budget ke bahar hai")


#4thquestion:-
a=int(input("enter first:"))
b=int(input("enter second:"))
c=int(input("enter third"))
if a>b and a>c:
    print(a,"is max")
elif b>a and b>c:
    print(b," is max")
elif c>a and c>b:
    print(c, "is max")

# 5 question:-
list1=[1,342,75,23,98]
list2=[75,23,98,12,78,10,1]
i=0
while i<len(list1):
    if list1[i] in list2:
        list.append(list1[i])
    i+=1
print(list)

#6th question
l=["sun","moon","star","moon"]
i=0
k=[]
while i<len(l):
    if l[i] in l:
        if l[i] not in k:
            k.append(l[i])
        i+=1
    print(k)

# 7question
a=[1,2,6,8,9]
b=[6,7,2,1,0]
i=0
k=[]
while i<len(a):
    if a[i] not in b:
        k.append(a[i])
    i+=1
print(k)

# question11
words = "navgurukul is great"
k=[]
i=0
p=words.split()
while i<len(p):
    k.append(p[i])
    i+=1
print(k)