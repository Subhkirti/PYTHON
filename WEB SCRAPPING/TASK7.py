import json
data=open("Task5.json","r+")
d=json.load(data)
def analyse_director(d):
    director_list=[]
    dic={}
    for i in d:
        if "Director" in i:
            direc=i["Director"]
            for j in direc:
                if j not in dic:
                    direc=j
                    dic[j]=1
                else:
                    dic[j]+=1
        else:
            continue
    director_list.append(dic)
    
    with open("Task7.json","w") as file:
        json.dump(director_list,file,indent=4)
        return director_list
analyse_director(d)

