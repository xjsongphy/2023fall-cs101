"""于2023-12-19测试通过"""
ls = [float(i.rstrip('%')) for i in input().split()]
n = len(ls)
price = [100] + [0]*n
for i in range(n):
    price[i + 1] = price[i]*(1 + 0.01*ls[i])

dp = [0]*n + [price[-1]]
dp_i = [0]*n + [n]
for i in range(2, n + 2):
    p = price[-i]
    dp[-i] = min(p, dp[-i + 1])
    dp_i[-i] = [dp_i[-i + 1], n - i + 1][p < dp[-i + 1]]

lose = 0.0
for i in range(1, n):
    p = (dp[i] - price[i])*100/price[i]
    if p < lose:
        lose = p
        t = dp_i[i] - i
print('%.1f' % lose, end='% ')
print(t)
