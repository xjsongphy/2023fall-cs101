"""于2023-12-19测试通过"""
n, m = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()


def judge(dist):
    now = ls[0]
    count = 1
    for i in range(1, n):
        if ls[i] - now >= dist:
            count += 1
            now = ls[i]
    return [False, True][count >= m]


l, r = 0, ls[-1] - ls[0] + 1
while r - l > 1:
    mid = (l + r)//2
    if judge(mid):
        l = mid
    else:
        r = mid
print(l)