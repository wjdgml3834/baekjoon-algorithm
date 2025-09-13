cnt = 0 

for i in range(8):
    line = input()
    if i % 2 == 0:
        for j in range(0,len(line),1):
            if j % 2 == 0 and line[j] == "F":
                cnt += 1
    
    else:
         for j in range(0,len(line),1):
            if j % 2 == 1 and line[j] == "F":
                cnt += 1

print(cnt)