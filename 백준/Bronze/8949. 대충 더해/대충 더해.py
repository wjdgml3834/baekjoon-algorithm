lst = input().split()

n1 = lst[0]
n2 = lst[1]

len1 = len(n1)
len2 = len(n2)
gap = abs(len1 - len2)

if len1 > len2:
    n2 = "0"*gap + n2 

elif len1 < len2:
    n1 = "0"*gap + n1

rst = ""
for i in range(0,len(n1),1):
    sum_digit = int(n1[i]) + int(n2[i])
    rst += str(sum_digit)

rst = int(rst)
print(rst)