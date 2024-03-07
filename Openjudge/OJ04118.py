"""于2023-12-25测试通过"""
from bisect import bisect_right
from functools import lru_cache

for _ in range(int(input())):
    n, k = map(int, input().split())
    m, p = list(map(int, input().split())), list(map(int, input().split()))


    @lru_cache()
    def dfs(i):
        index = bisect_right(m, m[i] + k)
        ans = 0
        for j in range(index, n):
            ans = max(ans, dfs(j))
        return ans + p[i]


    print(max([dfs(i) for i in range(n)]))