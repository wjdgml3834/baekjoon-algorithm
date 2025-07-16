n = int(input())

for i in range(0,n,1):
    lst = list(map(int,input().split()))
    total = 0
    mn = 101
    for j in lst:
        if j % 2 == 0:
            if j < mn:
                mn = j
            total += j
    
    print(total, mn)   