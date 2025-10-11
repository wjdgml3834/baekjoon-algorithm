A,B,C = map(int,input().split()) # 주차요금 A,B,C 변수 

time_lst = [0] * 101 # 시간대별 차 대수 담을 변수 

for _ in range(3):
    in_time, out_time = map(int,input().split()) # 들어온시간, 나간시간
    
    for i in range(in_time,out_time,1): 
        time_lst[i] += 1

total = 0 # 총 요금 변수 

for i in range(1,101,1):
    if time_lst[i] == 1: # 차가 한 대 일때 
        total = total + (time_lst[i] * A) 
    
    elif time_lst[i] == 2: # 차가 두 대 일때
        total = total + (time_lst[i] * B)
    
    elif time_lst[i] == 3: # 차가 세 대 일때 
        total = total + (time_lst[i] * C) 

print(total)