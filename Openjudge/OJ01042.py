"""于2023-12-27测试通过"""
from heapq import heapify, heappop, heappush, heappushpop

while True:
    n = int(input())
    if not n:
        break
    h = 12*int(input())
    f, d = list(map(int, input().split())), list(map(int, input().split()))
    t = [0] + list(map(int, input().split()))
    ls = []
    max_fish = 0
    ans = tuple([0]*(n + 1))
    for i in range(n):
        h -= t[i]
        if h <= 0:
            break
        ls.append((-f[i], i))
        heap = ls[:]
        heapify(heap)
        new_ans = [0] * (n + 1)
        for j in range(h):
            fi, k = heappop(heap)
            new_ans[0] -= fi
            fi = min(fi + d[k], 0)
            new_ans[k + 1] += 5
            heappush(heap, (fi, k))
            ans = max(ans, tuple(new_ans))
    print(', '.join([str(ans[i]) for i in range(1, n + 1)]))
    print(f'Number of fish expected: {ans[0]}', end='\n\n')