word = input()
word = word.upper()
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lst = [0] * 26
result = ""

for ch in word:
    idx = alphabet.index(ch)
    lst[idx] = lst[idx] + 1

mx = max(lst)
idx = lst.index(mx) 
result = alphabet[idx]

if lst.count(mx) > 1:
    result = "?"

print(result)