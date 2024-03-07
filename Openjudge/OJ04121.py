"""于2023-10-26测试通过"""
for _ in range(int(input())):
    n = int(input())
    prices = list(map(int, input().split()))
    earnings, r_earnings = [0], [0]
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        earnings.append(max(earnings[-1], prices[i] - min_price))
    prices.reverse()
    max_price = prices[0]
    for i in range(1, n):
        max_price = max(max_price, prices[i])
        r_earnings.append(max(r_earnings[-1], max_price - prices[i]))
    r_earnings.reverse()
    print(max([earnings[i] + r_earnings[i] for i in range(n)]))