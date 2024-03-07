"""于2023-11-1测试通过"""
import heapq


n = int(input())
heap = list(map(int, input().split()))
heapq.heapify(heap)
cost = 0
for i in range(n - 1):
    length = heapq.heappop(heap) + heapq.heappop(heap)
    cost += length
    heapq.heappush(heap, length)
print(cost)


# n = int(input())
# ls = sorted(list(map(int, input().split())), reverse=True)
# cost = 0
# for i in range(n - 1):
#     length = ls.pop() + ls.pop()
#     cost += length
#     ls.append(length)
#     ls.sort(reverse=True)
# print(cost)