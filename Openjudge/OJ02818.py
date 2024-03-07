"""于2023-11-13测试通过"""
while True:
    n = int(input())
    if not n:
        break
    key = [int(s) - 1 for s in input().split()]
    d, t = [], []
    for i in range(n):
        j = i
        d.append([i])
        while True:
            j = key[j]
            if j == i:
                t.append(len(d[i]))
                break
            d[i].append(j)
    while True:
        data = input()
        try:
            space = data.index(' ')
            k = int(data[:space])
            info = data[space + 1:]
            info += ' '*(n - len(info))
            new_info = ['']*n
            for i in range(n):
                new_info[d[i][k % t[i]]] = info[i]
            print(''.join(new_info))
        except ValueError:
            break
    print()