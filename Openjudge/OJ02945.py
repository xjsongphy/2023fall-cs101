"""于2023-11-20测试通过"""
k = int(input())
h = list(map(int, input().split()))
h.reverse()
dp = [[0]*k for _ in range(k)]
for i in range(k):
    for j in range(i):
        if not i:
            dp[0][0] = 1
        else:
            dp[i][j] = [0, dp[j][j]][h[j] <= h[i]] + 1
    dp[i][i] = max(dp[i])
    dp[i][i] = max(1, dp[i][i])
print(max([dp[i][i] for i in range(k)]))