A = int(input())
B = int(input())
C = int(input())
ABC = A * B * C
st_ABC = str(ABC)
lst_ABC = list(map(int,st_ABC))

for i in range(0,10,1):
    cnt = lst_ABC.count(i)
    print(cnt)