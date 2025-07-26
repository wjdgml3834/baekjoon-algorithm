S = input()
dic = {}
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in range(0,len(alphabet),1):
    letter = alphabet[i]
    dic[letter] = 0

for i in range(0,len(S),1):
    for key in dic.keys():
        if key == S[i]:
            dic[key] = dic[key] + 1

for v in dic.values():
    print(v, end=" ")