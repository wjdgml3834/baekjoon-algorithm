inp = list(map(int,input().split()))
A = int(inp[0])
B = int(inp[1])
total_sum = 0
lst = []

for i in range(1,1001,1): # 숫자 
    for j in range(0,i,1): # 횟수
        lst.append(i)


for i in range(A-1,B,1): # A번째의 인덱스는 A-1번째부터 시작
    total_sum += lst[i]

print(total_sum)