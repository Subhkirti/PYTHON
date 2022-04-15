import json
d={"shopping_list":{"chaco":"15","Biscuits":"50","Diary_milk":"30","ice_cream":"20",}}
user=input("Which item you want?")
item=input("How many items you want?")
for i in d:
    for j in d[i]:
        for r in d[i][j]:
            if item==d[i][j]:
                del d[i][j]
with open("d.json","w+") as file:
    json.dump(d,file,indent=4)
f1=open('d.json','r')
if user in f1:
    d["shopping_list"][user]=item
else:
    pass
print(d)








    
      



