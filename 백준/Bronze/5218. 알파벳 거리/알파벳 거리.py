n = int(input())

for i in range(0,n,1):
    distance = []
    lst = input().split()
    f = lst[0]
    r = lst[1]
    for j in range(0,len(f),1):
        x = f[j]
        y = r[j]
        if y >= x:
            result = ord(y) - ord(x)
            distance.append(result)
        else:
            result = (ord(y) + 26) - ord(x)
            distance.append(result)
          
    for k in range(n):
        str_value = [str(x) for x in distance]
        joined = " ".join(str_value)
    print("Distances: " + joined)