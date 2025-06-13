lst1 = list(map(int,input().split()))
A = lst1[0]
X = lst1[1]
lst2 = list(map(int,input().split()))
result = []

for i in lst2:
    if i < X:
        result.append(i)

for i in result:
    print(i, end=" ")