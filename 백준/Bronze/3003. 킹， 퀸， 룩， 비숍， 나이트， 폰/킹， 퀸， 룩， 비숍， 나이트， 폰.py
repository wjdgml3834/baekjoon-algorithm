lst = [1,1,2,2,2,8] 
user_lst = list(map(int,input().split()))
result = []

for i in range(0,len(lst),1):
    diff = lst[i] - user_lst[i]
    result.append(diff)

for i in result:
    print(i, end=" ")