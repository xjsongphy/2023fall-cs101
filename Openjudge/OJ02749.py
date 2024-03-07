"""于2023-12-26测试通过"""
from functools import lru_cache


@lru_cache()
def func(a, lim):
    ans = 0
    if a == 1:
        return 1
    for i in range(lim, a + 1):
        if a % i == 0:
            ans += func(a // i, i)
    return ans


for _ in range(int(input())):
    print(func(int(input()), 2))