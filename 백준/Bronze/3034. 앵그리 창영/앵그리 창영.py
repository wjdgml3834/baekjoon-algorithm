import math

lst= list(map(int,input().split()))
N = lst[0] # 성냥의 개수
W = lst[1] # 성냥박스 가로길이
H = lst[2] # 성냥박스 세로길이 

for _ in range(N):
    length = int(input())
    
    mx = math.sqrt(W ** 2 + H **2) # 성냥박스가 들어갈 수 있는 최대 = 대각선 길이
    
    if length <= mx:
        print("DA")
    else:
        print("NE")