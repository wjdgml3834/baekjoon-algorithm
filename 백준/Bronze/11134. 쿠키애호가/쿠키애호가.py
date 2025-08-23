T = int(input())

for _ in range(T):
    lst = list(map(int,input().split()))
    
    N = lst[0]
    C = lst[1]
    q = N // C
    r = N % C
    
    if r != 0:
        q += 1
    
    print(q)