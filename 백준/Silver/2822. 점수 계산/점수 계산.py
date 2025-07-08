lst = []
arr = [0] * 151
total_sum = 0
result_lst = []

for i in range(0,8,1):
    n = int(input())
    lst.append(n)

for i in range(0,len(lst),1):
    idx = lst[i]
    arr[idx] = i+1

lst.sort()

for i in range(-1,-6,-1):
    total_sum += lst[i]
    result_lst.append(arr[lst[i]])
    
result_lst.sort()
print(total_sum)
for i in result_lst:
    print(i, end=" ")