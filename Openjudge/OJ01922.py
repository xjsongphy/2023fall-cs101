"""于2023-12-8测试通过"""
from math import ceil
while True:
    n = int(input())
    if not n:
        break
    times = []
    for _ in range(n):
        v, t = map(int, input().split())
        if t < 0:
            continue
        times.append(t + 16200/v)
    print(ceil(min(times)))