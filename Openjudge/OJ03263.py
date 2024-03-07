"""于2023-12-27测试通过"""
while True:
    n = int(input())
    if not n:
        break
    dp = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n - 2, -1, -1):
        for j in range(i + 1):
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1], dp[i][j])
    r, c = map(int, input().split())
    print(dp[r - 1][c - 1])