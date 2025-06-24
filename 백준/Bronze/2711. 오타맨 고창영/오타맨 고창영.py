N = int(input()) # 테스트 케이스 수

for i in range(N):
    lst = input().split() # 공백을 기준으로 
    idx = int(lst[0]) # 
    st = lst[1]
    answer = st[:idx-1] + st[idx:]
    print(answer)