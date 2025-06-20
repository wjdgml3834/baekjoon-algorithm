lst = list(map(int,input().split()))
N = lst[0]
X = lst[1]
A = list(map(int,input().split()))

for i in A:
    if i < X:
        print(i, end=" ")