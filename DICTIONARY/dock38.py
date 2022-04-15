d={'c1': 'Red', 'c2': 'Green', 'c3': None}
for i,j in dict(d).items():
    if j is None:
        del d[i]
        
print(d)

        





