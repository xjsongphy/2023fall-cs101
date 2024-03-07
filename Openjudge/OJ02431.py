"""于2023-11-3测试通过"""
import heapq as h

n = int(input())
stations = {0: 0}
for i in range(n):
    l, p = map(int, input().split())
    stations[l] = p
l, p = map(int, input().split())
heap = []
h.heapify(heap)
for i in sorted(list(stations.keys()), reverse=True):
    p -= l - i
    l = i
    if p < 0:
        while len(heap) and p < 0:
            p -= h.heappop(heap)
        if p < 0:
            print(-1)
            exit()
    if l:
        h.heappush(heap, -stations[i])
        if not p:
            p -= h.heappop(heap)
print(n - len(heap))