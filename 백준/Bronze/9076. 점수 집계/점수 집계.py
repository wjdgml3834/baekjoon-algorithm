n = int(input())

for i in range(0,n,1):
    lst = list(map(int, input().split()))
    mx = max(lst)
    mn = min(lst)
    lst.remove(mx)
    lst.remove(mn)
    mx = max(lst)
    mn = min(lst)
    if mx - mn >= 4:
        print("KIN")
    else:
        total = sum(lst)
        print(total)