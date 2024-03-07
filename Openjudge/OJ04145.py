"""于2023-12-26测试通过"""
while True:
    n, k = map(int, input().split())
    if not n + k:
        break
    a, b = list(map(int, input().split())), list(map(int, input().split()))
    l, r = 0, 101
    eps = 0.0001


    def judge(lim):
        c = sorted([100*a[i] - lim*b[i] for i in range(n)], reverse=True)
        return sum(c[:n - k])


    while r - l > eps:
        mid = (l + r)/2
        t = judge(mid)
        if t >= eps:
            l = mid
        elif t <= -eps:
            r = mid
        else:
            l = mid
            break
    print(round(l))