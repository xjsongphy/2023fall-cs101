"""于2023-12-23测试通过"""
n = int(input())
heights = list(map(int, input().split()))
dp = [1] * n
dp_low = dp[:]
for i in range(n - 2, -1, -1):
    for j in range(i + 1, n):
        if heights[i] > heights[j]:
            dp_low[i] = max(dp_low[i], dp_low[j] + 1)
        elif heights[i] < heights[j]:
            dp[i] = max(dp[i], max(dp[j], dp_low[j]) + 1)
print(max(max(dp), max(dp_low)))