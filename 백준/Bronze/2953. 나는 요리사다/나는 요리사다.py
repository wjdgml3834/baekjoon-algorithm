mx = 0 
mxidx = 0

for i in range(0,5,1):
    lst = list(map(int,input().split()))
    total = 0 
    for j in lst: 
        total += j
    if mx < total:
        mx = total
        mxidx = i+1 

print(mxidx, mx)