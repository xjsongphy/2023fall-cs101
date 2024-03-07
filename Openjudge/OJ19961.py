"""于2023-12-22测试通过"""
from copy import deepcopy

m, n, p = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(m)]
ans = set()


def left(ma):
    m, n = len(ma), len(ma[0])
    while True:
        c = False
        for i in range(m):
            for j in range(n - 1, 0, -1):
                if ma[i][j] and not ma[i][j - 1]:
                    ma[i][j], ma[i][j - 1] = 0, ma[i][j]
                    c = True
        if not c:
            break
    for i in range(m):
        for j in range(n - 1, 0, -1):
            if ma[i][j] == ma[i][j - 1]:
                ma[i][j - 1] *= 2
                ma[i][j] = 0
    while True:
        c = False
        for i in range(m):
            for j in range(n - 1, 0, -1):
                if ma[i][j] and not ma[i][j - 1]:
                    ma[i][j], ma[i][j - 1] = 0, ma[i][j]
                    c = True
        if not c:
            break


def rotate(ma):
    m, n = len(ma), len(ma[0])
    new_ma = [[0] * m for _ in range(n)]
    for i in range(m):
        for j in range(n):
            new_ma[j][m - i - 1] = ma[i][j]
    return new_ma


def dfs(matrix, step):
    if not step:
        ans.add(max([max(i) for i in matrix]))
        return
    step -= 1
    for i in range(4):
        new_matrix = deepcopy(matrix)
        left(new_matrix)
        dfs(new_matrix, step)
        matrix = rotate(matrix)


dfs(matrix, p)
print(max(ans))