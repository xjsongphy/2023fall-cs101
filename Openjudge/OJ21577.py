"""于2023-11-1测试通过"""
m, n = map(int, input().split())
forest = [list(map(int, input().split())) + [0] for _ in range(m)]
space = set([])
for i in range(m):
    for j in range(1, n + 1):
        if forest[i][n - j]:
            forest[i][n - j] = 0
        else:
            forest[i][n - j] = forest[i][n - j + 1] + 1
for i in range(m):
    for j in range(n):
        max_width = forest[i][j]
        for k in range(i, m):
            if not max_width:
                break
            max_width = min(max_width, forest[k][j])
            space.add((k - i + 1)*max_width)
print(max(space))
