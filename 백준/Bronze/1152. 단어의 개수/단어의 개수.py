st = input()

cnt = st.count(" ")

if st[0] == " ":
    cnt -= 1

if st[len(st)-1] == " ":
    cnt -= 1

rst = cnt + 1

print(rst)
    