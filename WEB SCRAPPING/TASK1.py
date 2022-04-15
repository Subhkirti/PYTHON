from bs4 import BeautifulSoup
import requests
import json
res=requests.get("https://www.rottentomatoes.com/top/bestofrt/top_100_animation_movies/")
soup = BeautifulSoup(res.text,"html.parser") 
def scrape_top_list():
    list=[]
    main_div=soup.find("div",class_="panel-body content_body allow-overflow")
    sub=main_div.find("table",class_="table")
    trs=sub.find_all("tr")
    for i in trs:
        dic={}
        td=i.find_all("td")
        for k in td:
            rank=i.find("td",class_="bold").get_text()[:-1]
            dic["Rank"]=int(rank)
            rating=i.find("span", class_="tMeterScore").get_text()[1:3]
            dic["Rating"]=float(rating)
            reviews=i.find("td",class_="right hidden-xs").get_text()
            dic["Reviews"]=int(reviews)
            name=i.find("a",class_="unstyled articleLink")["href"][3:]
            dic["Name"]=name
            movieurl=i.find("a",class_ = "unstyled articleLink")["href"]
            url= "https://www.rottentomatoes.com" + movieurl
            dic["Url"]=url
            Year = i.find("a",class_ = "unstyled articleLink").get_text()
            year = Year.strip()
            dic["Year"] = int(year[-5:-1])
        list.append(dic)
        if {} in list:
            list.remove({})
    with open("Task1.json","w+") as file:
        json.dump(list,file,indent = 4)
    return list
scrape_top_list()
