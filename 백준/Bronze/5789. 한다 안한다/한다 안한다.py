N = int(input())

for _ in range(N):
    st = input()
    idx1 = len(st) // 2 
    idx2 = (len(st) // 2) - 1
    n1 = st[idx1]
    n2 = st[idx2]
    if n1 == n2:
        print("Do-it")
    else:
        print("Do-it-Not")