"""于2023-12-28测试通过"""
from heapq import heapify, heappop, heappush

for _ in range(int(input())):
    n, k = map(int, input().split())
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






# factorials = [1]
# m = int(input())
# for i in range(m):
#     n, k = map(int, input().split())
#     if len(factorials) <= n:
#         for j in range(len(factorials), n + 1):
#             factorials.append(factorials[-1]*j)
#     previous = [int(i) for i in input().split()]
#     num = 0
#     for j in range(n):
#         for a in range(j + 1, n):
#             if previous[a] < previous[j]:
#                 num += factorials[n - 1 - j]
#     num = (num + k) % factorials[n] + 1
#     nums = {j + 1: 1 for j in range(n)}
#     space = False
#     for j in range(n):
#         if num % factorials[n - 1 - j] == 0:
#             index = 0
#             for l in range(1, n + 1):
#                 if nums[l]:
#                     index += 1
#                 if index == num // factorials[n - 1 - j]:
#                     if space:
#                         print(' ', end='')
#                     space = True
#                     print(l, end='')
#                     nums[l] = 0
#                     break
#             num = factorials[n - 1 - j]
#         else:
#             index = 0
#             for l in range(1, n + 1):
#                 if nums[l]:
#                     index += 1
#                 if index == num // factorials[n - 1 - j] + 1:
#                     if space:
#                         print(' ', end='')
#                     space = True
#                     print(l, end='')
#                     nums[l] = 0
#                     break
#             num = num % factorials[n - 1 - j]
#     print()