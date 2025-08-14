n = 1
while True:
    st1 = input()
    st2 = input()
    
    if st1 == 'END':
        break
    
    lst1 = [0] * 26
    lst2 = [0] * 26
    
    for i in range(0,len(st1),1):
        ch = st1[i]
        idx = ord(ch) - ord("a")
        lst1[idx] +=1
    
    for i in range(0,len(st2),1):
        ch = st2[i]
        idx = ord(ch) - ord("a")
        lst2[idx] +=1
        
    is_same = "same"
    
    if len(lst1) >= len(lst2):
        for i in range(0,len(lst1),1):
            if lst1[i] != lst2[i]:
                is_same = "different"
                break
    else:
        for i in range(0,len(lst2),1):
            if lst1[i] != lst2[i]:
                is_same = "different"
                break
    
    print(f"Case {n}: {is_same}")
    
    n += 1