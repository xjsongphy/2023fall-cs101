"""于2023-12-26测试通过"""
r = int(input())
total = 0
pre = [0]*(r + 1)
for _ in range(int(input())):
    l, t, w, h = map(int, input().split())
    total += w*h
    for i in range(1, w + 1):
        pre[l + i] += h
found = False
t = 0
for i in range(1, r + 1):
    pre[i] += pre[i - 1]
    if not found:
        t = 2 * pre[i] - total
        if t >= 0:
            found = True
            l = i
    else:
        if pre[i] == pre[l]:
            l = i
        else:
            print(l)
            exit()
print(r)