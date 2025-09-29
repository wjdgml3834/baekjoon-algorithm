lst = []
for _ in range(5):
    water = int(input())
    lst.append(water)

A,B,C,D,P = lst 

if P <= C:
    x_cost = A * P 
    y_cost = B
    
    if x_cost < y_cost:
        print(x_cost)
    
    elif x_cost > y_cost:
        print(y_cost)

else:
    x_cost = A * P
    y_cost = B + ((P-C) * D)
    
    if x_cost < y_cost:
        print(x_cost)
    
    elif  x_cost > y_cost:
        print(y_cost)
    