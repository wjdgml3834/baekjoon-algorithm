N = int(input())

for _ in range(N):
    lst = [0] * 26
    st = input().lower()
    st2 = ""
    for ch in st:
        gap = ord(ch) - ord("a")
        if gap >=0 and gap <= 25:
            st2 = st2 + ch
    
    for ch in st2:
        idx = ord(ch) - ord("a")
        lst[idx] += 1
    
    is_pangram = True
    missing_words = ""
    
    for idx in range(0,len(lst),1):
        if lst[idx] == 0:
            missing_ch = chr(idx + ord("a"))
            missing_words += missing_ch
            is_pangram = False
    
    if is_pangram:
        print("pangram")
    else:
        print(f"missing {missing_words}")