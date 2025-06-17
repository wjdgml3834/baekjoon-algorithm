while True:
  lst = list(map(int,input().split()))
  lst.sort()
  a = lst[0]
  b = lst[1]
  c = lst[2]
  if a == 0 and b == 0 and c == 0:
    break
  if c >= a+b:
    print("Invalid") 
    continue
  if a == b and b == c:
    print("Equilateral")
  elif a == b or b == c or c == a:
    print("Isosceles")
  else:
    print("Scalene")