S = input()
lst = [0] * 26
alphabet = "abcdefghijklmnopqrstuvwxyz"

for ch in S:
    idx = alphabet.index(ch)
    lst[idx] = lst[idx] + 1

for i in lst:
    print(i, end= " ")