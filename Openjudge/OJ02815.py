"""于2023-11-24测试通过"""
r, c = int(input()), int(input())
matrix = [list(map(int, input().split())) for _ in range(r)]
dp = [[0] * c for _ in range(r)]


def dfs(i, j):
    if dp[i][j]:
        return 0
    dp[i][j] = 1
    direction = [(8, 1, 0), (4, 0, 1), (2, -1, 0), (1, 0, -1)]
    step = 1
    t = matrix[i][j]
    for d, dx, dy in direction:
        if t >= d:
            t -= d
            continue
        x = i + dx
        y = j + dy
        if not dp[x][y]:
            step += dfs(x, y)
    return step


ans = count = 0
for i in range(r):
    for j in range(c):
        result = dfs(i, j)
        if result:
            count += 1
            ans = max(ans, result)
print(count)
print(ans)