"""于2023-11-3测试通过"""
x, y = map(int, input().split())
if x > y:
    x, y = y, x
while x != y:
    t = 1
    while t <= y:
        t *= 2
    t = t//2
    x, y = min(x, t//2 + (y - t)//2), max(x, t//2 + (y - t)//2)
print(x)