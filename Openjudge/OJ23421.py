"""于2023-10-4测试通过"""
n, b = map(int, input().split())
values = [int(i) for i in input().split()]
weights = [int(i) for i in input().split()]
maps = [[None for i in range(b)] for j in range(n)]

for i in range(n):
    for j in range(b):
        if i == 0:
            maps[i][j] = [0, values[i]][j + 1 >= weights[i]]
        else:
            if j + 1 == weights[i]:
                maps[i][j] = max(maps[i - 1][j], values[i])
            elif j + 1 > weights[i]:
                maps[i][j] = max(maps[i - 1][j], values[i] + maps[i - 1][j - weights[i]])
            else:
                maps[i][j] = maps[i - 1][j]

print(maps[-1][-1])