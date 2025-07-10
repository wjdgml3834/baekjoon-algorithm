
lst = [0] * 42
cnt = 0

for i in range(10):
    n = int(input())
    remain = n % 42
    lst[remain] = lst[remain] + 1

for i in lst:
    if i >= 1:
        cnt += 1

print(cnt)