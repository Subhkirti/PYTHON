f=open("meraki1.txt","r")
data=f.read()
f.close()
print(data)
i=1
c=0
while i<len(data):
    if data[i]=="\n":
        c+=1
    i=i+1
print(c)
