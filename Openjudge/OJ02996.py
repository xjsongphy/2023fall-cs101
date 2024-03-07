"""于2023-12-28测试通过"""
from heapq import heapify, heappop, heappush

n, k = int(input()), int(input())
ls = list(map(int, input().split()))
for i in range(k):
    found = False
    j = n - 2
    heap = [ls[-1]]
    heapify(heap)
    for j in range(n - 2, -1, -1):
        heappush(heap, ls[j])
        if ls[j] < ls[j + 1]:
            found = True
            p = ls[j]
            break
    if found:
        ocp = False
        idx = j
        j += 1
        while j < n:
            t = heappop(heap)
            if not ocp and t > p:
                ls[idx] = t
                ocp = True
                continue
            ls[j] = t
            j += 1
        if not ocp:
            ls[idx] = heappop(heap)
    else:
        ls = [i for i in range(1, n + 1)]
print(' '.join([str(i) for i in ls]))