f=open('meraki3.txt',"w")
x =["Kotak", "HDFC", "RBL", "SBI", "Bank of Baroda"]
i=0
while i<len(x):
    f.write(x[i])
    f.write("\n")
    i=i+1
f.close()