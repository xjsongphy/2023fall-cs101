"""于2023-11-12测试通过"""
t = 0

def arr(m, lim, n):
    global t
    if n == 1 and m <= lim:
        t += 1
    elif n > 1:
        for i in range(min(lim, m) + 1):
            arr(m - i, i, n - 1)


for _ in range(int(input())):
    m, n = map(int, input().split())
    t = 0
    arr(m, m, n)
    print(t)
