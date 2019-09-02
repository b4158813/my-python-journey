def triangles():
    l=[1]
    i=len(l)
    while True:
        yield l
        l=[1]+[l[i]+l[i+1] for i in range(len(l)-1)]+[1]
        i+=1

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break