n = int(input())

for _ in range(n):
    lst = list(map(int,input().split()))
    lst.sort()
    a = lst[0]
    b = lst[1]
    mx = 0
    rst = 0 
    
    for i in range(2,a+1,1):
        if a % i == 0 and b % i == 0:
            mx = i 
    
    if mx == 0:
        rst = a * b
    
    else:
        a_remain = a // mx 
        b_remain = b // mx
        rst = mx * a_remain * b_remain
    
    print(rst)