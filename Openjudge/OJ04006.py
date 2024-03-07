"""于2023-12-22测试通过"""
k, n = map(int, input().split())
for _ in range(k):
    x, y = map(int, input().split())
    layer = min([x, n - x + 1, y, n - y + 1]) - 1
    start = (n + n - 2 * layer) * layer * 2 + 1
    layer += 1
    if x == layer:
        print(start + y - layer)
    elif n - x + 1 == layer:
        print(start + 2 * (n - 2 * layer + 1) + n - layer + 1 - y)
    elif y == layer:
        print(start + 3 * (n - 2 * layer + 1) + n - layer + 1 - x)
    else:
        print(start + n - 3 * layer + x + 1)