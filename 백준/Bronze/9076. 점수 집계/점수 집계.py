n = int(input())

for i in range(0,n,1):
    lst = list(map(int, input().split()))
    lst.sort()
    mx = lst[len(lst) - 1]
    mn = lst[0]
    lst.remove(mx)
    lst.remove(mn)
    mx = lst[len(lst) - 1]
    mn = lst[0]
    if mx - mn >= 4:
        print("KIN")
    else:
        temp_total = 0
        for j in lst:
            temp_total += j
        print(temp_total)