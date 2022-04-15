import json
from TASK1 import scrape_top_list
from TASK4 import movie_details
movie=scrape_top_list()
def get_movies_details():
        details=[]
        for i in movie:
                details.append(movie_details(i["Url"]))
        with open("Task5.json","w+") as file:
                json.dump(details,file,indent=4)
                return details
movie_detail=get_movies_details()


