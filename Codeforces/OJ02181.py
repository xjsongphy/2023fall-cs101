""""""
n = int(input())
a = [int(input()) for _ in range(n)]
ans = 0
b = True
for i in range(n - 1):
    if b:
        if a[i] > a[i + 1]:
            ans += a[i]
            b = False
    else:
        if a[i] < a[i + 1]:
            ans -= a[i]
            b = True
if b:
    ans += a[-1]
print(ans)
# 讨论归纳法可以证明贪心正确性

# 二维dp，超空间；优化空间超时
# n = int(input())
# ls = [int(input()) for _ in range(n)]
# dp = [[0]*(n - i) for i in range(n)]
# dp[0][0] = ls[0]
# for i in range(1, n):
#     dp[0][i] = max(dp[0][i - 1], ls[i])
# for i in range(1, n):
#     for j in range(i, n):
#         if i == j:
#             dp[i][0] = dp[i - 1][0] + [1, -1][i % 2]*ls[i]
#         else:
#             dp[i][j - i] = max(dp[i][j - i - 1], dp[i - 1][j - i] + [1, -1][i % 2]*ls[j])
# print(max([dp[i][-1] for i in range(n)]))

