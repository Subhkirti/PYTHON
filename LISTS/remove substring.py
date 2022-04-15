ms="the quick brown fox over lazy dog.the dog slept over a varandah"
ss="over"
i=0
k=" "
s=ms.split()
while i<len(s):
    if s[i]==ss:
        k=k+" on"
    else:
        k=k+" "+s[i]
    i+=1
print(k)