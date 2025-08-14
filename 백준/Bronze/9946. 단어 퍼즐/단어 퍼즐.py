n = 1 # 케이스 횟수를 세기 위함
while True:
    st1 = input() # 처음 완성한 알파벳들
    st2 = input() # 회수한 알파벳들
    
    if st1 == 'END': # END가 나오면 바로 while문 탈출
        break
    
    lst1 = [0] * 26 # 알바벳 담을 리스트
    lst2 = [0] * 26
    
    for i in range(0,len(st1),1):
        ch = st1[i]
        idx = ord(ch) - ord("a")
        lst1[idx] +=1
    
    for i in range(0,len(st2),1):
        ch = st2[i]
        idx = ord(ch) - ord("a")
        lst2[idx] +=1
        
    is_same = True
    
    if len(lst1) >= len(lst2):
        for i in range(0,len(lst1),1):
            if lst1[i] != lst2[i]:
                is_same = False
                break
    else:
        for i in range(0,len(lst2),1):
            if lst1[i] != lst2[i]:
                is_same = False
                break
    
    result = ""
    
    if is_same:
        result = "same"
    else:
        result = "different"
    
    print(f"Case {n}: {result}")
    
    n += 1 # 케이스 횟수 올림