"""于2023-10-10测试通过"""
from copy import deepcopy

board = 1
while True:
    w, h = map(int, input().split())
    if w + h == 0:
        break
    maps = [[] for i in range(h + 2)]
    for i in range(h + 2):
        maps[i].append(0)
        if i == 0 or i == h + 1:
            for j in range(w):
                maps[i].append(0)
        else:
            for j in input():
                maps[i].append([0, 1][j == 'X'])
        maps[i].append(0)

    print(f'Board #{board}:')
    pair = 1
    while True:
        y1, x1, y2, x2 = map(int, input().split())
        if x1 + y1 + x2 + y2 == 0:
            break
        begin = {((x1, y1), 1): '', ((x1, y1), 2): ''}
        end = (x2, y2)

        queue = begin
        next_queue = {}
        searched = {}
        step = 0
        found = False
        while True:
            for i in queue.keys():
                if i[0] == end:
                    print(f'Pair {pair}: {step} segments.')
                    found = True
                    break
                else:
                    searched[i] = 1
                    x = i[0][0]
                    y = i[0][1]
                    if maps[x][y] == 1 and step != 0:
                        continue
                    if i[1] == 1:
                        for j in range(x + 1, h + 2):
                            next = ((j, y), 2)
                            if queue.get(next) or next_queue.get(next) or searched.get(next):
                                break
                            next_queue[next] = ''
                            if maps[j][y] == 1:
                                break
                        for j in range(0, x):
                            next = ((x - 1 - j, y), 2)
                            if queue.get(next) or next_queue.get(next) or searched.get(next):
                                break
                            next_queue[next] = ''
                            if maps[x- 1 - j][y] == 1:
                                break
                    else:
                        for j in range(y + 1, w + 2):
                            next = ((x, j), 1)
                            if queue.get(next) or next_queue.get(next) or searched.get(next):
                                break
                            next_queue[next] = ''
                            if maps[x][j] == 1:
                                break
                        for j in range(0, y):
                            next = ((x, y - 1 - j), 1)
                            if queue.get(next) or next_queue.get(next) or searched.get(next):
                                break
                            next_queue[next] = ''
                            if maps[x][y - 1 - j] == 1:
                                break
            if found:
                break
            if len(next_queue) == 0:
                print(f'Pair {pair}: impossible.')
                break
            queue = deepcopy(next_queue)
            next_queue = {}
            step += 1
        pair += 1
    board += 1
    print()