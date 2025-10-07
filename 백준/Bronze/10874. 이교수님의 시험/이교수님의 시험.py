n = int(input())

for i in range(0,n,1):
	lst = list(map(int,input().split()))
	cnt = 0
	
	for ind in range(0,10,1):
		if lst[ind] == (ind % 5) + 1:
			cnt += 1 
			
	if cnt == 10:
		print(i+1)