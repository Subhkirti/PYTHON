a="Himani"
b="Somi"
p=[ ]
s=list(a)
l= list(b)
i=0
while i<len(a):
	if s[i] in l:
		if s[i] not in p:
			p.append(s[i])
	i=i+1
print(p)