n = int(input()) # 테스트 케이스 개수  

for _ in range(n):
    lst = list(map(int,input().split()))
    lst.sort() # a는 작은거, b는 큰걸로 정렬한다.
    a = lst[0]
    b = lst[1]
    mx = 0 # 나눠지는 최대 공약수
    rst = 0  
    
    for i in range(2,a+1,1):
        if a % i == 0 and b % i == 0: # 만약 둘다로 나눠지는 애들 중에서 최대를 찾는다.
            mx = i 
    
    if mx == 0: # 만약 그대로면 서로 곱해버린다.
        rst = a * b
    
    else:
        a_q = a // mx # 더이상 나눠지지 않는 a와 관련된 몫
        b_q = b // mx # 더이상 나눠지지 않는 b와 관련된 몫
        rst = mx * a_q * b_q # 최소공배수는 이들을 모두 곱한것이다.
    
    print(rst)