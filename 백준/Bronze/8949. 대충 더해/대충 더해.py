lst = list(map(int,input().split()))
a = lst[0]
b = lst[1]
lst2 = []
st_a = str(a)
st_b = str(b)

if len(st_a) >= len(st_b):
    for _ in range(len(st_a)):
        a_digit = a % 10
        b_digit = b % 10
        sum_digit = a_digit + b_digit
        lst2.append(str(sum_digit))
        a //= 10
        b //= 10

else:
    for _ in range(len(st_b)):
        a_digit = a % 10
        b_digit = b % 10
        sum_digit = a_digit + b_digit
        lst2.append(str(sum_digit))
        a //= 10
        b //= 10


lst2.reverse()
join_result = "".join(lst2)
result = int(join_result)
print(result)