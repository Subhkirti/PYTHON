l2=[["harry",37.21],["berry",37.21],["tina",37.2],["akriti",41],["harsh",39]]
min=l2[0][1]
for i in range(len(l2)):
    for j in range(len(l2[i])):
        if j%2!=0:
            if l2[i][j]<min:
                min=l2[i][j]
smin=l2[0][1]
minname=0
l3=[]
for i in range(len(l2)):
    for j in range(len(l2[i])):
        if j%2!=0:
            if l2[i][j]>min and l2[i][j]<=smin:
                smin=l2[i][j]
                minname=l2[i][0]
                l3.append(minname)

print(l3[-1])
print(l3[-2])