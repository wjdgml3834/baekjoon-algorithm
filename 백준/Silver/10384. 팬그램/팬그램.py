N = int(input()) # 테스트 케이스 개수 

for i in range(1,N+1,1): 
    st = input()
    st = st.lower() # 우선 소문자로 다 바꾼다. 
    st2 = "" # 기타 문장부호를 빼서 담을 문자열 변수 
    lst = [0] * 26 # 알파벳 담을 리스트
    
    for ch in st: # 기타 문장 부호를 없앤다. 
        gap = ord(ch) - ord("a")
        if gap >=0 and gap <= 25:
            st2 = st2 + ch
    
    for ch in st2: # 알파벳 리스트에 담는다. 
        idx = ord(ch) - ord("a")
        lst[idx] += 1

    mn = 10000 # 최솟값을 찾기 위한 변수 
    
    for j in lst: # 최솟값 찾는 로직 
        if j < mn:
            mn = j 
    
    if mn == 1: # 최솟값이 1이라는것은 무조건 팬그램 보장이고, 1번 팬그램이라는 뜻 
        rst = "Pangram!"
    
    elif mn == 2:
        rst = "Double pangram!!"
    
    elif mn == 3:
        rst = "Triple pangram!!!"
    
    else: 
        rst = "Not a pangram"
    
    print(f"Case {i}: {rst}")