import json
data=open("Task5.json","r+")
d=json.load(data)
def analyse_genre(d):
    genre_list=[]
    dic={}
    for i in d:
        if "Genre" in i:
            genre=i["Genre"]
            for j in genre:
                if j not in dic:
                    genre=j
                    dic[j]=1
                else:
                    dic[j]+=1
        else:
            continue
    genre_list.append(dic)
    
    with open("Task11.json","w") as file:
        json.dump(genre_list,file,indent=4)
        return genre_list
analyse_genre(d)

