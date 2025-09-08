lst = list(map(int,input().split()))
a = lst[0]
b = lst[1]
c = lst[2]

if a + b == c:
    print(f"{a}+{b}={c}")


elif a - b == c:
    print(f"{a}-{b}={c}")
    

elif a * b == c:
    print(f"{a}*{b}={c}")


elif a / b == c:
    print(f"{a}/{b}={c}")
    
    
elif b + c == a:
    print(f"{a}={b}+{c}")


elif b - c == a:
    print(f"{a}={b}-{c}")


elif b * c == a:
    print(f"{a}={b}*{c}")


elif b / c == a:
    print(f"{a}={b}/{c}")