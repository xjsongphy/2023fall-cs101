"""于2023-12-25测试通过"""
for _ in range(int(input())):
    r, c, k = map(int, input().split())
    vis = {}
    matrix = [list(input()) for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == 'S':
                ls = [(i, j)]
            if matrix[i][j] == 'E':
                end = (i, j)
    time = 0
    found = False
    while True:
        next_ls = []
        for i, j in ls:
            t = time % k
            if (i, j) == end:
                print(time)
                next_ls = []
                found = True
                break
            if t != 0 and matrix[i][j] == '#':
                continue
            if (i, j) in vis:
                if t in vis[(i, j)]:
                    continue
                vis[(i, j)][t] = 1
            else:
                vis[(i, j)] = {t: 1}
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= i + di < r and 0 <= j + dj < c:
                    next_ls.append((i + di, j + dj))
        time += 1
        if not next_ls:
            break
        ls = next_ls[:]
    if not found:
        print('Oop!')