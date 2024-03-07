"""于2023-12-27测试通过"""
v, p = map(int, input().split())
x = sorted(list(map(int, input().split())))
dp = [0]*v
cache = [[-1]*v for _ in range(v)]
pre = 0
for i in range(v):
    pre += x[i]
    dp[i] = x[i]*(i + 1) - pre


def cost(i, j):
    ans = 0
    k = i + 1
    while k < j:
        t = x[k] - x[i]
        if t > x[j] - x[k]:
            break
        ans += t
        k += 1
    while k < j:
        ans += x[j] - x[k]
        k += 1
    return ans


for i in range(v):
    for j in range(i):
        cache[j][i] = cost(j, i)
for i in range(1, p):
    for j in range(v - 1, i - 1, -1):
        dp[j] = min([dp[k] + cache[k][j] for k in range(i - 1, j)])
ans = float('inf')
sub = sum(x[p - 1:])
for i in range(p - 1, v):
    ans = min(ans, dp[i] + sub - x[i]*(v - i))
    sub -= x[i]
print(ans)