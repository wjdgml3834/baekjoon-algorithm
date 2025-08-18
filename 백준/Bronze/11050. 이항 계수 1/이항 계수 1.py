lst = list(map(int,input().split()))
N = lst[0]
K = lst[1]
c = 1
p = 1

for i in range(N,N-K,-1):
    c = c * i
    p = p * (N - (i-1))

result = c // p
print(result)