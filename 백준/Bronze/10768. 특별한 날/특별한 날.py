mm = int(input())
dd = int(input())

if mm > 2:
    print("After")
elif mm < 2:
    print("Before")
else:
    if dd > 18:
        print("After")
    elif dd < 18:
        print("Before")
    else:
        print("Special")