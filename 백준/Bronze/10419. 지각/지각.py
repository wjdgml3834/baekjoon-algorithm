T = int(input())

for _ in range(T):
    d = int(input())
    i = 0
    while True:
        total = i + (i**2)
        
        if total > d:
            break
        
        i += 1
    
    rst = i - 1
    print(rst)