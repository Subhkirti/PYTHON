import json
with open( "Task1.json","r+")as f:
    data=json.load(f)
def group_by_year(movies):
    y_list=[]
    for i in movies:
        year=i["Year"]
        if year not in y_list:
            y_list.append(year)
    dic={}
    for j in y_list:
        for x in movies:
            if str(j)==str(x["Year"]):
                dic[j]=[x]
    with open("Task2.json","w+") as file:
        json.dump(dic,file,indent = 4)
    return dic
group_by_year(data)

