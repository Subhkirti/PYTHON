file=open("w3q11.txt","w")
s=file.write("Python is")
file.close()
file2=open("w3q11.txt","r")
h=file2.read()
i=0
while i<len(h):
    i+=1
print(i)
file2.close()