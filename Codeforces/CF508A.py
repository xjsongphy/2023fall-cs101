"""于2023-8-31测试通过"""


def calculate_function(x, y):
    return matrix[x][y] + matrix[x + 1][y] + matrix[x][y + 1] + matrix[x + 1][
        y + 1]


n, m, k = map(int, input().split())
matrix = [[0 for j in range(m + 2)] for i in range(n + 2)]
if n == 1 or m == 1:
    print(0)
    exit()
for i in range(0, k):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    if calculate_function(x - 1, y - 1) == 4:
        print(i + 1)
        exit()
    if calculate_function(x, y) == 4:
        print(i + 1)
        exit()
    if calculate_function(x - 1, y) == 4:
        print(i + 1)
        exit()
    if calculate_function(x, y - 1) == 4:
        print(i + 1)
        exit()
print(0)