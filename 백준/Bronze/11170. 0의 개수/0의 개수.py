T = int(input())

for _ in range(T):
    lst = list(map(int,input().split()))
    N = lst[0]
    M = lst[1]
    cnt = 0 
    for i in range(N,M+1,1):
        i = str(i)
        for j in i:
            if j == "0":
                cnt += 1
    print(cnt)