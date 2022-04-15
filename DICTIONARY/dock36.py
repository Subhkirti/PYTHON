x={'key1': 1, 'key2': 3, 'key3': 2}
y={"key1":1,"key2":2}
for i in x:
    for j in y:
        if i==j and x[i]==y[j]:
            print(i,":",x[i],"is present in both x and y")
            break
        else:
            print(i,":",x[j],"is present not in both x and y")
            break
    


    
   


    