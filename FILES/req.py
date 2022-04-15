import requests
import json
def request():
    a = requests.get("http://saral.navgurukul.org/api/courses")
    print("No. Courses---ID")
    with open("courses.json","w") as f:
        dict=json.loads(a.text)
        json.dump(dict,f,indent=4)
    with open("courses.json","r") as f:
        data = json.load(f)
    id= [] 
    i = 0
    while i < len(data['availableCourses']):
        print(i+1,data['availableCourses'][i]['name'],"---",data['availableCourses'][i]['id'])
        id.append(data['availableCourses'][i]['id'])
        i+=1 
    user= int(input("**select the serial number:"))
    ex=requests.get("http://saral.navgurukul.org/api/courses/"+str(id[user])+"/exercises")
    a=ex.json()
    j=0
    l=0
    slug=[]
    while j<len(a["data"]):
        print(l+1,a["data"][j]["name"])
        slug.append(a['data'][j]["slug"])
        l=l+1
        j=j+1
    slugname=int(input("**Enter your slug number:"))
    sluglist=requests.get("http://saral.navgurukul.org/api/courses/"+ str(user)+"/exercise/getBySlug?slug=" + slug[slugname])
    b=sluglist.json()
    print(b["content"],":-content")
    print()
    print("**Up:-If you wanted to go back Menu")
    print("Next;-If you wanted to go to the content of next exercise")
    print("Previous:-If you wanted to go to the content of next exercise")
    print("Exit:ous:-If you wanted to go to the content of next exercise")
    print("Exit:ous:-If you wanted to go to the content of next exercise")
    print("Exit:ous:-If you wanted to go to the content of next exercise")
    print("Exit:ous:-If you wanted to go to the content of next exercise")
    print("Exit:-If you wanted to start again!**")
    next_step = input("choose your next step:")
    i=0
    while i<len(slug):    while i<len(slug):

        if next_step == "up" or next_step == "Up":
            sluglist = requests.get("http://saral.navgurukul.org/api/courses/"+ str(user)+"/exercise/getBySlug?slug=" + slug[slugname-1])
            print("content:-",b["content"])
            break
        elif next_step == "previous" or next_step == "Previous":
            print("content",b["content"])
            break
        elif next_step == "next" or next_step == "Next":
            sluglist = requests.get("http://saral.navgurukul.org/api/courses/"+ str(user)+"/exercise/getBySlug?slug=" + slug[slugname+1])
            print("content:-",b["content"]) 
        elif next_step == "exit" or next_step == "Exit":
            request()
request()
        
    
    

    

    





        








            

         
       
  


    
