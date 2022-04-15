import json  
d='{"Name":"Ram", "Class":"IV","Age":9 }'
f=json.loads(d)
print(f)
print(f["Name"])