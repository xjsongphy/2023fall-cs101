""""于2023-8-26测试通过"""
while True:
    output = []
    n, p, m = map(int, input().split())
    if n == p == m == 0:
        break
    monkey = [i for i in range(1, n + 1)]

    i, j = 1, p - 1
    while len(monkey) > 1:
        if i == m:
            i = 0
            output.append(monkey.pop(j))
            if j > len(monkey) - 1:
                j = 0
        else:
            j = [j + 1, 0][j == len(monkey) - 1]
        i += 1
    output.append(monkey[0])
    print(','.join([str(i) for i in output]))
