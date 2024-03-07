"""于2023-12-22测试通过"""
import heapq

m, n, p = map(int, input().split())
t = [['#']*(n + 2)]
matrix = t + [['#'] + input().split() + ['#'] for _ in range(m)] + t[:]
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if matrix[i][j] != '#':
            matrix[i][j] = int(matrix[i][j])
for _ in range(p):
    x1, y1, x2, y2 = map(int, input().split())
    x1 += 1
    y1 += 1
    x2 += 1
    y2 += 1
    if matrix[x1][y1] == '#' or matrix[x2][y2] == '#':
        print('NO')
        continue
    heap = []
    heapq.heapify(heap)
    visited = [[0] * (n + 2) for _ in range(m + 2)]
    heapq.heappush(heap, (0, x1, y1))
    min_cost = float('inf')
    while len(heap):
        c, x, y = heapq.heappop(heap)
        if visited[x][y]:
            continue
        t, visited[x][y] = matrix[x][y], 1
        if (x, y) == (x2, y2):
            print(c)
            break
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if matrix[x + dx][y + dy] == '#' or visited[x + dx][y + dy]:
                continue
            heapq.heappush(heap, (c + abs(matrix[x + dx][y + dy] - t), x + dx, y + dy))
    if not visited[x2][y2]:
        print('NO')