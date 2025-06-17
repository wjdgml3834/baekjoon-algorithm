lst = list(input().split("-"))
result_lst = []

for i in range(0,len(lst),1):
    st = lst[i]
    for j in st:
        result_lst.append(st[0])
        break
        
short_name = "".join(result_lst)
print(short_name)