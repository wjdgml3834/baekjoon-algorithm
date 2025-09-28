N, M = map(int,input().split())
lst = []

for i in range(1,N+1,1): # 우선 바구니 리스트를 만들어준다. 
    lst.append(i)
    
for _ in range(M):
    idx1, idx2 = map(int,input().split()) 
    if idx1 == idx2: # 바구니 번호가 같다면 아무 변화도 일으키지 않는다.
        continue
    idx1 = idx1 - 1 # 0부터 시작하기 위해 -1 해준다. 
    idx2 = idx2 - 1
    
    ball1 = lst.pop(idx1) # 공을 1개 빼서
    
    lst.insert(idx2, ball1) # idx2번째 인덱스에 넣는다.
    
    ball2 = lst.pop(idx2-1) # 빼줄때는 리스트가 변화되어서 -1 해주어야 한다.  
    
    lst.insert(idx1, ball2) # idx1번째 인덱스에 넣는다.

    
for i in lst:
    print(i, end=" ") 