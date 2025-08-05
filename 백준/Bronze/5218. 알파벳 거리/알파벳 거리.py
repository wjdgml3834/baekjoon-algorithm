n = int(input())

for i in range(n):
	st = input().split()
	st1 = st[0]
	st2 = st[1]
	print("Distances:", end=" ")
	for idx in range(0,len(st1),1):
		gap = ord(st1[idx]) - ord(st2[idx])
		if gap > 0 :
			gap = 26 - gap
		print(abs(gap), end= " ")
		
	print() # 줄바꿈