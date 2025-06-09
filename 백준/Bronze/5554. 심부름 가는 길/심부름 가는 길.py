total_ss = 0

for i in range(0,4,1):
    user_input = int(input())
    total_ss += user_input

mm = total_ss // 60
ss = total_ss % 60

print(mm)
print(ss)