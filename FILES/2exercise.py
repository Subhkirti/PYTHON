file = open("3exersisebank.txt", "r")
j=file.readline()
count = 1
while count<len(j):
    if "\n" in j:
        count+=1
print(count)
file.close()

