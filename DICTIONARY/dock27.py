s= [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
i=0

user=input("enter:")
sum=0
while i<len(s):
    if user=="id":
        sum=s[i][user]+sum
    i+=1
print(sum)
   

