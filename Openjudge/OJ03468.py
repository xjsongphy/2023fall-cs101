"""于2023-12-26测试通过"""
while True:
    try:
        n = int(input())
    except EOFError:
        break

    ls = sorted(list(map(int, input().split())))
    s = sum(ls)
    if 2 * ls[-1] < s:
        total = s / 2
    else:
        total = s - ls[-1]

    print('%.1f' % total)