N = int(input())

rst = 0 

for i in range(0,N,1):
	st = input()
	
	lst = [st[0]]
	
	is_success = True
	
	for ind in range(1, len(st), 1):
		now = st[ind]
		prev = st[ind - 1]
		
		if st[ind] != prev:
			if now in lst:
				is_success = False 
				break
			else:
				lst.append(now)
	
	if is_success:
		rst += 1
	
print(rst)