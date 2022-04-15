import json
with open( "Task2.json","r+")as f:
    data=json.load(f)
def group_of_decade(movies):
    dic={}
    list1=[]
    for i in movies:
        m=int(i)%10
        decade=int(i)-m
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        dic[i]=[]
    for i in dic:
        dec10=i+9
        for x in movies:
            if int(x)<=dec10 and int(x)>=i:
                for v in movies[x]:
                    dic[i].append(v)
    with open("Task3.json","w+") as file:
        json.dump(dic,file,indent = 4)
    return(dic)
group_of_decade(data)






        



   
   


   
                  
      


  