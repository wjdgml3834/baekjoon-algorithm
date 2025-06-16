burger1 = int(input())
burger2 = int(input())
burger3 = int(input())
cola = int(input())
sprite = int(input())
burger_lst = [burger1, burger2, burger3]
soda_lst = [cola, sprite]
burger_min = 2001
soda_min = 2001

for i in burger_lst:
    if i < burger_min:
        burger_min = i

for i in soda_lst:
    if i < soda_min:
        soda_min = i

result = (burger_min + soda_min) - 50

print(result)