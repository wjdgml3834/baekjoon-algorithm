def func(n):
    total = 1
    while n > 0:
        r = n % 10
        total *= r
        n = n // 10
    
    return total 

while True:
    S = int(input())
    
    if S == 0:
        break
    
    lst = []
    lst.append(S)
    
    while S >= 10:
        new_num = func(S)
        S = new_num
        lst.append(S)
    
    for i in lst:
        print(i, end=" ")

    print()