list=[{"first":"1"},{"second":"2"},{"third":"1"},{"four":"5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
i=0
empty=[]
while i<len(list):
    for key in list[i]:
        if list[i][key] not in empty:
            empty.append(list[i][key])
        i+=1
print(empty)
    

    



