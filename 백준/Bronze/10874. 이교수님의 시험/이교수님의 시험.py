answer_lst = []

for i in range(1,11,1):
    answer = ((i-1) % 5) + 1
    answer_lst.append(answer)

N = int(input())

for i in range(1,N+1,1):
    lst = list(map(int,input().split()))
    
    if lst == answer_lst:
        print(i)