"""于2023-12-24测试通过"""
# 贪心算法
s, e = [], []
ls = []
count = 0
for _ in range(int(input())):
    si, ei = map(int, input().split())
    if si < 0 or ei > 60:
        continue
    ls.append((si + 1, ei + 1))
    count += 1
ls.sort(key=lambda t: t[1])
for si, ei in ls:
    s.append(si)
    e.append(ei)
end = e[0]
ans = 1
for i in range(1, count):
    if s[i] > end:
        end = e[i]
        ans += 1
print(ans)

# 动态规划解法
# s, e = [], []
# ls = []
# count = 0
# for _ in range(int(input())):
#     si, ei = map(int, input().split())
#     if si < 0 or ei > 60:
#         continue
#     ls.append((si + 1, ei + 1))
#     count += 1
# ls.sort(key=lambda t: t[1])
# for si, ei in ls:
#     s.append(si)
#     e.append(ei)
# dp = [[0]*62 for _ in range(count)]
# for i in range(62):
#     if i >= e[0]:
#         dp[0][i] = 1
# for i in range(1, count):
#     for j in range(1, 62):
#         dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
#         if j >= e[i]:
#             dp[i][j] = max(dp[i][j], dp[i - 1][s[i] - 1] + 1)
# print(dp[-1][-1])