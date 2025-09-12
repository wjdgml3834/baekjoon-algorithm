word = input()
N = int(input())
cnt = 0 
for _ in range(N):
    st = input()
    st = st * 2
    if word in st:
        cnt += 1

print(cnt)