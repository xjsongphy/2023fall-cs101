"""于2023-10-23测试通过"""
n, m = map(int, input().split())
matrix = [[0 for i in range(m + 2)]]
matrix += [[0] + list(map(int, input().split())) + [0] for i in range(n)]
matrix += [matrix[0][:]]
c = 0

for i in range(1, n + 1):
    for j in range(1, m + 1):
        if matrix[i][j]:
            c += 4 - matrix[i - 1][j] - matrix[i][j - 1] - matrix[i + 1][j] - matrix[i][j + 1]
print(c)