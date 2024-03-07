"""于2023-12-10测试通过"""
l, n, m = map(int, input().split())
ls = [0] + [int(input()) for _ in range(n)] + [l]
std = l//2
left, right = 0, l
while right - left > 1:
    count = now = 0
    for i in range(1, n + 1):
        if ls[i] - now < std:
            count += 1
        else:
            now = ls[i]
    count += (l - now < std)
    if count <= m:
        left = std
        std = (right + std)//2
    elif count > m:
        right = std
        std = (left + std)//2
print(left)