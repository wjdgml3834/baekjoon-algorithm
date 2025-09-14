lst = list(map(int,input().split()))
A = lst[0]
B = lst[1]

A_str = str(A) # 자릿수 5와 6 파악을 위해 문자열로 변환
B_str = str(B)

A_min = "" # A 최소 담을 변수
A_max = "" # A 최대 담을 변수
B_min = "" # B 최소 담을 변수
B_max = "" # B 최대 담을 변수

for i in A_str: # A가 최소일때 -> 모든 숫자 5로 봄
    if i == "5" or i == "6":
        A_min = A_min + "5"
    
    else:
        A_min = A_min + i 
        

for i in A_str: # A가 최대일 때 -> 모든 숫자 6으로 봄
    if i == "5" or i == "6":
        A_max = A_max + "6"
    
    else:
        A_max = A_max + i 


for i in B_str: # B가 최소일때 -> 모든 숫자 5로 봄
    if i == "5" or i == "6":
        B_min = B_min + "5"
    
    else:
        B_min = B_min + i 


for i in B_str: # B가 최대 일때 -> 모든 숫자 6으로 봄
    if i == "5" or i == "6":
        B_max = B_max + "6"
    
    else:
        B_max = B_max + i 
        
A_min = int(A_min)  # 숫자형으로 모두 변환       
A_max = int(A_max)        
B_min = int(B_min)        
B_max = int(B_max)        
        
rst_min = A_min + B_min
rst_max = A_max + B_max

print(rst_min, rst_max)