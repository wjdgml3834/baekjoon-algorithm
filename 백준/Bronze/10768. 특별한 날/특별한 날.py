special_total = (29 * 2) + 18
mm = int(input())
dd = int(input())
date_total = (29 * mm) + dd

if special_total > date_total:
    print("Before")
elif special_total < date_total:
    print("After")
else:
    print("Special")