"""于2023-12-22参考题解测试通过"""
from heapq import heappush, heappop, heapify
n, m, start, matrix = 0, 0, 0, 0


def bfs():
    visited = [[0 for _ in range(m)] for _ in range(n)]
    q = []
    heapify(q)
    heappush(q, (0, start[0], start[1]))
    visited[start[0]][start[1]] = 1
    while len(q):
        time, x, y = heappop(q)
        time += 1
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m) or visited[nx][ny] or matrix[nx][ny] == '#':
                continue
            if matrix[nx][ny] == 'a':
                return time
            else:
                heappush(q, (time + (matrix[nx][ny] == 'x'), nx, ny))
                visited[nx][ny] = True
    return 'Impossible'


for _ in range(int(input())):
    n, m = map(int, input().split())
    matrix = [input() for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 'r':
                start = (i, j)
                break
    print(bfs())

# from queue import Queue
# searched, time = None, None
#
#
# def allowed(x, y):
#     if searched[x][y] <= time:
#         return False
#     elif matrix[x][y] == '#':
#         return False
#     return True
#
#
# for _ in range(int(input())):
#     m, n = map(int, input().split())
#     matrix = ['#'*(n + 2)] + ['#' + input() + '#' for i in range(m)] + ['#'*(n + 2)]
#     ls = Queue()
#     for i in range(1, m + 1):
#         if 'r' in matrix[i]:
#             j = matrix[i].index('r')
#             ls.put((i, j, 0))
#             break
#     for i in range(1, m + 1):
#         if 'a' in matrix[i]:
#             j = matrix[i].index('a')
#             end = (i, j)
#             break
#     searched = [[float('inf') for i in range(n + 2)] for j in range(m + 2)]
#     min_time = float('inf')
#     while not ls.empty():
#         x, y, time = ls.get()
#         t = abs(end[0] - x) + abs(end[1] - y)
#         if time + t >= min_time or not allowed(x, y):
#             continue
#         if (x, y) == end:
#             min_time = min(min_time, time)
#             searched[end[0]][end[1]] = min_time
#             continue
#         time += (matrix[x][y] == 'x')
#         searched[x][y] = time
#         time += 1
#         if time + t >= min_time:
#             continue
#         for dx, dy in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
#             if matrix[x + dx][y + dy] == '#':
#                 continue
#             elif searched[x + dx][y + dy] <= time:
#                 continue
#             ls.put((x + dx, y + dy, time))
#     if not min_time == float('inf'):
#         print(min_time)
#     else:
#         print('Impossible')