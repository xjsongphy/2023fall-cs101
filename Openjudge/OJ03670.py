"""于2023-10-23测试通过"""
matrix = [list(map(int, input().split())) for i in range(5)]
for i in range(5):
    j = matrix[i].index(max(matrix[i]))
    if not sum([matrix[k][j] < matrix[i][j] for k in range(5)]):
        print(i + 1, j + 1, max(matrix[i]))
        exit()
print('not found')