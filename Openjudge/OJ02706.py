"""于2023-12-12测试通过"""
from math import log, ceil

p = int(input())
n = ceil(p*(log(2, 10)))
print(n)
t = 2
lim = pow(10, 500)
for _ in range(int(log(p, 2))):
    t *= t
    if t >= lim:
        t = t % lim
for _ in range(p - pow(2, int(log(p, 2)))):
    t *= 2
    if t >= lim:
        t = t % lim
t -= 1
t = str(t).rjust(500, '0')
for i in range(10):
    print(t[i*50: (i + 1)*50])