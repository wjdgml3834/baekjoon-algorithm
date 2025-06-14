x_lst = []
y_lst = []
result_x = 0
result_y = 0

for i in range(0,3,1):
    lst = list(map(int,input().split()))
    x = lst[0]
    y = lst[1]
    x_lst.append(x)
    y_lst.append(y)

for i in x_lst:
    if x_lst.count(i) == 1:
        result_x = i

for i in y_lst:
    if y_lst.count(i) == 1:
        result_y = i 
        
print(result_x, result_y)