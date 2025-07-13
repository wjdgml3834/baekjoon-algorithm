total = 0 # 총합
hundread = 100 # 7난쟁이 키 합 100
lst = [] # 난쟁이들 담을 리스트
fake1 = 0 # 가짜 난쟁이1
fake2 = 0 # 가짜 난쟁이2

for i in range(0,9,1): # 수를 입력받고, 리스트를 만들고, 총합을 구한다.
    n = int(input())
    lst.append(n)
    total += n
    
remain = total - hundread # 총합에서 - 100을 한 수에서 난쟁이 두명의 합이 똑같은지 본다.

for i in lst:   
    for j in lst:
        if i != j and (i + j == remain): # 만약 두 수가 다르고, 합이 나머지와 같다면
             fake1 = i # 가짜 난쟁이들을 저장한다.
             fake2 = j
             break # 그리고 빠져나온다.

lst.remove(fake1) # 리스트에서 그 난쟁이 키를 삭제한다. 
lst.remove(fake2)

lst.sort() # 오름 차순 정렬

for i in lst:
    print(i)