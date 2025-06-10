T = int(input())
for i in range(0,T,1):
    lst = list(map(int, input().split()))
    a = lst[0]
    b = lst[1]
    result = a + b
    template = "Case %d: %d" 
    sentence = template % (i+1,result)
    print(sentence)