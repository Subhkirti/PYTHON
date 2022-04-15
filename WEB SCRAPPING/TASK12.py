import bs4
import requests
import json
url="https://www.rottentomatoes.com/m/spider_man_into_the_spider_verse"
def cast(url):
    res=requests.get(url)
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    main_div=soup.find("div",class_="castSection")
    di=main_div.find_all("div",class_="cast-item media inlineBlock")
    di2=main_div.find_all("div",class_="cast-item media inlineBlock moreCasts hide")
    l=[]
    for i in di:
        dic={}
        a=i.find("a")["href"][11:]
        dic["name"]=a
        l.append(dic)
    for i in di2:
        dic={}
        b=i.find("a")["href"][11:]
        dic["name"]=b
        l.append(dic)
    with open("Task12.json","w+") as file:
        json.dump(l,file,indent = 4)
        return l
cast(url)