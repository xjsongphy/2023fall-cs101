"""于2023-12-24测试通过"""
s, e, v = [], [], []
ls = []
count = 0
for _ in range(int(input())):
    si, ei, vi = map(str, input().split())
    sm, sd = map(int, si.split('.'))
    em, ed = map(int, ei.split('.'))
    if em >= 3 or (em == 2 and ed >= 21):
        continue
    ls.append(((sm - 1)*31 + sd - 6, (em - 1)*31 + ed - 6, int(vi)))
    count += 1
ls.sort(key=lambda t: t[1])
for si, ei, vi in ls:
    s.append(si)
    e.append(ei)
    v.append(vi)
dp = [[0]*46 for _ in range(count)]
for i in range(46):
    if i >= e[0]:
        dp[0][i] = v[0]
for i in range(1, count):
    for j in range(1, 46):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        if j >= e[i]:
            dp[i][j] = max(dp[i][j], dp[i - 1][s[i] - 1] + v[i])
print(dp[-1][-1])