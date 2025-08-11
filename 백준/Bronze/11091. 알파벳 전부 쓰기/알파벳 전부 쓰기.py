n = int(input())
alphabet = "abcdefghijklmnopqrstuvwxyz"

for _ in range(n):
    lst = [0] * 26
    sentence = input().lower()
    stripped_sentence = sentence.replace(" ", "")
    for ch in stripped_sentence:
        idx = alphabet.find(ch)
        if idx != -1:
            lst[idx] += 1
    
    is_pangram = True
    missing_words = ""
    
    for idx in range(0,len(lst),1):
        if lst[idx] == 0:
            missing_st = chr(idx + ord("a"))
            missing_words = missing_words + missing_st
            is_pangram = False
    
    if is_pangram:
        print("pangram")
    else: 
        print(f"missing {missing_words}")