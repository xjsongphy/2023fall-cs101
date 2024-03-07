"""于2023-12-23测试通过"""
r, c = map(int, input().split())
d_i = [0, 1, 0, -1]
d_j = [1, 0, -1, 0]
i = j = 1
dire = 0
t = [[-1]*(c + 2)]
matrix = t + [[-1] + list(map(int, input().split())) + [-1] for i in range(r)] +  t[:]

for k in range(1, r*c + 1):
    print(matrix[i][j])
    matrix[i][j] = -1
    if matrix[i + d_i[dire]][j + d_j[dire]] == -1:
        dire = (dire + 1) % 4
    i += d_i[dire]
    j += d_j[dire]
