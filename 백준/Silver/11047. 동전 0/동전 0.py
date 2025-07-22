lst = list(map(int,input().split()))
N = lst[0]
K = lst[1]
coin_lst = []
total = 0 

for i in range(0,N,1):
    n = int(input())
    coin_lst.append(n)
coin_lst.append(K)
coin_lst.sort(reverse=True)
idx = coin_lst.index(K)
for i in range(idx+1,len(coin_lst),1):
    q = K // coin_lst[i]
    remain = K % coin_lst[i]
    total += q
    K = remain
    
print(total)