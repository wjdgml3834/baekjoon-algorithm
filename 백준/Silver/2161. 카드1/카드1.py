N = int(input()) # 카드 개수
lst = [] # 카드 리스트
rst = 0 # 가장 마지막 남는 수 
discard_lst = [] # 버리는 카드 저장할 리스트 

for i in range(1,N+1,1): # 우선 카드를 리스트에 다 넣는다. 
    lst.append(i)
    
while True:
    if N == 1: # 만약 N이 1이면 바로 나온다. 
        rst = 1
        break

    delete_num = lst.pop(0) # 맨 첫요소 삭제하고
    discard_lst.append(delete_num) # 버리는 리스트에 카드 추가 
    
    if len(lst) == 1: # 만약 길이가 1 즉, 하나만 남으면 break 한다.
        rst = lst[0]
        break
    
    moving_num = lst.pop(0) # 움직이는 요소는 제거해서 기억했다가 
    lst.append(moving_num) # 가장 뒤로 보낸다. 

discard_lst.append(rst) # 마지막에 남는 카드도 추가한다. 

for i in discard_lst:
    print(i, end=" ")