from bs4 import BeautifulSoup
import requests
import json
url="https://www.rottentomatoes.com/m/luca_2021"
def movie_details(movie_url):
    res=requests.get(movie_url)
    soup = BeautifulSoup(res.text,"html.parser") 
    h1=soup.find("h1", class_="scoreboard__title").get_text()
    li=soup.find_all("li",class_="meta-row clearfix")
    dic={}
    dic["Name"]=h1
    for k in li:
        f=k.text
        b=f.split()
        # print(b)
        if "Rating:" in b:
            dic["Rating"]=b[1]
        elif "Genre:" in b:
            j=b[1:]
            f=""
            i=0
            while i<len(j):
                f=f+j[i]
                i+=1
            l=f.split(",")
          
            dic["Genre"]=l
        elif "Language:" in b:
            dic['Language']=b[2]
        elif "Director:" in b:
            w=b[1:]
            h=" "
            i=0
            while i<len(w):
                h=h+w[i]
                i+=1
            l=h.split(",")
            dic["Director"]=l
        elif "Producer:" in b:
            dic["Producer"]=b[1:]
        elif "Runtime:" in b:
            s=b[1:]
            for i in s:
                if "h" in i:
                    first=int(i[0:-1])*60
                elif "m" in i:
                    sec=int(i[:-1])
            dic["Runtime"]=first+sec
    with open("Task4.json","w+") as file:
        json.dump(dic,file,indent = 4)
    return dic
movie_details(url)



     
        














