"""于2023-11-28测试通过"""
n, m = 0, 0


def fill(i, j):
    t = 0
    if 0 <= i < n and 0 <= j < m:
        if ponds[i][j]:
            ponds[i][j] = 0
            t += 1
            for r in [-1, 0, 1]:
                for s in [-1, 0, 1]:
                    if not t == s == 0:
                        t += fill(i + r, j + s)
    return t


for _ in range(int(input())):
    n, m = map(int, input().split())
    ponds = [[[0, 1][j == 'W'] for j in input()] for i in range(n)]
    i, space = 0, set([])
    for i in range(n):
        for j in range(m):
            space.add(fill(i, j))
    print(max(space))