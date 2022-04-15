list= [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
sum =0
tax=0
dic={}
for d in list:
    if d["item"]=="item1":
        sum=sum+ d['amount']
        dic["item1"]=sum
    else: 
        tax=tax+d["amount"]
        dic["item2"]=tax
print(dic)
        

    






