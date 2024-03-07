"""于2023-12-7测试通过"""
from queue import Queue
m, n = map(int, input().split())
matrix = [[-1]*(n + 2)] + [[-1] + list(map(int, input().split())) + [-1] for _ in range(m)] + [[-1]*(n + 2)]
ls = Queue()
ls.put((1, 1, 0))
searched = {}
while not ls.empty():
    x, y, step = ls.get()
    if matrix[x][y] == 1:
        print(step)
        exit()
    elif matrix[x][y] in [2, -1] or (x, y) in searched:
        continue
    searched[(x, y)] = 1
    step += 1
    ls.put((x + 1, y, step))
    ls.put((x - 1, y, step))
    ls.put((x, y + 1, step))
    ls.put((x, y - 1, step))
print('NO')