f=open("rrt.txt","r")
f1=open("delhi.txt","w")
f2=open("shimla.txt","w")
f3=open("other.txt","w")
c=f.read()
d=c.split("\n")
i=0
while i<len(d):
    if "delhi" in d[i]:
        f1.write(d[i])
        f1.write("\n")
    elif "shimla" in d[i]:
        f2.write(d[i])
        f2.write("\n")
    else:
        f3.write(d[i])
        f3.write("\n")
    i+=1
f.close()
