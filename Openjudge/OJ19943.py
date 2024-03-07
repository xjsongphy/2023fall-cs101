"""于2023-11-1测试通过"""
n, m = map(int, input().split())
matrix = [[0]*n for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    matrix[a][a] += 1
    matrix[b][b] += 1
    matrix[a][b] -= 1
    matrix[b][a] -= 1
for i in range(n):
    print(' '.join([str(s) for s in matrix[i]]))