n = int(input())

for i in range(0,n,1):
    mx = -1
    mn = 101 
    gapmx = -1
    gap_lst = []
    
    lst = list(map(int,input().split()))
    
    lst.remove(lst[0])
    
    lst.sort(reverse=True)
    
    mx = lst[0]
    mn = lst[len(lst)-1]
    
    for j in range(0,len(lst)-1,1):
        diff = lst[j] - lst[j+1]
        gap_lst.append(diff)
    
    gap_lst.sort(reverse=True)
    gapmx = gap_lst[0]    
    
    print(f"Class {i+1}")
    print(f"Max {mx}, Min {mn}, Largest gap {gapmx}")