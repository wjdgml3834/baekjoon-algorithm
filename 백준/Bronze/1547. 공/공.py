M = int(input()) # 위치를 바꾸는 횟수
lst = [1,2,3] # 컵 3개 리스트 

for _ in range(M):
    x,y = map(int,input().split())
    idx1 = lst.index(x) # x,y 값의 인덱스를 찾아준다.
    idx2 = lst.index(y)
    
    tmp = lst[idx1] # 찾은 값들을 서로 바꾼다. 
    lst[idx1] = lst[idx2]
    lst[idx2] = tmp

rst = lst[0] # 1번공이 들어있는 즉 가장 첫번째 요소를 출력한다. 
print(rst)