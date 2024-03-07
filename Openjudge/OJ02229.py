"""于2023-12-27测试通过"""
n = int(input())
dp = [[1]]
max_idx = [0]
eps = 1000000000
for i in range(1, n + 1):
    if i & 1:
        dp.append([dp[i - 1][0]])
        max_idx.append(0)
        continue
    dp.append(dp[i - 1])
    c = 2
    idx = 1
    while c <= i:
        if idx <= max_idx[i - c]:
            dp[i].append(dp[i - c][idx])
        elif i == c:
            dp[i].append(1)
        elif i % c:
            break
        c = c << 1
        idx += 1
    max_idx.append(idx - 1)
    for j in range(idx - 2, -1, -1):
        dp[i][j] += dp[i][j + 1]
        dp[i][j + 1] %= eps
    dp[i][0] %= eps
print(dp[-1][0])