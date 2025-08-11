n = int(input())

for _ in range(n):
    lst = list(map(int,input().split()))
    N = lst[0]
    M = lst[1]
    U = (2 * M) - N
    T = M - U
    print(U, T) 