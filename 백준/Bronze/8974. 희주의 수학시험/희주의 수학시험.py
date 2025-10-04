lst = [] # 수열을 만들 빈 리스트

for i in range(1,1001,1): # 수열을 담아준다. 
    for _ in range(i):
        lst.append(i)


A,B = map(int,input().split())
total = 0 # 총합을 구할 변수 

for i in range(A,B+1,1): 
    num = int(lst[i-1]) # 인덱스는 -1 해야 한다. 
    total += num

print(total)