N = int(input())

for i in range(N):
    lst = list(input().split())
    idx = int(lst[0])
    st = lst[1]
    answer = st[:idx-1] + st[idx:]
    print(answer)