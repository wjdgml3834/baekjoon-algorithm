lst = []
w_lst = []
k_lst = []
w_total = 0
k_total = 0

for i in range(0,20,1):
    n = int(input())
    lst.append(n)
w_lst = lst[0:10]
k_lst = lst[10:20]
w_lst.sort(reverse=True)
k_lst.sort(reverse=True)
w_total = w_lst[0] + w_lst[1] + w_lst[2]
k_total = k_lst[0] + k_lst[1] + k_lst[2]

print(w_total, k_total)