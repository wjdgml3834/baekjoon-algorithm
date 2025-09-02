T = int(input())

for _ in range(T):
    lst1 = list(map(int,input().split()))
    N = lst1[0]
    K = lst1[1]
    lst2 = list(map(int,input().split()))
    total = 0
    for x in lst2:
        q = x // K
        total = total + q
    
    print(total)