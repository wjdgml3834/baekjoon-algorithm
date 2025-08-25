import math

lst= list(map(int,input().split()))
N = lst[0]
W = lst[1]
H = lst[2]

for _ in range(N):
    length = int(input())
    
    mx = math.sqrt(W ** 2 + H **2)
    
    if length <= mx:
        print("DA")
    else:
        print("NE")