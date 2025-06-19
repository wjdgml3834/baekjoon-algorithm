st = input()
is_pelindrome = True
for i in range(0,len(st)//2,1):
    if st[i] != st[len(st)-(i+1)]:
        is_pelindrome = False
        break

if is_pelindrome:
    print(1)
else:
    print(0)