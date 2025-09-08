a_lst = list(map(int,input().split()))
b_lst = list(map(int,input().split()))

a_total = 0
b_total = 0 
flag = "D"

for idx in range(0,10,1):
    a_card = a_lst[idx]
    b_card = b_lst[idx]
    
    if a_card > b_card:
        a_total += 3
        flag = "A"
        
    elif a_card < b_card:
        b_total += 3
        flag = "B"
        
    else:
        a_total += 1
        b_total += 1
    
if flag == "D":
    print(a_total,b_total)
    print(flag)

elif a_total == b_total and flag != "D":
    print(a_total,b_total)
    print(flag)

else:
    if a_total > b_total:
        print(a_total,b_total)
        print("A")
    
    elif a_total < b_total:
        print(a_total,b_total)
        print("B")