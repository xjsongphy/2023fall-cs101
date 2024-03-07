"""于2023-11-9测试通过"""
n = int(input())
prices = sorted(list(map(int, input().split())))
for _ in range(int(input())):
    m = int(input())
    if m < prices[0]:
        print(0)
    elif m >= prices[-1]:
        print(n)
    else:
        l, r = 0, n - 1
        while r - l > 1:
            mid = int((l + r)/2)
            if prices[mid] <= m:
                l = mid
            else:
                r = mid
        print([r, r + 1][m == prices[r]])

