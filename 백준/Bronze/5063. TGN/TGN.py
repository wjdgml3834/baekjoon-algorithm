N = int(input())
for i in range(0,N,1):
    lst = list(map(int,input().split()))
    r = lst[0]
    e = lst[1]
    c = lst[2]
    ad_profit = e - c
    if ad_profit > r:
        print("advertise")
    elif ad_profit < r:
        print("do not advertise")
    else:
        print("does not matter")