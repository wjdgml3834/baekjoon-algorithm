N = int(input())
cnt = 0 
for _ in range(N):
    lst = [0] * 26
    st = input()
    is_group = True
    
    for i in range(0,len(st),1): 
        if i != len(st) - 1:
            if st[i] != st[i+1]:
                last_idx = i + 1 
                ch = st[i]
                idx = ord(ch) - 97
                if lst[idx] != last_idx and lst[idx] !=0:
                    is_group = False
                    break
                else:
                    lst[idx] = last_idx
         
        else: 
            last_idx = i + 1
            ch = st[i]
            idx = ord(ch) - 97
            if lst[idx] != last_idx and lst[idx] !=0:
                is_group = False
                break

    if is_group:
        cnt += 1

print(cnt)   