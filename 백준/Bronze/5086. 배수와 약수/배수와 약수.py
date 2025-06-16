
while True:
    lst = list(map(int,input().split()))
    a = lst[0]
    b = lst[1]
    if a == 0 and b == 0:
        break
    if b % a == 0:
        print("factor")
    elif a % b == 0:
        print("multiple")
    else:
        print("neither")