st = input()
lst = []
for char in st:
    lst.append(char)
result =[]
    
for i in range(0,len(lst),1):
    if lst[i] == lst[len(lst)-(i+1)]:
        result.append(lst[i])

if len(result) == len(lst):
    print(1)
else:
    print(0)