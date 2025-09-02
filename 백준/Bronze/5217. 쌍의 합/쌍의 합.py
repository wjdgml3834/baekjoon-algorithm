T = int(input())

for i in range(0, T, 1):
    m = int(input())
    
    print("Pairs for %d:" %m, end=" ")
    
    cnt = 0
    
    for j in range(1,13,1):
        for k in range(j+1,13,1):
            hap = j + k
            
            if hap ==m:
                if cnt >0:
                    print(", ", end="")
                print(j,k,end="")
                
                cnt +=1 
    print()