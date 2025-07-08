lst = [] # 점수를 입력받을 리스트
arr = [0] * 151 # 순서를 기억할 index
total_sum = 0 # 총합
result_lst = [] # 최종 결과에 포함된 문제 번호

for i in range(0,8,1): # 우선 점수를 입력받을 리스트를 만들어준다.
    n = int(input())
    lst.append(n)

for i in range(0,len(lst),1): # 입력받은 점수의 순서를 기억하게 한다. 
    idx = lst[i]
    arr[idx] = i+1

lst.sort() # 오름차순으로 정렬한다.

for i in range(-1,-6,-1): # 가장 큰 5개만 불러온다.
    sc = lst[i] # 점수
    total_sum += sc # 점수의 총합
    order = arr[sc] # 순서 = 기존 저장해둔 arr의 value값을 불러온다.
    result_lst.append(order) # 순서를 리스트에 담는다.
    
result_lst.sort() # 문제 번호도 증가하도록 정렬한다.

print(total_sum)
for i in result_lst:
    print(i, end=" ")