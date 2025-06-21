lst = []
for i in range(0,10,1):
    user_input = int(input())
    lst.append(user_input)

total_sum = 0
cnt = 0
mode = 0

for i in range(0,len(lst),1):
    total_sum += lst[i]
    if lst.count(lst[i]) > cnt:
        cnt = lst.count(lst[i])
        mode = lst[i]

avg = total_sum // len(lst)

print(avg)
print(mode)