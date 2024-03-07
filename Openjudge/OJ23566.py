"""于2023-9-25测试通过"""
n, m = map(int, input().split())
shops = {i:0 for i in range(1, m + 1)}
for i in range(n):
    good = input().split()
    shops[int(good[0])] += int(good[1])
min_price = []
discount = []
for i in range(m):
    coupon = input().split('-')
    min_price.append(int(coupon[0]))
    discount.append(int(coupon[1]))
raw_price = 0
price = 0
for i in range(m):
    raw_price += shops[i + 1]
    price += shops[i + 1]
    if shops[i + 1] >= min_price[i]:
        price -= discount[i]
price -= (raw_price//200)*30
print(price)
