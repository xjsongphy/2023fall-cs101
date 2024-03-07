"""于2023-12-23测试通过"""
from queue import Queue

n = int(input())
t = [1]*(n + 2)
matrix = [t] + [[1] + list(map(int, input().split())) + [1] for _ in range(n)] + [t[:]]
direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
x, y = [], []
end = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if matrix[i][j] == 9:
            end = (i, j)
        elif matrix[i][j] == 5:
            x.append(i)
            y.append(j)
x1, x2 = x
y1, y2 = y
q = Queue()
visited = {}
q.put((x1, y1, x2, y2))
while not q.empty():
    x1, y1, x2, y2 = q.get()
    if (x1, y1) in visited:
        continue
    if (x1, y1) == end or (x2, y2) == end:
        print('yes')
        exit()
    visited[(x1, y1)] = 1
    for i in range(4):
        dx, dy = direction[i]
        if (x1 + dx, y1 + dy) in visited or matrix[x1 + dx][y1 + dy] == 1 or matrix[x2 + dx][y2 + dy] == 1:
            continue
        q.put((x1 + dx, y1 + dy, x2 + dx, y2 + dy))
print('no')