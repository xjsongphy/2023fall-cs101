"""于2023-12-25测试通过"""
from functools import lru_cache

n = int(input())
ls = list(map(int, input().split()))
cnt = [1]*n
eps = 0.001


@lru_cache()
def dfs(cnt):
    cnt = list(cnt)
    if sum(cnt) == 1:
        for i in range(n):
            if cnt[i] == 1:
                return set([ls[i]])
    elif sum(cnt) == 0:
        return set([1])

    i = 0
    ans = set()
    while i < n:
        if cnt[i] == 1:
            j = i + 1
            a = ls[i]
            while j < n:
                if cnt[j] == 1:
                    new_cnt = cnt[:]
                    new_cnt[i] = new_cnt[j] = 0
                    b = ls[j]
                    p = [a + b, a - b, b - a, a * b, a / b, b / a]
                    for a in p:
                        for b in dfs(tuple(new_cnt)):
                            for q in [a + b, a - b, b - a, a * b]:
                                ans.add(q)
                            if abs(b) > eps:
                                ans.add(a / b)
                j += 1
        i += 1
    return ans


for p in dfs(tuple(cnt)):
    if abs(p - 42) < eps:
        print('YES')
        exit()
print('NO')