lst = list(input().split())
A = lst[0]
B = lst[1]
A_reverse = ""
B_reverse = ""

for i in range(len(A)-1,-1,-1):
    A_reverse = A_reverse + A[i]

for i in range(len(B)-1,-1,-1):
    B_reverse = B_reverse + B[i]

A_reverse = int(A_reverse)
B_reverse = int(B_reverse)

if A_reverse > B_reverse:
    print(A_reverse)
else:
    print(B_reverse)