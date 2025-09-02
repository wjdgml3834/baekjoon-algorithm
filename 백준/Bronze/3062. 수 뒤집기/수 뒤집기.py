T = int(input())

for _ in range(T):
    N = input()
    reverse_N = N[::-1]
    N = int(N)
    reverse_N = int(reverse_N)
    total = N + reverse_N
    lst = list(str(total))
    is_sy = True
    for i in range(0,len(lst)//2,1):
        if lst[i] != lst[len(lst)-1-i]:
            is_sy = False
    
    if is_sy:
        print("YES")
    else:
        print("NO")