n = int(input())
rst = set()

for _ in range(n):
    lst = input().split()
    name = lst[0]
    status = lst[-1]
    if status == 'enter':
        rst.add(name)
        
    else:
        rst.discard(name)
        
sorted_rst = sorted(rst, reverse=True)

for i in sorted_rst:
        print(i)