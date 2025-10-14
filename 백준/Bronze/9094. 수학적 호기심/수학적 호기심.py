T = int(input())

for _ in range(T):
    n,m = map(int,input().split())
    cnt = 0 
    
    for a in range(1,n,1):
        for b in range(a+1,n,1):
            expression = (a*a + b*b + m) % (a*b) 
            if expression == 0:
                cnt += 1
            
    print(cnt)