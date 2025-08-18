lst = list(map(int,input().split()))
N = lst[0]
K = lst[1]
c = 1
p = 1

for i in range(N, N-K, -1):
    c = c * i

for i in range(K,0,-1):
    p = p * i
    
result = c // p

print(result)