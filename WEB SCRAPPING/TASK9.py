import random
import time
import requests
import os
import json
from TASK1 import scrape_top_list
t1=scrape_top_list()
with open("Task1.json","r+") as file:
    a=json.load(file)
def  txt():
    random_sleep=random.randint(1,3)
    for i in a:
        path="/home/admin123/Task8"+i["Name"]+".json"
        if os.path.exists(path):
            pass
        else:
            create=open("/home/admin123/Task9"+i["Name"]+".json","w")
            url=requests.get(i["Url"])
            create1=create.write(url.text)
            create.close()
        time.sleep(random_sleep)
txt()
  
    





