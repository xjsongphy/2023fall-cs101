"""于2023-11-9测试通过"""
s, m = input(), int(input())
dp = [0, s[0] == s[1]]
for i in range(1, len(s) - 1):
    dp.append(dp[-1] + (s[i] == s[i + 1]))
dp.append(dp[-1])
for _ in range(m):
    l, r = map(int, input().split())
    print(dp[r - 1] - dp[l - 1])