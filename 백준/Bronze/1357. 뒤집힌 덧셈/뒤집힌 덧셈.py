lst = input().split()
X = lst[0]
Y = lst[1]
Rev_X = 0
Rev_Y = 0
result = 0
X_sq = 1 
Y_sq = 1
XY_sq = 1

for i in range(0,len(X),1):
    Rev_X = Rev_X + int(X[i]) * X_sq
    X_sq = X_sq * 10 

for i in range(0,len(Y),1):
    Rev_Y = Rev_Y + int(Y[i]) * Y_sq
    Y_sq = Y_sq * 10 

Rev_XY = str(Rev_X + Rev_Y)

for i in range(0,len(Rev_XY),1):
    result = result + int(Rev_XY[i]) * XY_sq
    XY_sq = XY_sq * 10 

print(result)