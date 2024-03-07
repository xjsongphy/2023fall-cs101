"""于2023-12-24测试通过"""
import math

while True:
    L, n, c = map(float, input().split())
    if L == -1:
        break
    low, high = 0.0, 0.5 * L
    s = (1 + n * c) * L
    while high - low > 1e-5:
        mid = (low + high) / 2
        r = (4 * mid * mid + L * L) / (8 * mid)
        if 2 * r * math.asin(L / (2 * r)) < s:
            low = mid
        else:
            high = mid
    h = mid
    print("{:.3f}".format(h))

