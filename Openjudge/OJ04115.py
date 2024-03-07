"""于2023-12-7测试通过"""
from queue import Queue
m, n, t = map(int, input().split())
matrix = [[-1]*(n + 2)] + [[-1] + list(input()) + [-1] for _ in range(m)] + [[-1]*(n + 2)]
ls = Queue()
x, y = 0, 0
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if matrix[i][j] == '@':
            x, y = i, j
            break
ls.put((x, y, t, 0))
searched = {}
while not ls.empty():
    x, y, left, time = ls.get()
    if matrix[x][y] == '+':
        print(time)
        exit()
    elif matrix[x][y] == '#':
        left -= 1
        if left < 0:
            continue
    if matrix[x][y] == -1:
        continue
    if (x, y) in searched:
        if searched[(x, y)] >= left:
            continue
    searched[(x, y)] = left
    time += 1
    ls.put((x + 1, y, left, time))
    ls.put((x - 1, y, left, time))
    ls.put((x, y + 1, left, time))
    ls.put((x, y - 1, left, time))
print(-1)



