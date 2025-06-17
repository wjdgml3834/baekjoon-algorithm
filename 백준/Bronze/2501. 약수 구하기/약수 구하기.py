lst = list(map(int,input().split()))
N = lst[0]
K = lst[1]
divisor_lst = []

for i in range(1,N+1,1):
    if N % i == 0:
        divisor_lst.append(i)

if len(divisor_lst) < K:
    print(0)
else:
    result = divisor_lst[K-1]
    print(result)