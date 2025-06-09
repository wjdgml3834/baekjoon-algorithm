N = int(input())
a_win = 0
b_win = 0

for i in range(0,N,1):
    lst = list(map(int,input().split()))
    a = lst[0]
    b = lst[1]
    if a > b:
        a_win += 1
    elif b > a:
        b_win += 1

print(a_win, b_win)