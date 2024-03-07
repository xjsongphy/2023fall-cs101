"""于2023-10-23测试通过"""
n = int(input())
delta_i = [0, 1, 0, -1]
delta_j = [1, 0, -1, 0]
i = j = 1
direction = 0
matrix = [['-1']*(n + 2)]
matrix += [['-1'] + ['0']*n + ['-1'] for i in range(n)]
matrix += [['-1']*(n + 2)]

for k in range(1, n*n + 1):
    matrix[i][j] = str(k)
    if matrix[i + delta_i[direction]][j + delta_j[direction]] != '0':
        direction = (direction + 1) % 4
    i += delta_i[direction]
    j += delta_j[direction]
for i in range(1, n + 1):
    print(' '.join(matrix[i][1:n + 1]))
