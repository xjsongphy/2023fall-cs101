"""于2023-12-23测试通过"""
n, b = map(int, input().split())
ls = sorted([int(input()) for _ in range(n)], reverse=True)
total = 0
for i in range(n):
    total += ls[i]
    if total >= b:
        print(i + 1)
        break
