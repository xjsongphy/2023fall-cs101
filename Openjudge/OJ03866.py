"""于2023-11-6测试通过"""
from queue import Queue

while True:
    w, h = map(int, input().split())
    if not w + h:
        break
    matrix = [[1]*(w + 2)]
    for r in range(h):
        string = input()
        matrix.append([1])
        for s in range(w):
            if string[s] == '@':
                i, j = r + 1, s + 1
            matrix[-1].append([0, 1][string[s] == '#'])
        matrix[-1].append(1)
    matrix += [[1] * (w + 2)]
    total = 0
    queue = Queue()
    queue.put((i, j))
    while not queue.empty():
        l = queue.get()
        i, j = l[0], l[1]
        if matrix[i][j]:
            continue
        total += 1
        matrix[i][j] = 1
        if not matrix[i + 1][j]:
            queue.put((i + 1, j))
        if not matrix[i - 1][j]:
            queue.put((i - 1, j))
        if not matrix[i][j + 1]:
            queue.put((i, j + 1))
        if not matrix[i][j - 1]:
            queue.put((i, j - 1))
    print(total)