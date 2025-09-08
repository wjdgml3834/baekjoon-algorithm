T = int(input())

for _ in range(T):
    n = int(input())
    cnt = 0 
    print("Pairs for %d:" %n, end=" ")
    
    for i in range(1,13,1):
        for j in range(i+1,13,1):
            total = i + j 
            if total == n:
                if cnt > 0:
                    print(",", end=" ")
                
                print(i,j,end="")
                cnt += 1 
    print()