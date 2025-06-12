lst = list(map(int,input().split()))
L = lst[0]
P = lst[1]
newspaper_lst = list(map(int,input().split()))
result = []

for i in newspaper_lst:
    num = i - (L*P)
    result.append(num)

for i in result:
    print(i, end=" ")