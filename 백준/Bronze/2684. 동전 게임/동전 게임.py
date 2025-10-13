P = int(input())
sq_lst = ['TTT','TTH','THT','THH','HTT','HTH','HHT','HHH']

for _ in range(P):
    st = input()
    lst = [0] * 8 
    
    for idx in range(0,len(st)-2,1):
        coins = st[idx] + st[idx+1] + st[idx+2]
        for i in range(0,len(sq_lst),1):
            if sq_lst[i] == coins:
                lst[i] += 1
    
    for i in lst:
        print(i, end=" ")