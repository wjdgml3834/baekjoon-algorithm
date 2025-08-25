n = 1
while True:
    st1 = input()
    st2 = input()
    
    if st1 == "END":
        break
    
    lst1 = list(st1)
    lst2 = list(st2)
    
    lst1.sort()
    lst2.sort()
    
    is_same = False
    
    if lst1 == lst2:
        is_same = True
    
    if is_same == True:
        print("Case %d: same" %n)
        
    else:
        print("Case %d: different" %n)
        
    n += 1