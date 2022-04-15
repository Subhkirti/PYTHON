f=open("w3q12.txt","r")
d=f.read()
print(f.closed)
# if i run without closing.
f.close()
print(f.closed)
# if i run with closing.

