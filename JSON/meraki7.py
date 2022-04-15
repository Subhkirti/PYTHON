import json
dic={"Name":"Abhishek",'Designation':'CEO of navgurukul','Gender':'male','Age':29}
f=json.dumps(dic)
print(type(f))
print(f)