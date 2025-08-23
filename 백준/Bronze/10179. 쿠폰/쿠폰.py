N = int(input())

for _ in range(N):
    original_price = float(input()) 
    discount_price = original_price * 0.8
    discount_price = round(discount_price,2)
    print(f"${discount_price:.2f}")