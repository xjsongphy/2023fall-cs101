"""于2023-12-24测试通过"""
from math import ceil

n, m = map(int, input().split())
ls = [int(input()) for _ in range(n)]
l, r = 0, sum(ls)


def judge(lim):
    count = 1
    total = 0
    for i in range(n):
        if ls[i] > lim:
            return False
        if total + ls[i] > lim:
            count += 1
            total = ls[i]
        else:
            total += ls[i]
    if count > m:
        return False
    return True


while r - l > 1:
    mid = ceil((l + r) / 2)
    if judge(mid):
        r = mid
    else:
        l = mid
print(r)