import random
file=open("w3q10.txt","r")
s=file.read()
k=random.choice(s)
print(k)
file.close()
