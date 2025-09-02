n = int(input())
m = int(input())

lst = list(map(int,input().split()))

lst.sort() # 필수

left = 0
right = n-1

ans = 0 

while True:
    if left == right:
        break
    
    total = lst[left] + lst[right]
    
    if total == m:
        ans += 1
        right -= 1
        
    elif total > m:
        right -= 1
        
    else:
        left += 1

print(ans)