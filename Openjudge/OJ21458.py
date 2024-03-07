"""于2023-12-22测试通过"""
t, n = map(int, input().split())
ts, ws = [], []
for _ in range(n):
    ti, wi = map(int, input().split())
    ts.append(ti)
    ws.append(wi)
dp = [[0] + [-1] * t for _ in range(n)]
dp[0][ts[0]] = ws[0]
for i in range(1, n):
    for j in range(t + 1):
        dp[i][j] = dp[i - 1][j]
        if j < ts[i]:
            continue
        if dp[i - 1][j - ts[i]] != -1:
            dp[i][j] = max(dp[i][j], ws[i] + dp[i - 1][j - ts[i]])
print(dp[-1][-1])