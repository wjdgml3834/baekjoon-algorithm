N,M = map(int,input().split())

lst = [0] * (N+1)

for _ in range(M):
    start,end,num = map(int,input().split())
    
    for i in range(start,end+1,1):
        lst[i] = num 
    
for i in range(1,len(lst),1):
    print(lst[i], end=" ")