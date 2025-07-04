total_sum = 0
mx = 0 
p = 0

for i in range(0,5,1):
    lst = list(map(int,input().split()))
    total_sum = 0
    
    for j in range(0,4,1):
        total_sum += lst[j]
        
    if mx < total_sum:
        mx = total_sum
        p = i+1
        
print(p, mx)