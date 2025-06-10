lst1 = list(map(int,input().split()))
lst2 = list(map(int,input().split()))
S = 0
T = 0

for i in lst1:
    S += i

for i in lst2:
    T += i
    
if S > T:
    print(S)
elif S < T:
    print(T)
else:
    print(S)