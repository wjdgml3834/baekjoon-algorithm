lst = list(map(int,input().split()))
N = lst[0]
M = lst[1]
friends_lst = [0] * (N+1)

for _ in range(M):
    idx1, idx2 = map(int,input().split())
    friends_lst[idx1] += 1
    friends_lst[idx2] += 1

for i in range(1,len(friends_lst),1):
    print(friends_lst[i])