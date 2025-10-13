M = int(input())
lst = [1,2,3]

for _ in range(M):
    x,y = map(int,input().split())
    idx1 = lst.index(x)
    idx2 = lst.index(y)
    
    tmp = lst[idx1]
    lst[idx1] = lst[idx2]
    lst[idx2] = tmp

rst = lst[0]
print(rst)