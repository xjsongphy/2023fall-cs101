"""于2023-12-6测试通过"""
n = int(input())
d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
t = [[-1]*(n + 2)]
matrix = t + [[-1] + list(map(int, input().split())) + [-1] for _ in range(n)] + t
dx = x = y = 1
dy = i = 0
for _ in range(n*n):
    t = matrix[x][y]
    print(['', chr(t)][t > 0], end='')
    matrix[x][y] = -1
    i = [i, (i + 1) % 4][matrix[x + dx][y + dy] < 0]
    dx, dy = d[i]
    x += dx
    y += dy
