"""于2023-12-24测试通过"""
while True:
    s, e = [], []
    ls = []
    count = 0
    n = int(input())
    if not n:
        break
    for _ in range(n):
        si, ei = map(int, input().split())
        ls.append((si + 1, ei + 1))
        count += 1
    ls.sort(key=lambda t: t[1])
    for si, ei in ls:
        s.append(si)
        e.append(ei)
    dp = [[0]*1002 for _ in range(count)]
    for i in range(1002):
        if i >= e[0]:
            dp[0][i] = 1
    for i in range(1, count):
        for j in range(1, 1002):
            dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
            if j >= e[i]:
                dp[i][j] = max(dp[i][j], dp[i - 1][s[i]] + 1)
    print(dp[-1][-1])