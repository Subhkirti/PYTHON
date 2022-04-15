import requests
import os
import json
with open("Task1.json","r+") as file:
    a=json.load(file)
def  txt():
    for i in a:
        path="/home/admin123/PYTHON/Task8"+i["Name"]+".text"
        if os.path.exists(path):
            pass
        else:
            create=open(path,"w")   
            url=requests.get(i["Url"])
            create.write(url.text)
            create.close()
txt()


