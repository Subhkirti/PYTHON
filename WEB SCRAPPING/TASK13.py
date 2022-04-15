from TASK4 import movie_details
from TASK12 import cast
import json
url="https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse"
t12=cast(url)
t4=movie_details(url)
def cast_details(t4,t12):
    dic=[]
    t4["cast"]=t12
    dic.append(t4)
    with open("Task13.json","w+") as file:
        json.dump(dic,file,indent=4)
        return dic
print(cast_details(t4,t12))
   
  
         






   
  
         














