"""于2023-10-18测试通过"""
n, m = map(int, input().split())
zero = [0 for i in range(m + 2)]
before = [zero]
for i in range(n):
    before.append([0])
    for j in list(map(int, input().split())):
        before[i + 1].append(j)
    before[i + 1].append(0)
before.append(zero[:])

for i in range(1, n + 1):
    for j in range(1, m + 1):
        t = -before[i][j]
        for r in range(3):
            for s in range(3):
                t += before[i + r - 1][j + s - 1]
        if before[i][j]:
            print(['0', '1'][t in [2, 3]], end=['', ' '][j < m])
        else:
            print(['0', '1'][t == 3], end=['', ' '][j < m])
    print()
