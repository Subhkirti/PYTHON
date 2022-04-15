dict={"name":"Raju","marks":56}
l=[]
user=input("Enter:")
for i in dict:
    l.append(i)
if user in l:
    print("exist")
else:
    print("Not exist")