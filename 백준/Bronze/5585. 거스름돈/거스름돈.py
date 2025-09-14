pay_money = int(input()) # 지불할 돈
left_money = 1000 - pay_money # 돌려줘야할 돈
cnt = 0 # 매수 
lst = [500,100,50,10,5,1] # 잔돈 종류를 리스트에 담는다. 

for i in lst:
    r = left_money // i # 몫이 매수이다. 
    cnt += r
    left_money = left_money % i # 나머지는 남은 잔돈으로 0이 될때까지 돌린다. 

print(cnt)