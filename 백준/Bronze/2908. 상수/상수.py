lst = input().split()
f = lst[0]
r = lst[1]
fnum = 0
rnum = 0
sq = 1

for i in range(0,3,1):
    fnum = fnum + int(f[i]) * sq
    rnum = rnum + int(r[i]) * sq
    sq = sq * 10

if fnum > rnum:
    print(fnum)
else:
    print(rnum)