N, M = map(int,input().split())
lst = []

for i in range(1,N+1,1):
    lst.append(i)
    
for _ in range(M):
    idx1, idx2 = map(int,input().split())
    if idx1 == idx2:
        continue
    idx1 = idx1 - 1 
    idx2 = idx2 - 1
    
    ball1 = lst.pop(idx1) 
    
    lst.insert(idx2, ball1)
    
    ball2 = lst.pop(idx2-1)
    
    lst.insert(idx1, ball2)

    
for i in lst:
    print(i, end=" ") 