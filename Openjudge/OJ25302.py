"""于2023-11-28测试通过"""
for _ in range(int(input())):
    d = {}
    n = int(input())
    for i in range(n):
        x, y = map(int, input().split())
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
        if y in d:
            d[y] -= 1
        else:
            d[y] = -1
    ans = 0
    t = 0
    for i in sorted(d.keys()):
        t += d[i]
        ans = max(t, ans)
    print(ans)
