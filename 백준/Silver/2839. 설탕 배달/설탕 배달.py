N = int(input())
n = N
rst = -1 
cnt = 0 

while n >= 0: 
    if n % 5 == 0: # 예를 들어 6이면 나머지가 0이라서 cnt 0이 된다.
        q = n // 5 
        cnt += q 
        rst = cnt
        break 
    
    n -= 3
    cnt += 1

print(rst)