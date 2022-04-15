import json
with open( "Task5.json","r+")as f:
    data=json.load(f)
def analysis_movies_language(data):
    dic={}
    for i in data:
        if "Language" in i:
            language=i["Language"]
            
            if language not in dic:
                dic[language]=1
    
            else:
                dic[language]+=1
        else:
            continue
    # print(dic)
    with open( "Task6.json","w+")as file:
        json.dump(dic,file,indent=4)
        return dic
print(analysis_movies_language(data))



