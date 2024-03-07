"""于2023-9-25测试通过"""
import sys
sys.setrecursionlimit(80000)
n, m = map(int, input().split())


def fill_pond(i, j):
    if 0 <= i < n and 0 <= j < m:
        if ponds[i][j]:
            ponds[i][j] = 0
            for r in [-1, 0, 1]:
                for s in [-1, 0, 1]:
                    fill_pond(i + r, j + s)


ponds = [[[0, 1][j == 'W'] for j in input()] for i in range(n)]
i, total = 0, 0
for i in range(n):
    for j in range(m):
        if ponds[i][j]:
            fill_pond(i, j)
            total += 1
print(total)