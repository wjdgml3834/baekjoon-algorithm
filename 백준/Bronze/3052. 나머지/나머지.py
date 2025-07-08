lst = []
result = []

for i in range(0,10,1):
    n = int(input())
    remain = n % 42
    lst.append(remain)

for i in range(0,len(lst),1):
    if lst.count(lst[i]) >= 2 and lst[i] not in result:
            result.append(lst[i])
    elif lst.count(lst[i]) == 1:
        result.append(lst[i])
                        
print(len(result))