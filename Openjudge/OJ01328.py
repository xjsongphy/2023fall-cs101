"""于2023-12-13测试通过"""
from math import sqrt

num = 1
while True:
    n, d = map(int, input().split())
    if n + d == 0:
        break
    x_y = {}
    for _ in range(n):
        x, y = map(int, input().split())
        if x in x_y:
            x_y[x] = max(x_y[x], y)
        else:
            x_y[x] = y
    n = len(x_y)
    count = 1
    x = list(sorted(x_y.keys()))
    try:
        ls = [x[i] + sqrt(d**2 - x_y[x[i]]**2) for i in range(n)]
    except ValueError:
        count = -n
    for i in range(2, n + 1):
        ls[-i] = min(ls[-i], ls[-i + 1])
    l = ls[0]
    for i in range(1, n):
        if (x[i] - l)**2 + x_y[x[i]]**2 - d**2 > 0.001:
            l = ls[i]
            count += 1
    if d < 0 or count <= 0:
        count = -1
    print(f'Case {num}: {count}')
    num += 1
    input()