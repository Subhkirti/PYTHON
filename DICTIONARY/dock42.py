d={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
p=int(input("enter your no:"))
for i in d.values():
    if p==i:
        print("all are 12 in the dictionary")
        break
    else:
        print("all are not ",p,"in the dictionary.")
        break