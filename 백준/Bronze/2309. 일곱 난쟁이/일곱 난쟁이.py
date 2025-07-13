total = 0
hundread = 100 
lst = []
fake1 = 0
fake2 = 0 

for i in range(0,9,1):
    n = int(input())
    lst.append(n)
    total += n
    
remain = total - hundread

for i in lst:   
    for j in lst:
        if i != j and (i + j == remain):
             fake1 = i
             fake2 = j

lst.remove(fake1)
lst.remove(fake2)

lst.sort()

for i in lst:
    print(i)