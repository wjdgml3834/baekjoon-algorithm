lst = []
for i in range(0,10,1):
    user_input = int(input())
    lst.append(user_input)

total_sum = 0
cnt = 0
mode = 0

for i in lst:
    total_sum += i
    if lst.count(i) > cnt:
        cnt = lst.count(i)
        mode = i

avg = total_sum // len(lst)

print(avg)
print(mode)