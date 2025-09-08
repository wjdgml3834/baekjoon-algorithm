import operator

lst = list(map(int,input().split()))
a = lst[0]
b = lst[1]
c = lst[2]
ops = {
    "+" : operator.add,
    "-" : operator.sub,
    "*" : operator.mul,
    "/" : operator.truediv
}
flag = False

while True:
    if flag == True:
        break
    
    for x in ops.keys():
        if ops[x](a,b) == c:
            print(f"{a}{x}{b}={c}")
            flag = True
            break
        
        elif ops[x](b,c) == a:
             print(f"{a}={b}{x}{c}")
             flag = True
             break