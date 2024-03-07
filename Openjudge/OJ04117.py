""""""
while True:
    try:
        n = int(input())
    except EOFError:
        break
    dp = [1] + [[0]*i for i in range(1, n + 1)]
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            if j == i:
                dp[i][j - 1] = 1
            elif i - j >= j:
                dp[i][j - 1] = dp[i - j][j - 1]
        for j in range(i - 2, -1, -1):
            dp[i][j] += dp[i][j + 1]
    print(dp[-1][0])
