N = int(input())
M = int(input())
lst = list(map(int,input().split()))

lst.sort() # 우선 오름차순으로 정렬하는 것이 중요

left = 0  # 왼쪽 포인터
right = N - 1 # 오른쪽 포인터
rst = 0 # 결과 담을 변수

while True:
    if left == right: # 두 포인터가 같아지면 break
        break
    
    total = lst[left] + lst[right]
    
    if total == M: # 같으면 rst 하나 올리고, 오른쪽 포인터를 내린다.
        rst += 1
        right -= 1
        
    elif total > M: # total이 크면 오른쪽 포인터를 내린다.
        right -= 1
        
    else: # 그 외에는 왼쪽 포인터를 올린다.
        left += 1 
    
print(rst)