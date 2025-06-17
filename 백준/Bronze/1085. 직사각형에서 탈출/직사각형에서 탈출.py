user_input = list(map(int,input().split()))
x = user_input[0]
y = user_input[1]
w = user_input[2]
h = user_input[3]
min_num = 1001

lst = [x,y,w-x,h-y]

for i in lst:
    if i < min_num:
        min_num = i
        
print(min_num)