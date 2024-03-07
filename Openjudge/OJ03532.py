"""于2023-11-27测试通过"""
n = int(input())
ls = [-1] + list(map(int, input().split()))
dp = [0, ls[1]] + [0]*(n - 1)
for i in range(2, n + 1):
    for j in range(i):
        if ls[i] > ls[j]:
            dp[i] = max(dp[i], dp[j] + ls[i])
print(max(dp))

