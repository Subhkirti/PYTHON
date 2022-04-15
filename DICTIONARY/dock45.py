d=[{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
u=input('enter:')
for i in range(len(d)): 
	if d[i]['id'] == u:
		del d[i]
		break
	elif d[i]['color']==u:
		del d[i]
		break
print (d)
