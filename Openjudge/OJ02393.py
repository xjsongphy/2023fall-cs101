"""于2023-9-25测试通过"""
n, s = map(int, input().split())
total_price = 0
min_price = float("inf")
for i in range(n):
    c, y = map(int, input().split())
    min_price = min(min_price + s, c)
    total_price += min_price*y
print(total_price)
