
count = 0
i = 1
j=100
while(j>= i//2):
    if(j% i == 0):
        count = count + 1
        break
    i = i + 1

if (count == 0 and i!= 1):
    print(i,"is a Prime Number")
else:
    print(i,"is not a Prime Number")