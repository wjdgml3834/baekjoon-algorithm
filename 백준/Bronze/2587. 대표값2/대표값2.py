total_sum = 0 
mean_lst = []

for i in range(0,5,1):
    n = int(input())
    total_sum += n
    mean_lst.append(n)

avg = int(total_sum / 5)

mean_lst.sort()

middle = len(mean_lst) // 2

mean_num = mean_lst[middle]

print(avg)
print(mean_num)