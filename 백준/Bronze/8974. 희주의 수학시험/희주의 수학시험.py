lst = []

for i in range(1,1001,1):
    for _ in range(i):
        lst.append(i)


A,B = map(int,input().split())
total = 0 


for i in range(A,B+1,1):   
    num = int(lst[i-1])
    total += num

print(total)