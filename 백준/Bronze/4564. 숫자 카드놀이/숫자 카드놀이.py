def func(n): # 자릿수를 곱하는 함수 
    total = 1 
    while n > 0: # 자릿수를 하나씩 분해해서 곱하는 로직 
        r = n % 10 
        total *= r
        n = n // 10
    
    return total 

while True:
    S = int(input())
    
    if S == 0: # 0을 입력받으면 반복문을 종료한다. 
        break
    
    lst = [] # 결과를 담을 리스트 
    lst.append(S) # 첫 값은 무조건 넣어준다.
    
    while S >= 10: # 한자릿수 될때까지 계속 함수 호출해서 반복한다. 
        new_num = func(S)
        S = new_num
        lst.append(S)
    
    for i in lst:
        print(i, end=" ")

    print() # 입력 편하게 하기 위함 