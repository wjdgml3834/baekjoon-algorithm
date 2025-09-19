T = int(input())

for _ in range(T):
    n = int(input())
    vote_lst = []
    
    for _ in range(n):
        num = int(input())
        vote_lst.append(num)
        
    mx = -1
    
    for i in vote_lst:
        if mx < i:
            mx = i 
    
    R = vote_lst.index(mx) + 1
    
    if vote_lst.count(mx) != 1:
        print("no winner")
    
    
    elif mx > sum(vote_lst) / 2:
        print(f"majority winner {R}")
        
    
    elif mx <= sum(vote_lst) / 2:
        print(f"minority winner {R}")