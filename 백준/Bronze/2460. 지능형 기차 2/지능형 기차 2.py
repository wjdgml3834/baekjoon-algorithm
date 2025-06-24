now = 0
mx = 0

for i in range(0,10,1):
    lst = list(map(int,input().split()))
    off = lst[0]
    on = lst[1]
    now = now - off + on
    if now > mx:
        mx = now

print(mx)