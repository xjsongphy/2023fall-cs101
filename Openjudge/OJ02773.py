"""于2023-11-15测试通过"""
t, m = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(m)]
dp = [[0]*(t + 1) for _ in range(m)]
for i in range(m):
    for j in range(1, t + 1):
        if j >= data[i][0]:
            if not i:
                dp[0][j] = data[i][1]
            else:
                dp[i][j] = max(data[i][1] + dp[i - 1][j - data[i][0]], dp[i - 1][j])
        else:
            dp[i][j] = dp[i - 1][j]
print(dp[-1][-1])