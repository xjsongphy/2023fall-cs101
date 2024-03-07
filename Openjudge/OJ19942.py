"""于2023-11-1测试通过"""
m, n, p, q = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
kernel = [list(map(int, input().split())) for _ in range(p)]
ans = [[0]*(n - q + 1) for _ in range(m - p + 1)]

for i in range(p):
    for j in range(q):
        for r in range(m - p + 1):
            for s in range(n - q + 1):
                ans[r][s] += matrix[i + r][j + s]*kernel[i][j]

for i in range(m - p + 1):
    print(' '.join([str(j) for j in ans[i]]))
