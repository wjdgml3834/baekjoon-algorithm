lst = list(map(int,input().split()))
A = lst[0]
B = lst[1]

def func(num,fr,to):
    n = num # 혹시 몰라서 원본 복사 
    rst = 0 # 반환할 숫자
    sq = 1  # 자릿수 곱해줄 변수
    
    while n > 0:
        r = n % 10 # 일의 자릿수를 구하려면 10으로 나눈 나머지를 구하면 된다. 
        
        if r == fr: # 만약 from이 나왔다면 to로 바꿔준다.
            r = to
        
        rst = rst + r * sq # 그 값을 총 더한다.
        
        sq = sq * 10 # 자릿수 올라가게 만든다.
        
        n = n // 10 # 10으로 나눈 몫이 그 다음 자릿수가 된다. 
    
    return rst 

min_sum = func(A,6,5) +  func(B,6,5)
max_sum = func(A,5,6) +  func(B,5,6)

print(min_sum, max_sum)