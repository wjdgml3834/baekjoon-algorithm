T = int(input())

for _ in range(T):
    sentence = input().split()
    lst = []
    for word in sentence:
        word = word[::-1]
        lst.append(word)
    
    for i in lst:
        print(i, end=" ")
    print()