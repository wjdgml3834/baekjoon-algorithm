lst = []
desc_lst = []
inp = input()
for i in inp:
    i = int(i)
    lst.append(i)

lst.sort(reverse=True)

for i in lst:
    i = str(i)
    desc_lst.append(i)

st = "".join(desc_lst)

n = int(st)

print(n)