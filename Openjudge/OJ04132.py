"""于2023-11-30测试通过"""
from copy import copy
n, m, x, y, total = 0, 0, 0, 0, 0


def walk(a, b, step, d):
    global total
    step += 1
    d[(a, b)] = 1
    for dx, dy in [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]:
        u = a + dx
        v = b + dy
        if 0 <= u < n and 0 <= v < m:
            if (u, v) in d:
                pass
            elif step == n * m:
                total += 1
            else:
                walk(u, v, step, copy(d))


for _ in range(int(input())):
    n, m, x, y = map(int, input().split())
    total = 0
    walk(x, y, 1, {})
    print(total)