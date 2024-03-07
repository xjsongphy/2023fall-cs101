"""于2023-12-7测试通过"""
from math import sqrt
n, d = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]
max_earning = (0, 0, 0)


def func(a, b):
    global max_earning
    sum1 = sum2 = earning = 0
    for i in range(d - 1):
        if i >= 3:
            ave = sum1/i
            std = sqrt(sum2/i - ave * ave)
            t = p[a][i + 1] - p[a][i] + p[b][i] - p[b][i + 1]
            u = p[a][i] - p[b][i] - ave
            if u > 0:
                k = u // std - [0, 1][u % std == 0]
                earning -= k * t
            elif u < 0:
                k = (-u) // std - [0, 1][(-u) % std == 0]
                earning += k * t
        t = p[a][i] - p[b][i]
        sum1 += t
        sum2 += t * t
    t = (earning, a + 1, b + 1)
    max_earning = [max(max_earning, t), t][max_earning == (0, 0, 0)]


for i in range(n - 1):
    for j in range(i + 1, n):
        func(i, j)
print(max_earning[1], max_earning[2], int(max_earning[0]))
