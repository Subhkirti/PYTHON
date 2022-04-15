l="MISSISSIPPI"
j=list(l)
f={}
for item in j:
    if item in f:
        f[item] += 1
    else:
        f[item] = 1
print(f)

