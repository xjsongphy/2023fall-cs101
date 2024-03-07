"""于2023-12-28测试通过"""
n, x = map(int, input().split())
a = sorted(list(map(int, input().split())))
dp_pre = [[True] + [False]*x for _ in range(n + 1)]
dp_sub = [[True] + [False]*x for _ in range(n + 1)]
ls = [0]
l = 1
for i in range(1, n + 1):
    t = a[i - 1]
    for j in range(l):
        p = ls[j]
        dp_pre[i][p] = True
        if p + t <= x:
            if dp_pre[i - 1][p + t]:
                continue
            dp_pre[i][p + t] = True
            l += 1
            ls.append(p + t)
ls = [0]
l = 1
for i in range(n - 1, -1, -1):
    t = a[i]
    for j in range(l):
        p = ls[j]
        dp_sub[i][p] = True
        if p + t <= x:
            if dp_sub[i + 1][p + t]:
                continue
            dp_sub[i][p + t] = True
            l += 1
            ls.append(p + t)
ans = []
for i in range(n):
    found = False
    for j in range(x + 1):
        if dp_pre[i][j] and dp_sub[i + 1][x - j]:
            found = True
    if found:
        continue
    ans.append(str(a[i]))
print(len(ans))
print(' '.join(ans))